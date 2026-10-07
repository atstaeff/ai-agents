# Quick start in WSL

Requirements: Python 3.11+ and your installed OpenCode 1. The companion uses only
Python's standard library; documentation development additionally uses uv and MkDocs.

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

In another WSL terminal, start the local dashboard for the same project:

```sh
python3 ~/tools/ai-agents/tools/ai_toolkit.py serve --workspace /path/to/project
```

Open **http://127.0.0.1:4097**. Create a work record, edit the plan in your editor,
append comments and update task evidence in the dashboard. The AI host must follow
its instructions to update that same file; there is no background session watcher.

See [runtime adapters](installation.md), [workflow](workflow.md) and
[work records](../toolkit/work-records.md).
