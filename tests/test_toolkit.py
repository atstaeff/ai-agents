from __future__ import annotations

import csv
import http.client
import io
import json
from pathlib import Path
import sys
import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import ai_toolkit as tk


class CatalogTests(unittest.TestCase):
    def test_checkout_starts_the_delivery_team_from_canonical_profiles(self):
        path = tk.ROOT/'opencode.json'
        config = json.loads(path.read_text())
        self.assertEqual(config, tk.repository_opencode_config())
        self.assertEqual(config['default_agent'], 'task-orchestrator')
        self.assertEqual(config['instructions'], ['toolkit/SESSION-RULES.md'])
        entries = {e.name: e for e in tk.select_entries(tk.catalog(), 'team') if e.kind == 'agent'}
        self.assertEqual(set(config['agent']), set(entries))
        for name, settings in config['agent'].items():
            source = entries[name].path
            self.assertTrue((tk.ROOT/source).is_file())
            self.assertIn(f'{{file:./{source}}}', settings['prompt'])
            self.assertIn(f'Canonical role source: {source}', settings['prompt'])
            self.assertEqual(settings['description'], entries[name].description)
            self.assertNotIn('model', settings)
            self.assertNotIn('variant', settings)
            if name in tk.TEAM_LEADS:
                self.assertEqual(settings['mode'], 'all')
            if name in tk.OPENCODE_REVIEW_ROUTE:
                self.assertEqual(settings['permission'], {'edit': {'*': 'deny'}, 'bash': 'deny', 'task': 'deny'})
            else:
                self.assertNotIn('permission', settings)
        self.assertNotIn('model', config)
        self.assertNotIn('permission', config)

    def test_checkout_configuration_drift_is_reported_without_overwriting_it(self):
        original = tk.catalog()
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ('README.md', 'AGENTS.md', 'CONTRIBUTING.md', '.github/copilot-instructions.md'):
                required = root/name
                required.parent.mkdir(parents=True, exist_ok=True)
                required.write_text('# Fixture instructions\n')
            path = root/'opencode.json'
            path.write_bytes((tk.ROOT/'opencode.json').read_bytes())
            before = path.read_bytes()
            with patch.object(tk, 'catalog', return_value=original):
                self.assertEqual(tk.check(root), [])
            changed = [replace(e, description=e.description+' Updated role.') if e.name == 'task-orchestrator' else e for e in original]
            with patch.object(tk, 'catalog', return_value=changed):
                self.assertTrue(any('Stale opencode.json' in e for e in tk.check(root)))
            self.assertEqual(path.read_bytes(), before)
            path.write_text('{broken')
            with patch.object(tk, 'catalog', return_value=original):
                self.assertTrue(any('Invalid repository OpenCode' in e for e in tk.check(root)))
            self.assertEqual(path.read_text(), '{broken')

    def test_native_configuration_cli_is_deterministic_and_read_only(self):
        before = (tk.ROOT/'opencode.json').read_bytes()
        with patch('sys.stdout', new_callable=io.StringIO) as output:
            self.assertEqual(tk.main(['opencode-config']), 0)
            first = output.getvalue()
        with patch('sys.stdout', new_callable=io.StringIO) as output:
            self.assertEqual(tk.main(['opencode-config']), 0)
            self.assertEqual(output.getvalue(), first)
        self.assertEqual(json.loads(first), json.loads(before))
        self.assertEqual((tk.ROOT/'opencode.json').read_bytes(), before)

    def test_complete_catalog_and_links(self):
        entries = tk.catalog()
        self.assertTrue({'agent', 'skill'} <= {e.kind for e in entries})
        self.assertEqual({e.domain for e in entries}, set(tk.domains()))
        self.assertEqual(tk.check(), [])

    def test_link_check_covers_project_knowledge_and_excludes_local_work(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in ('README.md', 'PROJECT.md', 'AGENTS.md', 'CONTRIBUTING.md',
                         '.github/copilot-instructions.md'):
                path = root/name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text('# Entry\n')
            (root/'PROJECT.md').write_text('[Context](missing-context.md)\n')
            (root/'knowledge').mkdir()
            (root/'knowledge/current.md').write_text('[Contract](missing-contract.md)\n')
            (root/'workspace/work').mkdir(parents=True)
            (root/'workspace/work/private.md').write_text('[Local only](absent.md)\n')
            with patch.object(tk, 'catalog', return_value=[]):
                errors = tk.check(root)
                self.assertTrue(any('PROJECT.md -> missing-context.md' in e for e in errors))
                self.assertTrue(any('knowledge/current.md -> missing-contract.md' in e for e in errors))
                self.assertFalse(any('private.md' in e for e in errors))
                (root/'PROJECT.md').write_text('# Context\n')
                (root/'knowledge/current.md').write_text('# Contract\n')
                self.assertEqual(tk.check(root), [])

    def test_frontmatter_rejects_duplicate_or_invalid_values(self):
        for text in ('No metadata', '---\nname: test\nname: other\n---\n', '---\nname: "broken\n---\n'):
            with self.subTest(text=text), self.assertRaises(tk.ToolkitError):
                tk.metadata(text)

    def test_unicode_and_slug_validation(self):
        meta, body = tk.metadata('---\nname: "joerg"\ndescription: "Act as Jörg"\n---\n\nBody')
        self.assertEqual((meta['description'], body), ('Act as Jörg', 'Body'))
        for name in ('../escape', 'Bad_Name', 'double--dash', 'x'*65, ''):
            with self.subTest(name=name), self.assertRaises(tk.ToolkitError):
                tk.slug(name)

    def test_obsidian_uri_encodes_every_component(self):
        self.assertEqual(tk.obsidian_uri('Jörgs Wissen & Ideen', '01_Projects/Kunden #1.md'),
                         'obsidian://open?vault=J%C3%B6rgs%20Wissen%20%26%20Ideen&file=01_Projects%2FKunden%20%231.md')
        self.assertIn('Projects%2FNote.md', tk.obsidian_uri('Vault', 'Projects\\Note.md'))

    def test_obsidian_uri_rejects_absolute_and_parent_paths(self):
        for path in ('/mnt/c/vault/note.md','C:\\vault\\note.md','../note.md','Projects/../note.md','Projects//note.md'):
            with self.subTest(path=path), self.assertRaises(tk.ToolkitError):
                tk.obsidian_uri('Vault', path)


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.output = Path(self.temp.name) / 'bundle'

    def test_all_native_layouts_and_rebased_links(self):
        for runtime, skills, agents in [('opencode','skills','agents'), ('copilot','.github/skills','.github/agents'), ('claude','.claude/skills','.claude/agents'), ('portable','.agents/skills','agents')]:
            with self.subTest(runtime=runtime):
                output = self.output / runtime
                result = tk.export(runtime, output)
                expected = {kind: {e.name for e in tk.catalog() if e.kind == kind} for kind in ('agent', 'skill')}
                self.assertEqual((result['agents'], result['skills']), tuple(len(expected[k]) for k in ('agent', 'skill')))
                self.assertEqual({p.parent.name for p in (output/skills).glob('*/SKILL.md')}, expected['skill'])
                self.assertEqual({p.name.removesuffix('.agent.md').removesuffix('.md') for p in (output/agents).glob('*.md')}, expected['agent'])
                for path in list((output/skills).rglob('*.md')) + list((output/agents).glob('*.md')):
                    for target in tk.LINK.findall(path.read_text()):
                        if not tk.urlsplit(target).scheme:
                            self.assertTrue((path.parent / tk.unquote(target.split('#')[0])).exists(), (path,target))
                skill = output/skills/'api-design/SKILL.md'
                self.assertIn('references/api-design.md',skill.read_text())

    def test_opencode_primary_profiles_permissions_and_no_model_forcing(self):
        tk.export('opencode', self.output)
        config = json.loads((self.output/'opencode.json').read_text())
        self.assertEqual(config['default_agent'], 'task-orchestrator')
        self.assertNotIn('model', config)
        self.assertNotIn('plugin', config)
        self.assertTrue(Path(config['instructions'][0]).is_file())
        self.assertIn('mode: primary', (self.output/'agents/joerg.md').read_text())
        self.assertIn('mode: subagent', (self.output/'agents/python-expert.md').read_text())
        self.assertNotIn("'workspace/work/**': allow", (self.output/'agents/plan.md').read_text())
        self.assertNotIn("'workspace/archive/**': allow", (self.output/'agents/plan.md').read_text())
        self.assertNotIn("'.ai/work/**': allow", (self.output/'agents/plan.md').read_text())
        self.assertNotIn("'workspace/**': allow", (self.output/'agents/plan.md').read_text())
        self.assertIn('bash: deny', (self.output/'agents/code-reviewer.md').read_text())

    def test_private_plan_directory_is_explicit_and_scoped_to_markdown(self):
        plans = Path(self.temp.name) / 'My Second Brain' / 'Project Plans'
        plans.mkdir(parents=True)
        options = tk.OpenCodeOptions(plan_directory=plans)
        tk.export('opencode', self.output, opencode_options=options)
        plan = (self.output/'agents/plan.md').read_text()
        self.assertIn("    '*': deny", plan)
        self.assertIn(f'    {json.dumps(str(plans) + "/*.md")}: allow', plan)
        self.assertIn(f'  external_directory:\n    {json.dumps(str(plans) + "/*")}: allow', plan)
        self.assertIn('  bash: deny\n  task: deny', plan)
        config = json.loads((self.output/'opencode.json').read_text())
        private = Path(config['instructions'][1])
        self.assertIn(str(plans), private.read_text())
        self.assertNotIn(str(plans), (self.output/'catalog/agents/general/plan.agent.md').read_text())
        self.assertNotIn(str(plans), (self.output/'agents/code-reviewer.md').read_text())
        self.assertEqual(list(plans.iterdir()), [])  # Export does not create notes in the vault.
        private.write_text('Human-owned private settings')
        with self.assertRaisesRegex(tk.ToolkitError, 'edited file'):
            tk.export('opencode', self.output, opencode_options=options)

    def test_plan_directory_rejects_missing_broad_and_repository_paths(self):
        for directory in (Path('relative'), Path(self.temp.name)/'missing', Path.home(),
                          Path('/'), tk.ROOT, tk.ROOT/'agents'):
            with self.subTest(directory=directory), self.assertRaises(tk.ToolkitError):
                tk.export('opencode', self.output, opencode_options=tk.OpenCodeOptions(plan_directory=directory))
        with self.assertRaisesRegex(tk.ToolkitError, 'require --runtime opencode'):
            tk.export('claude', self.output, opencode_options=tk.OpenCodeOptions(plan_directory=Path(self.temp.name)))
        plans = Path(self.temp.name)/'plans'
        plans.mkdir()
        with self.assertRaisesRegex(tk.ToolkitError, 'separate from personal plan'):
            tk.export('opencode', plans/'bundle', opencode_options=tk.OpenCodeOptions(plan_directory=plans))
        self.assertFalse(self.output.exists())

    def test_cli_exports_a_private_plan_location_without_enabling_repo_edits(self):
        plans = Path(self.temp.name)/'plans'
        plans.mkdir()
        with patch('sys.stdout', new_callable=io.StringIO):
            self.assertEqual(tk.main(['export', '--runtime', 'opencode', '--output', str(self.output),
                                     '--plan-directory', str(plans)]), 0)
        plan = (self.output/'agents/plan.md').read_text()
        self.assertNotIn("'workspace/work/**': allow", plan)
        self.assertIn(str(plans), plan)

    def test_claude_import_permissions_and_existing_instructions(self):
        tk.export('claude', self.output)
        entrypoint = self.output / 'CLAUDE.md'
        imported = entrypoint.read_text().strip().removeprefix('@')
        self.assertTrue((self.output / imported).is_file())
        self.assertEqual((self.output / imported).read_bytes(), (tk.ROOT / 'toolkit/SESSION-RULES.md').read_bytes())
        for name in ('plan', 'code-reviewer', 'architecture-reviewer'):
            profile = (self.output / f'.claude/agents/{name}.md').read_text()
            frontmatter = profile.split('---')[1]
            self.assertIn('tools: Read, Grep, Glob', frontmatter)
            self.assertNotIn('Bash', frontmatter)
            self.assertNotIn('permission:', frontmatter)
        writer = (self.output / '.claude/agents/build.md').read_text().split('---')[1]
        self.assertNotIn('tools:', writer)
        self.assertNotIn('model:', writer)
        self.assertFalse((self.output / '.claude/settings.json').exists())
        entrypoint.write_text('Existing customer rules')
        with self.assertRaisesRegex(tk.ToolkitError, 'edited file'):
            tk.export('claude', self.output)
        self.assertEqual(entrypoint.read_text(), 'Existing customer rules')

    def test_claude_cli_dry_run_and_unmanaged_file_protection(self):
        args = ['export', '--runtime', 'claude', '--output', str(self.output)]
        with patch('sys.stdout', new_callable=io.StringIO):
            self.assertEqual(tk.main(args + ['--dry-run']), 0)
        self.assertFalse(self.output.exists())
        self.output.mkdir()
        (self.output / 'CLAUDE.md').write_text('Customer guidance')
        with self.assertRaisesRegex(tk.ToolkitError, 'unmanaged or edited'):
            tk.export('claude', self.output)
        self.assertFalse((self.output / '.claude').exists())
        self.assertEqual((self.output / 'CLAUDE.md').read_text(), 'Customer guidance')

    def test_update_is_idempotent_and_protects_human_edits(self):
        tk.export('opencode', self.output)
        before = (self.output/'opencode.json').read_bytes()
        tk.export('opencode', self.output)
        self.assertEqual((self.output/'opencode.json').read_bytes(), before)
        (self.output/'agents/joerg.md').write_text('My custom instructions')
        with self.assertRaisesRegex(tk.ToolkitError, 'edited file'):
            tk.export('opencode', self.output)
        self.assertEqual((self.output/'agents/joerg.md').read_text(), 'My custom instructions')

    def test_plannotator_opt_in_preserves_plan_permissions_and_catalog(self):
        options = tk.OpenCodeOptions(plannotator=True)
        tk.export('opencode', self.output, opencode_options=options)
        config = json.loads((self.output/'opencode.json').read_text())
        self.assertEqual(config['plugin'], [['@plannotator/opencode@latest', {'workflow': 'user-managed'}]])
        self.assertEqual(config['share'], 'disabled')
        self.assertEqual(config['permission']['submit_plan'], 'deny')
        self.assertNotIn('model', config)
        plan = (self.output/'agents/plan.md').read_text()
        self.assertIn('  submit_plan: allow\n  plan_exit: deny\n', plan)
        self.assertNotIn("'workspace/work/**': allow", plan)
        self.assertNotIn("'*.md': allow", plan)
        self.assertIn('  bash: deny\n  task: deny\n', plan)
        self.assertIn('installed tool schema', plan)
        self.assertNotIn('Plannotator plan review is enabled.', (self.output/'catalog/agents/general/plan.agent.md').read_text())
        with patch.object(tk, 'atomic_write', wraps=tk.atomic_write) as write:
            again = tk.export('opencode', self.output, opencode_options=options)
        write.assert_not_called()
        self.assertEqual(again['changed'], 0)

    def test_models_and_variants_are_independent_without_enabling_plugins(self):
        options = tk.OpenCodeOptions(plan_model='local/planner', plan_variant='high',
                                     build_model='other/coder', build_variant='medium')
        tk.export('opencode', self.output, opencode_options=options)
        config = json.loads((self.output/'opencode.json').read_text())
        self.assertEqual(config['agent'], {'plan': {'model': 'local/planner', 'variant': 'high'},
                                           'build': {'model': 'other/coder', 'variant': 'medium'}})
        self.assertNotIn('plugin', config)
        self.assertNotIn('model', config)
        self.assertIn('bash: deny', (self.output/'agents/plan.md').read_text())

    def test_team_routes_are_native_selected_settings_and_preserve_review_permissions(self):
        options = tk.OpenCodeOptions(lead_model='approved/strong', lead_variant='high',
                                     worker_model='approved/economical',
                                     review_model='approved/reviewer', review_variant='high')
        tk.export('opencode', self.output, preset='team', opencode_options=options)
        config = json.loads((self.output/'opencode.json').read_text())
        self.assertEqual(config['default_agent'], 'task-orchestrator')
        for name in ('joerg', 'product-manager', 'lead-architect', 'task-orchestrator', 'gcp-architect', 'test-strategist'):
            self.assertEqual(config['agent'][name], {'model': 'approved/strong', 'variant': 'high'})
        for name in ('python-expert', 'frontend-expert', 'terraform-engineer', 'devops-agent', 'documentation-editor'):
            self.assertEqual(config['agent'][name], {'model': 'approved/economical'})
        for name in ('code-reviewer', 'architecture-reviewer'):
            self.assertEqual(config['agent'][name], {'model': 'approved/reviewer', 'variant': 'high'})
            profile = (self.output/f'agents/{name}.md').read_text()
            self.assertIn("    '*': deny", profile)
            self.assertIn('  bash: deny\n  task: deny', profile)
        self.assertNotIn('game-developer', config['agent'])
        self.assertNotIn('model', config)
        self.assertNotIn('plugin', config)
        self.assertNotIn('permission', config['agent']['task-orchestrator'])
        for name in tk.TEAM_LEADS:
            self.assertIn('mode: all', (self.output/f'agents/{name}.md').read_text())
        self.assertNotIn('approved/strong', (self.output/'catalog/agents/delivery/product-manager.agent.md').read_text())
        self.assertEqual(tk.export('opencode', self.output, preset='team', opencode_options=options)['changed'], 0)

    def test_explicit_phase_model_replaces_tier_variant_without_stale_inheritance(self):
        options = tk.OpenCodeOptions(lead_model='approved/strong', lead_variant='high',
                                     worker_model='approved/economical', worker_variant='low',
                                     plan_model='local/planner',
                                     build_model='local/coder', build_variant='medium')
        tk.export('opencode', self.output, opencode_options=options)
        config = json.loads((self.output/'opencode.json').read_text())
        self.assertEqual(config['agent']['plan'], {'model': 'local/planner'})
        self.assertEqual(config['agent']['build'], {'model': 'local/coder', 'variant': 'medium'})
        self.assertEqual(config['agent']['joerg'], {'model': 'approved/strong', 'variant': 'high'})
        self.assertEqual(config['agent']['python-expert'], {'model': 'approved/economical', 'variant': 'low'})
        self.assertIn('  bash: deny\n  task: deny', (self.output/'agents/plan.md').read_text())

    def test_team_route_cli_validates_before_writes_and_preserves_local_configuration(self):
        args = ['export', '--runtime', 'opencode', '--preset', 'team', '--output', str(self.output),
                '--lead-model', 'approved/strong', '--lead-variant', 'high',
                '--worker-model', 'approved/economical',
                '--review-model', 'approved/reviewer', '--review-variant', 'high']
        with patch('sys.stdout', new_callable=io.StringIO):
            self.assertEqual(tk.main(args + ['--dry-run']), 0)
            self.assertFalse(self.output.exists())
            self.assertEqual(tk.main(args), 0)
        config_path = self.output/'opencode.json'
        config = json.loads(config_path.read_text())
        self.assertEqual(config['agent']['python-expert']['model'], 'approved/economical')
        config_path.write_text('Human-owned model configuration')
        with patch('sys.stderr', new_callable=io.StringIO):
            self.assertEqual(tk.main(args), 1)
        self.assertEqual(config_path.read_text(), 'Human-owned model configuration')
        for route in ('lead', 'worker', 'review'):
            output = self.output/route
            for settings in ({f'{route}_variant': 'high'}, {f'{route}_model': 'invalid'},
                             {f'{route}_model': 'approved/model', f'{route}_variant': 'bad name'}):
                with self.subTest(route=route, settings=settings), self.assertRaises(tk.ToolkitError):
                    tk.export('opencode', output, opencode_options=tk.OpenCodeOptions(**settings))
                self.assertFalse(output.exists())
            with self.assertRaisesRegex(tk.ToolkitError, 'runtime opencode'):
                tk.export('portable', output, opencode_options=tk.OpenCodeOptions(**{f'{route}_model': 'approved/model'}))
            self.assertFalse(output.exists())

    def test_portable_startup_entry_resolves_and_preserves_customer_instructions(self):
        self.output.mkdir()
        entry = self.output/'AGENTS.md'
        entry.write_text('Customer project instructions')
        with self.assertRaisesRegex(tk.ToolkitError, 'unmanaged or edited'):
            tk.export('portable', self.output, preset='team')
        self.assertEqual(entry.read_text(), 'Customer project instructions')
        self.assertFalse((self.output/'catalog').exists())
        entry.unlink()
        tk.export('portable', self.output, preset='team')
        target = tk.LINK.findall(entry.read_text())[0]
        self.assertEqual((entry.parent/target).read_bytes(), (tk.ROOT/'toolkit/SESSION-RULES.md').read_bytes())
        entry.write_text('Customer additions')
        with self.assertRaisesRegex(tk.ToolkitError, 'unmanaged or edited'):
            tk.export('portable', self.output, preset='team')
        self.assertEqual(entry.read_text(), 'Customer additions')

    def test_opencode_options_reject_invalid_input_before_writing(self):
        for options in (tk.OpenCodeOptions(plan_variant='high'), tk.OpenCodeOptions(build_variant='medium'),
                        tk.OpenCodeOptions(plan_model='no-provider'), tk.OpenCodeOptions(build_model='provider/'),
                        tk.OpenCodeOptions(plan_model='provider/model#high'),
                        tk.OpenCodeOptions(plan_model='provider/model\nother'),
                        tk.OpenCodeOptions(plan_model='provider/model', plan_variant='bad name')):
            with self.subTest(options=options), self.assertRaises(tk.ToolkitError):
                tk.export('opencode', self.output, opencode_options=options)
            self.assertFalse(self.output.exists())
        for runtime in ('copilot', 'claude', 'portable'):
            for options in (tk.OpenCodeOptions(plannotator=True), tk.OpenCodeOptions(build_model='provider/model')):
                with self.subTest(runtime=runtime, options=options), self.assertRaisesRegex(tk.ToolkitError, 'runtime opencode'):
                    tk.export(runtime, self.output, opencode_options=options)
                self.assertFalse(self.output.exists())

    def test_cli_exports_review_and_phase_settings_and_protects_edits(self):
        args = ['export', '--runtime', 'opencode', '--output', str(self.output), '--plannotator',
                '--plan-model', 'provider/planner', '--build-model', 'provider/coder',
                '--plan-variant', 'high', '--build-variant', 'medium']
        with patch('sys.stdout', new_callable=io.StringIO):
            self.assertEqual(tk.main(args + ['--dry-run']), 0)
            self.assertFalse(self.output.exists())
            self.assertEqual(tk.main(args), 0)
        path = self.output/'opencode.json'
        config = json.loads(path.read_text())
        self.assertEqual(config['agent']['plan']['variant'], 'high')
        self.assertEqual(config['agent']['build']['model'], 'provider/coder')
        config['agent']['build']['model'] = 'human/choice'
        path.write_text(json.dumps(config))
        with patch('sys.stderr', new_callable=io.StringIO):
            self.assertEqual(tk.main(args), 1)
        self.assertEqual(json.loads(path.read_text())['agent']['build']['model'], 'human/choice')

    def test_unchanged_exports_preserve_files_and_write_nothing(self):
        for runtime in ('opencode', 'copilot', 'claude', 'portable'):
            with self.subTest(runtime=runtime):
                output = self.output / runtime
                first = tk.export(runtime, output)
                before = {p: (p.stat().st_ino, p.stat().st_mtime_ns)
                          for p in output.rglob('*') if p.is_file()}
                with patch.object(tk, 'atomic_write', wraps=tk.atomic_write) as write:
                    second = tk.export(runtime, output)
                write.assert_not_called()
                self.assertEqual((second['changed'], second['removed']), (0, 0))
                self.assertEqual(second['unchanged'], first['files'])
                self.assertEqual(before, {p: (p.stat().st_ino, p.stat().st_mtime_ns)
                                         for p in before})

    def source_fixture(self):
        root = Path(self.temp.name) / 'source'
        for folder, name in (('agents', 'one.agent.md'), ('agents', 'two.agent.md'),
                             ('skills/skill', 'SKILL.md')):
            path = root / folder / name
            path.parent.mkdir(parents=True, exist_ok=True)
            slug = 'skill' if name == 'SKILL.md' else name.removesuffix('.agent.md')
            path.write_text(f'---\nname: {slug}\ndescription: A focused profile\n---\n\nOriginal body.\n')
        return root

    def test_source_update_only_rewrites_affected_files(self):
        root = self.source_fixture()
        tk.export('portable', self.output, root)
        source = root / 'agents/one.agent.md'
        source.write_text(source.read_text().replace('Original body.', 'Updated body.'))
        with patch.object(tk, 'atomic_write', wraps=tk.atomic_write) as write:
            result = tk.export('portable', self.output, root)
        self.assertEqual({call.args[0].relative_to(self.output).as_posix()
                          for call in write.call_args_list},
                         {'catalog/agents/one.agent.md', 'agents/one.agent.md', '.ai-toolkit-manifest.json'})
        self.assertEqual(result['changed'], 2)
        self.assertIn('Updated body.', (self.output / 'agents/one.agent.md').read_text())

    def test_obsolete_files_are_removed_but_edited_ones_are_protected(self):
        root = self.source_fixture()
        tk.export('portable', self.output, root)
        (root / 'agents/two.agent.md').unlink()
        edited = self.output / 'agents/two.agent.md'
        edited.write_text('Keep this human edit.')
        with self.assertRaisesRegex(tk.ToolkitError, 'edited file'):
            tk.export('portable', self.output, root)
        self.assertEqual(edited.read_text(), 'Keep this human edit.')
        preview = tk.export('portable', self.output, root, force=True, dry_run=True)
        self.assertEqual((preview['changed'], preview['removed']), (1, 2))
        self.assertTrue(edited.exists())
        result = tk.export('portable', self.output, root, force=True)
        self.assertEqual((result['changed'], result['removed']), (1, 2))
        self.assertFalse(edited.exists())
        self.assertFalse((self.output / 'catalog/agents/two.agent.md').exists())
        self.assertTrue((self.output / 'agents/one.agent.md').is_file())

    def test_missing_owned_file_is_restored(self):
        tk.export('opencode', self.output)
        missing = self.output / 'agents/build.md'
        expected = missing.read_bytes()
        missing.unlink()
        with patch.object(tk, 'atomic_write', wraps=tk.atomic_write) as write:
            result = tk.export('opencode', self.output)
        self.assertEqual(result['changed'], 1)
        self.assertEqual([call.args[0] for call in write.call_args_list], [missing])
        self.assertEqual(missing.read_bytes(), expected)

    def test_unmanaged_configuration_is_not_overwritten(self):
        self.output.mkdir()
        (self.output/'opencode.json').write_text('{"model":"my-model"}')
        with self.assertRaises(tk.ToolkitError):
            tk.export('opencode', self.output)
        self.assertFalse((self.output/'catalog').exists())
        tk.export('opencode', self.output, force=True)
        self.assertEqual(json.loads((self.output/'opencode.json').read_text())['default_agent'], 'task-orchestrator')

    def test_dry_run_writes_nothing(self):
        tk.export('portable',self.output,dry_run=True)
        self.assertFalse(self.output.exists())

    def test_manifest_traversal_and_symlinks_are_rejected(self):
        self.output.mkdir()
        manifest = self.output/'.ai-toolkit-manifest.json'
        manifest.write_text(json.dumps({'files':{'../outside.txt':'anything'}}))
        with self.assertRaises(tk.ToolkitError):
            tk.export('opencode',self.output)
        manifest.unlink()
        outside = Path(self.temp.name)/'outside'
        outside.mkdir()
        (self.output/'catalog').symlink_to(outside,target_is_directory=True)
        with self.assertRaises(tk.ToolkitError):
            tk.export('opencode',self.output,force=True)
        self.assertEqual(list(outside.iterdir()),[])

    def test_sources_and_parent_cannot_be_export_destinations(self):
        for output in (tk.ROOT,tk.ROOT.parent,tk.ROOT/'skills/generated'):
            with self.subTest(output=output), self.assertRaises(tk.ToolkitError):
                tk.export('opencode',output,dry_run=True)


class WorkTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.workspace = Path(self.temp.name)
        self.store = tk.WorkStore(self.workspace)
        self.record = self.store.create('feature', 'A useful feature', 'product')

    def test_create_read_and_duplicate_protection(self):
        self.assertEqual(self.record['title'],'A useful feature')
        self.assertEqual(self.record['path'], 'workspace/work/feature.md')
        self.assertFalse((self.workspace / '.ai').exists())
        self.assertEqual(self.record['tasks'][0]['status'],'open')
        self.assertEqual(len(self.store.list()),1)
        with self.assertRaises(tk.Conflict):
            self.store.create('feature','Duplicate')

    def test_create_preserves_literal_template_tokens_in_user_titles(self):
        titles = ['Investigate "{{title}}" escaping', 'Investigate {{kind}} escaping',
                  '{{id}} / {{title_json}} / {{title}} / {{kind}}',
                  'Quoted "title" with Unicode: Z\u00fcrich\nsecond line']
        for index, title in enumerate(titles):
            with self.subTest(title=title):
                record = self.store.create(f'literal-{index}', title, 'product')
                self.assertEqual(record['title'], title)
                self.assertEqual(record['kind'], 'product')
                self.assertIn('# ' + title.replace('\n', ' ') + '\n', record['markdown'])
                self.assertEqual(tk.WorkStore(self.workspace).read(record['id'])['title'], title)
        self.assertEqual([record['title'] for record in self.store.list()][1:], titles)

    def test_feedback_preserves_plan_comments_and_task_evidence(self):
        first = self.store.feedback('feature','Keep my exact words: <script>alert(1)</script>',self.record['etag'])
        second = self.store.feedback('feature','A second\nmultiline comment',first['etag'])
        self.assertIn('### F1',second['markdown'])
        self.assertIn('### F2',second['markdown'])
        self.assertIn('> Keep my exact words: <script>alert(1)</script>',second['markdown'])
        updated = self.store.task('feature','T1','done','unittest: acceptance scenario passed',second['etag'])
        self.assertIn('A second',updated['markdown'])
        self.assertIn('## Plan',updated['markdown'])
        self.assertEqual(updated['tasks'][0]['status'],'done')

    def test_stale_update_does_not_drop_other_comments(self):
        current = self.store.feedback('feature','New human comment',self.record['etag'])
        with self.assertRaises(tk.Conflict):
            self.store.task('feature','T1','done','checked',self.record['etag'])
        self.assertEqual(self.store.read('feature')['markdown'],current['markdown'])

    def test_two_concurrent_feedback_writes_require_retry(self):
        def write(comment):
            try:
                self.store.feedback('feature',comment,self.record['etag'])
                return 'saved'
            except tk.Conflict:
                return 'conflict'
        with ThreadPoolExecutor(max_workers=2) as pool:
            outcomes = list(pool.map(write,['one','two']))
        self.assertCountEqual(outcomes,['saved','conflict'])
        self.assertEqual(self.store.read('feature')['markdown'].count('### F1'),1)

    def test_external_editor_change_is_detected(self):
        path = self.store.path('feature')
        path.write_text(path.read_text()+'\nHuman note from the editor.\n')
        with self.assertRaises(tk.Conflict):
            self.store.feedback('feature','comment',self.record['etag'])
        self.assertIn('Human note',path.read_text())

    def test_editor_save_during_temporary_file_flush_is_preserved(self):
        path = self.store.path('feature')
        edited = self.record['markdown'] + '\nEditor save during preparation.\n'
        fsync = tk.os.fsync

        def save_from_editor(descriptor):
            editor_file = path.with_suffix('.editor')
            editor_file.write_text(edited)
            editor_file.replace(path)
            return fsync(descriptor)

        with patch.object(tk.os, 'fsync', side_effect=save_from_editor):
            with self.assertRaisesRegex(tk.Conflict, 'changed'):
                self.store.feedback('feature', 'Pending feedback', self.record['etag'])
        self.assertEqual(path.read_text(), edited)
        self.assertEqual(list(path.parent.glob('.feature.md.*')), [])

    def test_independent_stores_cannot_overwrite_concurrent_creation(self):
        path = self.store.path('simultaneous')
        ready = threading.Barrier(2)
        file_hash = tk._export_file_hash

        def observe_absence(target):
            observed = file_hash(target)
            if target == path:
                ready.wait(timeout=5)
            return observed

        def create(title):
            try:
                return tk.WorkStore(self.workspace).create('simultaneous', title)['title']
            except tk.Conflict:
                return 'conflict'

        with patch.object(tk, '_export_file_hash', side_effect=observe_absence):
            with ThreadPoolExecutor(max_workers=2) as pool:
                outcomes = list(pool.map(create, ['First creator', 'Second creator']))
        self.assertEqual(outcomes.count('conflict'), 1)
        saved = [outcome for outcome in outcomes if outcome != 'conflict']
        self.assertEqual(self.store.read('simultaneous')['title'], saved[0])
        self.assertEqual(list(path.parent.glob('.simultaneous.md.*')), [])

    def test_completed_task_needs_evidence_and_known_id(self):
        with self.assertRaises(tk.ToolkitError):
            self.store.task('feature','T1','done','',self.record['etag'])
        with self.assertRaises(tk.ToolkitError):
            self.store.task('feature','T9','open','',self.record['etag'])

    def test_archiving_requires_completion_and_preserves_record(self):
        with self.assertRaises(tk.ToolkitError):
            self.store.archive('feature',self.record['etag'])
        current = self.store.task('feature','T1','done','Acceptance checks passed',self.record['etag'])
        archived = self.store.archive('feature',current['etag'])
        self.assertEqual(archived['status'],'archived')
        self.assertEqual(archived['path'], 'workspace/archive/feature.md')
        self.assertEqual(len(self.store.list()),0)
        self.assertEqual(len(self.store.list(True)),1)
        self.assertIn('Acceptance checks passed',archived['markdown'])

    def test_archive_never_overwrites_a_destination_created_during_flush(self):
        current = self.store.task('feature', 'T1', 'done', 'Verified', self.record['etag'])
        destination = self.store.path('feature', True)
        fsync = tk.os.fsync

        def create_other_archive(descriptor):
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text('Archive created by another writer.\n')
            return fsync(descriptor)

        with patch.object(tk.os, 'fsync', side_effect=create_other_archive):
            with self.assertRaises(tk.Conflict):
                self.store.archive('feature', current['etag'])
        self.assertEqual(destination.read_text(), 'Archive created by another writer.\n')
        self.assertEqual(self.store.read('feature')['markdown'], current['markdown'])

    def test_archive_preserves_an_editor_save_during_flush(self):
        current = self.store.task('feature', 'T1', 'done', 'Verified', self.record['etag'])
        source = self.store.path('feature')
        edited = current['markdown'] + '\nEditor save before archiving.\n'
        fsync = tk.os.fsync

        def save_from_editor(descriptor):
            source.write_text(edited)
            return fsync(descriptor)

        with patch.object(tk.os, 'fsync', side_effect=save_from_editor):
            with self.assertRaisesRegex(tk.Conflict, 'changed'):
                self.store.archive('feature', current['etag'])
        self.assertEqual(source.read_text(), edited)
        self.assertFalse(self.store.path('feature', True).exists())

    def test_archive_retains_active_record_if_prepared_archive_is_edited(self):
        current = self.store.task('feature', 'T1', 'done', 'Verified', self.record['etag'])
        destination = self.store.path('feature', True)
        atomic_write = tk.atomic_write

        def edit_prepared_archive(path, data, **kwargs):
            atomic_write(path, data, **kwargs)
            if path == destination:
                path.write_text('Another writer edited the archive.\n')

        with patch.object(tk, 'atomic_write', side_effect=edit_prepared_archive):
            with self.assertRaisesRegex(tk.Conflict, 'Archive changed'):
                self.store.archive('feature', current['etag'])
        self.assertEqual(self.store.read('feature')['markdown'], current['markdown'])
        self.assertEqual(destination.read_text(), 'Another writer edited the archive.\n')

    def test_failed_active_removal_cleans_own_archive_and_allows_retry(self):
        current = self.store.task('feature', 'T1', 'done', 'Verified', self.record['etag'])
        source = self.store.path('feature')
        destination = self.store.path('feature', True)
        unlink = Path.unlink

        def refuse_active_removal(path, *args, **kwargs):
            if path == source:
                raise PermissionError('Active record cannot be removed')
            return unlink(path, *args, **kwargs)

        with patch.object(Path, 'unlink', refuse_active_removal):
            with self.assertRaisesRegex(PermissionError, 'Active record cannot be removed'):
                self.store.archive('feature', current['etag'])
        self.assertEqual(self.store.read('feature')['markdown'], current['markdown'])
        self.assertFalse(destination.exists())
        archived = self.store.archive('feature', current['etag'])
        self.assertEqual(archived['status'], 'archived')
        self.assertFalse(source.exists())

    def test_failed_active_removal_preserves_an_archive_edited_after_preflight(self):
        current = self.store.task('feature', 'T1', 'done', 'Verified', self.record['etag'])
        source = self.store.path('feature')
        destination = self.store.path('feature', True)
        unlink = Path.unlink

        def edit_archive_and_refuse_removal(path, *args, **kwargs):
            if path == source:
                destination.write_text('Archive edit made during active removal.\n')
                raise PermissionError('Active record cannot be removed')
            return unlink(path, *args, **kwargs)

        with patch.object(Path, 'unlink', edit_archive_and_refuse_removal):
            with self.assertRaisesRegex(PermissionError, 'Active record cannot be removed'):
                self.store.archive('feature', current['etag'])
        self.assertEqual(self.store.read('feature')['markdown'], current['markdown'])
        self.assertEqual(destination.read_text(), 'Archive edit made during active removal.\n')

    def test_malformed_or_duplicate_task_rows_are_not_silently_ignored(self):
        for replacement in ('| T1 | A task | unknown |  |','| T1 | A task | open |  |\n| T1 | Duplicate | done | test |'):
            with self.subTest(replacement=replacement):
                text = tk.TASK_ROW.sub(replacement,self.record['markdown'])
                self.store.path('feature').write_text(text)
                with self.assertRaises(tk.ToolkitError):
                    self.store.read('feature')

    def test_task_update_ignores_table_examples_outside_tasks_section(self):
        path = self.store.path('feature')
        example = '\n| T1 | Historical example | open |  |\n'
        path.write_text(path.read_text()+example)
        current = self.store.read('feature')
        updated = self.store.task('feature','T1','done','verified',current['etag'])
        self.assertTrue(updated['markdown'].endswith(example))

    def test_paths_and_symlinked_record_are_rejected(self):
        with self.assertRaises(tk.ToolkitError):
            self.store.create('../escape','Bad')
        target = self.workspace/'private.md'
        target.write_text('private')
        self.store.path('feature').unlink()
        (self.workspace/'workspace/work/feature.md').symlink_to(target)
        with self.assertRaises(tk.ToolkitError):
            self.store.read('feature')
        self.assertEqual(target.read_text(),'private')

    def test_csv_is_generated_and_formula_safe(self):
        path = self.store.path('feature')
        path.write_text(path.read_text().replace('Define and verify the outcome','=SUM(1,2)'))
        rows = list(csv.reader(io.StringIO(self.store.csv('feature'))))
        self.assertEqual(rows[0],['id','title','status','evidence'])
        self.assertEqual(rows[1][1],"'=SUM(1,2)")


class WorkspaceMigrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = tk.WorkStore(self.root)
        self.record = self.store.create('feature', 'Preserve human context')
        self.old = self.root / '.ai/work'
        self.old.parent.mkdir()
        (self.root / 'workspace/work').rename(self.old)

    def test_legacy_records_are_reported_without_creating_a_second_plan(self):
        before = (self.old / 'feature.md').read_bytes()
        for operation in (self.store.list, lambda: self.store.read('feature'),
                          lambda: self.store.create('feature', 'Another plan')):
            with self.assertRaisesRegex(tk.ToolkitError, 'Legacy .ai'):
                operation()
        self.assertEqual((self.old / 'feature.md').read_bytes(), before)
        self.assertFalse((self.root / 'workspace/work').exists())

    def test_cli_dry_run_then_migration_preserves_active_archive_and_unknown_content(self):
        before = (self.old / 'feature.md').read_bytes()
        modified = (self.old / 'feature.md').stat().st_mtime_ns
        old_archive = self.root / '.ai/archive'
        old_archive.mkdir()
        (old_archive / 'finished.md').write_text('Human history and evidence.\n')
        (self.root / '.ai/private.txt').write_text('Unrelated content')
        args = ['work', '--workspace', str(self.root), 'migrate']
        with patch('sys.stdout', new_callable=io.StringIO) as out:
            self.assertEqual(tk.main(args + ['--dry-run']), 0)
            self.assertEqual(len(json.loads(out.getvalue())['moves']), 2)
        self.assertTrue((self.old / 'feature.md').exists())
        self.assertFalse((self.root / 'workspace/work').exists())
        with patch('sys.stdout', new_callable=io.StringIO):
            self.assertEqual(tk.main(args), 0)
        current = self.store.read('feature')
        self.assertEqual(current['etag'], self.record['etag'])
        path = self.root / current['path']
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual(path.stat().st_mtime_ns, modified)
        self.assertEqual((self.root / 'workspace/archive/finished.md').read_text(), 'Human history and evidence.\n')
        self.assertEqual((self.root / '.ai/private.txt').read_text(), 'Unrelated content')
        self.assertTrue(self.store.migrate()['legacy_directory_remaining'])
        self.assertEqual(self.store.migrate()['moves'], [])

    def test_empty_legacy_parent_is_removed_only_after_actual_migration(self):
        preview = self.store.migrate(dry_run=True)
        self.assertFalse(preview['legacy_directory_removed'])
        self.assertTrue((self.root / '.ai').exists())
        result = self.store.migrate()
        self.assertTrue(result['legacy_directory_removed'])
        self.assertFalse(result['legacy_directory_remaining'])
        self.assertFalse((self.root / '.ai').exists())
        self.assertEqual(self.store.read('feature')['etag'], self.record['etag'])
        self.assertFalse(self.store.migrate()['legacy_directory_removed'])
        self.store.create('another-feature', 'New work stays in workspace')
        self.assertFalse((self.root / '.ai').exists())

    def test_empty_legacy_root_without_records_is_removed(self):
        (self.old / 'feature.md').unlink()
        self.old.rmdir()
        result = self.store.migrate()
        self.assertEqual(result['moves'], [])
        self.assertTrue(result['legacy_directory_removed'])
        self.assertFalse((self.root / '.ai').exists())

    def test_unknown_content_added_before_parent_cleanup_is_preserved(self):
        rmdir = Path.rmdir
        def intervening_write(path):
            if path == self.root / '.ai':
                (path / 'human-note.md').write_text('Keep this new content')
            return rmdir(path)
        with patch.object(Path, 'rmdir', intervening_write):
            result = self.store.migrate()
        self.assertTrue(result['legacy_directory_remaining'])
        self.assertFalse(result['legacy_directory_removed'])
        self.assertEqual((self.root / '.ai/human-note.md').read_text(), 'Keep this new content')
        self.assertEqual(self.store.read('feature')['etag'], self.record['etag'])

    def test_preflight_conflict_in_second_destination_moves_neither_directory(self):
        old_archive = self.root / '.ai/archive'
        old_archive.mkdir()
        (old_archive / 'old.md').write_text('old')
        destination = self.root / 'workspace/archive'
        destination.mkdir()
        (destination / 'human.md').write_text('preserve')
        for dry_run in (True, False):
            with self.subTest(dry_run=dry_run), self.assertRaises(tk.Conflict):
                self.store.migrate(dry_run)
        self.assertTrue((self.old / 'feature.md').exists())
        self.assertTrue((old_archive / 'old.md').exists())
        self.assertFalse((self.root / 'workspace/work').exists())
        self.assertEqual((destination / 'human.md').read_text(), 'preserve')

    def test_symlink_in_legacy_records_is_rejected_without_moving(self):
        target = self.root / 'private.md'
        target.write_text('private')
        (self.old / 'link.md').symlink_to(target)
        with self.assertRaisesRegex(tk.ToolkitError, 'symlinks'):
            self.store.migrate()
        self.assertTrue((self.old / 'feature.md').exists())
        self.assertFalse((self.root / 'workspace/work').exists())
        self.assertEqual(target.read_text(), 'private')

    def test_interrupted_migration_can_resume_after_one_directory_moved(self):
        old_archive = self.root / '.ai/archive'
        old_archive.mkdir()
        (old_archive / 'old.md').write_text('Preserve historical evidence')
        rename = Path.rename
        def interrupted(path, target):
            if path == old_archive:
                raise OSError('Interrupted second directory move')
            return rename(path, target)
        with patch.object(Path, 'rename', interrupted), self.assertRaises(OSError):
            self.store.migrate()
        self.assertTrue((self.root / 'workspace/work/feature.md').is_file())
        self.assertTrue((old_archive / 'old.md').is_file())
        with self.assertRaisesRegex(tk.ToolkitError, 'Legacy .ai'):
            self.store.read('feature')
        self.assertEqual(len(self.store.migrate()['moves']), 1)
        self.assertEqual(self.store.read('feature')['etag'], self.record['etag'])
        self.assertEqual((self.root / 'workspace/archive/old.md').read_text(), 'Preserve historical evidence')

    def test_symlinked_workspace_root_is_rejected_without_touching_target(self):
        (self.root / 'workspace').rmdir()
        target = self.root / 'other'
        target.mkdir()
        (self.root / 'workspace').symlink_to(target, target_is_directory=True)
        with self.assertRaises(tk.ToolkitError):
            self.store.migrate()
        self.assertEqual(list(target.iterdir()), [])
        self.assertTrue((self.old / 'feature.md').exists())


class APITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        cls.server = tk.serve(Path(cls.temp.name),0)
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(target=cls.server.serve_forever,daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()
        cls.temp.cleanup()

    def request(self, method, path, data=None, headers=None):
        connection = http.client.HTTPConnection('127.0.0.1',self.port,timeout=3)
        body = json.dumps(data) if data is not None else None
        merged = {'Content-Type':'application/json',**(headers or {})}
        connection.request(method,path,body,merged)
        response = connection.getresponse()
        status, response_headers, raw = response.status, dict(response.getheaders()), response.read()
        connection.close()
        value = json.loads(raw) if 'application/json' in response_headers.get('Content-Type','') else raw.decode()
        return status,response_headers,value

    def test_catalog_frontend_and_contract_are_served_locally(self):
        status,headers,html = self.request('GET','/')
        self.assertEqual(status,200)
        self.assertIn('AI Workbench',html)
        self.assertIn("script-src 'self'",headers['Content-Security-Policy'])
        self.assertNotIn('https://',html)
        served = self.request('GET','/api/v1/catalog')[2]
        self.assertEqual({(e['kind'], e['name'], e['domain']) for e in served},
                         {(e.kind, e.name, e.domain) for e in tk.catalog()})
        self.assertEqual(self.request('GET','/api/v1/catalog/domains')[2], tk.domains())
        self.assertEqual(self.request('GET','/api/v1/openapi.json')[2]['openapi'],'3.1.0')

    def test_full_create_comment_complete_flow_with_etags(self):
        status,headers,record = self.request('POST','/api/v1/work',{'id':'api-flow','title':'API flow'})
        self.assertEqual(status,201)
        self.assertEqual(record['path'], 'workspace/work/api-flow.md')
        old_etag = headers['ETag']
        status,_,record = self.request('POST','/api/v1/work/api-flow/feedback',{'text':'Keep this comment.'},{'If-Match':old_etag})
        self.assertEqual(status,200)
        status,_,_ = self.request('PATCH','/api/v1/work/api-flow/tasks/T1',{'status':'done','evidence':'checked'},{'If-Match':old_etag})
        self.assertEqual(status,412)
        status,_,updated = self.request('PATCH','/api/v1/work/api-flow/tasks/T1',{'status':'done','evidence':'Acceptance scenario checked'},{'If-Match':record['etag']})
        self.assertEqual(status,200)
        self.assertIn('Keep this comment.',updated['markdown'])

    def test_missing_if_match(self):
        self.request('POST','/api/v1/work',{'id':'missing-match','title':'Missing match'})
        self.assertEqual(self.request('POST','/api/v1/work/missing-match/feedback',{'text':'Hi'})[0],428)

    def test_legacy_records_report_migration_instead_of_an_empty_dashboard(self):
        old = Path(self.temp.name) / '.ai/work'
        old.mkdir(parents=True)
        record = old / 'old.md'
        record.write_text('Preserve legacy content')
        try:
            status, _, value = self.request('GET', '/api/v1/work')
            self.assertEqual(status, 400)
            self.assertIn('migrate', value['error'])
            self.assertEqual(record.read_text(), 'Preserve legacy content')
        finally:
            record.unlink()
            old.rmdir()

    def test_untrusted_host_origin_and_cross_site_requests(self):
        for headers in ({'Host':'attacker.example'}, {'Origin':'https://attacker.example'}, {'Sec-Fetch-Site':'cross-site'}):
            with self.subTest(headers=headers):
                self.assertEqual(self.request('GET','/api/v1/work',headers=headers)[0],403)

    def test_bad_input_paths_media_types_and_methods(self):
        for data in ({'id':'../escape','title':'Bad'}, {'id':'bad-title','title':42}, [], {'id':'bad-kind','title':'Bad','kind':'other'}):
            with self.subTest(data=data):
                self.assertEqual(self.request('POST','/api/v1/work',data)[0],400)
        self.assertEqual(self.request('GET','/api/v1/work/%2e%2e%2fsecret')[0],404)
        self.assertEqual(self.request('GET','/missing')[0],404)
        self.assertEqual(self.request('DELETE','/api/v1/work')[0],405)
        self.assertEqual(self.request('POST','/api/v1/work',{'id':'x','title':'X'},{'Content-Type':'text/plain'})[0],415)
        self.assertEqual(self.request('POST','/api/v1/work',{'id':'large','title':'x'*17000})[0],413)


if __name__ == '__main__':
    unittest.main()
