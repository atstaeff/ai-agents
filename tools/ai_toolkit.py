#!/usr/bin/env python3
"""Local catalog, runtime adapters and one-file work records. Python 3.11+, stdlib only."""
from __future__ import annotations

import argparse
import base64
import csv
import errno
import hashlib
import io
import json
import os
import posixpath
import re
import sys
import tempfile
import threading
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path, PurePosixPath
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TASK_STATES = {"open", "in_progress", "blocked", "done"}
MAX_RECORD = 1024 * 1024
LINK = re.compile(r"\[[^\]]*\]\(([^\s)]+)\)")
FENCE = re.compile(r"^```[^\n]*\n.*?^```[^\n]*$", re.M | re.S)
RUNTIMES = {'opencode', 'copilot', 'claude', 'portable', 'herd'}
EXPORT_MANIFEST = '.ai-toolkit-manifest.json'
EXPORT_JOURNAL = '.ai-toolkit-transaction.json'
EXPORT_LOCK = '.ai-toolkit-export.lock'
EXPORT_SOURCE_FOLDERS = ('agents', 'skills', 'toolkit', 'templates', 'marp-templates', 'reference-repos')
# A source archive and a checkout use the same publication policy. Git tracking
# and ignore rules are deliberately not the boundary for reading export sources.
EXPORT_SOURCE_SUFFIXES = {
    '.md', '.txt', '.rst', '.json', '.yaml', '.yml', '.toml', '.ini', '.cfg',
    '.csv', '.tsv', '.xml', '.html', '.css', '.scss', '.js', '.mjs', '.cjs',
    '.jsx', '.ts', '.tsx', '.py', '.sh', '.bash', '.ps1', '.sql', '.r', '.go',
    '.rs', '.java', '.kt', '.kts', '.c', '.h', '.cpp', '.hpp', '.cs', '.swift',
    '.dart', '.rb', '.php', '.lua', '.ipynb', '.svg', '.png', '.jpg', '.jpeg',
    '.gif', '.webp', '.ico', '.pdf', '.docx', '.pptx', '.xlsx', '.woff', '.woff2',
    '.ttf', '.otf',
}
EXPORT_SOURCE_NAMES = {'license', 'notice', 'copying', 'makefile', 'dockerfile',
                       '.gitignore', '.dockerignore', '.editorconfig'}
EXPORT_PRIVATE_DIRECTORIES = {
    '__pycache__', 'node_modules', 'venv', 'site-packages', 'dist', 'build',
    'target', 'coverage', 'htmlcov', 'generated', 'exports', 'graphify-out',
    'cache', 'logs', 'tmp', 'temp', 'private', 'secrets', 'credentials',
    'local', 'local-state',
}
EXPORT_PRIVATE_SUFFIXES = {'.env', '.pem', '.key', '.p12', '.pfx', '.jks', '.keystore',
                           '.kdbx', '.tfstate', '.tfplan', '.sqlite', '.sqlite3', '.db'}
EXPORT_PRIVATE_NAME = re.compile(
    r'(^|[._-])(?:secrets?|credentials?|tokens?|passwords?|api[._-]?keys?|'
    r'private[._-]?keys?|service[._-]?accounts?)(?=[._-]|$)')
_UNCHECKED = object()


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
    domain: str = 'general'


def domains() -> dict:
    return json.loads((ROOT / 'toolkit/catalog-domains.json').read_text(encoding='utf-8'))


def catalog(root: Path = ROOT, *, source_files: dict[str, bytes] | None = None) -> list[Entry]:
    entries = []
    known_domains = domains()
    # Export parses only the bytes approved by its source policy, including in a
    # non-Git source archive. Do not reopen omitted files for their metadata.
    agents = (sorted((root / 'agents').rglob('*.agent.md')) if source_files is None else
              [root / name for name in sorted(source_files) if name.startswith('agents/') and name.endswith('.agent.md')])
    skills = (sorted((root / 'skills').rglob('*.md')) if source_files is None else
              [root / name for name in sorted(source_files) if name.startswith('skills/') and name.endswith('.md')])
    paths = [("agent", p) for p in agents
             if 'references' not in p.relative_to(root / 'agents').parts]
    paths += [("skill", p) for p in skills
              if "references" not in p.relative_to(root / "skills").parts and p.name != 'README.md'
              and (p.name == "SKILL.md" or len(p.relative_to(root / "skills").parts) <= 2)]
    seen = set()
    for kind, path in paths:
        text = (path.read_text(encoding='utf-8') if source_files is None else
                source_files[path.relative_to(root).as_posix()].decode('utf-8'))
        meta, _ = metadata(text)
        name = slug(meta.get("name", ""))
        description = meta.get("description", "")
        if not 1 <= len(description) <= 1024:
            raise ToolkitError(f"Invalid description: {path}")
        expected = path.name.removesuffix(".agent.md") if kind == "agent" else (path.parent.name if path.name == "SKILL.md" else path.stem)
        if name != expected or (kind, name) in seen:
            raise ToolkitError(f"Mismatched or duplicate name: {path}")
        seen.add((kind, name))
        relative = path.relative_to(root / f'{kind}s')
        domain = relative.parts[0] if len(relative.parts) > (1 if kind == 'agent' else 2) else 'general'
        if domain not in known_domains:
            raise ToolkitError(f'Unknown catalog domain: {domain} in {path}')
        entries.append(Entry(name, description, kind, path.relative_to(root).as_posix(), domain))
    if not any(e.kind == 'agent' for e in entries) or not any(e.kind == 'skill' for e in entries):
        raise ToolkitError('The catalog must contain both agents and skills.')
    return entries


def catalog_presets() -> dict:
    return json.loads((ROOT / 'toolkit/catalog-presets.json').read_text(encoding='utf-8'))


def select_entries(entries: list[Entry], preset: str = 'all',
                   agent_names: tuple[str, ...] = (), skill_names: tuple[str, ...] = ()) -> list[Entry]:
    """Select native registrations; canonical references remain available on demand."""
    presets = catalog_presets()
    if preset not in presets:
        raise ToolkitError(f'Unknown catalog preset: {preset}')
    requested = {'agent': set(agent_names), 'skill': set(skill_names)}
    for kind, names in requested.items():
        known = {e.name for e in entries if e.kind == kind}
        declared = set(presets[preset][kind + 's']) if preset != 'all' else set()
        unknown = (names | declared) - known
        if unknown:
            aliases = json.loads((ROOT / 'toolkit/catalog-aliases.json').read_text()).get(kind + 's', {})
            migrated = [f'{name} -> {aliases[name]}' for name in sorted(unknown) if name in aliases]
            hint = '; retired names: ' + ', '.join(migrated) if migrated else ''
            raise ToolkitError(f'Unknown {kind} selection: {", ".join(sorted(unknown))}{hint}')
        names.update(declared)
    selected = [e for e in entries if preset == 'all' or e.name in requested[e.kind]]
    if not any(e.kind == 'agent' for e in selected) or not any(e.kind == 'skill' for e in selected):
        raise ToolkitError('Select at least one agent and one skill.')
    return selected


def catalog_markdown(entries: list[Entry], kind: str | None = None) -> str:
    title = {'agent': 'Agents', 'skill': 'Skills', None: 'Agents and skills'}[kind]
    intro = ('Agents define accountable roles and expected handoffs.' if kind == 'agent' else
             'Skills provide focused procedures and references; selecting one does not require another session.')
    text = f'# {title}\n\n{intro}\n\nGenerated from canonical profiles with `catalog --format markdown`; edit the profile sources.\n'
    for domain, info in domains().items():
        selected = [e for e in entries if e.domain == domain and (kind is None or e.kind == kind)]
        if not selected:
            continue
        text += f'\n## {info["title"]}\n\n{info["description"]}\n\n| Name | Select for |\n| --- | --- |\n'
        for entry in selected:
            path = Path(entry.path).relative_to(f'{kind}s').as_posix() if kind else entry.path
            text += f'| [{entry.name}]({path}) | {entry.description.replace("|", "&#124;")} |\n'
    return text


def check(root: Path = ROOT) -> list[str]:
    errors = []
    entries = []
    try:
        entries = catalog(root)
        for kind in ('agent', 'skill'):
            index = root / f'{kind}s/README.md'
            if index.exists() and 'Generated from canonical profiles' in index.read_text(encoding='utf-8'):
                if index.read_text(encoding='utf-8').strip() != catalog_markdown(entries, kind).strip():
                    errors.append(f'Stale catalog index: {kind}s/README.md; regenerate with catalog --kind {kind} --format markdown.')
    except ToolkitError as exc:
        errors.append(str(exc))
    if (root / 'toolkit/catalog-presets.json').is_file():
        for preset in catalog_presets():
            try:
                select_entries(entries, preset)
            except ToolkitError as exc:
                errors.append(str(exc))
    alias_path = root / 'toolkit/catalog-aliases.json'
    if alias_path.is_file():
        active = {(e.kind + 's', e.name) for e in entries}
        for kind, aliases in json.loads(alias_path.read_text()).items():
            for old, new in aliases.items():
                if (kind, old) in active or (kind, new) not in active:
                    errors.append(f'Invalid catalog alias: {kind}/{old} -> {new}')
    paths = list((root / "agents").rglob("*.md")) + list((root / "skills").rglob("*.md"))
    paths += list((root / "toolkit").rglob("*.md")) + list((root / "templates").rglob("*.md"))
    paths += list((root / "examples").rglob("*.md"))
    paths += list((root / "knowledge").rglob("*.md"))
    if (root / "PROJECT.md").is_file():
        paths.append(root / "PROJECT.md")
    for directory, folders, filenames in os.walk(root / 'workspace'):
        if Path(directory) == root / 'workspace':
            folders[:] = [name for name in folders if name not in {'work', 'archive', 'generated', 'exports'}]
        paths += [Path(directory) / name for name in filenames if name.endswith('.md')]
    paths += [root / p for p in ("README.md", "AGENTS.md", "CONTRIBUTING.md", ".github/copilot-instructions.md")]
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


def _atomic_write_file(path: Path, data: bytes, expected_hash=_UNCHECKED) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=path.parent, prefix=f".{path.name}.", delete=False) as stream:
        temporary = Path(stream.name)
        try:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
            stream.close()
            if expected_hash is not _UNCHECKED and _export_file_hash(path) != expected_hash:
                raise Conflict(f'File changed while preparing the update: {path.name}. Reload and retry.')
            if expected_hash is None:
                # Installing the prepared inode must fail if another creator won
                # after the absence check. replace() would overwrite that file.
                try:
                    os.link(temporary, path)
                except FileExistsError as exc:
                    raise Conflict(f'File already exists: {path.name}. Reload and retry.') from exc
            else:
                os.replace(temporary, path)
        finally:
            temporary.unlink(missing_ok=True)


def atomic_write(path: Path, data: bytes, *, expected_hash=_UNCHECKED) -> None:
    _atomic_write_file(path, data, expected_hash)


def _export_private_path(relative: Path, *, directory: bool = False) -> bool:
    parts = tuple(part.casefold() for part in relative.parts)
    if not parts:
        return False
    directories = parts if directory else parts[:-1]
    if any(part.startswith('.') or part in EXPORT_PRIVATE_DIRECTORIES
           or EXPORT_PRIVATE_NAME.search(part) is not None for part in directories):
        return True
    if any(parts[index] == 'workspace' and parts[index + 1] in {'work', 'archive', 'generated', 'exports'}
           for index in range(len(parts) - 1)):
        return True
    name = parts[-1]
    return (not directory and (
        (name.startswith('.') and name not in EXPORT_SOURCE_NAMES)
        or EXPORT_PRIVATE_NAME.search(name) is not None
        or name in {'id_rsa', 'id_dsa', 'id_ecdsa', 'id_ed25519', 'auth.json', 'auth.yaml', 'auth.yml',
                    'session.json', 'sessions.json', 'memory.json', 'package-lock.json', 'npm-shrinkwrap.json', 'pnpm-lock.yaml'}
        or '.local.' in name or name.endswith(('.local', '~'))
        or Path(name).suffix in EXPORT_PRIVATE_SUFFIXES))


def _export_source_files(root: Path) -> dict[str, bytes]:
    """Read only publishable source types, pruning local state at every depth."""
    sources = {}
    for folder in EXPORT_SOURCE_FOLDERS:
        source_directory = root / folder
        if source_directory.is_symlink():
            raise ToolkitError(f'Cannot export a symlink: {source_directory}')
        for directory, folders, filenames in os.walk(source_directory, followlinks=False):
            parent = Path(directory)
            for name in sorted(folders + filenames):
                if (parent / name).is_symlink():
                    raise ToolkitError(f'Cannot export a symlink: {parent / name}')
            folders[:] = sorted(name for name in folders
                                if not _export_private_path((parent / name).relative_to(root), directory=True))
            for name in sorted(filenames):
                path = parent / name
                relative = path.relative_to(root)
                if (not _export_private_path(relative) and path.is_file()
                        and (path.suffix.casefold() in EXPORT_SOURCE_SUFFIXES or name.casefold() in EXPORT_SOURCE_NAMES)):
                    sources[relative.as_posix()] = path.read_bytes()
    return sources


def _export_relative(relative: str) -> str:
    if (not isinstance(relative, str) or not relative or '\\' in relative
            or any(ord(c) < 32 for c in relative)
            or PurePosixPath(relative).is_absolute()
            or PurePosixPath(relative).as_posix() != relative
            or any(part in {'', '.', '..'} for part in relative.split('/'))
            or re.match(r'^[A-Za-z]:', relative)
            or relative in {EXPORT_MANIFEST, EXPORT_JOURNAL, EXPORT_LOCK}):
        raise ToolkitError('Invalid export manifest path; use normalized relative file paths.')
    return relative


def _export_target(output: Path, relative: str) -> Path:
    target = output / _export_relative(relative)
    if not target.resolve().is_relative_to(output.resolve()):
        raise ToolkitError('Export path escapes its destination.')
    _export_file_hash(target)
    return target


def _export_file_hash(path: Path) -> str | None:
    if path.is_symlink() or any(parent.is_symlink() for parent in path.parents):
        raise ToolkitError('Export destination must not contain symlinks.')
    if not path.exists():
        return None
    if not path.is_file():
        raise ToolkitError(f'Export target is not a file: {path.name}')
    return digest(path.read_bytes())


def _export_manifest(path: Path) -> dict[str, str]:
    if _export_file_hash(path) is None:
        return {}
    try:
        old = json.loads(path.read_text(encoding='utf-8'))['files']
        if not isinstance(old, dict):
            raise ValueError('files must be an object')
        for relative, checksum in old.items():
            _export_relative(relative)
            if not isinstance(checksum, str) or not re.fullmatch(r'[0-9a-f]{64}', checksum):
                raise ValueError('invalid content digest')
        return old
    except (ValueError, KeyError, TypeError) as exc:
        raise ToolkitError('Invalid export manifest; select another output directory.') from exc


@contextmanager
def _export_writer(output: Path):
    # Cooperative exporters serialize; arbitrary editors still require coordination.
    lock = output / EXPORT_LOCK
    output.mkdir(parents=True, exist_ok=True)
    try:
        descriptor = os.open(lock, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
    except FileExistsError as exc:
        raise Conflict(f'Another export owns {lock}. If interrupted, verify its owner has stopped before removing this lock and retrying.') from exc
    try:
        with os.fdopen(descriptor, 'w', encoding='utf-8') as stream:
            json.dump({'pid': os.getpid()}, stream)
            stream.flush()
            os.fsync(stream.fileno())
        yield
    finally:
        lock.unlink(missing_ok=True)


def _recover_export(output: Path) -> None:
    """Roll back an uncommitted journal without replacing intervening edits."""
    journal_path = output / EXPORT_JOURNAL
    if _export_file_hash(journal_path) is None:
        return
    try:
        journal = json.loads(journal_path.read_text(encoding='utf-8'))
        if (journal['schemaVersion'] != 1 or journal['state'] not in {'pending', 'complete'}
                or not isinstance(journal['files'], dict)):
            raise ValueError('invalid transaction shape')
        before_manifest = journal['manifestBefore']
        if before_manifest is not None:
            before_manifest = base64.b64decode(before_manifest, validate=True)
        after_manifest = journal['manifestAfter']
        if not isinstance(after_manifest, str) or not re.fullmatch(r'[0-9a-f]{64}', after_manifest):
            raise ValueError('invalid manifest digest')
        recover = []
        for relative, record in journal['files'].items():
            target = _export_target(output, relative)
            before = record['before']
            if before is not None:
                before = base64.b64decode(before, validate=True)
            after = record['after']
            if after is not None and (not isinstance(after, str) or not re.fullmatch(r'[0-9a-f]{64}', after)):
                raise ValueError('invalid file digest')
            recover.append((target, before, after))
    except (ValueError, KeyError, TypeError) as exc:
        raise ToolkitError('Invalid interrupted export journal; preserve it and inspect the destination before retrying.') from exc
    manifest_path = output / EXPORT_MANIFEST
    current_manifest = _export_file_hash(manifest_path)
    if journal['state'] == 'complete':
        if current_manifest != after_manifest:
            raise Conflict('The manifest changed after an interrupted export committed; preserve the journal and reconcile the edit.')
        journal_path.unlink()
        return
    previous_manifest = digest(before_manifest) if before_manifest is not None else None
    if current_manifest not in {previous_manifest, after_manifest}:
        raise Conflict('The manifest changed during an interrupted export; preserve the journal and reconcile the edit.')
    for target, before, after in recover:
        current = _export_file_hash(target)
        previous = digest(before) if before is not None else None
        if current not in {previous, after}:
            raise Conflict(f'An interrupted export target was edited: {target.name}. Preserve the journal and reconcile the edit.')
    for target, before, after in recover:
        current = _export_file_hash(target)
        previous = digest(before) if before is not None else None
        if current == previous:
            continue
        if current != after:
            raise Conflict(f'Export recovery target changed: {target.name}. Preserve the journal and retry after reconciliation.')
        if before is None:
            target.unlink()
        else:
            _atomic_write_file(target, before, current)
    current_manifest = _export_file_hash(manifest_path)
    if current_manifest != previous_manifest:
        if current_manifest != after_manifest:
            raise Conflict('The manifest changed during export recovery; preserve the journal and reconcile the edit.')
        if before_manifest is None:
            manifest_path.unlink()
        else:
            _atomic_write_file(manifest_path, before_manifest, current_manifest)
    journal_path.unlink()


def _write_export(output: Path, planned: dict[str, bytes], runtime: str,
                  force: bool, dry_run: bool) -> dict[str, int]:
    manifest_path = output / EXPORT_MANIFEST

    def prepare():
        old = _export_manifest(manifest_path)
        hashes = {relative: digest(data) for relative, data in planned.items()}
        expected = {}
        changed, removed = [], []
        for relative in sorted(set(planned) | set(old)):
            target = _export_target(output, relative)
            current = _export_file_hash(target)
            expected[relative] = current
            if current is not None and not force and (relative not in old or current != old[relative]):
                raise ToolkitError(f'Refusing to overwrite an unmanaged or edited file: {relative}. Use a separate output or explicitly pass --force.')
            if relative in planned:
                if current != hashes[relative]:
                    changed.append(relative)
            elif current is not None:
                removed.append(relative)
        manifest = (json.dumps({'runtime': runtime, 'files': hashes}, indent=2) + '\n').encode()
        return changed, removed, expected, manifest

    if dry_run:
        if (output / EXPORT_LOCK).exists() or (output / EXPORT_JOURNAL).exists():
            raise Conflict('The export has an active writer or interrupted transaction; recover it before previewing.')
        changed, removed, _, _ = prepare()
    else:
        # Reject symlinked destinations before creating the writer lock.
        _export_file_hash(manifest_path)
        with _export_writer(output):
            _recover_export(output)
            changed, removed, expected, manifest = prepare()
            before_manifest = manifest_path.read_bytes() if manifest_path.exists() else None
            if changed or removed or before_manifest != manifest:
                journal = {
                    'schemaVersion': 1,
                    'state': 'pending',
                    'manifestBefore': base64.b64encode(before_manifest).decode() if before_manifest is not None else None,
                    'manifestAfter': digest(manifest),
                    'files': {relative: {
                        'before': base64.b64encode((output / relative).read_bytes()).decode() if expected[relative] is not None else None,
                        'after': digest(planned[relative]) if relative in planned else None,
                    } for relative in changed + removed},
                }
                journal_path = output / EXPORT_JOURNAL
                _atomic_write_file(journal_path, (json.dumps(journal, indent=2) + '\n').encode(), None)
                try:
                    for relative in changed:
                        atomic_write(output / relative, planned[relative], expected_hash=expected[relative])
                    for relative in removed:
                        target = output / relative
                        if _export_file_hash(target) != expected[relative]:
                            raise Conflict(f'Export target changed before removal: {relative}. Reload and retry.')
                        target.unlink()
                    if before_manifest != manifest:
                        atomic_write(manifest_path, manifest, expected_hash=digest(before_manifest) if before_manifest is not None else None)
                    pending_hash = _export_file_hash(journal_path)
                    journal['state'] = 'complete'
                    _atomic_write_file(journal_path, (json.dumps(journal, indent=2) + '\n').encode(), pending_hash)
                    journal_path.unlink()
                except BaseException as exc:
                    try:
                        _recover_export(output)
                    except (ToolkitError, OSError) as recovery_error:
                        raise ToolkitError(f'Export interrupted: {exc}. Recovery is pending: {recovery_error}') from exc
                    raise
    return {'changed': len(changed), 'unchanged': len(planned) - len(changed), 'removed': len(removed)}


@dataclass(frozen=True)
class OpenCodeOptions:
    plannotator: bool = False
    plan_model: str | None = None
    build_model: str | None = None
    plan_variant: str | None = None
    build_variant: str | None = None
    plan_directory: Path | None = None
    lead_model: str | None = None
    lead_variant: str | None = None
    worker_model: str | None = None
    worker_variant: str | None = None
    review_model: str | None = None
    review_variant: str | None = None

    def validate(self) -> None:
        if self.plan_directory is not None:
            directory = self.plan_directory
            if (not isinstance(directory, Path) or not directory.is_absolute()
                    or not directory.is_dir() or any(c in str(directory) for c in '*?[]\n\r')):
                raise ToolkitError('Plan directory must be an existing absolute directory without wildcard characters.')
            if directory.resolve() in {Path.home().resolve(), *Path.home().resolve().parents}:
                raise ToolkitError('Choose a dedicated plan directory, not a home directory or filesystem root.')
        for phase in ('plan', 'build', 'lead', 'worker', 'review'):
            model = getattr(self, f'{phase}_model')
            variant = getattr(self, f'{phase}_variant')
            if model is not None and (not isinstance(model, str) or not re.fullmatch(r'[^/\s#]+/[^\s#]+', model)):
                raise ToolkitError(f'{phase.title()} model must use provider/model-id, without whitespace or #variant.')
            if variant is not None:
                if model is None:
                    raise ToolkitError(f'{phase.title()} variant requires a configured {phase} model.')
                if not isinstance(variant, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]*', variant):
                    raise ToolkitError(f'{phase.title()} variant must be a model-supported variant name.')


HERD_UPSTREAM_REVISION = 'fbda6618c7b53524faddbed070e4fbc14970e412'
TEAM_LEADS = {'product-manager', 'lead-architect', 'task-orchestrator'}
HERD_LEADS = TEAM_LEADS | {'joerg'}
OPENCODE_LEAD_ROUTE = HERD_LEADS | {'plan', 'build', 'gcp-architect', 'test-strategist'}
OPENCODE_REVIEW_ROUTE = {'code-reviewer', 'architecture-reviewer'}


def _catalog_reading_links(planned: dict[str, bytes], root: Path) -> None:
    """Keep copied references local; point omitted public sources at their reading view."""
    for name, data in list(planned.items()):
        if not name.startswith('catalog/') or not name.endswith('.md'):
            continue
        source = root / name.removeprefix('catalog/')
        content = data.decode('utf-8')
        fences = [(match.start(), match.end()) for match in FENCE.finditer(content)]

        def rebase(match):
            if any(start <= match.start() < end for start, end in fences):
                return match[0]
            parts = urlsplit(match[1])
            if parts.scheme or parts.netloc or not parts.path:
                return match[0]
            original = (source.parent / unquote(parts.path)).resolve()
            if not original.is_relative_to(root.resolve()):
                raise ToolkitError(f'Catalog reference leaves the source repository: {source.relative_to(root)} -> {match[1]}')
            relative = original.relative_to(root.resolve())
            if _export_private_path(relative, directory=original.is_dir()):
                raise ToolkitError(f'Catalog references private or generated state: {source.relative_to(root)}')
            copied = 'catalog/' + relative.as_posix()
            if copied in planned or (original.is_dir() and any(path.startswith(copied + '/') for path in planned)):
                return match[0]
            if not original.exists():
                raise ToolkitError(f'Catalog reference does not exist: {source.relative_to(root)} -> {match[1]}')
            if relative.parts and relative.parts[0] in EXPORT_SOURCE_FOLDERS:
                raise ToolkitError(f'Catalog reference is excluded from export: {source.relative_to(root)} -> {match[1]}')
            view = 'tree' if original.is_dir() else 'blob'
            target = f'https://github.com/atstaeff/ai-agents/{view}/main/{quote(relative.as_posix(), safe="/")}'
            if parts.query:
                target += '?' + parts.query
            if parts.fragment:
                target += '#' + parts.fragment
            start, end = match.start(1) - match.start(), match.end(1) - match.start()
            return match[0][:start] + target + match[0][end:]

        planned[name] = LINK.sub(rebase, content).encode('utf-8')


def _herd_installed_markdown(text: str, exported_path: str, installed_path: str) -> str:
    """Convert workspace links to the reference skill installed by Herd's importer."""
    def rebase(match):
        parts = urlsplit(match.group(1))
        if parts.scheme or parts.netloc or not parts.path:
            return match[0]
        target = posixpath.normpath(posixpath.join(posixpath.dirname(exported_path), unquote(parts.path)))
        if not target.startswith('catalog/'):
            raise ToolkitError(f'Herd reference is outside the catalog: {target}')
        installed = 'skills/ai-agents-catalog/references/' + target
        relative = posixpath.relpath(installed, posixpath.dirname(installed_path))
        if parts.fragment:
            relative += '#' + parts.fragment
        return match[0].replace(match.group(1), relative)
    return LINK.sub(rebase, text)


def herd_files(entries: list[Entry], planned: dict[str, bytes], output: Path) -> dict[str, bytes]:
    """NickGuAI/Herd package v1 and portable import v2; no invented runtime fields.

    Source contract: apps/herd/modules/commanders/{packages/registry.ts,
    template-bundle.ts,routes/register-core.ts} at HERD_UPSTREAM_REVISION.
    Providers, models, effort and effective worker tools remain local settings.
    """
    if any(e.kind == 'skill' and e.name == 'ai-agents-catalog' for e in entries):
        raise ToolkitError('The ai-agents-catalog skill name is reserved by the Herd adapter.')
    agents = [e for e in entries if e.kind == 'agent']
    leads = [e for e in agents if e.name in HERD_LEADS] or agents[:1]
    skills = [e for e in entries if e.kind == 'skill']
    catalog_skill = (
        '---\nname: ai-agents-catalog\n'
        'description: Locate selected specialist profiles and shared references for a bounded Herd worker task.\n---\n\n'
        '# AI Agents catalog\n\n'
        'Read [selected specialists](references/SPECIALISTS.md) and '
        '[catalog metadata](references/catalog/index.json) before loading one relevant profile. '
        'Load only the instructions needed for the current task. '
        'Use the project\'s actual assignment and knowledge sources.\n\n'
        'Give each worker its role, bounded write scope, acceptance checks, context paths and '
        'expected evidence. Plan and reviewer workers require read-only tools configured '
        'in their execution host. These catalog instructions do not enforce tool permissions.\n'
    ).encode()
    specialist_index = '# Selected specialists\n\n| Role | Select for |\n| --- | --- |\n'
    for entry in agents:
        specialist_index += f'| [{entry.name}](catalog/{entry.path}) | {entry.description.replace("|", "&#124;")} |\n'
    reference_files = {'SKILL.md': catalog_skill, 'references/SPECIALISTS.md': specialist_index.encode()}
    reference_files.update({'references/' + name: data for name, data in planned.items() if name.startswith('catalog/')})

    def binding(skill_id: str, files: dict[str, bytes], required: bool) -> dict:
        # Herd's v2 parser requires nonempty base64 content for each bundled file.
        if any(not data for data in files.values()):
            raise ToolkitError(f'Herd cannot import an empty skill file: {skill_id}')
        return {'skillId': skill_id, 'source': 'commander-local', 'required': required,
                'bundle': {'dirName': skill_id, 'files': [
                    {'path': path, 'contentBase64': base64.b64encode(data).decode()}
                    for path, data in sorted(files.items())]}}

    native_skills = {}
    for entry in skills:
        source = f'herd/skills/{entry.name}/SKILL.md'
        body = _herd_installed_markdown(planned[source].decode(), source, f'skills/{entry.name}/SKILL.md')
        native_skills[entry.name] = {'SKILL.md': body.encode()}
        interface = f'herd/skills/{entry.name}/agents/openai.yaml'
        if interface in planned:
            native_skills[entry.name]['agents/openai.yaml'] = planned[interface]

    result = {}
    for lead in leads:
        directory = f'herd/commanders/{lead.name}'
        source = f'herd/specialists/{lead.name}.md'
        _, body = metadata(planned[source].decode())
        commander_md = _herd_installed_markdown(body, source, 'COMMANDER.md')
        commander_md += ('\n## Herd handoff\n\n'
                         'Use the installed ai-agents-catalog skill to select a specialist. '
                         'Dispatch only authorized work with a bounded scope and expected evidence; '
                         'verify the combined result before completion. Configure provider, model, '
                         'effort and worker tool restrictions in Herd and the worker host.\n')
        required = {'agent-routing', 'repository-contribution', 'work-management'}
        canonical = planned[f'catalog/{lead.path}'].decode()
        required.update(entry.name for entry in skills if f'/{entry.name}/SKILL.md' in canonical)
        skill_metadata = [{'id': 'ai-agents-catalog', 'label': 'AI Agents catalog',
                           'purpose': 'Load selected specialist instructions and shared references on demand.', 'required': True}]
        skill_metadata += [{'id': entry.name, 'label': entry.name, 'purpose': entry.description,
                            'required': entry.name in required} for entry in skills]
        manifest = {key: [{k: v for k, v in item.items() if k != 'required'}
                          for item in skill_metadata if item['required'] == is_required]
                    for key, is_required in (('required', True), ('optional', False))}
        package = {'schemaVersion': 1, 'id': lead.name, 'version': '1.0.0',
                   'displayName': lead.name.replace('-', ' ').title(), 'host': lead.name,
                   'role': lead.name.replace('-', ' ').title(), 'summary': lead.description,
                   'description': lead.description}
        result[directory + '/package.json'] = (json.dumps(package, indent=2) + '\n').encode()
        result[directory + '/COMMANDER.md'] = commander_md.encode()
        result[directory + '/skills.manifest.json'] = (json.dumps(manifest, indent=2) + '\n').encode()
        result[directory + '/memory-seed.md'] = b'# Memory\n\nNo operator memory is included. Read the assigned project sources.\n'
        result[directory + '/onboarding.md'] = (
            '# Install\n\nImport the corresponding `.bundle.json` from `herd/imports/` '
            'with Herd Marketplace\'s Install from file action. Select the execution '
            'machine, project directory, provider, model and effort locally before dispatching work. '
            'Package manifests describe dependencies; the portable bundle embeds them.\n'
        ).encode()
        if 'catalog/LICENSE' in planned:
            result[directory + '/LICENSE'] = planned['catalog/LICENSE']
        bindings = [binding('ai-agents-catalog', reference_files, True)]
        bindings += [binding(entry.name, native_skills[entry.name], entry.name in required) for entry in skills]
        bundle = {'schemaVersion': 2, 'exportedAt': datetime.now(UTC).isoformat(),
                  'commander': {'displayName': package['displayName'], 'host': lead.name},
                  'commanderMd': commander_md, 'memorySnapshot': {'memoryMd': '', 'syncRevision': 0},
                  'skills': skill_metadata, 'skillBindings': bindings, 'automations': []}
        destination = f'herd/imports/{lead.name}.bundle.json'
        existing = output / destination
        if _export_file_hash(existing) is not None:
            try:
                previous = json.loads(existing.read_text(encoding='utf-8'))
                comparison = {**bundle, 'exportedAt': previous['exportedAt']}
                if isinstance(previous['exportedAt'], str) and comparison == previous:
                    bundle = comparison
            except (ValueError, KeyError, TypeError):
                pass  # Normal ownership validation reports edited files before writing.
        result[destination] = (json.dumps(bundle, indent=2) + '\n').encode()
    result['herd/README.md'] = (
        '# Herd export\n\n'
        'Target: NickGuAI/Herd, not HerdOS or Herdr. Import each selected leader from '
        '`imports/*.bundle.json` using Marketplace → Install from file. `commanders/` contains '
        'inspectable package-v1 sources; `skills/` and `specialists/` are workspace references. '
        'The v2 import installs selected skills and an on-demand reference catalog.\n\n'
        'Choose project directory, machine, provider, model, effort and worker permissions in '
        'the local Herd installation. Imports inherit its default provider. Backend package-v1 '
        'loading defaults an omitted provider to Claude. This adapter supplies no automatic '
        'model-tier routing, enforced tool restrictions, credentials, automations or private memory. '
        'Validate discovery, references and effective permissions on your installed version.\n\n'
        f'Upstream schema reviewed at https://github.com/NickGuAI/Herd/tree/{HERD_UPSTREAM_REVISION}: '
        '`docs/guides/commander-packages.md`, `docs/guides/commander-bundles.md`, '
        '`apps/herd/modules/commanders/packages/registry.ts`, '
        '`apps/herd/modules/commanders/template-bundle.ts` and '
        '`apps/herd/modules/commanders/routes/register-core.ts`.\n'
    ).encode()
    return result


def export(runtime: str, output: Path, root: Path = ROOT, force: bool = False, dry_run: bool = False,
           *, opencode_options: OpenCodeOptions | None = None, preset: str = 'all',
           agent_names: tuple[str, ...] = (), skill_names: tuple[str, ...] = ()) -> dict:
    if runtime not in RUNTIMES:
        raise ToolkitError("Unknown runtime.")
    options = opencode_options or OpenCodeOptions()
    if runtime != 'opencode' and options != OpenCodeOptions():
        raise ToolkitError('Plannotator, model, variant and plan-directory options require --runtime opencode.')
    options.validate()
    plan_directory = options.plan_directory.resolve() if options.plan_directory else None
    if plan_directory and (root.resolve().is_relative_to(plan_directory)
                           or plan_directory.is_relative_to(root.resolve())):
        raise ToolkitError('Keep the personal plan directory outside the source repository.')
    output = output.absolute()
    if plan_directory and (output.resolve().is_relative_to(plan_directory)
                           or plan_directory.is_relative_to(output.resolve())):
        raise ToolkitError('Keep generated bundles separate from personal plan directories.')
    if output.resolve() == root.resolve() or output.resolve() in root.resolve().parents:
        raise ToolkitError("Export to a separate directory, not the source repository or its parent.")
    if any(output.resolve().is_relative_to((root / folder).resolve()) for folder in ('agents','skills','toolkit','templates','marp-templates','reference-repos','tools','assets','website')):
        raise ToolkitError('Export outside canonical source folders.')
    source_files = _export_source_files(root)
    planned = {'catalog/' + name: data for name, data in source_files.items()}
    license_path = root / 'LICENSE'
    if license_path.is_symlink():
        raise ToolkitError('Cannot export a symlinked license.')
    if license_path.is_file():
        planned['catalog/LICENSE'] = license_path.read_bytes()
    _catalog_reading_links(planned, root)
    entries = select_entries(catalog(root, source_files=source_files), preset, agent_names, skill_names)
    selected_agents = {e.name for e in entries if e.kind == 'agent'}
    for phase in ('plan', 'build'):
        if (getattr(options, f'{phase}_model') or getattr(options, f'{phase}_variant')
                or (phase == 'plan' and (options.plannotator or options.plan_directory))) and phase not in selected_agents:
            raise ToolkitError(f'{phase} options require selecting the {phase} agent.')
    planned['catalog/index.json'] = (json.dumps([asdict(e) for e in entries], indent=2) + '\n').encode()
    for entry in entries:
        if entry.kind == "skill":
            base = {"opencode": "skills", "copilot": ".github/skills", "claude": ".claude/skills", "portable": ".agents/skills", "herd": "herd/skills"}[runtime]
            destination = f"{base}/{entry.name}/SKILL.md"
            interface = 'catalog/' + (Path(entry.path).parent / 'agents/openai.yaml').as_posix()
            if interface in planned:
                planned[f'{base}/{entry.name}/agents/openai.yaml'] = planned[interface]
        else:
            base = {"opencode": "agents", "copilot": ".github/agents", "claude": ".claude/agents", "portable": "agents", "herd": "herd/specialists"}[runtime]
            suffix = ".md" if runtime in {"opencode", "claude", "herd"} else ".agent.md"
            destination = f"{base}/{entry.name}{suffix}"
        meta, body = metadata(planned[f'catalog/{entry.path}'].decode('utf-8'))
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
            mode = ('all' if entry.name in TEAM_LEADS else
                    'primary' if entry.name in {'joerg', 'plan', 'build'} else 'subagent')
            header += f"mode: {mode}\n"
            if entry.name in {"code-reviewer", "architecture-reviewer", "plan"}:
                header += "permission:\n  edit:\n    '*': deny\n"
                if entry.name == "plan" and plan_directory:
                    header += f'    {json.dumps(str(plan_directory) + "/*.md")}: allow\n'
                    header += f'  external_directory:\n    {json.dumps(str(plan_directory) + "/*")}: allow\n'
                header += "  bash: deny\n  task: deny\n"
                if entry.name == 'plan' and options.plannotator:
                    header += "  submit_plan: allow\n  plan_exit: deny\n"
            if entry.name == 'plan' and options.plannotator:
                body += '\nPlannotator plan review is enabled. Submit the current plan with `submit_plan` using the installed tool schema. Incorporate requested changes and resubmit; do not hand off to implementation until the user approves this revision. If the tool fails or is unavailable, remain in planning and request explicit review in the current conversation. Tool feedback never expands host permissions.\n'
        elif entry.kind == "agent" and runtime == "copilot":
            if entry.name in {"code-reviewer", "architecture-reviewer", "plan"}:
                header += "tools: [read, search]\n"
                body += '\nThis adapter provides read/search tools only. Return a proposed patch or plan; writing a work record requires switching to a writing agent.\n'
        elif entry.kind == "agent" and runtime == "claude":
            if entry.name in {"code-reviewer", "architecture-reviewer", "plan"}:
                header += "tools: Read, Grep, Glob\n"
                body += '\nThis adapter permits file reading and search only. Return proposed plans or findings to the coordinating session; it owns required review, record updates and executable verification. Do not claim checks you cannot run.\n'
        planned[destination] = (header + "---\n\n" + body).encode()
    if runtime == "opencode":
        preferred = catalog_presets()[preset].get('default_agent', 'joerg')
        config = {"$schema": "https://opencode.ai/config.json", "default_agent": preferred if preferred in selected_agents else next(e.name for e in entries if e.kind == "agent"),
                  "instructions": [str(output / "catalog/toolkit/SESSION-RULES.md")],
                  "permission": {"external_directory": {str(output / 'catalog') + '/*': 'allow'},
                                 "edit": {str(output / 'catalog') + '/*': 'deny'}}}
        if plan_directory:
            private_name = 'private-planning.md'
            planned[private_name] = (
                '# Private planning location\n\n'
                f'Personal working plans belong in this existing directory: {plan_directory}\n'
                'Keep one Markdown plan per outcome. Preserve existing notes and comments.\n'
                'Do not copy personal paths or plan contents into shared project artifacts.\n'
                'Resolve the exact vault name and vault-relative path from private user instructions\n'
                'before constructing an Obsidian URI; never invent them.\n'
            ).encode()
            config['instructions'].append(str(output / private_name))
        for entry in entries:
            if entry.kind != 'agent':
                continue
            route = ('review' if entry.name in OPENCODE_REVIEW_ROUTE else
                     'lead' if entry.name in OPENCODE_LEAD_ROUTE else 'worker')
            model, variant = getattr(options, f'{route}_model'), getattr(options, f'{route}_variant')
            if model is not None:
                settings = {'model': model}
                if variant is not None:
                    settings['variant'] = variant
                config.setdefault('agent', {})[entry.name] = settings
        for phase in ('plan', 'build'):
            model = getattr(options, f'{phase}_model')
            variant = getattr(options, f'{phase}_variant')
            if model is not None:
                # An explicit phase model replaces its route, including the old variant.
                settings = {'model': model}
                if variant is not None:
                    settings['variant'] = variant
                config.setdefault('agent', {})[phase] = settings
        if options.plannotator:
            # Let our native profiles own prompts and permissions. The plugin's
            # plan-agent mode would also allow edits to all Markdown files.
            config['plugin'] = [['@plannotator/opencode@latest', {'workflow': 'user-managed'}]]
            config['share'] = 'disabled'
            config['permission']['submit_plan'] = 'deny'
        planned['opencode.json'] = (json.dumps(config, indent=2) + '\n').encode()
        for name, agent, description in (("work-plan", "plan", "Plan an outcome in its existing planning home"), ("work-build", "build", "Implement and verify the current authorized plan"), ("brain", "second-brain", "Maintain the private PARA vault")):
            if agent not in selected_agents:
                continue
            planned[f'commands/{name}.md'] = f'---\ndescription: {description}\nagent: {agent}\n---\n\nFollow project instructions and load the next relevant skill only when needed. $ARGUMENTS\n'.encode()
    elif runtime == "copilot":
        planned['.github/copilot-instructions.md'] = b'At session start, read and apply `catalog/toolkit/SESSION-RULES.md`; reuse a matching loaded copy. Follow project-specific instructions. The authorized assignment activates autonomous team coordination within host permissions; load only the relevant skills.\n'
    elif runtime == "claude":
        planned['CLAUDE.md'] = b'@catalog/toolkit/SESSION-RULES.md\n'
    elif runtime == 'portable':
        planned['AGENTS.md'] = (
            '# Shared AI workflow\n\n'
            'At session start, read and apply [session rules](catalog/toolkit/SESSION-RULES.md); '
            'reuse a matching loaded copy. Follow applicable project instructions and host permissions. '
            'The authorized assignment activates autonomous team coordination. '
            'Load only the next relevant skill, not the full catalog.\n'
        ).encode()
    elif runtime == 'herd':
        planned.update(herd_files(entries, planned, output))
    changes = _write_export(output, planned, runtime, force, dry_run)
    return {'runtime': runtime, 'preset': preset, 'metadata_characters': sum(len(e.name) + len(e.description) for e in entries), 'output': str(output), 'agents': sum(e.kind == 'agent' for e in entries), 'skills': sum(e.kind == 'skill' for e in entries), 'files': len(planned), **changes, 'dry_run': dry_run}


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
            raise ToolkitError('Workspace must be an existing project-root directory.')
        self.lock = threading.RLock()

    def _checked_path(self, path: Path) -> Path:
        if not path.resolve().is_relative_to(self.workspace) or any(p.is_symlink() for p in [path, *path.parents] if p != self.workspace):
            raise ToolkitError('Work records must not traverse symlinks or leave the workspace.')
        return path

    def path(self, name: str, archived: bool = False) -> Path:
        name = slug(name)
        for folder in ('work', 'archive'):
            old = self._checked_path(self.workspace / '.ai' / folder)
            if old.exists() and (not old.is_dir() or any(old.iterdir())):
                raise ToolkitError('Legacy .ai work records exist. Stop writers and run work --workspace <project-root> migrate --dry-run, then migrate; do not create a parallel plan.')
        return self._checked_path(self.workspace / 'workspace' / ('archive' if archived else 'work') / f'{name}.md')

    def migrate(self, dry_run: bool = False) -> dict:
        """Explicitly move legacy record directories, preserving bytes and relative layout."""
        with self.lock:
            moves = []
            for folder in ('work', 'archive'):
                source = self._checked_path(self.workspace / '.ai' / folder)
                destination = self._checked_path(self.workspace / 'workspace' / folder)
                if not source.exists():
                    continue
                if not source.is_dir():
                    raise ToolkitError(f'Legacy work path is not a directory: {source.relative_to(self.workspace)}')
                if destination.exists():
                    raise Conflict(f'Migration destination already exists: workspace/{folder}. Reconcile the two directories manually; no automatic merge or overwrite.')
                for path in source.rglob('*'):
                    self._checked_path(path)
                    if not path.is_dir() and not path.is_file():
                        raise ToolkitError('Migration accepts only regular files and directories.')
                moves.append((source, destination))
            if not dry_run:
                for source, destination in moves:
                    self._checked_path(destination)
                    if destination.exists():
                        raise Conflict('Migration destination changed. Stop all writers and inspect both locations before retrying.')
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    source.rename(destination)
            legacy_root = self._checked_path(self.workspace / '.ai')
            removed = False
            if not dry_run and legacy_root.is_dir():
                try:
                    legacy_root.rmdir()
                    removed = True
                except OSError as exc:
                    # Preserve unknown files, including anything added after the moves.
                    if exc.errno not in {errno.ENOTEMPTY, errno.EEXIST}:
                        raise
            return {'dry_run': dry_run,
                    'legacy_directory_removed': removed,
                    'legacy_directory_remaining': legacy_root.exists(),
                    'moves': [
                {'from': source.relative_to(self.workspace).as_posix(),
                 'to': destination.relative_to(self.workspace).as_posix()}
                for source, destination in moves]}

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
            text = (ROOT/'templates/delivery/work-item.md').read_text(encoding='utf-8')
            text = text.replace('{{id}}', slug(name)).replace('{{title_json}}', json.dumps(title, ensure_ascii=False)).replace('{{kind}}', kind).replace('{{title}}', title.replace('\n', ' '))
            atomic_write(path, text.encode(), expected_hash=None)
            return self.read(name)

    def update(self, name: str, etag: str, transform) -> dict:
        with self.lock:
            current = self.read(name)
            if etag != current['etag']:
                raise Conflict('This record changed. Reload it before saving; your feedback has not been discarded.')
            text = transform(current['markdown'])
            # Catch edits made by the transform; atomic_write checks again after
            # preparing and flushing its temporary file.
            if self.read(name)['etag'] != etag:
                raise Conflict('The file changed while preparing the update. Reload and retry.')
            if len(text.encode()) > MAX_RECORD:
                raise ToolkitError('Work record exceeds the size limit.')
            atomic_write(self.path(name), text.encode(), expected_hash=current['etag'][1:-1])
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
            source = self.path(name)
            data = re.sub(r'^status:.*$', 'status: archived', current['markdown'], count=1, flags=re.M).encode()
            atomic_write(destination, data, expected_hash=None)
            archive_hash = digest(data)
            # Prepare the archive without changing the active record. If an
            # editor saved or removal fails, retain the active file and clean up
            # only the unedited archive created above. Failed creation never
            # enters this cleanup. This is a local check, not filesystem CAS.
            try:
                if _export_file_hash(source) != current['etag'][1:-1]:
                    raise Conflict('Record changed while preparing the archive. Reload and retry.')
                if _export_file_hash(destination) != archive_hash:
                    raise Conflict('Archive changed while preparing the move; the active record was retained.')
                source.unlink()
            except (ToolkitError, OSError) as exc:
                try:
                    if (_export_file_hash(source) is not None
                            and _export_file_hash(destination) == archive_hash):
                        destination.unlink()
                except (ToolkitError, OSError) as cleanup_error:
                    raise ToolkitError(f'Archive cleanup is pending: {cleanup_error}. Inspect active and archive copies before retrying.') from exc
                raise
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
                    if path == '/api/v1/catalog/domains':
                        return self.reply(200, domains())
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
    cat.add_argument('--preset', choices=list(catalog_presets()), default='all')
    cat.add_argument('--kind', choices=['agent','skill'])
    cat.add_argument('--domain', choices=list(domains()), help='Select a catalog discipline')
    cat.add_argument('--format', choices=['json', 'markdown'], default='json')
    adapter = sub.add_parser('export', help='Export isolated native runtime profiles')
    adapter.add_argument('--runtime', choices=sorted(RUNTIMES), required=True)
    adapter.add_argument('--output', type=Path, required=True)
    adapter.add_argument('--preset', choices=list(catalog_presets()), default='all', help='Native profile selection; all preserves existing behavior')
    adapter.add_argument('--agent', action='append', default=[], help='Add a named agent to the preset')
    adapter.add_argument('--skill', action='append', default=[], help='Add a named skill to the preset')
    adapter.add_argument('--force', action='store_true')
    adapter.add_argument('--dry-run', action='store_true')
    adapter.add_argument('--plannotator', action='store_true', help='Enable local Plannotator plan review in OpenCode 1')
    adapter.add_argument('--plan-model', help='OpenCode planning model: provider/model-id')
    adapter.add_argument('--build-model', help='OpenCode implementation model: provider/model-id')
    adapter.add_argument('--plan-variant', help='Variant supported by the configured planning model')
    adapter.add_argument('--plan-directory', type=Path, help='Existing absolute private directory for personal Markdown plans (OpenCode only)')
    adapter.add_argument('--build-variant', help='Variant supported by the configured implementation model')
    for route in ('lead', 'worker', 'review'):
        adapter.add_argument(f'--{route}-model', help=f'OpenCode {route} route: provider/model-id (configure once)')
        adapter.add_argument(f'--{route}-variant', help=f'Variant supported by the configured {route} model')
    uri = sub.add_parser('obsidian-uri', help='Encode a Windows Obsidian URI')
    uri.add_argument('--vault', required=True)
    uri.add_argument('--file', required=True)
    web = sub.add_parser('serve', help='Serve the local catalog and work dashboard on loopback only')
    web.add_argument('--workspace', type=Path, default=Path.cwd(), help='Project root; records live beneath workspace/work/')
    web.add_argument('--port', type=int, default=4097)
    work = sub.add_parser('work', help='Create and maintain one-file work records')
    work.add_argument('--workspace', type=Path, default=Path.cwd(), help='Project root; records live beneath workspace/work/')
    operations = work.add_subparsers(dest='operation', required=True)
    new = operations.add_parser('new')
    new.add_argument('id')
    new.add_argument('--title', required=True)
    new.add_argument('--kind', choices=['software','product','general'], default='software')
    listing = operations.add_parser('list')
    listing.add_argument('--archived', action='store_true')
    migration = operations.add_parser('migrate', help='Move legacy .ai work/archive directories into workspace; stop writers first')
    migration.add_argument('--dry-run', action='store_true')
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
            entries = [e for e in select_entries(catalog(), args.preset) if (args.kind is None or e.kind == args.kind)
                       and (args.domain is None or e.domain == args.domain)]
            print(catalog_markdown(entries, args.kind) if args.format == 'markdown'
                  else json.dumps([asdict(e) for e in entries], indent=2),
                  end='' if args.format == 'markdown' else '\n')
        elif args.command == 'export':
            options = OpenCodeOptions(
                plannotator=args.plannotator, plan_model=args.plan_model, build_model=args.build_model,
                plan_variant=args.plan_variant, build_variant=args.build_variant, plan_directory=args.plan_directory,
                lead_model=args.lead_model, lead_variant=args.lead_variant,
                worker_model=args.worker_model, worker_variant=args.worker_variant,
                review_model=args.review_model, review_variant=args.review_variant)
            print(json.dumps(export(args.runtime, args.output, force=args.force, dry_run=args.dry_run,
                                    opencode_options=options, preset=args.preset,
                                    agent_names=tuple(args.agent), skill_names=tuple(args.skill)), indent=2))
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
            elif args.operation == 'migrate':
                result = store.migrate(args.dry_run)
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
