#!/usr/bin/env python3
"""Local catalog, runtime adapters and one-file work records. Python 3.11+, stdlib only."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import os
import re
import sys
import tempfile
import threading
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TASK_STATES = {"open", "in_progress", "blocked", "done"}
MAX_RECORD = 1024 * 1024
LINK = re.compile(r"\[[^\]]*\]\(([^\s)]+)\)")
FENCE = re.compile(r"^```[^\n]*\n.*?^```[^\n]*$", re.M | re.S)


class ToolkitError(ValueError):
    """An actionable input or storage error."""


class Conflict(ToolkitError):
    """The caller edited a stale version of a work record."""


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def slug(value: str) -> str:
    if len(value) > 64 or not SLUG.fullmatch(value):
        raise ToolkitError("Use a lowercase slug with letters, digits and single hyphens (1–64 characters).")
    return value


def field(value: str, limit: int = 4000) -> str:
    value = value.strip()
    if not value or len(value) > limit or any(ord(c) < 32 and c not in '\n\t' for c in value):
        raise ToolkitError(f"Text must contain 1–{limit} characters and no control characters.")
    return value


def cell(value: str) -> str:
    return field(value).replace("|", "&#124;").replace("\n", " ")


def metadata(text: str) -> tuple[dict[str, str], str]:
    """Read our deliberately portable YAML scalar subset without runtime dependencies."""
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ToolkitError("Missing YAML frontmatter.")
    result = {}
    for line in match[1].splitlines():
        key, separator, value = line.partition(":")
        if not separator or not re.fullmatch(r"[a-z][a-z_-]*", key):
            raise ToolkitError("Use one scalar YAML value per frontmatter line.")
        value = value.strip()
        if value.startswith('"'):
            try:
                value = json.loads(value)
            except json.JSONDecodeError as exc:
                raise ToolkitError("Invalid quoted frontmatter value.") from exc
        if not isinstance(value, str) or not value:
            raise ToolkitError(f"Invalid frontmatter value: {key}")
        if key in result:
            raise ToolkitError(f"Duplicate frontmatter key: {key}")
        result[key] = value
    return result, text[match.end():].lstrip()


@dataclass(frozen=True)
class Entry:
    name: str
    description: str
    kind: str
    path: str


def catalog(root: Path = ROOT) -> list[Entry]:
    entries = []
    paths = [("agent", p) for p in sorted((root / "agents").glob("*.agent.md"))]
    paths += [("skill", p) for p in sorted((root / "skills").rglob("*.md"))
              if "references" not in p.relative_to(root / "skills").parts]
    seen = set()
    for kind, path in paths:
        meta, _ = metadata(path.read_text(encoding="utf-8"))
        name = slug(meta.get("name", ""))
        description = meta.get("description", "")
        if not 1 <= len(description) <= 1024:
            raise ToolkitError(f"Invalid description: {path}")
        expected = path.name.removesuffix(".agent.md") if kind == "agent" else (path.parent.name if path.name == "SKILL.md" else path.stem)
        if name != expected or (kind, name) in seen:
            raise ToolkitError(f"Mismatched or duplicate name: {path}")
        seen.add((kind, name))
        entries.append(Entry(name, description, kind, path.relative_to(root).as_posix()))
    if not any(e.kind == 'agent' for e in entries) or not any(e.kind == 'skill' for e in entries):
        raise ToolkitError('The catalog must contain both agents and skills.')
    return entries


def check(root: Path = ROOT) -> list[str]:
    errors = []
    try:
        catalog(root)
    except ToolkitError as exc:
        errors.append(str(exc))
    paths = list((root / "agents").rglob("*.md")) + list((root / "skills").rglob("*.md"))
    paths += list((root / "toolkit").rglob("*.md")) + list((root / "templates").rglob("*.md"))
    paths += [root / p for p in ("README.md", "AGENTS.md", "CONTRIBUTING.md", "copilot-instructions.md", ".github/copilot-instructions.md")]
    for path in paths:
        if not path.exists():
            errors.append(f"Missing file: {path.relative_to(root)}")
            continue
        text = FENCE.sub("", path.read_text(encoding="utf-8"))
        if "references" not in path.parts and re.search(r"\bTODO\b|\[INSERT", text):
            errors.append(f"Unfinished template: {path.relative_to(root)}")
        for target in LINK.findall(text):
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            destination = path.parent / unquote(parts.path)
            if not destination.exists():
                errors.append(f"Broken link: {path.relative_to(root)} -> {target}")
    return errors


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=f".{path.name}.", delete=False) as stream:
        temporary = Path(stream.name)
        try:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
            stream.close()
            os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)


@dataclass(frozen=True)
class OpenCodeOptions:
    plannotator: bool = False
    plan_model: str | None = None
    build_model: str | None = None
    plan_variant: str | None = None
    build_variant: str | None = None

    def validate(self) -> None:
        for phase in ('plan', 'build'):
            model = getattr(self, f'{phase}_model')
            variant = getattr(self, f'{phase}_variant')
            if model is not None and (not isinstance(model, str) or not re.fullmatch(r'[^/\s#]+/[^\s#]+', model)):
                raise ToolkitError(f'{phase.title()} model must use provider/model-id, without whitespace or #variant.')
            if variant is not None:
                if model is None:
                    raise ToolkitError(f'{phase.title()} variant requires a configured {phase} model.')
                if not isinstance(variant, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', variant):
                    raise ToolkitError(f'{phase.title()} variant must be a model-supported variant name.')


def export(runtime: str, output: Path, root: Path = ROOT, force: bool = False, dry_run: bool = False,
           *, opencode_options: OpenCodeOptions | None = None) -> dict:
    if runtime not in {"opencode", "copilot", "portable"}:
        raise ToolkitError("Unknown runtime.")
    options = opencode_options or OpenCodeOptions()
    if runtime != 'opencode' and options != OpenCodeOptions():
        raise ToolkitError('Plannotator, model and variant options require --runtime opencode.')
    options.validate()
    output = output.absolute()
    if output.resolve() == root.resolve() or output.resolve() in root.resolve().parents:
        raise ToolkitError("Export to a separate directory, not the source repository or its parent.")
    if any(output.resolve().is_relative_to((root / folder).resolve()) for folder in ('agents','skills','toolkit','templates','marp-templates','reference-repos','tools','assets')):
        raise ToolkitError('Export outside canonical source folders.')
    planned: dict[str, bytes] = {}
    for folder in ("agents", "skills", "toolkit", "templates", "marp-templates", "reference-repos"):
        for path in sorted((root / folder).rglob("*")):
            if path.is_file():
                if path.is_symlink():
                    raise ToolkitError(f"Cannot export a symlink: {path}")
                planned[f"catalog/{path.relative_to(root).as_posix()}"] = path.read_bytes()
    entries = catalog(root)
    planned['catalog/index.json'] = (json.dumps([asdict(e) for e in entries], indent=2) + '\n').encode()
    for entry in entries:
        if entry.kind == "skill":
            base = {"opencode": "skills", "copilot": ".github/skills", "portable": ".agents/skills"}[runtime]
            destination = f"{base}/{entry.name}/SKILL.md"
            interface = (root / entry.path).parent / 'agents/openai.yaml'
            if interface.is_file():
                planned[f'{base}/{entry.name}/agents/openai.yaml'] = interface.read_bytes()
        else:
            base = {"opencode": "agents", "copilot": ".github/agents", "portable": "agents"}[runtime]
            suffix = ".md" if runtime == "opencode" else ".agent.md"
            destination = f"{base}/{entry.name}{suffix}"
        meta, body = metadata((root / entry.path).read_text(encoding="utf-8"))
        def rebase(match):
            target = match.group(1)
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                return match.group(0)
            original = (root / entry.path).parent / unquote(parts.path)
            relative = original.resolve().relative_to(root.resolve())
            copied = output / "catalog" / relative
            if f"catalog/{relative.as_posix()}" not in planned:
                raise ToolkitError(f"Reference is not included in the bundle: {entry.path} -> {target}")
            target = Path(os.path.relpath(copied, (output / destination).parent)).as_posix()
            if parts.fragment:
                target += "#" + parts.fragment
            return match.group(0).replace(match.group(1), target)
        body = LINK.sub(rebase, body)
        header = f'---\nname: {json.dumps(meta["name"])}\ndescription: {json.dumps(meta["description"])}\n'
        if entry.kind == "agent" and runtime == "opencode":
            mode = "primary" if entry.name in {"joerg", "plan", "build"} else "subagent"
            header += f"mode: {mode}\n"
            if entry.name in {"code-reviewer", "architecture-reviewer", "plan"}:
                header += "permission:\n  edit:\n    '*': deny\n"
                if entry.name == "plan":
                    header += "    '.ai/work/**': allow\n    '.ai/archive/**': allow\n"
                header += "  bash: deny\n  task: deny\n"
                if entry.name == 'plan' and options.plannotator:
                    header += "  submit_plan: allow\n  plan_exit: deny\n"
            if entry.name == 'plan' and options.plannotator:
                body += '\nPlannotator plan review is enabled. Submit the current plan with `submit_plan` using the installed tool schema. Incorporate requested changes and resubmit; do not hand off to implementation until the user approves this revision. If the tool fails or is unavailable, remain in planning and request explicit review in the current conversation. Tool feedback never expands host permissions.\n'
        elif entry.kind == "agent" and runtime == "copilot":
            if entry.name in {"code-reviewer", "architecture-reviewer", "plan"}:
                header += "tools: [read, search]\n"
                body += '\nThis adapter provides read/search tools only. Return a proposed patch or plan; writing a work record requires switching to a writing agent.\n'
        planned[destination] = (header + "---\n\n" + body).encode()
    if runtime == "opencode":
        config = {"$schema": "https://opencode.ai/config.json", "default_agent": "joerg",
                  "instructions": [str(output / "catalog/toolkit/WORKFLOW.md")],
                  "permission": {"external_directory": {str(output / 'catalog') + '/*': 'allow'},
                                 "edit": {str(output / 'catalog') + '/*': 'deny'}}}
        for phase in ('plan', 'build'):
            model = getattr(options, f'{phase}_model')
            variant = getattr(options, f'{phase}_variant')
            if model is not None:
                agent = config.setdefault('agent', {}).setdefault(phase, {})
                agent['model'] = model
                if variant is not None:
                    agent['variant'] = variant
        if options.plannotator:
            # Let our native profiles own prompts and permissions. The plugin's
            # plan-agent mode would also allow edits to all Markdown files.
            config['plugin'] = [['@plannotator/opencode@latest', {'workflow': 'user-managed'}]]
            config['share'] = 'disabled'
            config['permission']['submit_plan'] = 'deny'
        planned['opencode.json'] = (json.dumps(config, indent=2) + '\n').encode()
        for name, agent, description in (("work-plan", "plan", "Plan an outcome in its existing planning home"), ("work-build", "build", "Implement and verify the current authorized plan"), ("brain", "second-brain", "Maintain the private PARA vault")):
            planned[f'commands/{name}.md'] = f'---\ndescription: {description}\nagent: {agent}\n---\n\nUse the relevant skills for this request and the shared workflow. $ARGUMENTS\n'.encode()
    elif runtime == "copilot":
        planned['.github/copilot-instructions.md'] = b'Read `catalog/toolkit/WORKFLOW.md` for shared workflow guidance when needed. Follow project-specific instructions and load only selected skills.\n'
    manifest_path = output / '.ai-toolkit-manifest.json'
    if manifest_path.is_symlink():
        raise ToolkitError("The export manifest must not be a symlink.")
    old = {}
    if manifest_path.exists():
        try:
            old = json.loads(manifest_path.read_text(encoding='utf-8'))['files']
        except (ValueError, KeyError, TypeError) as exc:
            raise ToolkitError("Invalid export manifest; select another output directory.") from exc
        if not isinstance(old, dict) or any(not isinstance(k, str) or not isinstance(v, str) for k, v in old.items()):
            raise ToolkitError("Invalid export manifest.")
    hashes = {relative: digest(data) for relative, data in planned.items()}
    changed = []
    removed = []
    for relative in sorted(set(planned) | set(old)):
        target = output / relative
        if Path(relative).is_absolute() or not target.resolve().is_relative_to(output.resolve()):
            raise ToolkitError("Export path escapes its destination.")
        if target.is_symlink() or any(parent.is_symlink() for parent in target.parents):
            raise ToolkitError("Export destination must not contain symlinks.")
        current_hash = None
        if target.exists():
            if not target.is_file():
                raise ToolkitError(f"Export target is not a file: {relative}")
            current_hash = digest(target.read_bytes())
            if not force and (relative not in old or current_hash != old[relative]):
                raise ToolkitError(f"Refusing to overwrite an unmanaged or edited file: {relative}. Use a separate output or explicitly pass --force.")
        if relative in planned:
            if current_hash != hashes[relative]:
                changed.append(relative)
        elif current_hash is not None:
            removed.append(relative)
    if not dry_run:
        for relative in changed:
            atomic_write(output / relative, planned[relative])
        for relative in removed:
            (output / relative).unlink()
        manifest = (json.dumps({'runtime': runtime, 'files': hashes}, indent=2) + '\n').encode()
        if not manifest_path.exists() or manifest_path.read_bytes() != manifest:
            atomic_write(manifest_path, manifest)
    return {'runtime': runtime, 'output': str(output), 'agents': sum(e.kind == 'agent' for e in entries), 'skills': sum(e.kind == 'skill' for e in entries), 'files': len(planned), 'changed': len(changed), 'unchanged': len(planned) - len(changed), 'removed': len(removed), 'dry_run': dry_run}


TASK_ROW = re.compile(r"^\| (?P<id>T[1-9][0-9]*) \| (?P<title>[^|]*) \| (?P<status>open|in_progress|blocked|done) \| (?P<evidence>[^|]*) \|$", re.M)


def tasks(text: str) -> list[dict]:
    section = re.search(r'\n## Tasks\n(.*?)(?=\n## |\Z)', text, re.S)
    if not section:
        raise ToolkitError('The record needs a Tasks section.')
    result = []
    seen = set()
    for line in section[1].splitlines():
        if not re.match(r'^\|\s*T\d', line):
            continue
        match = TASK_ROW.fullmatch(line)
        if not match or match['id'] in seen or not match['title'].strip():
            raise ToolkitError('Malformed or duplicate task row. Use four columns, stable T1… IDs and a valid status.')
        seen.add(match['id'])
        result.append(match.groupdict())
    return result


class WorkStore:
    def __init__(self, workspace: Path):
        self.workspace = workspace.resolve()
        if not self.workspace.is_dir():
            raise ToolkitError('Workspace must be an existing directory.')
        self.lock = threading.RLock()

    def path(self, name: str, archived: bool = False) -> Path:
        name = slug(name)
        path = self.workspace / '.ai' / ('archive' if archived else 'work') / f'{name}.md'
        if not path.resolve().is_relative_to(self.workspace) or any(p.is_symlink() for p in [path, *path.parents] if p != self.workspace):
            raise ToolkitError('Work records must not traverse symlinks or leave the workspace.')
        return path

    def read(self, name: str, archived: bool = False) -> dict:
        path = self.path(name, archived)
        if not path.is_file():
            raise FileNotFoundError(name)
        if path.stat().st_size > MAX_RECORD:
            raise ToolkitError('Work record exceeds the 1 MiB size limit.')
        data = path.read_bytes()
        text = data.decode('utf-8')
        meta, _ = metadata(text)
        if meta.get('id') != name:
            raise ToolkitError('Work frontmatter ID must match its filename.')
        return {'id': name, 'title': meta.get('title', name), 'kind': meta.get('kind', 'general'), 'status': meta.get('status', 'active'),
                'path': path.relative_to(self.workspace).as_posix(), 'etag': '"' + digest(data) + '"', 'markdown': text,
                'tasks': tasks(text)}

    def list(self, archived: bool = False) -> list[dict]:
        folder = self.path('placeholder', archived).parent
        result = []
        for path in sorted(folder.glob('*.md')):
            item = self.read(path.stem, archived)
            item.pop('markdown')
            result.append(item)
        return result

    def create(self, name: str, title: str, kind: str = 'software') -> dict:
        if kind not in {'software', 'product', 'general'}:
            raise ToolkitError('Kind must be software, product or general.')
        title = field(title, 200)
        with self.lock:
            path = self.path(name)
            if path.exists() or self.path(name, True).exists():
                raise Conflict('A work record with this ID already exists.')
            text = (ROOT/'templates/work-item.md').read_text(encoding='utf-8')
            text = text.replace('{{id}}', slug(name)).replace('{{title_json}}', json.dumps(title, ensure_ascii=False)).replace('{{kind}}', kind).replace('{{title}}', title.replace('\n', ' '))
            atomic_write(path, text.encode())
            return self.read(name)

    def update(self, name: str, etag: str, transform) -> dict:
        with self.lock:
            current = self.read(name)
            if etag != current['etag']:
                raise Conflict('This record changed. Reload it before saving; your feedback has not been discarded.')
            text = transform(current['markdown'])
            # Check again immediately before replacing a file another editor may have touched.
            if self.read(name)['etag'] != etag:
                raise Conflict('The file changed while preparing the update. Reload and retry.')
            if len(text.encode()) > MAX_RECORD:
                raise ToolkitError('Work record exceeds the size limit.')
            atomic_write(self.path(name), text.encode())
            return self.read(name)

    def task(self, name: str, task_id: str, status: str, evidence: str, etag: str) -> dict:
        if status not in TASK_STATES:
            raise ToolkitError('Invalid task status.')
        if status == 'done' and not evidence.strip():
            raise ToolkitError('A completed task needs evidence.')
        evidence = cell(evidence) if evidence.strip() else ''
        def change(text):
            found = False
            def replace(match):
                nonlocal found
                if match['id'] != task_id:
                    return match[0]
                found = True
                return f"| {task_id} | {match['title']} | {status} | {evidence or match['evidence']} |"
            section = re.search(r'\n## Tasks\n(.*?)(?=\n## |\Z)', text, re.S)
            assert section is not None  # validated by read()
            updated = text[:section.start(1)] + TASK_ROW.sub(replace, section[1]) + text[section.end(1):]
            if not found:
                raise ToolkitError('Task not found. Add task rows to the Markdown record with stable T1, T2… IDs.')
            return updated
        return self.update(name, etag, change)

    def feedback(self, name: str, comment: str, etag: str) -> dict:
        comment = field(comment)
        def change(text):
            if '\n## Feedback\n' not in text:
                raise ToolkitError('The record needs a Feedback section.')
            ids = [int(n) for n in re.findall(r'^### F(\d+) ', text, re.M)]
            now = datetime.now(UTC).isoformat(timespec='seconds')
            entry = f'\n### F{max(ids, default=0)+1} · {now}\n\n' + '\n'.join('> ' + line for line in comment.splitlines()) + '\n\nDisposition: open\n'
            marker = '\n## Feedback\n'
            start = text.index(marker) + len(marker)
            end = text.find('\n## ', start)
            end = len(text) if end < 0 else end
            return text[:end].rstrip() + '\n' + entry + text[end:]
        return self.update(name, etag, change)

    def archive(self, name: str, etag: str) -> dict:
        with self.lock:
            current = self.read(name)
            if etag != current['etag']:
                raise Conflict('Record changed; reload before archiving.')
            if not current['tasks'] or any(t['status'] != 'done' or not t['evidence'].strip() for t in current['tasks']):
                raise ToolkitError('Complete all tasks with evidence before archiving.')
            destination = self.path(name, True)
            if destination.exists():
                raise Conflict('Archive destination already exists.')
            self.update(name, etag, lambda text: re.sub(r'^status:.*$', 'status: archived', text, count=1, flags=re.M))
            destination.parent.mkdir(parents=True, exist_ok=True)
            self.path(name).rename(destination)
            return self.read(name, True)

    def csv(self, name: str) -> str:
        stream = io.StringIO(newline='')
        writer = csv.writer(stream)
        writer.writerow(['id', 'title', 'status', 'evidence'])
        for task in self.read(name)['tasks']:
            # Prevent spreadsheet formula execution when opening a generated CSV.
            writer.writerow([("'" + v if v.lstrip().startswith(('=', '+', '-', '@')) else v).replace('&#124;', '|') for v in task.values()])
        return stream.getvalue()


def obsidian_uri(vault: str, file: str) -> str:
    vault = field(vault, 200)
    file = field(file, 1000).replace('\\', '/')
    if file.startswith('/') or re.match(r'^[a-zA-Z]:', file) or any(p in {'.', '..', ''} for p in file.split('/')):
        raise ToolkitError('Use a vault-relative note path, not an absolute Windows or WSL path.')
    return f'obsidian://open?vault={quote(vault, safe="")}&file={quote(file, safe="")}'


def serve(workspace: Path, port: int, root: Path = ROOT) -> ThreadingHTTPServer:
    store = WorkStore(workspace)
    entries = catalog(root)
    class Handler(BaseHTTPRequestHandler):
        server_version = 'LocalAIToolkit/1'

        def setup(self):
            super().setup()
            self.connection.settimeout(10)

        def log_message(self, fmt, *args):
            # Avoid logging note contents, query strings or personal data.
            print(f'{self.command} {self.path.split("?")[0]}', file=sys.stderr)

        def reply(self, status: int, value, etag: str | None = None, content_type: str = 'application/json; charset=utf-8'):
            data = value if isinstance(value, bytes) else json.dumps(value, ensure_ascii=False).encode()
            self.send_response(status)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(data)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Content-Security-Policy', "default-src 'self'; script-src 'self'; style-src 'self'; connect-src 'self'; img-src 'self'; frame-ancestors 'none'; base-uri 'none'; form-action 'self'")
            if etag:
                self.send_header('ETag', etag)
            self.end_headers()
            self.wfile.write(data)

        def trusted(self):
            actual_port = self.server.server_address[1]
            hosts = {f'127.0.0.1:{actual_port}', f'localhost:{actual_port}'}
            if self.headers.get('Host') not in hosts:
                raise PermissionError('Only the loopback host is allowed.')
            origin = self.headers.get('Origin')
            if origin is not None and origin not in {f'http://{h}' for h in hosts}:
                raise PermissionError('Cross-origin requests are not allowed.')
            if self.headers.get('Sec-Fetch-Site') == 'cross-site':
                raise PermissionError('Cross-site requests are not allowed.')

        def handle_request(self):
            try:
                self.trusted()
                path = urlsplit(self.path).path
                if self.command == 'GET':
                    static = {'/': ('index.html','text/html'), '/app.js': ('app.js','text/javascript'), '/style.css': ('style.css','text/css')}
                    if path in static:
                        file, kind = static[path]
                        return self.reply(200, (root/'tools/web'/file).read_bytes(), content_type=kind+'; charset=utf-8')
                    if path == '/api/v1/catalog':
                        return self.reply(200, [asdict(e) for e in entries])
                    if path == '/api/v1/work':
                        return self.reply(200, store.list())
                    if path == '/api/v1/openapi.json':
                        return self.reply(200, (root/'toolkit/openapi.json').read_bytes())
                    match = re.fullmatch(r'/api/v1/work/([a-z0-9-]+)', path)
                    if match:
                        item = store.read(match[1])
                        return self.reply(200, item, item['etag'])
                    raise FileNotFoundError('Route not found.')
                if self.command not in {'POST','PATCH'}:
                    return self.reply(405, {'error':'Method not allowed.'})
                if self.headers.get('Transfer-Encoding'):
                    raise ToolkitError('Chunked requests are not supported.')
                if self.headers.get('Content-Type', '').split(';')[0].strip() != 'application/json':
                    return self.reply(415, {'error':'Use application/json.'})
                length = int(self.headers.get('Content-Length', '0'))
                if not 1 <= length <= 16384:
                    return self.reply(413, {'error':'JSON body must be 1–16384 bytes.'})
                data = json.loads(self.rfile.read(length))
                if not isinstance(data, dict):
                    raise ToolkitError('JSON body must be an object.')
                def argument(name, default=None):
                    value = data.get(name, default)
                    if not isinstance(value, str):
                        raise ToolkitError(f'Field {name} must be text.')
                    return value
                if path == '/api/v1/work' and self.command == 'POST':
                    item = store.create(argument('id'), argument('title'), argument('kind', 'software'))
                    return self.reply(201, item, item['etag'])
                match = re.fullmatch(r'/api/v1/work/([a-z0-9-]+)/(feedback|tasks/(T[1-9][0-9]*))', path)
                if not match:
                    raise FileNotFoundError('Route not found.')
                etag = self.headers.get('If-Match')
                if not etag:
                    return self.reply(428, {'error':'Supply If-Match from the current record ETag.'})
                if match[2] == 'feedback' and self.command == 'POST':
                    item = store.feedback(match[1], argument('text'), etag)
                elif match[3] and self.command == 'PATCH':
                    item = store.task(match[1], match[3], argument('status'), argument('evidence',''), etag)
                else:
                    return self.reply(405, {'error':'Method not allowed.'})
                self.reply(200, item, item['etag'])
            except PermissionError as exc:
                self.reply(403, {'error':str(exc)})
            except Conflict as exc:
                self.reply(412, {'error':str(exc)})
            except FileNotFoundError:
                self.reply(404, {'error':'Record or route not found.'})
            except (ToolkitError, ValueError, UnicodeError) as exc:
                self.reply(400, {'error':str(exc)})
            except OSError:
                self.reply(500, {'error':'Local storage operation failed; check the workspace permissions.'})

        do_GET = handle_request
        do_POST = handle_request
        do_PATCH = handle_request
        do_DELETE = handle_request
        do_PUT = handle_request

    server = ThreadingHTTPServer(('127.0.0.1', port), Handler)
    server.daemon_threads = True
    return server


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    sub.add_parser('check', help='Validate all catalog metadata and local links')
    cat = sub.add_parser('catalog', help='Print catalog metadata without loading all prompts')
    cat.add_argument('--kind', choices=['agent','skill'])
    adapter = sub.add_parser('export', help='Export isolated native runtime profiles')
    adapter.add_argument('--runtime', choices=['opencode','copilot','portable'], required=True)
    adapter.add_argument('--output', type=Path, required=True)
    adapter.add_argument('--force', action='store_true')
    adapter.add_argument('--dry-run', action='store_true')
    adapter.add_argument('--plannotator', action='store_true', help='Enable local Plannotator plan review in OpenCode 1')
    adapter.add_argument('--plan-model', help='OpenCode planning model: provider/model-id')
    adapter.add_argument('--build-model', help='OpenCode implementation model: provider/model-id')
    adapter.add_argument('--plan-variant', help='Variant supported by the configured planning model')
    adapter.add_argument('--build-variant', help='Variant supported by the configured implementation model')
    uri = sub.add_parser('obsidian-uri', help='Encode a Windows Obsidian URI')
    uri.add_argument('--vault', required=True)
    uri.add_argument('--file', required=True)
    web = sub.add_parser('serve', help='Serve the local catalog and work dashboard on loopback only')
    web.add_argument('--workspace', type=Path, default=Path.cwd())
    web.add_argument('--port', type=int, default=4097)
    work = sub.add_parser('work', help='Create and maintain one-file work records')
    work.add_argument('--workspace', type=Path, default=Path.cwd())
    operations = work.add_subparsers(dest='operation', required=True)
    new = operations.add_parser('new')
    new.add_argument('id')
    new.add_argument('--title', required=True)
    new.add_argument('--kind', choices=['software','product','general'], default='software')
    listing = operations.add_parser('list')
    listing.add_argument('--archived', action='store_true')
    task = operations.add_parser('task')
    task.add_argument('id')
    task.add_argument('task_id')
    task.add_argument('--status', choices=sorted(TASK_STATES), required=True)
    task.add_argument('--evidence', default='')
    feedback = operations.add_parser('feedback')
    feedback.add_argument('id')
    feedback.add_argument('--text', required=True)
    archive = operations.add_parser('archive')
    archive.add_argument('id')
    csv_cmd = operations.add_parser('csv')
    csv_cmd.add_argument('id')
    csv_cmd.add_argument('--output', type=Path)
    args = parser.parse_args(argv)
    try:
        if args.command == 'check':
            errors = check()
            if errors:
                print('\n'.join(errors), file=sys.stderr)
                return 1
            entries = catalog()
            print(f"Valid: {sum(e.kind == 'agent' for e in entries)} agents, {sum(e.kind == 'skill' for e in entries)} skills; local links resolve.")
        elif args.command == 'catalog':
            print(json.dumps([asdict(e) for e in catalog() if args.kind is None or e.kind == args.kind], indent=2))
        elif args.command == 'export':
            options = OpenCodeOptions(args.plannotator, args.plan_model, args.build_model,
                                      args.plan_variant, args.build_variant)
            print(json.dumps(export(args.runtime, args.output, force=args.force, dry_run=args.dry_run,
                                    opencode_options=options), indent=2))
        elif args.command == 'obsidian-uri':
            print(obsidian_uri(args.vault, args.file))
        elif args.command == 'serve':
            server = serve(args.workspace, args.port)
            print(f'Local toolkit: http://127.0.0.1:{server.server_address[1]} (workspace: {args.workspace.resolve()})', flush=True)
            try:
                server.serve_forever()
            except KeyboardInterrupt:
                pass
            finally:
                server.server_close()
        else:
            store = WorkStore(args.workspace)
            if args.operation == 'new':
                result = store.create(args.id, args.title, args.kind)
            elif args.operation == 'list':
                result = store.list(args.archived)
            elif args.operation == 'csv':
                data = store.csv(args.id)
                if args.output:
                    atomic_write(args.output, data.encode())
                    print(args.output)
                else:
                    print(data, end='')
                return 0
            else:
                etag = store.read(args.id)['etag']
                if args.operation == 'task':
                    result = store.task(args.id, args.task_id, args.status, args.evidence, etag)
                elif args.operation == 'feedback':
                    result = store.feedback(args.id, args.text, etag)
                else:
                    result = store.archive(args.id, etag)
            if isinstance(result, dict):
                result = {k:v for k,v in result.items() if k != 'markdown'}
            print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except (ToolkitError, OSError) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
