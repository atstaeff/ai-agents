"""Exercise user-service installation without altering the real user manager."""
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
import shutil
import socket
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import local_agents as cli


class LocalRuntimeTests(unittest.TestCase):
    def setUp(self):
        folder = self.enterContext(tempfile.TemporaryDirectory())
        self.project = Path(folder) / 'project % with spaces $'
        self.project.mkdir()
        (self.project / "AGENTS.md").write_text("# Project\n")
        self.directory = Path(folder) / "units"
        self.units = cli.units(self.project, 44096, "/usr/bin/true", "/usr/bin/true")

    def test_foreign_unit_prevents_partial_install(self):
        self.directory.mkdir()
        name = next(iter(self.units))
        path = self.directory / name
        path.write_text("[Service]\nExecStart=/usr/bin/true\n")
        with self.assertRaisesRegex(ValueError, "unmanaged"):
            cli.install(self.directory, self.units, 44096)
        self.assertEqual(list(self.directory.iterdir()), [path])
        self.assertTrue(path.read_text().startswith("[Service]"))

    def test_occupied_port_creates_no_units(self):
        with socket.socket() as other:
            other.bind(("127.0.0.1", 0))
            port = other.getsockname()[1]
            with self.assertRaisesRegex(ValueError, "unavailable"):
                cli.install(self.directory, self.units, port)
        self.assertFalse(self.directory.exists())

    def test_stopped_project_still_reserves_its_port(self):
        self.directory.mkdir()
        other = cli.units(self.project.parent / "other", 44096, "/usr/bin/true", "/usr/bin/true")
        target = next(name for name in other if name.endswith(".target"))
        (self.directory / target).write_text(other[target])
        with self.assertRaisesRegex(ValueError, "reserved"):
            cli.install(self.directory, self.units, 44096)
        self.assertEqual([p.name for p in self.directory.iterdir()], [target])

    def test_lifecycle_manages_only_project_units_and_preserves_source(self):
        name = cli.stack_name(self.project)
        def manager(argv, **kwargs):
            return str(self.directory / argv[-1]) if "--value" in argv else ""
        with patch.object(cli, "unit_directory", return_value=self.directory), \
             patch.object(cli, "doctor", return_value=("/usr/bin/true", "/usr/bin/true")), \
             patch.object(cli, "run", side_effect=manager) as run, patch.object(cli, "check_port"), \
             redirect_stdout(StringIO()), redirect_stderr(StringIO()):
            def command(action):
                self.assertEqual(cli.main([action, "--project", str(self.project)]), 0)
            command("install")
            run.assert_any_call(["systemctl", "--user", "enable", "--now", name + ".target"])
            self.assertEqual({p.name for p in self.directory.iterdir()}, set(self.units))
            (self.directory / "other.service").write_text("other")
            command("stop")
            run.assert_called_with(["systemctl", "--user", "stop", name + ".target"])
            command("uninstall")
            run.assert_any_call(["systemctl", "--user", "disable", "--now", name + ".target"])
        self.assertEqual([p.name for p in self.directory.iterdir()], ["other.service"])
        self.assertEqual((self.project / "AGENTS.md").read_text(), "# Project\n")

    def test_shadow_unit_is_not_stopped_or_removed(self):
        self.directory.mkdir()
        for name, value in self.units.items():
            (self.directory / name).write_text(value)
        with patch.object(cli, "unit_directory", return_value=self.directory), \
             patch.object(cli, "run", return_value="/elsewhere/unit.service") as run, \
             redirect_stderr(StringIO()):
            self.assertEqual(cli.main(["uninstall", "--project", str(self.project)]), 1)
        self.assertIn("FragmentPath", run.call_args.args[0][3])
        self.assertEqual({p.name for p in self.directory.iterdir()}, set(self.units))

    @unittest.skipUnless(shutil.which("systemd-analyze"), "systemd verifier is unavailable")
    def test_generated_units_are_accepted_by_systemd_with_realistic_paths(self):
        self.directory.mkdir()
        paths = []
        binary = shutil.which("true")
        for name, value in cli.units(self.project, 44096, binary, binary).items():
            path = self.directory / name
            path.write_text(value)
            paths.append(path)
        result = subprocess.run(["systemd-analyze", "verify", *paths],
                                capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
