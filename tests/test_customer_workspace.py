"""Validate optional graph generation without adding a toolkit runtime dependency."""

from importlib.util import find_spec
import json
from pathlib import Path
import runpy
from tempfile import TemporaryDirectory
from types import SimpleNamespace
import unittest
from unittest.mock import patch


TEMPLATE = Path(__file__).resolve().parents[1] / 'templates/customer-workspace'
HAS_YAML = find_spec('yaml') is not None
# Loading a source script this way does not create bytecode inside the copied template.
graph = SimpleNamespace(**runpy.run_path(str(TEMPLATE / 'examples/knowledge_graph.py'))) if HAS_YAML else None


@unittest.skipUnless(HAS_YAML, 'Optional graph parser: run with uv --group docs')
class KnowledgeGraphTests(unittest.TestCase):
    def setUp(self):
        self.temporary = TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve() / 'workspace'
        self.root.mkdir()

    def record(self, ident, filename=None, **changes):
        meta = {'knowledge_id': ident, 'title': f'Decision {ident}',
                'slug': f'decisions/{ident.lower()}', 'status': 'proposed',
                'owner': 'technical-owner', 'relations': {}}
        meta.update(changes)
        path = self.root / 'decisions' / (filename or f'{ident.lower()}.md')
        path.parent.mkdir(exist_ok=True)
        path.write_text('---\n' + graph.yaml.safe_dump(meta, sort_keys=False) + '---\n\n# Decision\n', encoding='utf-8')
        return path

    def test_example_matches_checked_in_index_and_json(self):
        root = (TEMPLATE / 'workspace').resolve()
        result = graph.load_graph(root)
        self.assertEqual(len(result['nodes']), 4)
        self.assertEqual(len(result['edges']), 6)
        self.assertEqual(result, json.loads((TEMPLATE / 'examples/knowledge-graph.json').read_text()))
        self.assertEqual(graph.render(result), (root / 'knowledge-map.md').read_text())

    def test_unknown_reference_is_rejected(self):
        self.record('ADR-0001', relations={'depends_on': ['ADR-MISSING']})
        with self.assertRaisesRegex(ValueError, 'Unknown or self reference'):
            graph.load_graph(self.root)

    def test_duplicate_knowledge_id_is_rejected(self):
        self.record('ADR-0001')
        self.record('ADR-0001', filename='second.md', slug='decisions/second')
        with self.assertRaisesRegex(ValueError, 'Duplicate knowledge_id'):
            graph.load_graph(self.root)

    def test_dependency_cycle_is_rejected(self):
        self.record('ADR-0001', relations={'depends_on': ['ADR-0002']})
        self.record('ADR-0002', relations={'depends_on': ['ADR-0001']})
        with self.assertRaisesRegex(ValueError, 'Cycle in depends_on'):
            graph.load_graph(self.root)

    def test_historical_replacement_chain_is_valid(self):
        self.record('ADR-0001', status='superseded')
        self.record('ADR-0002', status='superseded', relations={'supersedes': ['ADR-0001']})
        self.record('ADR-0003', status='accepted', relations={'supersedes': ['ADR-0002']})
        result = graph.load_graph(self.root)
        self.assertEqual([(edge['source'], edge['target']) for edge in result['edges']],
                         [('ADR-0002', 'ADR-0001'), ('ADR-0003', 'ADR-0002')])

    def test_proposal_cannot_supersede_an_agreed_decision(self):
        self.record('ADR-0001', status='superseded')
        self.record('ADR-0002', relations={'supersedes': ['ADR-0001']})
        with self.assertRaisesRegex(ValueError, 'supersedes requires an agreed replacement'):
            graph.load_graph(self.root)

    def test_manual_knowledge_map_is_preserved(self):
        path = self.root / 'knowledge-map.md'
        path.write_text('# Human notes\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Refusing to overwrite a manual page'):
            graph.write_changed(path, graph.render(graph.load_graph(self.root)), protect=True)
        self.assertEqual(path.read_text(), '# Human notes\n')

    def test_unchanged_generated_outputs_are_not_written_again(self):
        page = self.root / 'knowledge-map.md'
        output = self.root.parent / 'graph.json'
        result = graph.load_graph(self.root)
        text = graph.render(result)
        data = json.dumps(result, indent=2, ensure_ascii=False) + '\n'
        graph.write_changed(page, text, protect=True)
        graph.write_changed(output, data)
        original_times = (page.stat().st_mtime_ns, output.stat().st_mtime_ns)
        with patch.object(Path, 'write_text', side_effect=AssertionError('Unchanged output was rewritten')):
            graph.write_changed(page, text, protect=True)
            graph.write_changed(output, data)
        self.assertEqual(original_times, (page.stat().st_mtime_ns, output.stat().st_mtime_ns))

    def test_empty_workspace_has_a_readable_index_without_an_empty_diagram(self):
        result = graph.load_graph(self.root)
        self.assertEqual(result['nodes'], [])
        self.assertEqual(result['edges'], [])
        text = graph.render(result)
        self.assertIn('No records with knowledge_id', text)
        self.assertNotIn('```mermaid', text)

    def test_decision_directory_index_does_not_require_a_knowledge_id(self):
        directory = self.root / 'decisions'
        directory.mkdir()
        (directory / 'README.md').write_text('# Decisions\n', encoding='utf-8')
        self.assertEqual(graph.load_graph(self.root)['nodes'], [])

    def test_numbered_adr_requires_metadata(self):
        directory = self.root / 'decisions'
        directory.mkdir()
        (directory / '0001-choice.md').write_text('# Choice\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'ADR needs metadata'):
            graph.load_graph(self.root)

    def test_unknown_relation_type_is_rejected(self):
        self.record('ADR-0001', relations={'invented_relation': []})
        with self.assertRaisesRegex(ValueError, 'Unknown relation type'):
            graph.load_graph(self.root)

    def test_duplicate_route_slug_is_rejected(self):
        self.record('ADR-0001')
        self.record('ADR-0002', slug='decisions/adr-0001')
        with self.assertRaisesRegex(ValueError, 'Invalid or duplicate slug'):
            graph.load_graph(self.root)

    def test_source_symlink_cannot_import_records_from_outside_workspace(self):
        outside = self.root.parent / 'outside.md'
        outside.write_text('# Outside\n', encoding='utf-8')
        (self.root / 'link.md').symlink_to(outside)
        with self.assertRaisesRegex(ValueError, 'Knowledge source must be inside workspace'):
            graph.load_graph(self.root)


if __name__ == '__main__':
    unittest.main()
