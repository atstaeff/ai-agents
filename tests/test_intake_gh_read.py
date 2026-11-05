import copy
import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from intake_gh_read import list_candidates, parse_items
from intake_workflow import WorkflowError


class GitHubReadTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.profile = json.loads(
            (ROOT / "examples/intake/profiles/team-3.json").read_text(encoding="utf-8")
        )

    def test_filters_by_project_stage_and_repository(self):
        payload = {"items": [
            {"id": "PVT_1", "status": "Backlog",
             "content": {"type": "Issue", "repository": "example-org/small-service",
                         "number": 12, "title": "Story", "url": "https://github.com/example-org/small-service/issues/12"}},
            {"id": "PVT_2", "status": "Human Review",
             "content": {"type": "Issue", "repository": "example-org/small-service",
                         "number": 13}},
            {"id": "PVT_3", "status": "Backlog",
             "content": {"type": "Issue", "repository": "other/repo",
                         "number": 14}},
            {"id": "PVT_4", "status": "Backlog",
             "content": {"type": "PullRequest", "repository": "example-org/small-service",
                         "number": 15}},
        ]}
        calls = []
        def fake_runner(argv, **kwargs):
            calls.append((argv, kwargs))
            return SimpleNamespace(stdout=json.dumps(payload))
        result = list_candidates(self.profile, runner=fake_runner)
        self.assertEqual([i["issue_number"] for i in result["items"]], [12])
        self.assertFalse(result["remote_changes"])
        self.assertFalse(result["actual_ai_execution"])
        self.assertEqual(calls[0][0][:4], ["gh", "project", "item-list", "1"])

    def test_malformed_payload_fails(self):
        with self.assertRaises(WorkflowError):
            parse_items({"items": None}, "example/repo", {"Backlog"})

    def test_limit_has_bound(self):
        with self.assertRaises(WorkflowError):
            list_candidates(self.profile, limit=1000, runner=lambda *args, **kwargs: None)

    def test_gh_error_fails_closed(self):
        import subprocess
        def fails(*args, **kwargs):
            raise subprocess.CalledProcessError(1, args[0])
        with self.assertRaises(WorkflowError):
            list_candidates(self.profile, runner=fails)


if __name__ == "__main__":
    unittest.main()
