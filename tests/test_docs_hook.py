from dataclasses import replace
from copy import deepcopy
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
        self.assertIn('[workspace/README.md](../customer-workspace/context.md)', rendered)
        self.assertIn('(../customer-workspace/docusaurus.md)', rendered)
        self.assertEqual(current.edit_url, 'https://github.com/atstaeff/ai-agents/edit/main/templates/customer-workspace/README.md')

    def test_operating_model_uses_canonical_content_and_local_links(self):
        hook.on_pre_build({})
        current = page('concept.md')
        rendered = hook.on_page_markdown('Placeholder', current, {}, [])
        self.assertIn('# Work with AI as a teammate', rendered)
        self.assertIn('[work record](toolkit/work-records.md)', rendered)
        self.assertIn('[the worked assignment](customer-workspace/assignment.md)', rendered)
        self.assertEqual(current.edit_url, 'https://github.com/atstaeff/ai-agents/edit/main/toolkit/OPERATING-MODEL.md')

    def test_decision_frontmatter_is_not_treated_as_a_catalog_profile(self):
        hook.on_pre_build({})
        current = page('customer-workspace/decisions/adr-0001.md')
        rendered = hook.on_page_markdown('Placeholder', current, {}, [])
        self.assertIn('# ADR-0001: Retry-safe document upload', rendered)
        self.assertNotIn('knowledge_id:', rendered)
        self.assertNotIn('relations: {}', rendered)
        self.assertIn('(../knowledge.md)', rendered)
        self.assertIn('(adr-0002.md)', rendered)

    def test_map_renders_linked_svg_and_preserves_the_accessible_table(self):
        hook.on_pre_build({})
        current = page('customer-workspace/knowledge-map.md')
        rendered = hook.on_page_markdown('Placeholder', current, {}, [])
        self.assertIn('<svg ', rendered)
        self.assertEqual(rendered.count('<line class="knowledge-edge"'), 6)
        self.assertEqual(rendered.count('tabindex="0"'), 4)
        self.assertIn('href="../decisions/adr-0001/"', rendered)
        self.assertIn('href="../iteration/"', rendered)
        self.assertIn('| Record | Relation | Target |', rendered)
        self.assertIn('[ADR-0001](decisions/adr-0001.md)', rendered)
        self.assertNotIn('```mermaid', rendered)
        self.assertNotIn('<script', rendered)

    def test_map_links_work_in_a_portable_flat_html_build(self):
        hook.on_pre_build({})
        rendered = hook.on_page_markdown('', page('customer-workspace/knowledge-map.md'), {'use_directory_urls': False}, [])
        self.assertIn('href="decisions/adr-0001.html"', rendered)
        self.assertIn('href="iteration.html"', rendered)

    def test_graph_metadata_is_escaped_in_html(self):
        hook.on_pre_build({})
        data = deepcopy(hook.KNOWLEDGE_GRAPH)
        data['nodes'][0]['title'] = '<script>"injected"</script>'
        data['edges'][0]['type'] = '<unsafe>'
        rendered = hook.knowledge_diagram(data, 'customer-workspace/knowledge-map.md')
        self.assertNotIn('<script>', rendered)
        self.assertNotIn('<unsafe>', rendered)
        self.assertIn('&lt;script&gt;&quot;injected&quot;&lt;/script&gt;', rendered)
        self.assertIn('&lt;unsafe&gt;', rendered)


if __name__ == '__main__':
    unittest.main()
