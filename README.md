# AI Agents

**Build useful software with AI. Keep the reasoning your team needs to maintain it.**

An English engineering catalog and operating model for developers, product owners and
small teams: reusable skills, accountable AI roles, practical templates and durable
project knowledge. Use your existing GitHub/Jira workflow and choose the models and
hosts that fit the work.

[Documentation](https://atstaeff.github.io/ai-agents/) ·
[Operating model](toolkit/OPERATING-MODEL.md) ·
[Project starter](templates/project-starter/README.md) ·
[Templates](templates/README.md)

## Adopt in one project

1. Add or adapt [AGENTS.md](templates/agent-instructions/README.md). Link vision,
   boundaries, responsible people, actual tools, process, commands and knowledge.
2. Keep outcome and acceptance in the existing issue/ticket; deliver one reviewable increment.
3. Load the relevant [skills](skills/README.md) and [roles](agents/README.md).
   Verify the combined result and retain significant decisions at the project's own home.
4. Add [native orchestration](toolkit/ORCHESTRATION.md) and published knowledge views
   when they help the team.

A clear small change needs no separate plan, phase documents or agent team. Personal
execution notes stay private, subject to customer policy; the team can continue from
shared sources. Projects choose their own folders and accessible web documentation.

## Choose your starting point

| Goal | Use |
| --- | --- |
| Understand the value stream and responsibilities | [Engineering operating model](toolkit/OPERATING-MODEL.md) |
| Python/FastAPI, React/JavaScript, GCP and Terraform | [Engineering and platform expertise](toolkit/CATALOG-GUIDE.md) |
| Product discovery, PO work and stakeholders | [Catalog selection](toolkit/CATALOG-GUIDE.md) with `--preset product`; [templates](templates/README.md) |
| Several leads and economical specialists | [Preferred Herdr execution, model tiers and tabs](toolkit/HERDR.md) |
| Ponytail, Herdr and Graphify | [Native integration guide](toolkit/INTEGRATIONS.md) |
| Human-readable decisions and dependency views | [Docusaurus knowledge map](examples/engineering-demo/README.md) |
| Repository folders, optional tools and compatibility | [Repository map](toolkit/README.md) |

Use Herdr whenever its executable and selected server are usable. Complex decisions
use strong approved models with high reasoning; bounded specialists use economical
routes. Native commands handle mechanical coordination. Fill free capacity with
independent ready work, using labelled tabs and isolated checkouts. See the
[Herdr policy](toolkit/HERDR.md) for readiness, limits and fallback behavior.

## Install a focused catalog

The core toolkit runs on Python 3.11+ with the standard library. Export only the expertise
needed by the project; supported hosts include OpenCode, Claude Code, Copilot and Herd,
with a portable Agent Skills layout as well.

```sh
git clone https://github.com/atstaeff/ai-agents.git
cd ai-agents
python3 tools/ai_toolkit.py check
python3 tools/ai_toolkit.py catalog --preset engineering
python3 tools/ai_toolkit.py export --runtime opencode --preset engineering \
  --output /path/to/ai-agents-export --dry-run
```

Inspect the selection, repeat without `--dry-run`, then follow the
[runtime guide](toolkit/RUNTIMES.md) for discovery and an installed-host check. Use
`--agent` and `--skill` to add a specialty, or `--preset all` deliberately. Configure actual
models, effort, tools and permissions in the host. Re-export after source changes.
Existing edited and unmanaged files are protected; keep generated bundles separate from
canonical sources and customer knowledge.

## Knowledge that survives a session

| Source | Owns |
| --- | --- |
| AGENTS.md and linked project map | Context navigation, responsibilities and real tooling |
| Issue/ticket and PR/MR | Shared scope, acceptance, coordination and review evidence |
| Current Markdown and ADRs | Implemented behavior, operating knowledge and significant reasons |
| Docusaurus and scoped graph views | Derived reading and retrieval views of selected shared sources |

The [knowledge map demo](examples/engineering-demo/README.md) starts with areas, then
loads filtered records and direct relationships. It provides a bounded static example;
a million-record installation needs an incremental index service. Graphify is an optional
source of dependency evidence; canonical decisions remain reviewed project knowledge.

## Maintain this repository

`agents/` and `skills/` own reusable expertise; `templates/` supplies copyable artifacts.
`toolkit/` explains the method. `knowledge/` records this repository's own facts and decisions.
`examples/` and `reference-repos/` illustrate adoption. `tools/` and `tests/` implement and
verify the optional toolkit. `website/` owns Docusaurus sources; root `docs/` is generated.

```sh
uv sync --locked --group validation
python3 tools/ai_toolkit.py check
uv run --locked --group validation python -m unittest discover -s tests -v
python3 tools/workspace_smoke.py
npm --prefix website ci
npm --prefix website run test:graph
npm --prefix website run build
```

See [contributing](CONTRIBUTING.md), the [runbook](toolkit/REPOSITORY-WORKFLOW.md) and
[quality standard](toolkit/QUALITY-STANDARD.md). Test results and bounded observations
establish specific behavior; they do not promise a staffing reduction or defect-free delivery.
The catalog and toolkit are [MIT licensed](LICENSE). Third-party hosts and integrations
retain their own licenses and configuration requirements.
