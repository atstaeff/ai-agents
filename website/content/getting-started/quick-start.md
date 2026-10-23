# Quick start in WSL

Requirements: Python 3.11+ and your installed OpenCode 1. The companion uses only
Python's standard library; website development additionally uses Node.js and Docusaurus.

```sh
git clone https://github.com/atstaeff/ai-agents.git ~/tools/ai-agents
cd ~/tools/ai-agents
python3 tools/ai_toolkit.py check
python3 tools/ai_toolkit.py export --runtime opencode --output "$HOME/.config/ai-agents/opencode"
cd /path/to/project
OPENCODE_CONFIG_DIR="$HOME/.config/ai-agents/opencode" \
OPENCODE_CONFIG="$HOME/.config/ai-agents/opencode/opencode.json" opencode web
```

Jörg is the default agent. Use `/work-plan` to plan and `/work-build` to implement,
or ask Jörg to coordinate the whole outcome. Specialists and skills load as needed.

For comments and approval before Build, use the [local Plannotator setup](plan-review.md).
Add `--plannotator` when exporting; optional per-phase model and variant flags let Plan
and Build use different models or supported thinking levels. Review and approve the
current plan revision before starting `/work-build` for a gated assignment.

## Keep personal plans private

Start the project from `AGENTS.md`; use the [adoption guide](adopt-workspace.md).
Keep substantial personal working plans in your configured private Second Brain project
folder. Issues own shared scope and acceptance; PRs own code and verification. Preserve
significant decisions and affected project documentation after implementation.

Configure the private plan directory with the export's `--plan-directory` option; see
[the private setup example](https://github.com/atstaeff/ai-agents/blob/main/templates/agent-instructions/personal-planning.md).
If storage is unavailable, report an unsaved session plan and continue authorized work.
Small changes need no plan file. No mandatory workspace tree or YAML is needed.

## Optional local dashboard

In another WSL terminal, start the dashboard for the same project:

```sh
python3 ~/tools/ai-agents/tools/ai_toolkit.py serve --workspace /path/to/project
```

Open **http://127.0.0.1:4097**. For existing local records, edit the plan in your editor,
append comments and update task evidence in the dashboard. The AI host must follow
its instructions to update that same file; there is no background session watcher.

See the [concept](../concept.md), [runtime adapters](installation.md),
[working contract](workflow.md) and [local website preview](local-preview.md).
