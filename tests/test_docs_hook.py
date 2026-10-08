from dataclasses import replace
from pathlib import Path
import sys
from types import SimpleNamespace
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
import docs_hook as hook


def page(path):
    return SimpleNamespace(file=SimpleNamespace(src_uri=path), meta={})


class DocsHookTests(unittest.TestCase):
    def test_one_catalog_scan_serves_the_entire_build(self):
        with patch.object(hook, 'catalog', wraps=hook.catalog) as catalog:
            hook.on_pre_build({})
            for path in (hook.ROOT / 'assets/mkdocs').rglob('*.md'):
                current = page(path.relative_to(hook.ROOT / 'assets/mkdocs').as_posix())
                rendered = hook.on_page_markdown(path.read_text(), current, {}, [])
                self.assertTrue(rendered.strip(), path)
            catalog.assert_called_once()

    def test_a_new_build_refreshes_catalog_metadata(self):
        entries = hook.catalog()
        joerg = next(entry for entry in entries if entry.name == 'joerg')
        changed = [replace(entry, description='Updated routing guidance')
                   if entry == joerg else entry for entry in entries]
        with patch.object(hook, 'catalog', side_effect=[entries, changed]):
            hook.on_pre_build({})
            first = hook.on_page_markdown('', page('agents/index.md'), {}, [])
            hook.on_pre_build({})
            second = hook.on_page_markdown('', page('agents/index.md'), {}, [])
        self.assertIn(joerg.description, first)
        self.assertIn('Updated routing guidance', second)
        self.assertNotIn(joerg.description, second)

    def test_canonical_links_metadata_and_edit_targets_are_preserved(self):
        hook.on_pre_build({})
        current = page('agents/joerg.md')
        rendered = hook.on_page_markdown('Placeholder', current, {}, [])
        self.assertIn('(../skills/agent-routing.md)', rendered)
        self.assertIn('(../getting-started/workflow.md)', rendered)
        self.assertIn('personal assistant', current.meta['description'])
        self.assertEqual(current.edit_url, 'https://github.com/atstaeff/ai-agents/edit/main/agents/joerg.agent.md')
        workflow = hook.on_page_markdown('', page('getting-started/workflow.md'), {}, [])
        self.assertIn('https://github.com/atstaeff/ai-agents/blob/main/templates/work-item.md', workflow)
        alias = hook.on_page_markdown('', page('skills/feature-discovery.md'), {}, [])
        self.assertIn('Canonical source: [`skills/team-collaboration/feature-discovery-session.md`]', alias)

    def test_customer_template_uses_its_canonical_readme_and_links(self):
        hook.on_pre_build({})
        current = page('references/customer-workspace.md')
        rendered = hook.on_page_markdown('Placeholder', current, {}, [])
        self.assertIn('# Customer workspace template', rendered)
        self.assertNotIn('Placeholder', rendered)
        self.assertIn('[AGENTS.md](https://github.com/atstaeff/ai-agents/blob/main/templates/customer-workspace/AGENTS.md)', rendered)
        self.assertIn('[workspace/README.md](https://github.com/atstaeff/ai-agents/blob/main/templates/customer-workspace/workspace/README.md)', rendered)
        self.assertIn('https://github.com/atstaeff/ai-agents/blob/main/templates/customer-workspace/workspace/README.md', rendered)
        self.assertIn('https://github.com/atstaeff/ai-agents/blob/main/templates/customer-workspace/examples/docusaurus-integration.md', rendered)
        self.assertEqual(current.edit_url, 'https://github.com/atstaeff/ai-agents/edit/main/templates/customer-workspace/README.md')


if __name__ == '__main__':
    unittest.main()
