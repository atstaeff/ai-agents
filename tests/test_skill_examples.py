"""Execute the documented examples at their observed failure boundaries."""
import heapq
import math
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def example(skill, heading, language='python'):
    text = (ROOT / f'skills/engineering/{skill}/references/{skill}.md').read_text()
    section = text.split(heading, 1)[1]
    return re.search(rf'^```{language}\n(.*?)^```', section, re.M | re.S)[1]


def python_example(skill, heading):
    namespace = {'__name__': __name__}
    exec(compile(example(skill, heading), f'{skill} example', 'exec'), namespace)
    return namespace


class SkillExampleTests(unittest.TestCase):
    def test_observer_subscription_during_delivery_takes_effect_next_event(self):
        code = python_example('design-patterns', '### Observer')
        received = []

        def first(value):
            received.append(('first', value))
            code['subscribe']('event', lambda item: received.append(('later', item)))

        code['subscribe']('event', first)
        code['post_event']('event', 1)
        self.assertEqual(received, [('first', 1)])
        code['post_event']('event', 2)
        self.assertEqual(received, [('first', 1), ('first', 2), ('later', 2)])

    def test_astar_preserves_shortest_paths_and_rejects_invalid_endpoints(self):
        astar = python_example('game-mechanics', '## A* Pathfinding')['astar']
        grid = [[0] * 5 for _ in range(5)]
        route = astar(grid, (0, 0), (4, 4), allow_diagonal=False)
        self.assertEqual((route[0], route[-1], len(route)), ((0, 0), (4, 4), 9))
        self.assertTrue(all(abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1 for a, b in zip(route, route[1:])))
        diagonal = astar(grid, (0, 0), (4, 4))
        cost = sum(math.dist(a, b) for a, b in zip(diagonal, diagonal[1:]))
        self.assertAlmostEqual(cost, 4 * math.sqrt(2))
        for invalid_grid, start, goal in [([], (0, 0), (0, 0)), ([[1]], (0, 0), (0, 0)),
                                          (grid, (-1, 0), (0, 0)), (grid, (0, 0), (5, 0))]:
            self.assertEqual(astar(invalid_grid, start, goal), [])
        with self.assertRaisesRegex(ValueError, 'rectangular'):
            astar([[0, 0], [0]], (0, 0), (1, 0))

    def test_astar_unreachable_goal_does_not_expand_duplicate_paths(self):
        astar = python_example('game-mechanics', '## A* Pathfinding')['astar']
        grid = [[0] * 10 for _ in range(10)]
        for row in grid:
            row[8] = 1
        with patch.object(heapq, 'heappop', wraps=heapq.heappop) as pop:
            self.assertEqual(astar(grid, (0, 0), (9, 9), allow_diagonal=False), [])
        # Only 80 cells are reachable; allow bounded queue improvements, not path enumeration.
        self.assertLessEqual(pop.call_count, 160)

    def test_save_failure_preserves_previous_slot_and_cleans_temporary_file(self):
        code = python_example('game-architecture', '## Save / Load System')
        with tempfile.TemporaryDirectory() as directory:
            code['SaveSystem'].SAVE_DIR = Path(directory)
            store = code['SaveSystem']()
            original = code['SaveData'](score=10)
            store.save(1, original)
            before = (Path(directory) / 'save_1.json').read_bytes()
            replacement = code['SaveData'](score=20)
            for operation in ['fsync', 'replace']:
                with self.subTest(operation=operation), patch.object(code['os'], operation, side_effect=OSError('disk failure')):
                    with self.assertRaisesRegex(OSError, 'disk failure'):
                        store.save(1, replacement)
                self.assertEqual((Path(directory) / 'save_1.json').read_bytes(), before)
                self.assertEqual(replacement.timestamp, '')
                self.assertEqual(list(Path(directory).glob('.save-*')), [])
            self.assertEqual(store.load(1).score, 10)
            store.save(1, replacement)
            self.assertEqual(store.load(1).score, 20)
            self.assertTrue(replacement.timestamp)

    @unittest.skipUnless(shutil.which('node'), 'Node is required to execute the TypeScript example')
    def test_wfc_returns_valid_tiles_or_reports_a_contradiction(self):
        source = example('game-mechanics', '### Wave Function Collapse', 'typescript')
        assertions = """
const assert = require('node:assert/strict');
const rule = {tile: 'floor', allowedNeighbors: {up: ['floor'], down: ['floor'], left: ['floor'], right: ['floor']}, weight: 1};
assert.deepEqual(new WaveFunctionCollapse(2, 2, [rule]).generate(), [['floor', 'floor'], ['floor', 'floor']]);
const impossible = {...rule, allowedNeighbors: {up: [], down: [], left: [], right: []}};
assert.throws(() => new WaveFunctionCollapse(2, 1, [impossible]).generate(), /contradiction/);
assert.throws(() => new WaveFunctionCollapse(1, 1, []).generate(), /positive/);
assert.throws(() => new WaveFunctionCollapse(1, 1, [{...rule, weight: 0}]).generate(), /positive/);
"""
        runner = "const code = require('node:fs').readFileSync(0, 'utf8'); new Function('require', require('node:module').stripTypeScriptTypes(code, {mode: 'transform'}))(require);"
        result = subprocess.run(['node', '-e', runner], input=source + assertions,
                                text=True, capture_output=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == '__main__':
    unittest.main()
