#!/usr/bin/env python3
"""Manage a project's local Herdr and OpenCode services through systemd --user."""
from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import shutil
import socket
import subprocess
import sys

MARKER = "# Managed by ai-agents local_agents.py\n"
DEFAULT_PORT = 44096


def literal(value: str) -> str:
    if any(ord(char) < 32 or ord(char) == 127 for char in value):
        raise ValueError("Control characters are not supported in service paths.")
    return value.replace("%", "%%")


def unit_value(value: str) -> str:
    return '"' + literal(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


def units(project: Path, port: int, herdr: str, opencode: str) -> dict[str, str]:
    name = stack_name(project)
    target = name + ".target"
    herdr_unit = name + "-herdr.service"
    code_unit = name + "-opencode.service"
    # The ':' prefix disables systemd's dollar substitution in command arguments.
    def service(label: str, argv: list[str], extra: str = "") -> str:
        command = " ".join(unit_value(arg) for arg in argv)
        return (MARKER + f"[Unit]\nDescription={label}\nPartOf={target}\n"
                "StartLimitIntervalSec=120\nStartLimitBurst=5\n\n[Service]\nType=exec\n"
                f"WorkingDirectory={literal(str(project))}/.\n"
                f"{extra}ExecStart=:{command}\nRestart=always\nRestartSec=10\n"
                "TimeoutStopSec=30\n")

    return {
        herdr_unit: service("AI Agents Herdr", [herdr, "--session", name, "server"],
                            "UnsetEnvironment=HERDR_SESSION HERDR_SOCKET_PATH\n"),
        code_unit: service("AI Agents OpenCode", [opencode, "serve", "--hostname",
                                                 "127.0.0.1", "--port", str(port),
                                                 "--mdns=false"]),
        target: (MARKER + f"# OpenCode port: {port}\n[Unit]\nDescription=AI Agents local runtime\n"
                 f"Wants={herdr_unit} {code_unit}\n\n[Install]\nWantedBy=default.target\n"),
    }


def stack_name(project: Path) -> str:
    return "ai-agents-" + hashlib.sha256(os.fsencode(project)).hexdigest()[:12]


def unit_directory() -> Path:
    return Path(os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config") / "systemd/user"


def run(argv: list[str], *, capture: bool = False) -> str:
    result = subprocess.run(argv, check=True, text=True, capture_output=capture, timeout=45)
    return result.stdout if capture else ""


def executable(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise ValueError(f"{name} is not on PATH. Install and configure it first.")
    # Keep the installed launcher's name: some wrappers dispatch on argv[0].
    return str(Path(path).absolute())


def doctor() -> tuple[str, str]:
    if sys.platform != "linux":
        raise ValueError("Persistent services require Linux or WSL with systemd.")
    herdr, opencode = executable("herdr"), executable("opencode")
    manager = run(["systemctl", "--user", "show", "--property=Version"], capture=True).strip()
    if not manager.startswith("Version=") or not manager.removeprefix("Version="):
        raise ValueError("A running systemd user manager is required.")
    if "--session" not in run([herdr, "--help"], capture=True):
        raise ValueError("This Herdr release does not advertise named sessions.")
    help_text = run([opencode, "serve", "--help"], capture=True)
    if any(flag not in help_text for flag in ("--hostname", "--port", "--mdns")):
        raise ValueError("This OpenCode release lacks the supported serve options.")
    for binary in (herdr, opencode):
        print(f"{binary}: {run([binary, '--version'], capture=True).strip()}")
    return herdr, opencode


def check_port(port: int) -> None:
    with socket.socket() as listener:
        try:
            listener.bind(("127.0.0.1", port))
        except OSError as error:
            raise ValueError(f"Loopback port {port} is unavailable. Pick an unused --port.") from error


def owned_text(path: Path) -> str | None:
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise ValueError(f"Refusing to use a non-regular unit file: {path}")
    if not path.exists():
        return None
    value = path.read_text()
    if not value.startswith(MARKER):
        raise ValueError(f"Refusing to change an unmanaged unit: {path}")
    return value


def installed_port(settings: str) -> int:
    prefix = "# OpenCode port: "
    ports = [line.removeprefix(prefix) for line in settings.splitlines()
             if line.startswith(prefix)]
    if len(ports) != 1 or not ports[0].isascii() or not ports[0].isdigit():
        raise ValueError("Missing installed OpenCode port; reinstall the services.")
    port = int(ports[0])
    if not 1024 <= port <= 65535:
        raise ValueError("Invalid installed OpenCode port; reinstall the services.")
    return port


def install(directory: Path, expected: dict[str, str], port: int) -> None:
    existing = {name: owned_text(directory / name) for name in expected}
    for name, value in expected.items():
        if existing[name] not in (None, value):
            raise ValueError(f"{name} has different settings. Uninstall before changing them.")
    for other in directory.glob("ai-agents-*.target"):
        if other.name in expected or other.is_symlink() or not other.is_file():
            continue
        settings = other.read_text()
        if settings.startswith(MARKER) and installed_port(settings) == port:
            raise ValueError(f"Loopback port {port} is reserved by {other.name}. Pick another --port.")
    target = next(name for name in expected if name.endswith(".target"))
    if existing[target] is None:
        check_port(port)
    directory.mkdir(parents=True, exist_ok=True)
    for name, value in expected.items():
        if existing[name] is None:
            with (directory / name).open("x") as stream:
                stream.write(value)


def require_loaded_units(directory: Path, names: list[str]) -> None:
    for name in names:
        fragment = run(["systemctl", "--user", "show", "--property=FragmentPath",
                        "--value", name], capture=True).strip()
        if not fragment or Path(fragment).resolve() != (directory / name).resolve():
            raise ValueError(f"The user manager is not loading the managed {name}. "
                             "Check its configuration directory and unit overrides.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("doctor", "install", "start", "status", "logs",
                                           "stop", "uninstall", "herdr", "client"))
    parser.add_argument("--project", type=Path, default=Path.cwd())
    parser.add_argument("--port", type=int, default=DEFAULT_PORT,
                        help="OpenCode port for install (default: %(default)s)")
    args = parser.parse_args(argv)
    project = args.project.resolve()
    name = stack_name(project)
    target = name + ".target"
    services = [name + "-herdr.service", name + "-opencode.service"]
    ctl = ["systemctl", "--user"]
    directory = unit_directory()
    try:
        if not 1024 <= args.port <= 65535:
            raise ValueError("--port must be between 1024 and 65535.")
        if args.action in ("doctor", "install") and not (project / "AGENTS.md").is_file():
            raise ValueError(f"Choose a project root with AGENTS.md: {project}")
        if args.action == "doctor":
            doctor()
        elif args.action == "install":
            herdr, opencode = doctor()
            expected = units(project, args.port, herdr, opencode)
            install(directory, expected, args.port)
            run(ctl + ["daemon-reload"])
            require_loaded_units(directory, list(expected))
            run(ctl + ["enable", "--now", target])
            print(f"Enabled {target}. OpenCode: http://127.0.0.1:{args.port}")
            print("Use status and logs to inspect both processes.")
        elif args.action in ("herdr", "client"):
            settings = owned_text(directory / target)
            if not settings:
                raise ValueError("Install the project services first.")
            os.chdir(project)
            service = services[0 if args.action == "herdr" else 1]
            if not owned_text(directory / service):
                raise ValueError("Run install to complete the project units.")
            require_loaded_units(directory, [target, service])
            if args.action == "herdr":
                run(ctl + ["is-active", "--quiet", services[0]])
                env = os.environ.copy()
                env.pop("HERDR_SOCKET_PATH", None)
                env.pop("HERDR_SESSION", None)
                binary = executable("herdr")
                subprocess.run([binary, "--session", name, "workspace", "list"],
                               env=env, check=True, stdout=subprocess.DEVNULL, timeout=10)
                os.execve(binary, [binary, "--session", name], env)
            else:
                binary = executable("opencode")
                run(ctl + ["is-active", "--quiet", services[1]])
                port = installed_port(settings)
                os.execv(binary, [binary, "attach", f"http://127.0.0.1:{port}"])
        else:
            installed = [unit for unit in [*services, target] if owned_text(directory / unit)]
            if not installed:
                raise ValueError("No managed units found for this project.")
            require_loaded_units(directory, installed)
            if args.action == "uninstall":
                if target in installed:
                    run(ctl + ["disable", "--now", target])
                remaining = [unit for unit in services if unit in installed]
                if remaining:
                    run(ctl + ["stop", *remaining])
                for unit in installed:
                    (directory / unit).unlink()
                run(ctl + ["daemon-reload"])
            elif args.action == "logs":
                run(["journalctl", "--user", "--no-pager", "-n", "80",
                     "-u", services[0], "-u", services[1]])
            elif args.action == "status":
                return subprocess.call(ctl + ["status", "--no-pager", *services])
            else:
                if target not in installed or (args.action == "start" and len(installed) != 3):
                    raise ValueError("Run install to complete the project units.")
                run(ctl + [args.action, target])
        return 0
    except subprocess.CalledProcessError as error:
        detail = error.stderr.strip() if error.stderr else f"exit {error.returncode}"
        print(f"local-agents: {Path(error.cmd[0]).name}: {detail}", file=sys.stderr)
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        print(f"local-agents: {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
