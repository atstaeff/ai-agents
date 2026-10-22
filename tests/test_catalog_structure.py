"""Protect contributor discovery and generated public navigation."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import ai_toolkit as tk
import docs_hook as hook


class CatalogStructureTests(unittest.TestCase):
    def test_new_domain_packages_ignore_bundled_markdown_and_reject_duplicates(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def profile(path, name):
                target = root/path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(f'---\nname: {name}\ndescription: A synthetic fixture\n---\n\nInstructions.\n')
            profile('agents/architecture/reviewer.agent.md', 'reviewer')
            profile('skills/architecture/review/SKILL.md', 'review')
            extra = root/'skills/architecture/review/assets/example.md'
            extra.parent.mkdir()
            extra.write_text('Bundled prose without catalog metadata.')
            self.assertEqual([(e.name, e.domain) for e in tk.catalog(root)],
                             [('reviewer', 'architecture'), ('review', 'architecture')])
            profile('skills/quality/review/SKILL.md', 'review')
            with self.assertRaisesRegex(tk.ToolkitError, 'duplicate'):
                tk.catalog(root)
            (root/'skills/quality/review/SKILL.md').unlink()
            profile('agents/unknown/other.agent.md', 'other')
            with self.assertRaisesRegex(tk.ToolkitError, 'Unknown catalog domain'):
                tk.catalog(root)

    def test_cli_domain_filter_and_generated_indexes(self):
        result = subprocess.run([sys.executable, str(tk.ROOT/'tools/ai_toolkit.py'),
                                 'catalog', '--domain', 'architecture'], capture_output=True, text=True, check=True)
        actual = json.loads(result.stdout)
        self.assertTrue(actual)
        self.assertEqual({e['name'] for e in actual}, {e.name for e in tk.catalog() if e.domain == 'architecture'})
        for kind in ('agent', 'skill'):
            self.assertEqual((tk.ROOT/f'{kind}s/README.md').read_text().strip(), tk.catalog_markdown(tk.catalog(), kind).strip())

    def test_every_profile_and_template_is_generated_and_included(self):
        try:
            from mkdocs.config import load_config
            from mkdocs.structure.files import Files, InclusionLevel
        except ImportError:
            self.skipTest('Optional documentation dependencies are not installed')
        config = load_config(str(tk.ROOT/'website/mkdocs.yml'))
        hook.on_pre_build(config)
        config.plugins._current_plugin = 'hooks'  # Normally set by MkDocs' event dispatcher.
        files = hook.on_files(Files([]), config)
        for entry in tk.catalog():
            generated = files.get_file_from_path(f'{entry.kind}s/{entry.name}.md')
            self.assertIsNotNone(generated, entry.path)
            self.assertEqual(generated.inclusion, InclusionLevel.INCLUDED)
        for template in ('templates/architecture/decision.md', 'templates/delivery/work-item.md',
                         'templates/project/project-brief.md', 'templates/quality/verification.md'):
            self.assertEqual(files.get_file_from_path(template).inclusion, InclusionLevel.INCLUDED)
        nav = json.dumps(config['nav'])
        for entry in tk.catalog():
            self.assertIn(f'{entry.kind}s/{entry.name}.md', nav)
