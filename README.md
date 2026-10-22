# AI Agents — an engineering catalog and operating model

Manage reusable AI expertise and use it in real projects with clear outcomes, shared
knowledge and verifiable results. The repository combines a domain-organized agent and skill catalog, a
project operating model, reusable templates and a local Python toolkit. Shared sources
are English and independent of model vendors.

## Choose your starting point

| You want to… | Start here |
| --- | --- |
| Find or maintain engineering expertise | [Agent catalog](agents/README.md), [skill catalog](skills/README.md), [catalog guide](toolkit/CATALOG-GUIDE.md) |
| Deliver a product with a small accountable team and AI | [Operating model](toolkit/OPERATING-MODEL.md) |
| Set up a new or existing project | [Adoption guide](toolkit/ADOPT-WORKSPACE.md), [customer starter](templates/customer-workspace/README.md) |
| Define a decision, project request or architecture review | [Template chooser](templates/README.md) |
| Make quality measurable | [Engineering quality standard](toolkit/QUALITY-STANDARD.md) |
| Continue work across sessions and growing project knowledge | [Knowledge guide](toolkit/PROJECT-KNOWLEDGE.md), [recovery contract](toolkit/CONTEXT-RECOVERY.md) |
| Run this repository's workflow | [Repository runbook](toolkit/REPOSITORY-WORKFLOW.md) |

## Find expertise by discipline

The same domains organize source files, the website and the local catalog filter:

| Discipline | Examples |
| --- | --- |
| Foundations & Coordination | Jörg, Plan, Build, routing |
| Product & Project Management | Discovery, scope, stakeholder decisions, flow and technical debt |
| Architecture & Systems | Domain boundaries, APIs, system design and architecture review |
| Software & Platform Engineering | Cohesive code, refactoring, platforms and specialized applications |
| Programming Languages | Python, Go, Flutter and frontend practices |
| Quality, Security & Reliability | Tests, reviews, performance, trust boundaries and incident recovery |
| Knowledge & Communication | Context, project memory, private PARA and presentations |

Agents define roles and expected handoffs. Skills provide focused procedures and references.
Select only the expertise needed for the assignment; a skill does not require another chat.
The [catalog guide](toolkit/CATALOG-GUIDE.md) explains contribution and versioning.

## Use the catalog in OpenCode 1

Python 3.11+ runs the core toolkit with no runtime dependencies. Your AI host supplies
models, tools, permissions and any native delegation. Export from this checkout:

```sh
git clone https://github.com/atstaeff/ai-agents.git ~/tools/ai-agents
cd ~/tools/ai-agents
python3 tools/ai_toolkit.py check
python3 tools/ai_toolkit.py export --runtime opencode \
  --output "$HOME/.config/ai-agents/opencode"
```

Start OpenCode Web from the project root with your installed model/provider configured:

```sh
cd /path/to/project
OPENCODE_CONFIG_DIR="$HOME/.config/ai-agents/opencode" \
OPENCODE_CONFIG="$HOME/.config/ai-agents/opencode/opencode.json" \
opencode web
```

The bundle selects Jörg and supplies Plan/Build, specialists and native skills. No model
or plugin is forced. See [runtimes](toolkit/RUNTIMES.md) for Claude Code, Copilot and
portable exports, and [plan review](toolkit/PLAN-REVIEW.md) for optional Plannotator and
separate models. Re-export after source changes; the manifest protects human edits.
Perform the installed-host check before assuming effective discovery or permissions.

## Give the project a shared workspace

Start from `AGENTS.md`, `workspace/README.md`, `workspace/workspace.yml`, the working
agreement and decision roles. Reuse existing equivalents. The YAML maps actual systems,
repositories, optional flow fields and quality gates; it grants no access and executes
nothing. [Minimal, GitHub, Jira and multi-repo examples](toolkit/ADOPT-WORKSPACE.md)
share one schema.

Keep the active plan in the assigned issue/ticket, implementation evidence in the PR,
and significant rationale in customer-owned ADRs. Save a bounded handoff before switching
sessions. Load current relevant sources instead of carrying the entire conversation.
The [detailed workspace concept](toolkit/WORKSPACE-CONCEPT.md) covers the complete contract.

For a larger local request with no assigned tracker:

```sh
python3 tools/ai_toolkit.py work --workspace /path/to/project new onboarding \
  --title "Improve onboarding" --kind product
python3 tools/ai_toolkit.py serve --workspace /path/to/project
```

Open `http://127.0.0.1:4097`. The dashboard searches expertise and manages Markdown
records, comments and evidence under `workspace/work/`. It does not run models or
synchronize trackers. [Legacy migration](toolkit/WORK-RECORDS.md) is explicit and preserves
records; local work and archives stay outside knowledge publication by default.

## Repository map

| Directory | Maintained source |
| --- | --- |
| `agents/<domain>/` | Bounded role profiles and focused references |
| `skills/<domain>/<name>/` | Native SKILL.md entries, references and optional UI metadata |
| `toolkit/` | Operating model, quality/knowledge contracts, config schema and usage guides |
| `templates/` | Project, architecture, delivery, quality and catalog templates |
| `workspace/` | This repository's actual context, config, decisions and optional local work |
| `tools/`, `tests/` | Local CLI/API/dashboard, exporters, documentation hook and behavior checks |
| `website/` | MkDocs configuration and website-specific content/styles |
| `docs/` | Generated GitHub Pages output, rebuilt by the existing main workflow |

Profile pages and catalog navigation are generated from canonical metadata. Do not edit
exported bundles or generated website files. Customer-specific knowledge stays with the
customer; private vaults and credentials stay outside public repositories.

## Verify and contribute

```sh
python3 tools/ai_toolkit.py check
python3 -m unittest discover -s tests -v
uv sync --locked --group docs
uv run --locked --group docs python -m unittest discover -s tests -v
python3 tools/workspace_smoke.py
uv run --locked --group docs mkdocs build -f website/mkdocs.yml --strict \
  --site-dir "$PWD/workspace/generated/site"
```

The locked environment supplies optional config/graph and website dependencies. See
[contributing](CONTRIBUTING.md), the [local API](toolkit/API.md) and the
[documentation site](https://atstaeff.github.io/ai-agents/). Local/model observations do
not prove live tracker access, distributed coordination or a particular installed host.
License: [MIT](LICENSE).
