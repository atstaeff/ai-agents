# AI Agents — an engineering catalog and operating model

Manage reusable AI expertise and use it in real projects with clear outcomes, shared
knowledge and verifiable results. The repository combines a domain-organized agent and skill catalog, a
project operating model, reusable templates and a local Python toolkit. Shared sources
are English and independent of model vendors.

## Choose your starting point

| You want to… | Start here |
| --- | --- |
| Find or maintain engineering expertise | [Agent catalog](agents/README.md), [skill catalog](skills/README.md), [catalog guide](toolkit/CATALOG-GUIDE.md) |
| Deliver a product with a small accountable team and AI | [Engineering operating model](toolkit/OPERATING-MODEL.md), [team project starter](templates/project-starter/README.md) |
| Set up a new or existing project | [Team starter](templates/project-starter/README.md), [adoption guide](toolkit/ADOPT-PROJECT.md) |
| Define a decision, project request or architecture review | [Template chooser](templates/README.md) |
| Make quality measurable | [Engineering quality standard](toolkit/QUALITY-STANDARD.md) |
| Continue work across sessions and growing project knowledge | [Knowledge guide](toolkit/PROJECT-KNOWLEDGE.md), [recovery contract](toolkit/CONTEXT-RECOVERY.md) |
| Run this repository's workflow | [Repository runbook](toolkit/REPOSITORY-WORKFLOW.md) |

## Work together through AGENTS.md

Start with [AGENTS.md](AGENTS.md). It links vision/goals, stakeholders, scope, process,
work/review homes, current knowledge and decisions. The [team starter](templates/project-starter/README.md)
provides matching project and contribution pages; the [instruction chooser](templates/agent-instructions/README.md)
adds existing-repository, remote-documentation, multi-repository and component variants.

Use local Markdown or an explicitly adopted central web process. Keep each fact at its
owner and pin shared policy to a verified source revision or maintained documentation
version. No YAML manifest or workspace hierarchy is required. Docusaurus publishes the
same selected Markdown sources as a reading view.

Each assignment has an accountable human, bounded writer scope and integration owner.
Coordinate overlapping work, agree shared contracts and verify combined changes. Keep
one live plan in the assigned issue/ticket, update current knowledge and preserve significant
rationale. Completed plans stay historical; a bounded handoff lets another session continue.
See the [operating model](toolkit/OPERATING-MODEL.md) and [worked example](toolkit/examples/project-kernel.md).

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

## Shared project memory

Use [PROJECT.md](PROJECT.md) and the [knowledge index](knowledge/README.md) as filled
examples. Project facts and actual work/review links belong in the project; reusable
methods and skills stay in this catalog. Significant reasons live in
[decision records](knowledge/decisions/README.md); current knowledge links code/contracts
and actual evidence. [Project adoption](toolkit/ADOPT-PROJECT.md) explains setup and
[the detailed concept](toolkit/PROJECT-CONCEPT.md) covers source authority and publication.

Existing [YAML maps](toolkit/PROJECT-CONFIG.md) and the extended fictional customer
workspace remain optional compatibility examples. They are not the default project structure.

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
| `knowledge/` | This repository's current knowledge, stakeholders, agreement and decision history |
| `workspace/` | Optional ignored local workbench storage; no project context requirement |
| `tools/`, `tests/` | Local CLI/API/dashboard, exporters, catalog tooling and behavior checks |
| `website/` | [Docusaurus site, source publisher and preview guide](website/README.md) |
| `reference-repos/`, `marp-templates/` | Illustrative engineering references and presentation starters |
| `docs/` | Generated GitHub Pages output, rebuilt by the existing main workflow |

Profile pages and catalog navigation are generated from canonical metadata. Do not edit
exported bundles or generated website files. Customer-specific knowledge stays with the
customer; private vaults and credentials stay outside public repositories.

## Verify and contribute

```sh
python3 tools/ai_toolkit.py check
python3 -m unittest discover -s tests -v
uv sync --locked --group validation
uv run --locked --group validation python -m unittest discover -s tests -v
python3 tools/workspace_smoke.py
npm --prefix website ci
npm --prefix website run build
```

The uv lock supplies optional config/graph validation; the npm lock supplies website dependencies. See
[contributing](CONTRIBUTING.md), the [local API](toolkit/API.md) and the
[documentation site](https://atstaeff.github.io/ai-agents/). Local/model observations do
not prove live tracker access, distributed coordination or a particular installed host.
License: [MIT](LICENSE).
