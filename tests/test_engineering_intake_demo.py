import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from engineering_intake_demo import COLUMNS, MODEL_ROUTES, assess, simulate


class IntakePilotTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        data = json.loads((ROOT / "examples/intake/fixture.json").read_text())
        cls.data = data

    def test_board_handoff(self):
        result = simulate(self.data)
        self.assertEqual([event["column"] for event in result["board"]],
                         ["Backlog", "AI Takes Over", "AI Working", "Human Review"])
        self.assertFalse(result["report"]["remote_changes"])

    def test_missing_data_requires_clarification(self):
        issue = {**self.data["issue"], "acceptance_criteria": []}
        self.assertEqual(assess(issue, self.data["decisions"])["proposed_column"],
                         "Needs Clarification")

    def test_unknown_adr_requires_clarification(self):
        issue = {**self.data["issue"], "referenced_adrs": ["ADR-404"]}
        self.assertEqual(assess(issue, self.data["decisions"])["proposed_column"],
                         "Needs Clarification")

    def test_proposed_adr_not_accepted(self):
        result = assess(self.data["issue"], self.data["decisions"])
        self.assertEqual(result["accepted_adr_evidence"], ["ADR-100"])
        self.assertEqual(result["informative_adrs"], ["ADR-101"])

    def test_model_routing(self):
        self.assertEqual(MODEL_ROUTES["default"]["model"], "opencode/gpt-6.1-sol")
        self.assertEqual(MODEL_ROUTES["architecture"]["model"], "opencode/gpt-6-astra")

    def test_human_gate(self):
        self.assertIn("Ready for Engineering", COLUMNS)
        self.assertNotEqual(assess(self.data["issue"], self.data["decisions"])["proposed_column"],
                            "Ready for Engineering")


if __name__ == "__main__":
    unittest.main()
