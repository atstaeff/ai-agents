"""Render website catalog pages from canonical sources, with no duplicated instructions."""
from pathlib import Path
from html import escape
import json
import math
import os
import re
import sys
from urllib.parse import quote, unquote, urlsplit

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ai_toolkit import ROOT, LINK, catalog, metadata

DOCUMENTS = {
    'concept.md': 'toolkit/OPERATING-MODEL.md',
    'getting-started/workflow.md': 'toolkit/WORKFLOW.md',
    'getting-started/installation.md': 'toolkit/RUNTIMES.md',
    'getting-started/plan-review.md': 'toolkit/PLAN-REVIEW.md',
    'toolkit/work-records.md': 'toolkit/WORK-RECORDS.md',
    'toolkit/api.md': 'toolkit/API.md',
    'references/customer-workspace.md': 'templates/customer-workspace/README.md',
    'customer-workspace/context.md': 'templates/customer-workspace/workspace/README.md',
    'customer-workspace/working-agreement.md': 'templates/customer-workspace/workspace/working-agreement.md',
    'customer-workspace/stakeholders.md': 'templates/customer-workspace/workspace/stakeholders.md',
    'customer-workspace/project.md': 'templates/customer-workspace/examples/github-project.md',
    'customer-workspace/assignment.md': 'templates/customer-workspace/examples/issue-42.md',
    'customer-workspace/questions.md': 'templates/customer-workspace/examples/discussion-42.md',
    'customer-workspace/plan-review.md': 'templates/customer-workspace/examples/plan-review.md',
    'customer-workspace/review.md': 'templates/customer-workspace/examples/pull-request-57.md',
    'customer-workspace/decisions/adr-0001.md': 'templates/customer-workspace/workspace/decisions/0001-retry-safe-upload.md',
    'customer-workspace/decisions/adr-0002.md': 'templates/customer-workspace/workspace/decisions/0002-atomic-upload-claim.md',
    'customer-workspace/knowledge.md': 'templates/customer-workspace/workspace/knowledge/upload-retries.md',
    'customer-workspace/iteration.md': 'templates/customer-workspace/workspace/iterations/I1.md',
    'customer-workspace/knowledge-map.md': 'templates/customer-workspace/workspace/knowledge-map.md',
    'customer-workspace/docusaurus.md': 'templates/customer-workspace/examples/docusaurus-integration.md',
    'customer-workspace/runner.md': 'templates/customer-workspace/examples/local-runner.md',
    'contributing/index.md': 'CONTRIBUTING.md',
}
ENTRIES = []
SOURCES = {}
REVERSE = {}
KNOWLEDGE_GRAPH = {}


def on_pre_build(config):
    """Refresh once per build, including each rebuild under mkdocs serve."""
    global ENTRIES, SOURCES, REVERSE, KNOWLEDGE_GRAPH
    ENTRIES = catalog()
    SOURCES = {f'{e.kind}s/{e.name}.md': e.path for e in ENTRIES}
    SOURCES.update(DOCUMENTS)
    REVERSE = {value: key for key, value in SOURCES.items()}
    KNOWLEDGE_GRAPH = json.loads((ROOT / 'templates/customer-workspace/examples/knowledge-graph.json').read_text(encoding='utf-8'))


def knowledge_diagram(graph, page_uri, directory_urls=True):
    """Link the generated example records without loading an external renderer."""
    nodes = graph['nodes']
    if not nodes:
        return '<p>No knowledge records are available.</p>'
    columns = 2
    rows = math.ceil(len(nodes) / columns)
    positions = {node['id']: (220 + (index % columns) * 420, 90 + (index // columns) * 245)
                 for index, node in enumerate(nodes)}
    height = 180 + (rows - 1) * 245
    svg = [f'<div class="knowledge-diagram"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 {height}" role="group" aria-labelledby="knowledge-title knowledge-description">',
           '<title id="knowledge-title">Customer knowledge relationships</title>',
           '<desc id="knowledge-description">Links between decisions, process knowledge and iteration outcomes. Select a record to open it; the relationship table provides the same connections.</desc>',
           '<defs><marker id="knowledge-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" /></marker></defs>']
    labels = []
    for edge in graph['edges']:
        sx, sy = positions[edge['source']]
        tx, ty = positions[edge['target']]
        dx, dy = tx - sx, ty - sy
        scale = min(105 / abs(dx) if dx else math.inf,
                    38 / abs(dy) if dy else math.inf)
        start = (sx + dx * scale, sy + dy * scale)
        end = (tx - dx * scale, ty - dy * scale)
        svg.append(f'<line class="knowledge-edge" x1="{start[0]:.1f}" y1="{start[1]:.1f}" x2="{end[0]:.1f}" y2="{end[1]:.1f}" marker-end="url(#knowledge-arrow)" />')
        offset = -24 if edge['type'] == 'governed_by' else 20 if dx and dy else -12
        labels.append(f'<text class="knowledge-label" text-anchor="middle" x="{(sx + tx)/2:.1f}" y="{(sy + ty)/2 + offset:.1f}">{escape(edge["type"])}</text>')
    svg.extend(labels)
    for node in nodes:
        source = 'templates/customer-workspace/workspace/' + node['path']
        destination = Path(REVERSE[source])
        current = Path(page_uri)
        if directory_urls:
            href = Path(os.path.relpath(destination.with_suffix(''), current.with_suffix(''))).as_posix() + '/'
        else:
            href = Path(os.path.relpath(destination.with_suffix('.html'), current.parent)).as_posix()
        x, y = positions[node['id']]
        label = escape(f'{node["title"]}; {node["status"]}', quote=True)
        svg.extend([f'<a href="{escape(href, quote=True)}" tabindex="0" aria-label="{label}">',
                    f'<rect x="{x-105}" y="{y-38}" width="210" height="76" rx="10" />',
                    f'<text class="knowledge-id" text-anchor="middle" x="{x}" y="{y-5}">{escape(node["id"])}</text>',
                    f'<text class="knowledge-status" text-anchor="middle" x="{x}" y="{y+21}">{escape(node["status"])}</text>',
                    '</a>'])
    return '\n'.join(svg + ['</svg></div>'])


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
        if source in DOCUMENTS.values():
            frontmatter = re.match(r'\A---\n.*?\n---(?:\n|$)', text, re.S)
            if not frontmatter:
                raise ValueError(f'Unclosed documentation frontmatter: {source}')
            text = text[frontmatter.end():]
        else:
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
        start = match.start(1) - match.start()
        end = match.end(1) - match.start()
        return match[0][:start] + destination + match[0][end:]
    text = LINK.sub(rewrite,text)
    if page.file.src_uri == 'customer-workspace/knowledge-map.md':
        diagram = knowledge_diagram(KNOWLEDGE_GRAPH, page.file.src_uri, config.get('use_directory_urls', True))
        text = re.sub(r'```mermaid\n.*?\n```', lambda match: diagram, text, count=1, flags=re.S)
    page.edit_url = 'https://github.com/atstaeff/ai-agents/edit/main/' + source
    return text + f'\n---\nCanonical source: [`{source}`](https://github.com/atstaeff/ai-agents/blob/main/{source}).\n'
