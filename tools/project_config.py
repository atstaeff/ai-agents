# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML>=6,<7", "jsonschema>=4,<5"]
# ///
"""Validate declarative project tooling; never connect to systems or execute commands."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml
from jsonschema import Draft202012Validator

LOCATIONS = ('work', 'review', 'knowledge', 'decisions', 'iteration_reports', 'communication')
SCHEMA = json.loads((Path(__file__).resolve().parents[1] / 'toolkit/workspace.schema.json').read_text(encoding='utf-8'))
REQUIRED = set(SCHEMA['allOf'][0]['else']['required'])


class UniqueLoader(yaml.SafeLoader):
    """Reject ambiguous mappings instead of silently accepting the last key."""


def unique_mapping(loader, node, deep=False):
    loader.flatten_mapping(node)
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if not isinstance(key, str):
            raise ValueError('Configuration keys must be strings.')
        if key in result:
            raise ValueError(f'Duplicate configuration key: {key}')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def validate(data):
    errors = sorted(Draft202012Validator(SCHEMA).iter_errors(data), key=lambda error: str(list(error.path)))
    if errors:
        error = errors[0]
        label = '.'.join(str(part) for part in error.path) or 'configuration'
        raise ValueError(f'{label}: {error.message}')
    names = [repo['name'] for repo in data.get('repositories', [])]
    if len(names) != len(set(names)):
        raise ValueError('repositories names must be unique.')
    states = list(data.get('flow', {}).get('states', {}).values())
    if len(states) != len(set(states)):
        raise ValueError('flow.states must map to distinct board states.')
    return data


def markdown_sections(text):
    """Extract ATX sections, excluding fenced examples, comments and frontmatter."""
    text = re.sub(r'\A---\s*\n.*?\n---\s*\n', '', text, count=1, flags=re.S)
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    lines = []
    fence = None
    for line in text.splitlines():
        marker = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    headings = []
    seen = set()
    for index, line in enumerate(lines):
        match = re.match(r'^ {0,3}(#{1,6})\s+(.+?)\s*#*\s*$', line)
        if match:
            base = re.sub(r'[^\w\- ]', '', match[2].lower()).replace(' ', '-')
            slug, count = base, 0
            while slug in seen:
                count += 1
                slug = f'{base}-{count}'
            seen.add(slug)
            headings.append((index, len(match[1]), slug))
    sections = {'': '\n'.join(lines)}
    for position, (start, depth, slug) in enumerate(headings):
        end = next((index for index, level, _ in headings[position + 1:] if level <= depth), len(lines))
        sections[slug] = '\n'.join(lines[start + 1:end])
    return sections


def check_sources(data, project_root):
    """Check required version-2 pointers, never fetching remote or executing content."""
    root = project_root.resolve()
    references = {key: data[key] for key in
                  ('vision', 'stakeholders', 'scope', 'process')}
    errors = []
    for key, reference in references.items():
        try:
            parts = urlsplit(reference)
            if parts.scheme or parts.netloc or parts.query:
                raise ValueError('use a local Markdown entry; link external detail from that entry')
            target = (root / unquote(parts.path)).resolve()
            if not target.is_relative_to(root) or Path(unquote(parts.path)).is_absolute():
                raise ValueError('source must stay inside the project root')
            if target.suffix.lower() not in {'.md', '.markdown'} or not target.is_file():
                raise ValueError('Markdown source does not exist')
            sections = markdown_sections(target.read_text(encoding='utf-8'))
            anchor = unquote(parts.fragment)
            if anchor not in sections:
                raise ValueError(f'heading #{anchor} does not exist')
            body = sections[anchor]
            body_without_headings = re.sub(r'^ {0,3}#{1,6}\s+.*$', '', body, flags=re.M)
            if not re.search(r'\w', body_without_headings):
                raise ValueError('source section is empty')
            # Link labels and reference definitions are ordinary Markdown, not prompts.
            prompts = re.sub(r'\[[^\]\n]*\](?:\([^\n)]*\)|\[[^\]\n]*\])', '', body)
            definitions = re.findall(r'^\s*\[([^\]\n]+)\]:', prompts, flags=re.M)
            prompts = re.sub(r'^\s*\[[^\]\n]+\]:.*$', '', prompts, flags=re.M)
            for label in definitions:
                prompts = re.sub(r'\[' + re.escape(label) + r'\]', '', prompts, flags=re.I)
            if (re.search(r'\b(?:TODO|TBD|TBC|FIXME|REPLACE_ME|CHANGEME)\b', body)
                    or re.search(r'\[(?![xX ]\])[^\]\n]+\](?!\s*(?:\(|\[|:))', prompts)
                    or re.search(r'\{\{.+?\}\}|<(?:role|owner|goal|vision|replace)[^>]*>', body, re.I)):
                raise ValueError('source section still contains a placeholder')
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append(f'{key}: {exc} ({reference})')
    if errors:
        raise ValueError('Required project sources are incomplete:\n- ' + '\n- '.join(errors))


def load(path: Path, *, project_root: Path | None = None, check_references: bool = True):
    path = path.resolve()
    root = (project_root or path.parent).resolve()
    # Keep explicit v1 paths readable while preventing two live conventional maps.
    if path.name in {'workspace.yml', 'project.yaml'}:
        other = path.with_name('project.yaml' if path.name == 'workspace.yml' else 'workspace.yml')
        if path.exists() and other.exists():
            raise ValueError('Both workspace.yml and project.yaml exist; keep one authoritative configuration.')
        conventional_root = path.parent.parent if path.name == 'workspace.yml' and path.parent.name == 'workspace' else root
        current = conventional_root / 'project.yaml'
        old = conventional_root / 'workspace/workspace.yml'
        if path.exists() and current.exists() and old.exists():
            raise ValueError('Both project.yaml and workspace/workspace.yml exist; keep one authoritative configuration.')
    data = validate(yaml.load(path.read_text(encoding='utf-8'), Loader=UniqueLoader))
    if data.get('schema_version') == 2:
        if path != root / 'project.yaml':
            raise ValueError('Version 2 requires project.yaml at the declared project root.')
        if check_references:
            check_sources(data, root)
    return data


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--project-root', type=Path, help='Defaults to the manifest directory for version 2.')
    parser.add_argument('--structure-only', action='store_true', help='Check schema only; does not establish project readiness.')
    args = parser.parse_args(argv)
    try:
        data = load(args.config, project_root=args.project_root, check_references=not args.structure_only)
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
        print(f'Invalid project configuration: {exc}', file=sys.stderr)
        return 1
    name = data.get('project_name', data.get('name'))
    locations = (sum(key in data for key in ('work_tracking', 'code_review', 'knowledge_base', 'decision_records'))
                 if data.get('schema_version') == 2 else len(LOCATIONS))
    print(f'Valid project configuration: {name}; {locations} authoritative locations.')
    if data.get('schema_version') == 2 and not args.structure_only:
        print('Required local project sources checked for missing sections and obvious placeholders.')
    else:
        print('Structure checked only; project source completeness not established.')
    print('No connections made or commands executed; source quality and remote access require review.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
