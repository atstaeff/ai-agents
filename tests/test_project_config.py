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
HAS_YAML = find_spec('yaml') is not None and find_spec('jsonschema') is not None
cfg = SimpleNamespace(**runpy.run_path(str(ROOT / 'tools/project_config.py'))) if HAS_YAML else None


@unittest.skipUnless(HAS_YAML, 'Optional YAML/schema validator: run with uv --group validation')
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

    def test_schema_and_repository_config_are_valid(self):
        cfg.Draft202012Validator.check_schema(cfg.SCHEMA)
        data = cfg.load(ROOT / 'project.yaml')
        self.assertEqual(data['project_name'], 'AI Agents')
        self.assertEqual(data['work_tracking'], 'https://github.com/atstaeff/ai-agents/issues')
        for key in ('process', 'responsibilities'):
            self.assertTrue((ROOT / data[key]).is_file())

    def test_lean_starter_resolves_project_contribution_owners_and_knowledge(self):
        starter = ROOT / 'templates/lean-project'
        data = cfg.load(starter/'project.yaml', check_references=False)
        self.assertEqual(data['work_tracking'], 'workspace/work/')
        for key, expected in (('process', 'CONTRIBUTING.md'), ('responsibilities', 'PROJECT.md#responsibilities')):
            self.assertEqual(data[key], expected)
            self.assertTrue((starter/data[key].split('#')[0]).is_file())
        for key in ('knowledge_base', 'decision_records'):
            self.assertTrue((starter/data[key]).is_file())
        self.assertNotIn('commands', data)  # No fabricated setup/test commands.

    def manifest_fixture(self, root):
        paths = {
            'notes/purpose.md': '# Product\n\n## Vision\nHelp analysts resolve cases.\n\n## Goals\nReduce manual lookups.\n\n## Boundaries\nNo customer data migration.\n',
            'team/people.md': '# Owners\n\nThe requester owns acceptance.\n',
            'process/how.md': '# Contribution\n\nInspect, change and check the affected behavior.\n',
        }
        for name, content in paths.items():
            path = root/name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
        data = {
            'schema_version': 2, 'project_name': 'Quota example',
            'vision': 'notes/purpose.md#vision', 'goals': 'notes/purpose.md#goals',
            'scope_and_boundaries': 'notes/purpose.md#boundaries',
            'responsibilities': 'team/people.md', 'process': 'process/how.md',
            'work_tracking': 'Current request',
            'knowledge_base': 'notes/purpose.md',
            'decision_records': 'notes/decisions/',
        }
        path = root/'project.yaml'
        path.write_text(cfg.yaml.safe_dump(data))
        return path, data

    def test_project_kernel_example_uses_the_complete_explicit_contract(self):
        source = (ROOT/'toolkit/examples/project-kernel.md').read_text()
        snippet = source.split('```yaml\n', 1)[1].split('```', 1)[0]
        data = cfg.validate(cfg.yaml.load(snippet, Loader=cfg.UniqueLoader))
        self.assertEqual(data['schema_version'], 2)
        self.assertEqual(data['process'], 'CONTRIBUTING.md')
        self.assertEqual(data['decision_records'], 'architecture/decisions/')
        with self.assertRaises(ValueError):
            cfg.validate(dict(data, version=1))

    def test_manifest_accepts_project_chosen_content_directories_and_sections(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path, data = self.manifest_fixture(root)
            self.assertEqual(cfg.load(path), data)
            self.assertFalse((root/'workspace').exists())
            self.assertFalse((root/'PROJECT.md').exists())
            self.assertFalse((root/'CONTRIBUTING.md').exists())

    def test_flat_manifest_requires_filled_keys_and_rejects_nested_tool_configuration(self):
        with tempfile.TemporaryDirectory() as folder:
            _, data = self.manifest_fixture(Path(folder))
        for key in data:
            missing = dict(data)
            del missing[key]
            with self.subTest(key=key, value='missing'), self.assertRaises(ValueError):
                cfg.validate(missing)
            for value in ('', ' ', None, [], {'system': 'repository', 'location': 'source/'}):
                with self.subTest(key=key, value=value), self.assertRaises(ValueError):
                    cfg.validate(dict(data, **{key: value}))
        self.assertEqual(cfg.validate(dict(data, code_review='Current diff'))['code_review'], 'Current diff')
        for key, value in (('code_review', {}), ('contribution_guide', 'old-process.md'),
                           ('delivery_method', 'lean'), ('commands', {}),
                           ('context', {'vision': 'notes/purpose.md#vision'})):
            with self.subTest(key=key), self.assertRaises(ValueError):
                cfg.validate(dict(data, **{key: value}))

    def test_manifest_rejects_missing_files_anchors_empty_sections_and_placeholders(self):
        cases = [
            ('notes/missing.md', None, 'does not exist'),
            ('notes/purpose.md#absent', None, 'heading #absent'),
            ('notes/purpose.md#vision', '# Product\n\n## Vision\n<!-- fill this -->\n\n## Goals\nUseful goal.\n', 'section is empty'),
            ('notes/purpose.md#vision', '# Product\n\n## Vision\n[who this serves]\n', 'placeholder'),
            ('notes/purpose.md#vision', '# Product\n\n## Vision\nTBD\n', 'placeholder'),
            ('https://wiki.example/vision', None, 'local Markdown entry'),
            ('../outside.md', None, 'inside the project root'),
        ]
        for reference, text, error in cases:
            with self.subTest(reference=reference, error=error), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                path, data = self.manifest_fixture(root)
                data['vision'] = reference
                path.write_text(cfg.yaml.safe_dump(data))
                if text is not None:
                    (root/'notes/purpose.md').write_text(text)
                with self.assertRaisesRegex(ValueError, error):
                    cfg.load(path)

    def test_manifest_ignores_fenced_examples_and_valid_markdown_links(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path, _ = self.manifest_fixture(root)
            (root/'process/how.md').write_text('# Process\n\nFollow [the guide](../notes/purpose.md) and [details][source].\n\n[source]: ../notes/purpose.md\n\n```md\n## Fake heading\nTBD [template prompt]\n```\n')
            cfg.load(path)
            sections = cfg.markdown_sections((root/'process/how.md').read_text())
            self.assertNotIn('fake-heading', sections)

    def test_unfilled_starter_passes_structure_only_but_not_completeness(self):
        path = ROOT/'templates/lean-project/project.yaml'
        with self.assertRaisesRegex(ValueError, 'placeholder'):
            cfg.load(path)
        with patch('sys.stdout', new_callable=io.StringIO) as out:
            self.assertEqual(cfg.main(['--config', str(path), '--structure-only']), 0)
        self.assertIn('completeness not established', out.getvalue())
        with patch('sys.stderr', new_callable=io.StringIO) as err:
            self.assertEqual(cfg.main(['--config', str(path)]), 1)
        self.assertIn('vision', err.getvalue())

    def test_manifest_checks_are_read_only_and_never_execute_markdown_commands(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path, data = self.manifest_fixture(root)
            sentinel = root/'must-not-exist'
            guide = root/data['process']
            guide.write_text(guide.read_text() + f'\n```sh\ntouch {sentinel}\n```\n')
            before = {p: p.read_bytes() for p in root.rglob('*') if p.is_file()}
            cfg.load(path)
            self.assertEqual(before, {p: p.read_bytes() for p in root.rglob('*') if p.is_file()})
            self.assertFalse(sentinel.exists())

    def test_source_heading_ids_handle_indentation_and_duplicate_titles(self):
        sections = cfg.markdown_sections('   ## Vision\nFirst.\n\n## Vision\nSecond.\n\n## Vision-1\nThird.\n')
        self.assertEqual(sections['vision'].strip(), 'First.')
        self.assertEqual(sections['vision-1'].strip(), 'Second.')
        self.assertEqual(sections['vision-1-1'].strip(), 'Third.')

    def test_manifest_rejects_symlink_escape_and_wrong_root_filename(self):
        with tempfile.TemporaryDirectory() as folder, tempfile.TemporaryDirectory() as outside:
            root = Path(folder)
            path, data = self.manifest_fixture(root)
            external = Path(outside)/'external.md'
            external.write_text('External content.')
            (root/'linked.md').symlink_to(external)
            data['vision'] = 'linked.md'
            path.write_text(cfg.yaml.safe_dump(data))
            with self.assertRaisesRegex(ValueError, 'inside the project root'):
                cfg.load(path)
            renamed = path.with_name('other.yaml')
            path.rename(renamed)
            with self.assertRaisesRegex(ValueError, 'requires project.yaml'):
                cfg.load(renamed)

    def test_manifest_rejects_an_old_nested_map_without_mutating_either(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path, _ = self.manifest_fixture(root)
            old = root/'workspace/workspace.yml'
            old.parent.mkdir()
            old.write_text(cfg.yaml.safe_dump(self.data))
            before = (path.read_bytes(), old.read_bytes())
            for current in (path, old):
                with self.subTest(current=current), self.assertRaisesRegex(ValueError, 'Both project.yaml and workspace/workspace.yml'):
                    cfg.load(current)
            self.assertEqual(before, (path.read_bytes(), old.read_bytes()))

    def test_minimal_existing_config_does_not_require_new_sections(self):
        minimal = {key: self.data[key] for key in cfg.REQUIRED}
        self.assertEqual(cfg.validate(minimal), minimal)

    def test_optional_process_fields_reject_ambiguity_and_bad_types(self):
        changes = [
            {'repositories': [{'name': 'one', 'location': 'repo'}, {'name': 'one', 'location': 'other'}]},
            {'repositories': [{'name': 'one', 'location': 'repo', 'token': 'secret'}]},
            {'quality_gates': [{'name': 'Check', 'command': 'test', 'required': 'yes'}]},
            {'actions': {'merge': True}}, {'actions': {'send_everywhere': 'within_assignment'}},
            {'reviewers': 'owner'}, {'labels': {'ready': 1}},
            {'planning': {'priority': {'system': 'jira'}}},
        ]
        duplicate_states = copy.deepcopy(self.data['flow'])
        duplicate_states['states']['done'] = duplicate_states['states']['todo']
        changes.append({'flow': duplicate_states})
        for change in changes:
            with self.subTest(change=change), self.assertRaises(ValueError):
                cfg.validate(dict(self.data, **change))

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
        for value in (True, '1', 3):
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
            self.data['quality_gates'][0]['command'] = f'touch {sentinel}'
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
