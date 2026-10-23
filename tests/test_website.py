from dataclasses import replace
from copy import deepcopy
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'website'))
import generate as site


def page(path):
    return site.Page(path)


class WebsitePublishingTests(unittest.TestCase):
    def test_one_catalog_scan_serves_the_entire_build(self):
        with patch.object(site, 'catalog', wraps=site.catalog) as catalog:
            site.prepare({})
            for path in (site.ROOT / 'website/content').rglob('*.md'):
                current = page(path.relative_to(site.ROOT / 'website/content').as_posix())
                rendered = site.render(path.read_text(), current, {})
                self.assertTrue(rendered.strip(), path)
            catalog.assert_called_once()

    def test_a_new_build_refreshes_catalog_metadata(self):
        entries = site.catalog()
        joerg = next(entry for entry in entries if entry.name == 'joerg')
        changed = [replace(entry, description='Updated routing guidance')
                   if entry == joerg else entry for entry in entries]
        with patch.object(site, 'catalog', side_effect=[entries, changed]):
            site.prepare({})
            first = site.render('', page('agents/index.md'), {})
            site.prepare({})
            second = site.render('', page('agents/index.md'), {})
        self.assertIn(joerg.description, first)
        self.assertIn('Updated routing guidance', second)
        self.assertNotIn(joerg.description, second)

    def test_canonical_links_metadata_and_edit_targets_are_preserved(self):
        site.prepare({})
        current = page('agents/joerg.md')
        rendered = site.render('Placeholder', current, {})
        self.assertIn('(../skills/agent-routing.md)', rendered)
        self.assertIn('(../getting-started/session-rules.md)', rendered)
        self.assertIn('personal assistant', current.meta['description'])
        self.assertEqual(current.edit_url, 'https://github.com/atstaeff/ai-agents/edit/main/agents/general/joerg.agent.md')
        workflow = site.render('', page('getting-started/workflow.md'), {})
        self.assertIn('[work template](../templates/delivery/personal-plan.md)', workflow)
        alias = site.render('', page('skills/feature-discovery.md'), {})
        self.assertIn('Canonical source: [`skills/delivery/product-discovery/SKILL.md`]', alias)

    def test_customer_template_uses_its_canonical_readme_and_links(self):
        site.prepare({})
        current = page('references/customer-workspace.md')
        rendered = site.render('Placeholder', current, {})
        self.assertIn('# Customer workspace template', rendered)
        self.assertNotIn('Placeholder', rendered)
        self.assertIn('[AGENTS.md](https://github.com/atstaeff/ai-agents/blob/main/templates/customer-workspace/AGENTS.md)', rendered)
        self.assertIn('[workspace/README.md](../customer-workspace/context.md)', rendered)
        self.assertIn('(../customer-workspace/docusaurus.md)', rendered)
        self.assertEqual(current.edit_url, 'https://github.com/atstaeff/ai-agents/edit/main/templates/customer-workspace/README.md')

    def test_operating_model_uses_canonical_content_and_local_links(self):
        site.prepare({})
        current = page('concept.md')
        rendered = site.render('Placeholder', current, {})
        self.assertIn('# Work with AI as a teammate', rendered)
        self.assertIn('[work record](toolkit/work-records.md)', rendered)
        self.assertIn('[the worked assignment](customer-workspace/assignment.md)', rendered)
        self.assertEqual(current.edit_url, 'https://github.com/atstaeff/ai-agents/edit/main/toolkit/OPERATING-MODEL.md')

    def test_root_project_entries_keep_routes_links_and_single_canonical_sources(self):
        site.prepare({})
        current = page('repository-workspace.md')
        rendered = site.render('', current, {})
        self.assertEqual(current.edit_url, 'https://github.com/atstaeff/ai-agents/edit/main/PROJECT.md')
        self.assertIn('(contributing/index.md#working-process-and-skills)', rendered)
        starter = page('lean-project/workspace.md')
        rendered = site.render('', starter, {})
        self.assertEqual(starter.edit_url, 'https://github.com/atstaeff/ai-agents/edit/main/templates/project-starter/PROJECT.md')
        self.assertIn('(contributing.md)', rendered)
        pages, _, _ = site.generate()
        self.assertIn('lean-project/contributing.md', pages)
        self.assertNotIn('templates/project-starter/PROJECT.md', pages)
        self.assertNotIn('templates/project-starter/CONTRIBUTING.md', pages)

    def test_agents_entry_and_knowledge_publish_from_single_sources(self):
        site.prepare({})
        entry = page('project/agents.md')
        text = site.render('', entry, {})
        self.assertIn('(../repository-workspace.md)', text)
        self.assertIn('(../knowledge/index.md)', text)
        self.assertEqual(entry.edit_url, 'https://github.com/atstaeff/ai-agents/edit/main/AGENTS.md')
        knowledge = page('knowledge/architecture.md')
        text = site.render('', knowledge, {})
        self.assertIn('(decisions/adr-0003.md)', text)
        pages, sidebars, _ = site.generate()
        self.assertIn('knowledge/decisions/adr-0003.md', pages)
        self.assertNotIn('templates/project-starter/PROJECT.md', pages)
        self.assertNotIn('templates/project-starter/CONTRIBUTING.md', pages)
        self.assertTrue(any(item.get('type') == 'link' for item in
                            site.sidebar_items([{'Work': 'https://github.com/atstaeff/ai-agents/issues'}])))
        self.assertFalse(any('workspace/work/' in path for path in pages))

    def test_decision_frontmatter_is_not_treated_as_a_catalog_profile(self):
        site.prepare({})
        current = page('customer-workspace/decisions/adr-0001.md')
        rendered = site.render('Placeholder', current, {})
        self.assertIn('# ADR-0001: Retry-safe document upload', rendered)
        self.assertNotIn('knowledge_id:', rendered)
        self.assertNotIn('relations: {}', rendered)
        self.assertIn('(../knowledge.md)', rendered)
        self.assertIn('(adr-0002.md)', rendered)

    def test_map_renders_linked_svg_and_preserves_the_accessible_table(self):
        site.prepare({})
        current = page('customer-workspace/knowledge-map.md')
        rendered = site.render('Placeholder', current, {})
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
        site.prepare({})
        rendered = site.render('', page('customer-workspace/knowledge-map.md'), {'use_directory_urls': False})
        self.assertIn('href="decisions/adr-0001.html"', rendered)
        self.assertIn('href="iteration.html"', rendered)

    def test_graph_metadata_is_escaped_in_html(self):
        site.prepare({})
        data = deepcopy(site.KNOWLEDGE_GRAPH)
        data['nodes'][0]['title'] = '<script>"injected"</script>'
        data['edges'][0]['type'] = '<unsafe>'
        rendered = site.knowledge_diagram(data, 'customer-workspace/knowledge-map.md')
        self.assertNotIn('<script>', rendered)
        self.assertNotIn('<unsafe>', rendered)
        self.assertIn('&lt;script&gt;&quot;injected&quot;&lt;/script&gt;', rendered)
        self.assertIn('&lt;unsafe&gt;', rendered)


if __name__ == '__main__':
    unittest.main()
