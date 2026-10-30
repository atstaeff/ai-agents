"""Native Herd packages/imports and shared export ownership/recovery boundaries."""
from __future__ import annotations

import base64
import io
import json
from pathlib import Path, PurePosixPath
import sys
import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import ai_toolkit as tk


class ExportFixture(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.source = self.base / 'source'
        self.output = self.base / 'bundle'
        for name in ('product-manager', 'lead-architect', 'task-orchestrator', 'code-reviewer'):
            self.write(f'agents/{name}.agent.md',
                       f'---\nname: {name}\ndescription: Select {name} for focused work\n---\n\n'
                       f'# {name}\n\nOriginal body. Use [work](../skills/work-management/SKILL.md).\n')
        self.write('skills/work-management/SKILL.md',
                   '---\nname: work-management\ndescription: Coordinate a bounded assignment\n---\n\n'
                   '# Work\n\nRead [details](references/detail.md).\n')
        self.write('skills/work-management/references/detail.md', '# Details\n\nKeep one assignment.\n')
        self.write('LICENSE', 'MIT License\n\nCopyright (c) Fixture Owner\n')

    def write(self, relative, content):
        path = self.source / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
        return path

    def snapshot(self):
        return {path.relative_to(self.output).as_posix(): path.read_bytes()
                for path in self.output.rglob('*') if path.is_file()}

    def update_source(self):
        source = self.source / 'agents/product-manager.agent.md'
        source.write_text(source.read_text().replace('Original body.', 'Updated body.'))


class HerdExportTests(ExportFixture):
    # Required fields are checked independently against upstream registry.ts,
    # template-bundle.ts and routes/register-core.ts at this recorded revision.
    # These tests do not execute a Herd installation or prove host permissions.
    UPSTREAM_REVISION = 'fbda6618c7b53524faddbed070e4fbc14970e412'

    def test_windows_line_endings_preserve_examples_and_rebase_links_after_fences(self):
        skill = self.source / 'skills/work-management/SKILL.md'
        body = skill.read_text() + '\n```md\n[Example](missing.md)\n```\nAfter: [details](references/detail.md).\n'
        skill.write_bytes(body.replace('\n', '\r\n').encode())
        for runtime, prefix in [('portable', '.agents'), ('copilot', '.github'),
                                ('claude', '.claude'), ('opencode', ''), ('herd', 'herd')]:
            with self.subTest(runtime=runtime):
                output = self.base / runtime
                tk.export(runtime, output, self.source)
                native = output / prefix / 'skills/work-management/SKILL.md'
                content = native.read_text()
                self.assertIn('```md\n[Example](missing.md)\n```', content)
                real_link = tk.LINK.findall(content)[-1]
                self.assertTrue((native.parent / real_link).is_file())
                self.assertNotEqual(real_link, 'references/detail.md')

    def test_fenced_markdown_examples_survive_every_export_and_herd_import(self):
        example = '\n```markdown\n[Example](missing.md)\n[Literal](references/detail.md)\n```\n'
        example += '\n  ~~~~markdown\n[Example](missing.md)\n  ~~~~~\n'
        example += '\n````markdown\n```inner\n[Example](missing.md)\n```\n`````\n'
        example += '\n~~~markdown\n[Unclosed example](missing.md)\n'
        skill = self.source / 'skills/work-management/SKILL.md'
        skill.write_text(skill.read_text() + example)
        profile = self.source / 'agents/product-manager.agent.md'
        profile.write_text(profile.read_text() + example)
        for runtime, prefix in [('portable', '.agents'), ('copilot', '.github'),
                                ('claude', '.claude'), ('opencode', ''), ('herd', 'herd')]:
            with self.subTest(runtime=runtime):
                output = self.base / runtime
                tk.export(runtime, output, self.source)
                native = output / prefix / 'skills/work-management/SKILL.md'
                content = native.read_text()
                self.assertIn(example, content)
                real_link = tk.LINK.findall(content)[0]
                self.assertTrue((native.parent / real_link).is_file())
                self.assertIn(example, (output / 'catalog/skills/work-management/SKILL.md').read_text())
                if runtime == 'herd':
                    bundle = json.loads((output / 'herd/imports/product-manager.bundle.json').read_text())
                    self.assertIn(example, bundle['commanderMd'])
                    binding = next(item for item in bundle['skillBindings'] if item['skillId'] == 'work-management')
                    entry = next(item for item in binding['bundle']['files'] if item['path'] == 'SKILL.md')
                    self.assertIn(example, base64.b64decode(entry['contentBase64']).decode())

    def assert_bundle_installs(self, bundle, folder):
        self.assertEqual(bundle['schemaVersion'], 2)
        self.assertIsInstance(bundle['exportedAt'], str)
        self.assertEqual(set(bundle['commander']), {'displayName', 'host'})
        self.assertTrue(bundle['commander']['displayName'])
        self.assertTrue(tk.SLUG.fullmatch(bundle['commander']['host']))
        self.assertEqual(bundle['memorySnapshot'], {'memoryMd': '', 'syncRevision': 0})
        self.assertEqual(bundle['automations'], [])
        self.assertNotIn('permission:', bundle['commanderMd'])
        self.assertNotIn('mode:', bundle['commanderMd'])
        folder.mkdir()
        (folder / 'COMMANDER.md').write_text(bundle['commanderMd'])
        metadata = {item['id']: item for item in bundle['skills']}
        self.assertEqual(len(metadata), len(bundle['skills']))
        self.assertEqual(set(metadata), {item['skillId'] for item in bundle['skillBindings']})
        for binding in bundle['skillBindings']:
            self.assertEqual(binding['source'], 'commander-local')
            self.assertEqual(binding['required'], metadata[binding['skillId']]['required'])
            self.assertEqual(binding['bundle']['dirName'], binding['skillId'])
            files = binding['bundle']['files']
            self.assertIn('SKILL.md', {file['path'] for file in files})
            self.assertEqual(len(files), len({file['path'] for file in files}))
            for file in files:
                relative = PurePosixPath(file['path'])
                self.assertFalse(relative.is_absolute())
                self.assertEqual(relative.as_posix(), file['path'])
                self.assertNotIn('..', relative.parts)
                self.assertTrue(file['contentBase64'])
                target = folder / 'skills' / binding['skillId'] / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(base64.b64decode(file['contentBase64'], validate=True))
        # Resolve from the imported location, independently of the staging tree.
        native_files = [folder / 'COMMANDER.md', *folder.glob('skills/*/SKILL.md'),
                        folder / 'skills/ai-agents-catalog/references/SPECIALISTS.md']
        for path in native_files:
            for link in tk.LINK.findall(path.read_text()):
                parts = tk.urlsplit(link)
                if not parts.scheme and parts.path:
                    self.assertTrue((path.parent / tk.unquote(parts.path)).is_file(), (path, link))
        return metadata

    def test_native_packages_and_self_contained_v2_imports(self):
        result = tk.export('herd', self.output, self.source)
        self.assertEqual((result['agents'], result['skills']), (4, 1))
        self.assertEqual(tk.HERD_UPSTREAM_REVISION, self.UPSTREAM_REVISION)
        expected = {'product-manager', 'lead-architect', 'task-orchestrator'}
        self.assertEqual({path.name for path in (self.output / 'herd/commanders').iterdir()}, expected)
        source_before = {path: path.read_bytes() for path in self.source.rglob('*') if path.is_file()}
        for leader in expected:
            package_dir = self.output / 'herd/commanders' / leader
            package = json.loads((package_dir / 'package.json').read_text())
            self.assertEqual(package['schemaVersion'], 1)
            self.assertEqual(package['id'], leader)
            self.assertEqual(set(package), {'schemaVersion', 'id', 'version', 'displayName', 'host',
                                            'role', 'summary', 'description'})
            for field in set(package) - {'schemaVersion'}:
                self.assertIsInstance(package[field], str)
                self.assertTrue(package[field])
            manifest = json.loads((package_dir / 'skills.manifest.json').read_text())
            self.assertEqual({item['id'] for item in manifest['required']},
                             {'ai-agents-catalog', 'work-management'})
            self.assertEqual(manifest['optional'], [])
            for item in manifest['required']:
                self.assertEqual(set(item), {'id', 'label', 'purpose'})
            for name in ('COMMANDER.md', 'onboarding.md', 'memory-seed.md', 'LICENSE'):
                self.assertTrue((package_dir / name).is_file())
            bundle = json.loads((self.output / f'herd/imports/{leader}.bundle.json').read_text())
            metadata = self.assert_bundle_installs(bundle, self.base / f'installed-{leader}')
            self.assertEqual(set(metadata), {'ai-agents-catalog', 'work-management'})
            self.assertEqual(bundle['commanderMd'], (package_dir / 'COMMANDER.md').read_text())
            installed = self.base / f'installed-{leader}'
            notice = installed / 'skills/ai-agents-catalog/references/catalog/LICENSE'
            self.assertEqual(notice.read_bytes(), (self.source / 'LICENSE').read_bytes())
            self.assertTrue((installed / 'skills/ai-agents-catalog/references/catalog/agents/code-reviewer.agent.md').is_file())
        self.assertEqual(source_before, {path: path.read_bytes() for path in source_before})
        self.assertFalse((self.output / 'opencode.json').exists())

    def test_actual_selection_has_multiple_leads_and_optional_specialist_skills(self):
        selected = tk.select_entries(tk.catalog(), 'engineering')
        tk.export('herd', self.output, preset='engineering')
        expected_leads = {entry.name for entry in selected if entry.kind == 'agent' and entry.name in tk.HERD_LEADS}
        self.assertEqual({path.name for path in (self.output / 'herd/commanders').iterdir()}, expected_leads)
        bundle = json.loads((self.output / 'herd/imports/lead-architect.bundle.json').read_text())
        metadata = self.assert_bundle_installs(bundle, self.base / 'installed-real')
        self.assertTrue(metadata['api-design']['required'])
        self.assertFalse(metadata['python-patterns']['required'])
        self.assertEqual(set(metadata) - {'ai-agents-catalog'},
                         {entry.name for entry in selected if entry.kind == 'skill'})
        self.assertNotIn('obsidian-para', metadata)
        self.assertLess(len(bundle['commanderMd']), 7000)
        index = json.loads((self.output / 'catalog/index.json').read_text())
        self.assertEqual({(item['kind'], item['name']) for item in index},
                         {(entry.kind, entry.name) for entry in selected})

    def test_cli_dry_run_no_op_and_human_edit_protection(self):
        arguments = ['export', '--runtime', 'herd', '--output', str(self.output), '--preset', 'minimal']
        with patch('sys.stdout', new_callable=io.StringIO):
            self.assertEqual(tk.main(arguments + ['--dry-run']), 0)
            self.assertFalse(self.output.exists())
            self.assertEqual(tk.main(arguments), 0)
        before = self.snapshot()
        with patch.object(tk, 'atomic_write', wraps=tk.atomic_write) as write:
            again = tk.export('herd', self.output, preset='minimal')
        write.assert_not_called()
        self.assertEqual(again['changed'], 0)
        self.assertEqual(before, self.snapshot())
        command = self.output / 'herd/commanders/joerg/COMMANDER.md'
        command.write_text('Human-owned identity')
        with self.assertRaisesRegex(tk.ToolkitError, 'edited file'):
            tk.export('herd', self.output, preset='minimal')
        self.assertEqual(command.read_text(), 'Human-owned identity')

    def test_every_runtime_redistributes_root_notice_and_fixture_license_is_optional(self):
        for runtime in sorted(tk.RUNTIMES):
            with self.subTest(runtime=runtime):
                output = self.base / runtime
                tk.export(runtime, output, self.source)
                self.assertEqual((output / 'catalog/LICENSE').read_bytes(),
                                 (self.source / 'LICENSE').read_bytes())
        (self.source / 'LICENSE').unlink()
        tk.export('herd', self.output, self.source)
        self.assertFalse((self.output / 'catalog/LICENSE').exists())

    def test_opencode_options_are_rejected_before_herd_creates_files(self):
        for options in (tk.OpenCodeOptions(plannotator=True), tk.OpenCodeOptions(plan_model='provider/model')):
            with self.subTest(options=options), self.assertRaisesRegex(tk.ToolkitError, 'runtime opencode'):
                tk.export('herd', self.output, self.source, opencode_options=options)
            self.assertFalse(self.output.exists())

    def test_nested_catalog_links_use_public_reading_view_without_importing_project_rules(self):
        self.write('skills/work-management/references/detail.md',
                   '# Details\n\nRead [project contract](../../../AGENTS.md#rules) and '
                   '[example](../../../examples/public.md?plain=1#result).\n')
        self.write('AGENTS.md', '# Repository-only contract\n')
        self.write('examples/public.md', '# Public example\n')
        self.write('workspace/work/private.md', '# Private assignment\n')
        tk.export('herd', self.output, self.source)
        bundle = json.loads((self.output / 'herd/imports/product-manager.bundle.json').read_text())
        self.assert_bundle_installs(bundle, self.base / 'installed-nested')
        details = self.base / 'installed-nested/skills/ai-agents-catalog/references/catalog/skills/work-management/references/detail.md'
        self.assertIn('https://github.com/atstaeff/ai-agents/blob/main/AGENTS.md#rules', details.read_text())
        self.assertIn('https://github.com/atstaeff/ai-agents/blob/main/examples/public.md?plain=1#result', details.read_text())
        self.assertFalse((self.output / 'catalog/AGENTS.md').exists())
        self.assertFalse((self.output / 'catalog/workspace').exists())
        self.assertNotIn('Private assignment', json.dumps(bundle))

    def test_private_and_outside_catalog_references_fail_before_writing(self):
        self.write('workspace/work/private.md', '# Private assignment\n')
        for link in ('../../../workspace/work/private.md', '../../../../outside.md'):
            with self.subTest(link=link):
                self.write('skills/work-management/references/detail.md', f'# Details\n\n[Hidden]({link})\n')
                with self.assertRaises(tk.ToolkitError):
                    tk.export('herd', self.output, self.source)
                self.assertFalse(self.output.exists())


class ExportSafetyTests(ExportFixture):
    def test_private_and_generated_files_are_omitted_before_reading(self):
        excluded = [
            'skills/work-management/.env',
            'skills/work-management/.env.production',
            'skills/work-management/credentials.json',
            'skills/work-management/assets/access-token.txt',
            'skills/work-management/assets/api-keys.json',
            'skills/work-management/assets/private-keys.json',
            'skills/work-management/references/tokens/production.json',
            'skills/work-management/references/passwords/config.json',
            'skills/work-management/references/secret/config.json',
            'skills/work-management/references/api-keys/config.json',
            'skills/work-management/references/private-keys/config.json',
            'skills/credentials/SKILL.md',
            'toolkit/nested/secrets.json',
            'reference-repos/demo/id_rsa',
            'marp-templates/slides/private-key.pem',
            'templates/project-starter/config/service-account.json',
            'skills/work-management/references/.aws/credentials',
            'skills/work-management/references/node_modules/dependency/package.json',
            'skills/work-management/references/__pycache__/module.py',
            'skills/work-management/references/workspace/work/private.md',
            'skills/work-management/references/workspace/archive/history.md',
            'skills/work-management/references/.ai/work/private.md',
            'skills/work-management/references/generated/output.md',
            'skills/work-management/references/dist/output.json',
            'skills/work-management/references/build/output.json',
            'skills/work-management/references/.cache/snapshot.json',
            'skills/work-management/references/private/notes.md',
            'skills/work-management/references/local-state/session.json',
            'skills/work-management/references/terraform.tfstate',
            'skills/work-management/assets/unknown.payload',
        ]
        forbidden = {self.write(name, 'Synthetic private fixture; never export.\n') for name in excluded}
        read_bytes, read_text = Path.read_bytes, Path.read_text

        def guarded_bytes(path):
            self.assertNotIn(path, forbidden, f'Read excluded export source: {path}')
            return read_bytes(path)

        def guarded_text(path, *args, **kwargs):
            self.assertNotIn(path, forbidden, f'Read excluded export source: {path}')
            return read_text(path, *args, **kwargs)

        for runtime in ('portable', 'herd'):
            with self.subTest(runtime=runtime):
                output = self.base / runtime
                with patch.object(Path, 'read_bytes', guarded_bytes), patch.object(Path, 'read_text', guarded_text):
                    tk.export(runtime, output, self.source)
                for name in excluded:
                    self.assertFalse((output / 'catalog' / name).exists(), name)
                for path in output.rglob('*'):
                    if path.is_file():
                        self.assertNotIn(b'Synthetic private fixture', path.read_bytes(), path)

    def test_skill_assets_scripts_and_fixtures_export_without_git_metadata(self):
        assets = {
            'assets/icon.png': b'\x89PNG\r\n\x1a\nSynthetic public image asset',
            'assets/diagram.svg': b'<svg xmlns="http://www.w3.org/2000/svg"/>',
            'assets/template.docx': b'Synthetic public document template',
            'scripts/run.py': b'print("public example")\n',
            'scripts/run.sh': b'#!/bin/sh\nprintf "public example\\n"\n',
            'tests/fixtures/response.json': b'{"example": true}\n',
        }
        for name, data in assets.items():
            path = self.source / 'skills/work-management' / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        self.write('skills/work-management/references/detail.md',
                   '# Details\n\n[Image](../assets/icon.png), [script](../scripts/run.py), '
                   '[fixture](../tests/fixtures/response.json).\n')
        self.assertFalse((self.source / '.git').exists())
        for runtime in ('portable', 'herd'):
            with self.subTest(runtime=runtime):
                output = self.base / runtime
                tk.export(runtime, output, self.source)
                for name, data in assets.items():
                    self.assertEqual((output / 'catalog/skills/work-management' / name).read_bytes(), data)
                if runtime == 'herd':
                    bundle = json.loads((output / 'herd/imports/product-manager.bundle.json').read_text())
                    binding = next(item for item in bundle['skillBindings'] if item['skillId'] == 'ai-agents-catalog')
                    embedded = {item['path']: base64.b64decode(item['contentBase64'], validate=True)
                                for item in binding['bundle']['files']}
                    for name, data in assets.items():
                        self.assertEqual(embedded['references/catalog/skills/work-management/' + name], data)

    def test_links_to_excluded_secrets_and_nested_state_fail_before_writing(self):
        for index, relative in enumerate((
                '.env.production', 'credentials.json', 'assets/api-keys.json', 'assets/private-keys.json',
                'references/tokens/production.json', 'references/passwords/config.json',
                'references/secret/config.json', 'references/api-keys/config.json',
                'references/private-keys/config.json', 'references/local-state/session.json',
                'references/workspace/work/private.md', 'assets/unknown.payload')):
            self.write('skills/work-management/' + relative, 'Synthetic private fixture.\n')
            self.write('skills/work-management/references/detail.md', f'# Details\n\n[Hidden](../{relative})\n')
            for runtime in ('portable', 'herd'):
                with self.subTest(relative=relative, runtime=runtime):
                    output = self.base / runtime / f'excluded-{index}'
                    with self.assertRaises(tk.ToolkitError):
                        tk.export(runtime, output, self.source)
                    self.assertFalse(output.exists())

    def test_source_directory_and_native_interface_symlinks_are_rejected(self):
        external = self.base / 'external-agents'
        (self.source / 'agents').rename(external)
        (self.source / 'agents').symlink_to(external, target_is_directory=True)
        with self.assertRaisesRegex(tk.ToolkitError, 'Cannot export a symlink'):
            tk.export('herd', self.output, self.source)
        self.assertFalse(self.output.exists())
        (self.source / 'agents').unlink()
        external.rename(self.source / 'agents')
        outside_interface = self.base / 'external-interface'
        outside_interface.mkdir()
        (outside_interface / 'openai.yaml').write_text('private: must not be copied\n')
        (self.source / 'skills/work-management/agents').symlink_to(outside_interface, target_is_directory=True)
        with self.assertRaisesRegex(tk.ToolkitError, 'Cannot export a symlink'):
            tk.export('herd', self.output, self.source)
        self.assertFalse(self.output.exists())

    def test_noncanonical_manifest_alias_cannot_delete_an_active_file(self):
        tk.export('portable', self.output, self.source)
        manifest = self.output / tk.EXPORT_MANIFEST
        original = json.loads(manifest.read_text())
        checksum = original['files']['agents/product-manager.agent.md']
        for alias in ('agents/../agents/product-manager.agent.md', './agents/product-manager.agent.md',
                      'agents//product-manager.agent.md', 'agents\\product-manager.agent.md',
                      'C:/agents/product-manager.agent.md', tk.EXPORT_JOURNAL):
            with self.subTest(alias=alias):
                manifest.write_text(json.dumps({**original, 'files': {**original['files'], alias: checksum}}))
                before = self.snapshot()
                with self.assertRaisesRegex(tk.ToolkitError, 'Invalid export manifest'):
                    tk.export('portable', self.output, self.source)
                self.assertEqual(before, self.snapshot())
        manifest.write_text(json.dumps({**original, 'files': {'harmless.md': 'not-a-sha256'}}))
        with self.assertRaisesRegex(tk.ToolkitError, 'Invalid export manifest'):
            tk.export('portable', self.output, self.source)

    def test_write_failure_rolls_back_and_retry_needs_no_force(self):
        tk.export('portable', self.output, self.source)
        before = self.snapshot()
        self.update_source()
        original = tk.atomic_write
        calls = 0

        def fail_second(path, data, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError('simulated full disk')
            return original(path, data, **kwargs)

        with patch.object(tk, 'atomic_write', side_effect=fail_second):
            with self.assertRaisesRegex(OSError, 'simulated full disk'):
                tk.export('portable', self.output, self.source)
        self.assertEqual(before, self.snapshot())
        self.assertFalse((self.output / tk.EXPORT_LOCK).exists())
        self.assertFalse((self.output / tk.EXPORT_JOURNAL).exists())
        result = tk.export('portable', self.output, self.source)
        self.assertEqual(result['changed'], 2)

    def test_manifest_commit_failure_rolls_back_all_changed_files(self):
        tk.export('portable', self.output, self.source)
        before = self.snapshot()
        self.update_source()
        original = tk.atomic_write

        def fail_manifest(path, data, **kwargs):
            if path.name == tk.EXPORT_MANIFEST:
                raise OSError('manifest cannot be persisted')
            return original(path, data, **kwargs)

        with patch.object(tk, 'atomic_write', side_effect=fail_manifest):
            with self.assertRaisesRegex(OSError, 'manifest cannot be persisted'):
                tk.export('portable', self.output, self.source)
        self.assertEqual(before, self.snapshot())
        tk.export('portable', self.output, self.source)

    def test_repair_with_unchanged_manifest_still_rolls_back_on_failure(self):
        planned = {'a': b'generated A', 'b': b'generated B'}
        tk._write_export(self.output, planned, 'portable', False, False)
        original = tk.atomic_write
        for missing in (False, True):
            with self.subTest(missing=missing):
                for name in planned:
                    path = self.output / name
                    if missing:
                        path.unlink(missing_ok=True)
                    else:
                        path.write_text('Human ' + name)
                before = self.snapshot()

                def fail_second(path, data, **kwargs):
                    if path.name == 'b':
                        raise OSError('second repair failed')
                    return original(path, data, **kwargs)

                with patch.object(tk, 'atomic_write', side_effect=fail_second):
                    with self.assertRaisesRegex(OSError, 'second repair failed'):
                        tk._write_export(self.output, planned, 'portable', not missing, False)
                self.assertEqual(before, self.snapshot())
                self.assertFalse((self.output / tk.EXPORT_JOURNAL).exists())

    def test_failed_rollback_retains_journal_and_next_export_recovers(self):
        tk.export('portable', self.output, self.source)
        self.update_source()
        first_target = self.output / 'agents/product-manager.agent.md'
        original = tk.atomic_write
        primitive = tk._atomic_write_file
        calls = 0
        recovering = False

        def fail_write(path, data, **kwargs):
            nonlocal calls, recovering
            calls += 1
            if calls == 2:
                recovering = True
                raise OSError('simulated write failure')
            return original(path, data, **kwargs)

        def fail_rollback(path, data, expected_hash=tk._UNCHECKED):
            if recovering and path == first_target:
                raise OSError('rollback temporarily unavailable')
            return primitive(path, data, expected_hash)

        with patch.object(tk, 'atomic_write', side_effect=fail_write), \
                patch.object(tk, '_atomic_write_file', side_effect=fail_rollback):
            with self.assertRaisesRegex(tk.ToolkitError, 'Recovery is pending'):
                tk.export('portable', self.output, self.source)
        self.assertTrue((self.output / tk.EXPORT_JOURNAL).is_file())
        self.assertFalse((self.output / tk.EXPORT_LOCK).exists())
        result = tk.export('portable', self.output, self.source)
        self.assertEqual(result['changed'], 2)
        self.assertIn('Updated body.', first_target.read_text())
        self.assertFalse((self.output / tk.EXPORT_JOURNAL).exists())

    def test_late_human_edit_is_preserved_even_with_force(self):
        tk.export('portable', self.output, self.source)
        self.update_source()
        target = self.output / 'agents/product-manager.agent.md'
        original = tk.atomic_write

        def edit_at_replacement(path, data, **kwargs):
            if path == target:
                path.write_text('Human edit made after export preflight')
            return original(path, data, **kwargs)

        with patch.object(tk, 'atomic_write', side_effect=edit_at_replacement):
            with self.assertRaisesRegex(tk.ToolkitError, 'Recovery is pending'):
                tk.export('portable', self.output, self.source, force=True)
        self.assertEqual(target.read_text(), 'Human edit made after export preflight')
        self.assertTrue((self.output / tk.EXPORT_JOURNAL).exists())

    def test_competing_exporter_cannot_write_during_active_transaction(self):
        entered = threading.Event()
        release = threading.Event()
        original = tk.atomic_write

        def pause(path, data, **kwargs):
            if not entered.is_set():
                entered.set()
                if not release.wait(5):
                    raise AssertionError('writer was not released')
            return original(path, data, **kwargs)

        with ThreadPoolExecutor(max_workers=1) as pool, patch.object(tk, 'atomic_write', side_effect=pause):
            future = pool.submit(tk.export, 'portable', self.output, self.source)
            self.assertTrue(entered.wait(5))
            try:
                with self.assertRaisesRegex(tk.Conflict, 'Another export owns'):
                    tk.export('portable', self.output, self.source)
            finally:
                release.set()
            self.assertGreater(future.result(timeout=5)['changed'], 0)
        self.assertFalse((self.output / tk.EXPORT_LOCK).exists())
        self.assertEqual(tk.export('portable', self.output, self.source)['changed'], 0)


if __name__ == '__main__':
    unittest.main()
