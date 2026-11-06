"""Exercise bounded native exports, migration and preservation of edited files."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import ai_toolkit as tk
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'website'))
import generate as site


class CatalogSelectionTests(unittest.TestCase):
    def test_team_preset_exposes_three_leads_without_forcing_models(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            result = tk.export('opencode', root, preset='team')
            self.assertEqual((result['agents'], result['skills']), (13, 20))
            config = json.loads((root/'opencode.json').read_text())
            self.assertEqual(config['default_agent'], 'task-orchestrator')
            self.assertNotIn('agent', config)
            for name in ('product-manager', 'lead-architect', 'task-orchestrator'):
                profile = (root/f'agents/{name}.md').read_text()
                self.assertIn('mode: all', profile)
                for link in tk.LINK.findall(tk.FENCE.sub('', profile)):
                    if '://' not in link:
                        self.assertTrue((root/'agents'/link.split('#')[0]).exists())
            self.assertFalse((root/'agents/game-developer.md').exists())

    def test_engineering_exports_only_selected_native_profiles_in_every_runtime(self):
        layouts = {'opencode': ('agents', 'skills', '.md'),
                   'copilot': ('.github/agents', '.github/skills', '.agent.md'),
                   'claude': ('.claude/agents', '.claude/skills', '.md'),
                   'portable': ('agents', '.agents/skills', '.agent.md')}
        for runtime, (agents, skills, suffix) in layouts.items():
            with self.subTest(runtime=runtime), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                result = tk.export(runtime, root, preset='engineering')
                self.assertEqual((result['agents'], result['skills']), (9, 16))
                self.assertTrue((root/agents/('python-expert'+suffix)).is_file())
                self.assertFalse((root/agents/('game-developer'+suffix)).exists())
                self.assertFalse((root/skills/'obsidian-para/SKILL.md').exists())
                self.assertTrue((root/'catalog/toolkit/WORKFLOW.md').is_file())
                reviewer = (root/agents/('code-reviewer'+suffix)).read_text()
                if runtime == 'opencode':
                    self.assertIn('bash: deny', reviewer)
                    self.assertFalse((root/'commands/brain.md').exists())
                    config = json.loads((root/'opencode.json').read_text())
                    self.assertEqual(config['default_agent'], 'joerg')
                    self.assertEqual(Path(config['instructions'][0]).name, 'SESSION-RULES.md')
                elif runtime == 'claude':
                    self.assertIn('tools: Read, Grep, Glob', reviewer)
                elif runtime == 'copilot':
                    self.assertIn('tools: [read, search]', reviewer)
                for native in list((root/agents).glob('*'+suffix))+list((root/skills).rglob('SKILL.md')):
                    for link in tk.LINK.findall(tk.FENCE.sub('', native.read_text())):
                        if '://' not in link:
                            self.assertTrue((native.parent/link.split('#')[0]).exists(), (native, link))

    def test_canonical_process_is_exported_with_resolving_links_in_every_runtime(self):
        process = tk.ROOT/'engineering/process'
        sources = sorted(process.rglob('*.md'))
        self.assertTrue(sources, 'canonical engineering process Markdown is present')
        for runtime in tk.RUNTIMES:
            with self.subTest(runtime=runtime), tempfile.TemporaryDirectory() as folder:
                root = Path(folder)
                tk.export(runtime, root, preset='engineering')
                for source in sources:
                    exported = root/'catalog'/source.relative_to(tk.ROOT)
                    self.assertTrue(exported.is_file(), exported)
                    for link in tk.LINK.findall(tk.FENCE.sub('', exported.read_text())):
                        parts = tk.urlsplit(link)
                        if parts.scheme or parts.netloc or not parts.path:
                            continue
                        target = exported.parent/tk.unquote(parts.path)
                        self.assertTrue(target.exists(), (runtime, source, link))

    def test_process_allowlist_is_narrow_and_checker_finds_broken_local_links(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root/'engineering/process/phases').mkdir(parents=True)
            (root/'engineering/private').mkdir(parents=True)
            (root/'engineering/process/README.md').write_text('[Phase](phases/plan.md)\n')
            (root/'engineering/process/phases/plan.md').write_text('# Plan\n')
            (root/'engineering/process/private').mkdir()
            (root/'engineering/process/private/secret.md').write_text('private')
            (root/'engineering/unrelated.md').write_text('unrelated')
            sources = tk._export_source_files(root)
            self.assertEqual(set(sources), {
                'engineering/process/README.md', 'engineering/process/phases/plan.md'})
            self.assertFalse(any('private' in name or 'unrelated' in name for name in sources))

            (root/'engineering/process/README.md').write_text('[Missing](phases/missing.md)\n')
            self.assertTrue(any('Broken link: engineering/process/README.md' in error
                                for error in tk.check(root)))

    def test_nested_process_source_rejects_symlinked_engineering_ancestor(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)/'repo'
            outside = Path(folder)/'outside'
            (outside/'process').mkdir(parents=True)
            (outside/'process/README.md').write_text('must not read')
            root.mkdir()
            (root/'engineering').symlink_to(outside, target_is_directory=True)
            with self.assertRaisesRegex(tk.ToolkitError, 'Cannot export a symlink'):
                tk._export_source_files(root)

    def test_export_output_cannot_be_placed_under_canonical_engineering_tree(self):
        output = tk.ROOT/'engineering/.export-test'
        with self.assertRaisesRegex(tk.ToolkitError, 'canonical source folders'):
            tk.export('portable', output)
        self.assertFalse(output.exists())

    def test_additive_cli_selection_and_unknown_name_leave_no_partial_export(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)/'selected'
            command = [sys.executable, str(tk.ROOT/'tools/ai_toolkit.py'), 'export',
                       '--runtime', 'opencode', '--output', str(root), '--preset', 'engineering']
            bad = subprocess.run(command+['--skill', 'missing-skill'], capture_output=True, text=True)
            self.assertNotEqual(bad.returncode, 0)
            self.assertFalse(root.exists())
            retired = subprocess.run(command+['--skill', 'testing-strategies'], capture_output=True, text=True)
            self.assertIn('testing-strategies -> testing', retired.stderr)
            self.assertFalse(root.exists())
            good = subprocess.run(command+['--agent', 'golang-expert', '--skill', 'golang-patterns'],
                                  capture_output=True, text=True, check=True)
            self.assertEqual(json.loads(good.stdout)['skills'], 17)
            self.assertTrue((root/'agents/golang-expert.md').is_file())
            self.assertTrue((root/'skills/golang-patterns/SKILL.md').is_file())
            self.assertFalse((root/'agents/flutter-ios-expert.md').exists())

    def test_narrowing_removes_owned_profiles_but_preserves_edited_profiles(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            tk.export('opencode', root)
            game = root/'agents/game-developer.md'
            game.write_text(game.read_text()+'\nHuman custom rule.\n')
            before = {str(p.relative_to(root)):p.read_bytes() for p in root.rglob('*') if p.is_file()}
            with self.assertRaisesRegex(tk.ToolkitError, 'unmanaged or edited'):
                tk.export('opencode', root, preset='engineering')
            self.assertEqual(before, {str(p.relative_to(root)):p.read_bytes() for p in root.rglob('*') if p.is_file()})
            # Restore the exact owned version; narrowing can now remove it.
            game.unlink()
            tk.export('opencode', root)
            narrowed = tk.export('opencode', root, preset='engineering')
            self.assertGreater(narrowed['removed'], 0)
            self.assertFalse(game.exists())
            self.assertFalse((root/'commands/brain.md').exists())

    def test_phase_options_require_the_selected_phase_agent(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)/'output'
            with self.assertRaisesRegex(tk.ToolkitError, 'plan options require'):
                tk.export('opencode', root, preset='knowledge', opencode_options=tk.OpenCodeOptions(plannotator=True))
            self.assertFalse(root.exists())
            plans = Path(folder)/'private-plans'
            plans.mkdir()
            with self.assertRaisesRegex(tk.ToolkitError, 'plan options require'):
                tk.export('opencode', root, preset='knowledge',
                          opencode_options=tk.OpenCodeOptions(plan_directory=plans))
            self.assertFalse(root.exists())

    def test_retired_names_keep_public_pages_without_native_duplicates(self):
        aliases = json.loads((tk.ROOT/'toolkit/catalog-aliases.json').read_text())
        site.prepare({})
        active = {(e.kind+'s', e.name) for e in tk.catalog()}
        pages, _, _ = site.generate()
        for kind, names in aliases.items():
            for old, new in names.items():
                self.assertNotIn((kind, old), active)
                self.assertIn((kind, new), active)
                text = pages[f'{kind}/{old}.md']
                self.assertIn(f'[{new}]({new}.md)', text)
                self.assertIn('no longer a native profile', text)
