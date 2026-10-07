"""Render website catalog pages from canonical sources, with no duplicated instructions."""
from pathlib import Path
import os
import sys
from urllib.parse import quote, unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ai_toolkit import ROOT, LINK, catalog, metadata

DOCUMENTS = {
    'getting-started/workflow.md': 'toolkit/WORKFLOW.md',
    'getting-started/installation.md': 'toolkit/RUNTIMES.md',
    'toolkit/work-records.md': 'toolkit/WORK-RECORDS.md',
    'toolkit/api.md': 'toolkit/API.md',
    'contributing/index.md': 'CONTRIBUTING.md',
}
ENTRIES = []
SOURCES = {}
REVERSE = {}


def on_pre_build(config):
    """Refresh once per build, including each rebuild under mkdocs serve."""
    global ENTRIES, SOURCES, REVERSE
    ENTRIES = catalog()
    SOURCES = {f'{e.kind}s/{e.name}.md': e.path for e in ENTRIES}
    SOURCES.update(DOCUMENTS)
    REVERSE = {value: key for key, value in SOURCES.items()}


def on_page_markdown(markdown, page, config, files):
    source = SOURCES.get(page.file.src_uri)
    if page.file.src_uri == 'skills/feature-discovery.md':
        source = 'skills/team-collaboration/feature-discovery-session.md'
    if page.file.src_uri in {'agents/index.md','skills/index.md'}:
        kind = page.file.src_uri.split('/')[0][:-1]
        title = 'Agents' if kind == 'agent' else 'Skills'
        relevant = [e for e in ENTRIES if e.kind == kind]
        text = f'# {title}\n\n{len(relevant)} English profiles generated from canonical sources. Select by outcome; load focused references only when needed.\n\n'
        text += '| Name | Use when |\n| --- | --- |\n'
        for entry in relevant:
            text += f'| [{entry.name}]({entry.name}.md) | {entry.description.replace("|", "&#124;")} |\n'
        return text
    if not source:
        return markdown
    text = (ROOT/source).read_text(encoding='utf-8')
    if text.startswith('---\n'):
        meta, text = metadata(text)
        page.meta['description'] = meta['description']
    def rewrite(match):
        target = match.group(1)
        parts = urlsplit(target)
        if parts.scheme or parts.netloc or not parts.path:
            return match[0]
        resolved = ((ROOT/source).parent/unquote(parts.path)).resolve().relative_to(ROOT)
        if resolved.as_posix() in REVERSE:
            destination = Path(os.path.relpath(REVERSE[resolved.as_posix()],Path(page.file.src_uri).parent)).as_posix()
            if parts.fragment:
                destination += '#' + parts.fragment
        else:
            destination = 'https://github.com/atstaeff/ai-agents/blob/main/' + quote(resolved.as_posix(),safe='/')
            if parts.fragment:
                destination += '#' + parts.fragment
        return match[0].replace(target,destination)
    text = LINK.sub(rewrite,text)
    page.edit_url = 'https://github.com/atstaeff/ai-agents/edit/main/' + source
    return text + f'\n---\nCanonical source: [`{source}`](https://github.com/atstaeff/ai-agents/blob/main/{source}).\n'
