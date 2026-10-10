"""The optional YAML validator checks ownership config without calling external tools."""
import copy
from importlib.util import find_spec
import io
from pathlib import Path
import runpy
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
HAS_YAML = find_spec('yaml') is not None
cfg = SimpleNamespace(**runpy.run_path(str(ROOT / 'tools/project_config.py'))) if HAS_YAML else None


@unittest.skipUnless(HAS_YAML, 'Optional YAML validator: run with uv --group docs')
class ProjectConfigTests(unittest.TestCase):
    def setUp(self):
        self.github = ROOT / 'templates/customer-workspace/workspace/project.yaml'
        self.data = cfg.load(self.github)

    def test_examples_keep_tracker_and_review_independent(self):
        jira = cfg.load(ROOT / 'templates/customer-workspace/examples/project-jira.yaml')
        self.assertEqual(self.data['work']['system'], 'github')
        self.assertEqual((jira['work']['system'], jira['review']['system']), ('jira', 'github'))
        self.assertEqual(jira['knowledge']['system'], 'confluence')
        self.assertEqual(jira['decisions']['system'], 'repository')

    def test_other_tools_are_valid_without_a_vendor_allowlist(self):
        self.data['work'] = {'system': 'customer-tracker', 'location': 'https://tracker.example/project'}
        self.data['review']['system'] = 'gitlab'
        self.assertEqual(cfg.validate(self.data)['work']['system'], 'customer-tracker')

    def test_invalid_fields_and_types_are_rejected(self):
        invalid = []
        for key in cfg.REQUIRED:
            item = copy.deepcopy(self.data)
            del item[key]
            invalid.append(item)
        for value in (True, '1', 2):
            invalid.append(dict(self.data, version=value))
        invalid.extend([dict(self.data, models={}), dict(self.data, commands={'deploy': 'publish'}),
                        dict(self.data, commands={'check': ['test']}), dict(self.data, name=' '),
                        dict(self.data, work={'system': 'jira'}),
                        dict(self.data, work={'system': 'jira', 'location': '', 'token': 'invalid'})])
        for data in invalid:
            with self.subTest(data=data), self.assertRaises(ValueError):
                cfg.validate(data)

    def test_duplicate_keys_and_yaml_objects_are_rejected(self):
        for content in ('version: 1\nversion: 1\n', 'work:\n  system: jira\n  system: github\n',
                        '!!python/object/apply:builtins.print [unexpected]\n', '[not, a, mapping]'):
            with tempfile.TemporaryDirectory() as folder:
                path = Path(folder) / 'project.yaml'
                path.write_text(content)
                with self.subTest(content=content), self.assertRaises((ValueError, cfg.yaml.YAMLError)):
                    cfg.load(path)

    def test_validation_does_not_execute_commands_or_change_config(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'project.yaml'
            sentinel = Path(folder) / 'must-not-exist'
            self.data['commands']['check'] = f'touch {sentinel}'
            path.write_text(cfg.yaml.safe_dump(self.data))
            before = path.read_bytes()
            with patch('sys.stdout', new_callable=io.StringIO):
                self.assertEqual(cfg.main(['--config', str(path)]), 0)
            self.assertFalse(sentinel.exists())
            self.assertEqual(path.read_bytes(), before)

    def test_cli_missing_file_fails_without_traceback(self):
        with patch('sys.stderr', new_callable=io.StringIO) as err:
            self.assertEqual(cfg.main(['--config', '/nonexistent/project.yaml']), 1)
        self.assertIn('Invalid project configuration', err.getvalue())
