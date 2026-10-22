# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML>=6,<7", "jsonschema>=4,<5"]
# ///
"""Validate declarative project tooling; never connect to systems or execute commands."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

import yaml
from jsonschema import Draft202012Validator

LOCATIONS = ('work', 'review', 'knowledge', 'decisions', 'iteration_reports', 'communication')
SCHEMA = json.loads((Path(__file__).resolve().parents[1] / 'toolkit/workspace.schema.json').read_text(encoding='utf-8'))
REQUIRED = set(SCHEMA['required'])


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


def load(path: Path):
    # Explicit legacy paths remain supported; two conventional live configs are ambiguous.
    if path.name in {'workspace.yml', 'project.yaml'}:
        other = path.with_name('project.yaml' if path.name == 'workspace.yml' else 'workspace.yml')
        if path.exists() and other.exists():
            raise ValueError('Both workspace.yml and project.yaml exist; keep one authoritative configuration.')
    return validate(yaml.load(path.read_text(encoding='utf-8'), Loader=UniqueLoader))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--config', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        data = load(args.config)
    except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
        print(f'Invalid project configuration: {exc}', file=sys.stderr)
        return 1
    print(f'Valid project configuration: {data["name"]}; {len(LOCATIONS)} authoritative locations.')
    print('Structure checked only; no connections made and no commands executed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
