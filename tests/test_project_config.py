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
        self.github = ROOT / 'templates/customer-workspace/workspace/workspace.yml'
        self.data = cfg.load(self.github)

    def test_examples_keep_tracker_and_review_independent(self):
        jira = cfg.load(ROOT / 'templates/customer-workspace/examples/workspace-jira.yml')
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

    def test_explicit_legacy_filename_remains_valid(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'project.yaml'
            path.write_text(cfg.yaml.safe_dump(self.data))
            self.assertEqual(cfg.load(path), self.data)

    def test_two_conventional_configs_are_rejected_without_changing_either(self):
        with tempfile.TemporaryDirectory() as folder:
            current = Path(folder) / 'workspace.yml'
            legacy = Path(folder) / 'project.yaml'
            current.write_text(cfg.yaml.safe_dump(self.data))
            alternate = copy.deepcopy(self.data)
            alternate['work']['system'] = 'jira'
            legacy.write_text(cfg.yaml.safe_dump(alternate))
            before = (current.read_bytes(), legacy.read_bytes())
            for path in (current, legacy):
                with self.subTest(path=path.name), self.assertRaisesRegex(ValueError, 'Both workspace.yml and project.yaml'):
                    cfg.load(path)
            self.assertEqual((current.read_bytes(), legacy.read_bytes()), before)

    def test_a_missing_requested_default_does_not_claim_two_configs_exist(self):
        with tempfile.TemporaryDirectory() as folder:
            legacy = Path(folder) / 'project.yaml'
            legacy.write_text(cfg.yaml.safe_dump(self.data))
            with self.assertRaises(FileNotFoundError):
                cfg.load(Path(folder) / 'workspace.yml')
