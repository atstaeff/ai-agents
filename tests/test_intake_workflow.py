import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from intake_workflow import WorkflowError, plan_transition, validate_profile


class ConfigurableWorkflowTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profiles = [
            json.loads((ROOT / f"examples/intake/profiles/team-{n}.json").read_text(encoding="utf-8"))
            for n in (3, 10, 20)
        ]

    def test_each_team_has_different_workflow(self):
        sizes = [len(validate_profile(p)["process"]["stages"]) for p in self.profiles]
        self.assertEqual(sizes, [5, 6, 7])

    def test_all_are_offline(self):
        for p in self.profiles:
            with self.subTest(team=p["team"]["id"]):
                out = plan_transition(p, "review", "ready", approved=True)
                self.assertFalse(out["remote_changes"])
                self.assertTrue(out["requires_verified_human_approval"])
                self.assertEqual(out["status"], "blocked_pending_external_approval_verifier")

    def test_no_direct_handoff(self):
        p = copy.deepcopy(self.profiles[0])
        p["process"]["transitions"].append(
            {"from": "working", "to": "ready", "actor": "controller", "gate": "none"}
        )
        with self.assertRaises(WorkflowError):
            validate_profile(p)

    def test_no_unsafe_live_or_engineering(self):
        for field, value in (("mode", "live"), ("allow_implementation", True),
                             ("require_human_approval", False)):
            p = copy.deepcopy(self.profiles[0])
            p["automation"][field] = value
            with self.subTest(field=field), self.assertRaises(WorkflowError):
                validate_profile(p)

    def test_review_can_return_for_rework(self):
        result = plan_transition(self.profiles[0], "review", "claimed", actor="human")
        self.assertEqual(result["status"], "proposed")

    def test_ai_cannot_act_as_human(self):
        with self.assertRaises(WorkflowError):
            plan_transition(self.profiles[0], "review", "claimed", actor="controller")

    def test_unknown_skill_rejected(self):
        p = copy.deepcopy(self.profiles[0])
        p["roles"]["product"]["skills"] = ["unapproved-skill"]
        with self.assertRaises(WorkflowError):
            validate_profile(p)

    def test_unapproved_prompt_path_rejected(self):
        p = copy.deepcopy(self.profiles[0])
        p["prompts"] = ["../secrets"]
        p["roles"]["product"]["prompt"] = "../secrets"
        with self.assertRaises(WorkflowError):
            validate_profile(p)

    def test_model_override_per_team(self):
        p = copy.deepcopy(self.profiles[1])
        p["models"]["specialist"]["model"] = "approved-team-specific-model"
        self.assertEqual(validate_profile(p)["models"]["specialist"]["model"],
                         "approved-team-specific-model")

    def test_no_terminal_handoff_outgoing(self):
        p = copy.deepcopy(self.profiles[0])
        p["process"]["transitions"].append(
            {"from": "ready", "to": "backlog", "actor": "human", "gate": "none"}
        )
        with self.assertRaises(WorkflowError):
            validate_profile(p)

    def test_unknown_field_rejected(self):
        p = copy.deepcopy(self.profiles[0])
        p["automation"]["bypass_review"] = True
        with self.assertRaises(WorkflowError):
            validate_profile(p)


if __name__ == "__main__":
    unittest.main()
