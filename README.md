# AI Agents

**Build useful software with AI. Keep the context and evidence your team needs to continue.**

An English catalog of reusable AI roles, focused skills and project templates, with a
practical engineering process and optional local Python tools. Use your existing stack,
tracker and review workflow. Your host runs the models and controls tools and permissions.

[Try the first task](website/content/getting-started/quick-start.md) ·
[Documentation](https://atstaeff.github.io/ai-agents/) ·
[Catalog](toolkit/CATALOG-GUIDE.md) ·
[Templates](templates/README.md)

## Start with a small result

The [quick start](website/content/getting-started/quick-start.md) gives you a disposable
portable export and a supplied note-to-runbook exercise. The local export needs only Git,
Python 3.11+ and a Bash shell; the AI task uses a host and model access you already have.
It separates local file checks from an actual host result and shows what success looks like.
No project manifest, server or agent team is needed.

Already have a checkout? Inspect a focused selection without installing anything:

```sh
python3 tools/ai_toolkit.py check
python3 tools/ai_toolkit.py catalog --preset minimal
```

For native installation, follow the [runtime guide](toolkit/RUNTIMES.md). Adapters emit
OpenCode, Claude Code, VS Code/Copilot and Herd layouts, plus portable Agent Skills and
profiles. An export is not an installed-host validation: record observed discovery,
model/effort, permissions and limits with the [runtime check](templates/delivery/runtime-check.md).
Configure providers and credentials in the host; generated profiles install no host or model.

## Adopt in one project

After the first task, merge the [project starter](templates/project-starter/README.md)
or an [AGENTS.md variant](templates/agent-instructions/README.md) into existing instructions.
Begin with what the next assignment needs:

1. Identify its outcome, acceptance, accountable human and real work/review homes.
2. Link relevant project facts, rules and actual check commands. Keep existing owners.
3. Read only the relevant [skills](skills/README.md) and [role profiles](agents/README.md).
   Make one reviewable change, run its checks and preserve significant reasons.
4. Add coordination, knowledge views or more templates when a concrete need appears.

A clear small change needs no separate plan or additional agent. Personal execution notes
stay private, subject to project policy; shared sources must let a teammate continue.
Projects choose their own folders or authorized web documentation. Adopt binding external
policy at an explicit revision; evolving technique links do not silently change project rules.

## Choose your next step

| Goal | Use |
| --- | --- |
| Find expertise for Python/FastAPI, React/JavaScript, GCP or Terraform | [Catalog selection](toolkit/CATALOG-GUIDE.md) |
| Clarify a product problem, acceptance or stakeholder decision | [Product preset](toolkit/CATALOG-GUIDE.md) and [templates](templates/README.md) |
| Understand delivery roles and information ownership | [Engineering operating model](toolkit/OPERATING-MODEL.md) |
| Coordinate leads and bounded specialists | [Orchestration](toolkit/ORCHESTRATION.md) and [runtime/capacity check](templates/delivery/runtime-check.md) |
| Use Herdr, Ponytail or Graphify | [Native integrations](toolkit/INTEGRATIONS.md) |
| Explore decisions and relationships in Docusaurus | [Knowledge map example](examples/engineering-demo/README.md) |
| Inspect optional local tools and repository structure | [Repository map](toolkit/README.md) |

Use Herdr whenever its executable and selected server are usable. Complex judgment uses
strong approved models with high reasoning; bounded work uses proven economical routes;
mechanical coordination uses native tools. Delegate useful independent ready slices by
default, group isolated writer workspaces and label agent/checks/log panes. All leads and
child agents share one capacity/budget within measured machine, provider and review limits.
See the [Herdr policy](toolkit/HERDR.md) for native skill discovery, layout and fallback.

## Knowledge that survives a session

| Source | Owns |
| --- | --- |
| AGENTS.md and linked project sources | Context navigation, responsibilities, process and real tooling |
| Issue/ticket and PR/MR | Shared scope, acceptance, coordination and review evidence |
| Current Markdown and ADRs | Implemented behavior, operating knowledge and significant reasons |
| Docusaurus and scoped graph views | Derived reading and retrieval views of selected shared sources |

The [knowledge map demo](examples/engineering-demo/README.md) starts with areas, then
loads filtered records and direct relationships. It is a bounded static example; a
million-record installation needs an incremental index service. Graphify can supply
dependency evidence; reviewed project knowledge remains authoritative.

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
[quality standard](toolkit/QUALITY-STANDARD.md). Checks and bounded observations establish
specific behavior; they do not establish productivity gains or staffing reductions.
The catalog and toolkit are [MIT licensed](LICENSE). Third-party hosts and integrations
retain their own licenses and configuration requirements.
