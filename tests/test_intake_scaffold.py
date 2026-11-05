import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
from intake_scaffold import scaffold
from intake_workflow import validate_profile


class ScaffoldTests(unittest.TestCase):
    def test_profiles_install_without_overwriting_project(self):
        for size in (3, 10, 20):
            with self.subTest(size=size), tempfile.TemporaryDirectory() as temp:
                target = Path(temp)
                (target / "AGENTS.md").write_text("Keep existing instructions\n")
                paths = scaffold(target, size)
                config = json.loads((target / ".product-intake/config.json").read_text())
                validate_profile(config)
                self.assertEqual(config["team"]["size"], size)
                self.assertEqual((target / "AGENTS.md").read_text(),
                                 "Keep existing instructions\n")
                self.assertEqual(len(paths), 5)
                for prompt in config["prompts"]:
                    self.assertTrue((target / ".product-intake" / prompt).is_file())

    def test_repeat_fails_without_overwrite(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp)
            scaffold(target, 3)
            with self.assertRaises(FileExistsError):
                scaffold(target, 10)
            config = json.loads((target / ".product-intake/config.json").read_text())
            self.assertEqual(config["team"]["size"], 3)

    def test_missing_target(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(FileNotFoundError):
                scaffold(Path(temp) / "missing", 3)


if __name__ == "__main__":
    unittest.main()
