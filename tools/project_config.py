# /// script
# requires-python = ">=3.11"
# dependencies = ["PyYAML>=6,<7"]
# ///
"""Validate declarative project tooling; never connect to systems or execute commands."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

import yaml

LOCATIONS = ('work', 'review', 'knowledge', 'decisions', 'iteration_reports', 'communication')
REQUIRED = {'version', 'name', 'working_agreement', 'stakeholders', *LOCATIONS}


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


def text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{label} must be a non-empty string.')


def validate(data):
    if not isinstance(data, dict):
        raise ValueError('Project configuration must be a mapping.')
    missing = REQUIRED - data.keys()
    unknown = data.keys() - REQUIRED - {'commands'}
    if missing or unknown:
        raise ValueError(f'Invalid fields: missing={sorted(missing)}, unknown={sorted(unknown)}')
    if type(data['version']) is not int or data['version'] != 1:
        raise ValueError('Unsupported project configuration version; expected integer 1.')
    for name in ('name', 'working_agreement', 'stakeholders'):
        text(data[name], name)
    for name in LOCATIONS:
        location = data[name]
        if not isinstance(location, dict) or set(location) != {'system', 'location'}:
            raise ValueError(f'{name} requires exactly system and location.')
        text(location['system'], f'{name}.system')
        text(location['location'], f'{name}.location')
    commands = data.get('commands', {})
    if not isinstance(commands, dict) or commands.keys() - {'setup', 'start', 'check'}:
        raise ValueError('commands accepts only setup, start and check.')
    for key, value in commands.items():
        if value is not None:
            text(value, f'commands.{key}')
    return data


def load(path: Path):
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
