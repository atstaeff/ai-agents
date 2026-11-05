import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from intake_config import ConfigError, validate


class TeamConfigurationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.config = json.loads((ROOT / "examples/intake/team-config.json").read_text(encoding="utf-8"))

    def test_sample_valid(self):
        self.assertEqual(validate(self.config)["schema_version"], "1")

    def test_no_engineering(self):
        c = copy.deepcopy(self.config)
        c["automation"]["allow_engineering"] = True
        with self.assertRaises(ConfigError):
            validate(c)

    def test_no_live_mode_without_adapter(self):
        c = copy.deepcopy(self.config)
        c["automation"]["mode"] = "live"
        with self.assertRaises(ConfigError):
            validate(c)

    def test_no_bypass_review(self):
        c = copy.deepcopy(self.config)
        c["automation"]["require_human_approval"] = False
        with self.assertRaises(ConfigError):
            validate(c)

    def test_unsupported_schema(self):
        c = copy.deepcopy(self.config)
        c["schema_version"] = "2"
        with self.assertRaises(ConfigError):
            validate(c)

    def test_duplicate_board_status(self):
        c = copy.deepcopy(self.config)
        c["workflow"]["review"] = c["workflow"]["working"]
        with self.assertRaises(ConfigError):
            validate(c)

    def test_cannot_drop_readiness_baseline(self):
        c = copy.deepcopy(self.config)
        c["checks"]["required"].remove("acceptance_criteria")
        with self.assertRaises(ConfigError):
            validate(c)

    def test_can_customize_reviewer_and_model(self):
        c = copy.deepcopy(self.config)
        c["reviewers"]["product"] = ["team-product"]
        c["models"]["specialist"]["id"] = "org-approved-economical-model"
        self.assertEqual(validate(c), c)

    def test_unknown_key_fails_closed(self):
        c = copy.deepcopy(self.config)
        c["automation"]["skip_approval"] = True
        with self.assertRaises(ConfigError):
            validate(c)

    def test_limits_bounded(self):
        c = copy.deepcopy(self.config)
        c["limits"]["max_concurrent_issues"] = 10000
        with self.assertRaises(ConfigError):
            validate(c)


if __name__ == "__main__":
    unittest.main()
