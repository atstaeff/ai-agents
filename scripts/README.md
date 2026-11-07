# Keep Herdr and OpenCode running locally

Use this on Linux or WSL with systemd and a running user manager. Install Herdr and
OpenCode first, configure the providers in OpenCode, and choose a project containing
`AGENTS.md`. In this checkout OpenCode already selects the Delivery lead. For another
project, adopt its instructions and [configure its catalog](../toolkit/RUNTIMES.md).
No repository YAML, workbench, hosted service or Docusaurus build is needed.

## Set up once

From this repository, run:

```sh
python3 scripts/local_agents.py doctor --project /path/to/project
python3 scripts/local_agents.py install --project /path/to/project
python3 scripts/local_agents.py status --project /path/to/project
```

Omit `--project` when the current directory is the project root. The installer writes
three user units and enables the project target for future user-manager starts.
Herdr runs a dedicated named headless session. OpenCode serves on
`127.0.0.1:44096` with mDNS disabled. Use `install --port 44097` for a second project
or a port conflict. The client uses the installed port. Existing units with different
settings are left intact; uninstall and reinstall to change the port or executable path.

Each service restarts independently after exit, with a delay and systemd's restart
limit. Check `logs` if repeated startup failures reach that limit. Fix the cause,
wait for the rate limit to clear and run `start` again. A running service is not proof
of model access; check the first real authorized task against your installed releases.

For service availability before login and after logout on Linux, enable user lingering
once with `loginctl enable-linger "$USER"` if supported by your machine. On WSL, systemd
must be enabled and the distribution must be running. This setup does not start Windows,
wake a suspended host or keep a stopped WSL distribution alive.

## Use the running services

Use the same script and project argument with these commands:

| Command | Result |
| --- | --- |
| `herdr` | Attach to the project's named Herdr session |
| `client` | Connect the OpenCode terminal to the local server; run it inside a Herdr pane to use that surface |
| `status` / `logs` | Inspect both service processes or their recent journal output |
| `stop` / `start` | Stop or start this project's services; the login startup setting stays enabled |
| `uninstall` | Disable startup, stop the services and remove their managed unit files |

Keep binaries and the project checkout at stable paths. Uninstall before moving them.
Services run as your user and use your existing host configuration; the CLI copies no
credentials into units. If your provider needs environment variables that only exist in
an interactive shell, configure them in the user service environment before starting.
Keep the endpoint local and use OpenCode's own authentication if other users share
the machine. Stopping the Herdr service stops its panes; keep durable work and decisions
at their project sources before stopping.

The services keep the tools ready; they do not poll a tracker or send prompts on their
own. Start from an authorized issue or assignment. The project
[process index](../engineering/process/README.md) and
[session rules](../toolkit/SESSION-RULES.md) route the work from there.

See the upstream [Herdr CLI reference](https://herdr.dev/docs/cli-reference/) and
[OpenCode server guide](https://opencode.ai/docs/server/) for release-specific behavior.
