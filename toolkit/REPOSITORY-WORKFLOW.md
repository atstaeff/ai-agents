# Run this repository

Read [AGENTS.md](../AGENTS.md) first. It links actual context, decisions and commands.
The repository keeps existing `workspace/` paths for compatibility, without making that
layout a requirement for projects adopting the catalog.

## Set up and verify

```sh
uv sync --locked --group validation
python3 tools/ai_toolkit.py check
uv run --locked --group validation python -m unittest discover -s tests -v
python3 tools/workspace_smoke.py
npm --prefix website ci
npm --prefix website run build
```

The smoke command exercises the optional local record store, stale writes, export and
migration in generated fixtures. It does not prove live tracker access or installed-host
behavior. `workspace/generated/` and exports are ignored and excluded from publication.

## Export and start OpenCode 1

```sh
python3 tools/ai_toolkit.py export --runtime opencode \
  --output "$HOME/.config/ai-agents/opencode"
cd /path/to/project
OPENCODE_CONFIG_DIR="$HOME/.config/ai-agents/opencode" \
OPENCODE_CONFIG="$HOME/.config/ai-agents/opencode/opencode.json" opencode web
```

Re-export after canonical source changes. The manifest protects human edits. Configure
models/providers locally. For private plans, follow [personal planning](../templates/agent-instructions/personal-planning.md);
for an optional review gate, follow [plan review](PLAN-REVIEW.md).
Perform the [installed-host check](PORTABILITY.md#verify-a-new-host-once).

## Deliver

Use the current request or assigned issue for scope. Keep personal working steps in the
configured Second Brain; if unavailable, report unsaved planning and continue in-session.
Prepare a focused branch and PR with actual checks. Update affected knowledge and relevant
ADRs after implementation. Do not require the team to access personal plans. Merge and
deployment remain separately authorized.

## Docusaurus demo

Follow the [demo README](../examples/engineering-demo/README.md) to install, build and open
the interactive decision graph at `/knowledge-graph/`. It reads only the demo's allowlisted
shared content and is part of the existing Docusaurus site.
