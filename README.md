# AI Agents — less process, durable knowledge

A portable English catalog of agents and skills for practical AI-assisted engineering.
Start from `AGENTS.md`, keep personal working plans in your Second Brain, implement and
verify a focused change, then preserve relevant project decisions and documentation.

| Need | Start here |
| --- | --- |
| Understand the engineering model | [Operating model](toolkit/OPERATING-MODEL.md) |
| Set up a project | [AGENTS.md templates](templates/agent-instructions/README.md) and [adoption](toolkit/ADOPT-PROJECT.md) |
| Find expertise | [Agents](agents/README.md), [skills](skills/README.md), [catalog guide](toolkit/CATALOG-GUIDE.md) |
| Open private plans from Windows/WSL | [Personal planning](templates/agent-instructions/personal-planning.md) |
| Explore decisions and AI topics | [Runnable Docusaurus demo](examples/engineering-demo/README.md) |
| Understand repository folders | [Repository and toolkit guide](toolkit/README.md) |
| Run this repository | [Runbook](toolkit/REPOSITORY-WORKFLOW.md) |

## Information ownership

| Personal | Shared delivery | Durable project knowledge |
| --- | --- | --- |
| Second Brain: working plan, experiments, resume point | Issue: scope/acceptance; PR: changes and actual checks | Code, relevant ADRs, architecture and operations |

The team can maintain the result without your private plan. Share a joint execution plan
only when collaboration needs it. Customer policy determines permitted storage. No mandatory
workspace directory, YAML configuration, extra tracker, agent team or ADR for every edit.

## Use with OpenCode 1

Python 3.11+ runs the core toolkit without third-party runtime dependencies:

```sh
git clone https://github.com/atstaeff/ai-agents.git ~/tools/ai-agents
cd ~/tools/ai-agents
python3 tools/ai_toolkit.py check
python3 tools/ai_toolkit.py export --runtime opencode --preset engineering \
  --output "$HOME/.config/ai-agents/opencode"
cd /path/to/project
OPENCODE_CONFIG_DIR="$HOME/.config/ai-agents/opencode" \
OPENCODE_CONFIG="$HOME/.config/ai-agents/opencode/opencode.json" opencode web
```

The engineering preset registers 8 agents and 16 skills. Use `--preset all` for the full
catalog or add focused entries with `--agent` and `--skill`. The [catalog guide](toolkit/CATALOG-GUIDE.md) explains selection and retired names. Your host supplies
models, tools and permissions. Re-export after source changes; the manifest protects edits.
Use [private plan-directory configuration](templates/agent-instructions/personal-planning.md)
to let Plan write to a narrow external folder. See [runtime adapters](toolkit/RUNTIMES.md)
for other hosts and [optional review](toolkit/PLAN-REVIEW.md) when a plan gate is required.

## Decisions you can explore

The [Docusaurus demo](examples/engineering-demo/README.md) builds a local site with an
interactive graph from shared Markdown: decisions, system components and AI topics.
Search, filter, inspect relationships and open the original documentation. Private plans
are excluded by construction. The existing [Docusaurus site](https://atstaeff.github.io/ai-agents/)
remains the catalog website; this change does not deploy either site.

## Maintain and verify

Edit canonical `agents/`, `skills/`, `toolkit/` and `templates/` sources. `tools/` and
`tests/` contain the optional CLI/API/dashboard and exporters. Existing `workspace/`
metadata and local records remain compatible; they are optional. `website/` builds the
catalog website and root `docs/` is generated output.

```sh
uv sync --locked --group validation
python3 tools/ai_toolkit.py check
uv run --locked --group validation python -m unittest discover -s tests -v
python3 tools/workspace_smoke.py
npm --prefix website ci
npm --prefix website run build
```

See [contributing](CONTRIBUTING.md), [templates](templates/README.md) and
[quality](toolkit/QUALITY-STANDARD.md). License: [MIT](LICENSE).
