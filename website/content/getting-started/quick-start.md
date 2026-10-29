# Try one small task

First export a small catalog into a temporary directory. Then use an installed AI host
to turn a supplied note into a short runbook. No project adoption, server or API key is
needed for the export; the AI task uses your host's own model access.

## 1. Check the local catalog

Use Bash on Linux, macOS or WSL with Git and Python 3.11+. Run these commands in one
shell; keep it open for the next step.

```sh
set -eu
git clone https://github.com/atstaeff/ai-agents.git
cd ai-agents
python3 tools/ai_toolkit.py check
trial_dir="$(mktemp -d "${TMPDIR:-/tmp}/ai-agents-first-XXXXXX")"
python3 tools/ai_toolkit.py export --runtime portable --preset minimal \
  --skill technical-writing --output "$trial_dir"
python3 - "$trial_dir" <<'PY'
from pathlib import Path
import sys

root = Path(sys.argv[1])
for relative in (
    "agents/build.agent.md",
    ".agents/skills/technical-writing/SKILL.md",
    "catalog/toolkit/SESSION-RULES.md",
):
    assert (root / relative).is_file(), relative
print(f"Portable catalog ready: {root}")
print("No AI host was started.")
PY
cat > "$trial_dir/NOTES.md" <<'MD'
# Upload retry notes

Endpoint: POST /uploads.
An upload ID can be retried for 24 hours.
A retry with the same ID and body returns the original result.
A retry with the same ID and a different body returns HTTP 409.
No service, automated test, review or deployment is supplied by this exercise.
MD
```

Success is `Portable catalog ready:` followed by a path, with no catalog errors. This
checks local files and export structure. It does not test a host, model or live service.
If Python is too old, use a Python 3.11+ installation. If the catalog check fails, resolve
the reported source error before continuing; do not use `--force` to bypass it.

## 2. Open the disposable project in your host

Use [Herdr](herdr.md) when its executable and selected server are usable. Reuse the
matching project session and start its supported interactive CLI in the temporary
directory through Herdr's native agent commands. The host's desktop/web UI can also
serve as your control surface; qualify its actual Herdr integration before relying on it.
If Herdr is unavailable, state that gap and use your authorized host directly. Herdr
is distinct from the optional Herd fleet exporter.

The portable files can be read explicitly without claiming native discovery. Choose
the row for a host you already have; these commands do not install or configure it.

| Host | Open the exercise | Native installation and discovery |
| --- | --- | --- |
| OpenCode | In the same shell, run `cd "$trial_dir"`, then `opencode web`; open its displayed local URL | [OpenCode setup](installation.md#opencode-in-wsl) supplies the native export and both configuration variables |
| Claude Code | Run `cd "$trial_dir"`, then `claude` | [Claude Code setup](installation.md#claude-code) supplies native agents, skills and instruction imports |
| VS Code / Copilot | Run `code "$trial_dir"`; open Copilot Chat in Agent mode | [Copilot setup](installation.md#copilot) explains the project-native layout and tool limits |
| Herd fleet | Export and import a selected native bundle, then assign the exercise to a worker with access to this directory | [Herd imports](installation.md#herd-fleet-imports) explains the actual import path and worker requirements |
| Another host | Open the printed directory and ask the session to read the files named below | [Portable layout](portability.md) requires an explicit check of that host's discovery and tools |

Configure credentials, model, effort and permissions in the host. If it cannot read or
write the exercise directory, resolve that access gap before continuing. Adapter format
checks do not establish compatibility with your installed host version.

## 3. Run the first task

Paste this into the host session opened at the temporary directory:

```text
Read catalog/skills/knowledge/technical-writing/SKILL.md and NOTES.md.
Create RUNBOOK.md with three sections: Behavior, Operator check, Evidence limits.
Use only the supplied facts. Describe proposed manual checks for a retry with the
same ID and body, and a retry with the same ID and a different body.
Mark those checks as unrun. Do not make network calls, install tools, or edit
other files. Report the file created and the limits of the evidence.
```

Review `RUNBOOK.md`. A successful result preserves the endpoint, 24-hour window,
original-result behavior and HTTP 409 conflict, and labels the proposed checks as
unrun. It must not claim a service was tested or deployed. This is a small documentation
result; native skill discovery, reviewer restrictions and delegation remain separate
host capabilities to qualify.

Keep the temporary directory for inspection or remove it when finished.

## 4. Adopt only what your next assignment needs

Merge the [project starter](lean-project.md) or an [AGENTS.md variant](agents-templates.md)
into existing instructions. Identify the assignment, acceptance, real checks and required
sources before the work depends on them. Add context and knowledge as the work produces it;
no YAML manifest, empty knowledge tree or full agent team is required.

Before relying on a host for real delivery, record its observed discovery, model/effort,
permissions, handoff and limits with the [runtime check template](../templates/delivery/runtime-check.md).
Before parallel work, record capacity and bounded writer scopes there and follow
[orchestration](orchestration.md). Use strong/high reasoning for complex judgment,
economical proven routes for bounded work and native tools for mechanical coordination.

Keep shared scope and acceptance in the actual issue or ticket, implementation evidence
in the linked PR, and current knowledge at the project's chosen home. Personal plans
stay private or explicitly unsaved in-session. See the [working contract](workflow.md).
