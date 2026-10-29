# Manage agents and skills

Agents define roles, decision boundaries and expected handoffs. Skills provide reusable
procedures and focused references. A skill can be used in the current session; selecting
another profile does not automatically start another agent.

## One catalog, seven disciplines

Browse [agents](../agents/README.md) and [skills](../skills/README.md). Canonical sources
use `agents/<domain>/<name>.agent.md` and `skills/<domain>/<name>/SKILL.md`.
[Domain metadata](catalog-domains.json) drives the catalog, website and local filter.
Names remain unique across each kind so exported native IDs stay predictable.

| Domain | Responsibility |
| --- | --- |
| general | Foundations, selection and bounded coordination |
| delivery | Product discovery, project flow, scope and stakeholder decisions |
| architecture | Domain modeling, interfaces and consequential system decisions |
| engineering | Application/platform implementation and specialized products |
| languages | Language and framework practices |
| quality | Verification, security, performance and recovery |
| knowledge | Project memory, private knowledge work and communication |

Roles and disciplines overlap in real work. Choose one primary home and link relevant
expertise rather than maintaining copies under several categories. Keep runtime-specific
tools and permissions in exporters; a Python skill does not require a Python-only agent.

## Select a bounded runtime catalog

Use a preset to register only useful native agents/skills in the host:

| Preset | Native agents | Native skills | Use |
| --- | --- | --- | --- |
| minimal | 3 | 4 | General execution with explicit on-demand expertise |
| team | 13 | 20 | Autonomous Product/Engineering/Delivery leads, Python/React/GCP/Terraform, checks and review |
| engineering | 9 | 16 | Python, architecture, implementation, quality and delivery |
| product | 4 | 7 | Discovery, stakeholder proposals and coordination |
| knowledge | 3 | 5 | Private notes and presentations |
| platform | 6 | 10 | Google Cloud, Terraform, delivery and security |
| documentation | 2 | 5 | Focused technical authoring and editing |
| all | 22 | 41 | Complete active catalog; default export with Delivery as the OpenCode entry |

The source of these selections is [catalog-presets.json](catalog-presets.json).
Presets are selections, not security boundaries or separate copies of expertise.
Add a needed specialty explicitly; installing more native profiles increases discovery
metadata, even if their bodies are loaded later. Actual host injection differs by version.

```sh
python3 tools/ai_toolkit.py catalog --preset engineering
python3 tools/ai_toolkit.py export --runtime opencode --preset engineering \
  --agent golang-expert --skill golang-patterns --output /path/to/export --dry-run
```

Remove --dry-run after inspecting the selection. Without --preset, export preserves
all active entries for existing users. Commands are generated only for selected agents;
for example /brain requires second-brain. Phase-specific options require that phase agent;
lead/worker/review routes apply only to selected profiles. A narrower re-export removes only
unchanged owned profiles; edited files stop the
update before writes. Prefer a new output directory when protecting local customizations.

The bundle retains the canonical reference catalog for on-demand reading and stable
relative links. This is not text automatically injected into every prompt. The native
catalog/index.json lists only the selection; use this checkout for a complete catalog query.

## Select by uncertainty and outcome

Reuse applicable instructions already loaded. Handle clear small tasks directly. For
substantial work, read the project entry and current assignment once, then only relevant
contract/decision sections and the next useful skill body. A skill or profile link is not
a checklist to recursively load every target. Expand when a real uncertainty requires it;
never discard a governing constraint for a fixed context budget.

Runtime adapters use [session rules](SESSION-RULES.md) as the compact shared startup
contract. [The detailed workflow](WORKFLOW.md), recovery and project-concept guides stay
available for their specific uncertainty. Roles supply a viewpoint/authority boundary;
skills supply procedure. Another skill does not require another session.

## Focused stack and documentation expertise

Use python-patterns for Python/FastAPI boundaries, frontend-patterns for React and
JavaScript application behavior, gcp-patterns for Google Cloud and terraform-iac for
state-aware infrastructure changes. Existing specialists own these capabilities; no
separate agent is needed for every library. Technical-writing and documentation-editor
cover source-verified procedures, narrative and independent editing.

The platform and documentation presets keep these additional capabilities opt-in.
The engineering preset includes frontend-expert alongside Python and review roles.
[Native orchestration](ORCHESTRATION.md) combines lead viewpoints and selected specialists.

## Consolidated names and migration

Three roles were consolidated: context-manager into task-orchestrator; stakeholder-agent
and proposal-pitch into product-manager. Context retention remains every contributor's
responsibility; it does not require a separate memory session. Product proposals and
stakeholder acceptance share the evidence and scope of product discovery.

Ten shallow/overlapping skill entries now point directly to their owner:

| Retired skill | Active owner |
| --- | --- |
| general | agent-routing |
| architecture, system-design | architecture-planning |
| team-collaboration, progress-sync | work-management |
| feature-discovery-session | product-discovery |
| agile-methodologies | project-management |
| testing-strategies | testing |
| game-development | game-architecture |
| creative-apps | creative-app-patterns |

[Alias metadata](catalog-aliases.json) keeps old public website profile URLs available
as migration pointers. Retired native IDs and old source paths are no longer installed:
update personal commands/configuration to the active names before re-exporting. Focused
examples moved into the surviving skill's references; no second active procedure is maintained.
Historical observations keep their original names/counts as dated evidence.

## Add or improve expertise

1. Inspect existing metadata and choose whether an existing skill/agent already owns
   the outcome. Improve it before adding a competing generalist.
2. Choose a discipline and a stable lowercase hyphenated name. Use the
   [skill template](../templates/catalog/skill-template.md) or
   [agent template](../templates/catalog/agent-template.md).
3. Write a concrete selection description. Specify useful inputs, actions, output and
   evidence. Give an agent its role/authority boundary; give a skill its procedure.
4. Put long examples in that skill's `references/`, or its agent domain's `references/`.
   Link focused sections from the entry. Keep private project facts in the project-owned knowledge space.
5. Run catalog/link checks, export tests and strict docs build. For consequential
   behavior, forward-test a realistic assignment, missing-tool case and small bypass.
6. Review the diff, actual observations and limitations. Version the canonical source
   through a PR; re-export deliberately into the host after integration.

Keep frontmatter to portable `name` and `description`. Existing flat agent sources and
legacy topic skill files remain readable by the loader for older catalog fixtures;
new repository contributions use the normalized domain layout. Generated exports are
deployment artifacts, not another source to edit.

## Generated indexes and exports

Refresh the GitHub entry indexes after metadata changes:

```sh
python3 tools/ai_toolkit.py catalog --kind agent --format markdown > agents/README.md
python3 tools/ai_toolkit.py catalog --kind skill --format markdown > skills/README.md
python3 tools/ai_toolkit.py check
```

The check detects stale generated indexes. Runtime adapters flatten category paths into
their native layout and rebase references. The manifest preserves human edits and removes
only verified obsolete owned files. Updating a catalog does not update an installed bundle
until it is re-exported. Perform the [host check](PORTABILITY.md#verify-a-new-host-once)
after changing host/version or effective permissions.

## Quality of the catalog itself

Judge entries by correct selection, useful output, preserved constraints and actual
verification. A count of agents or many framework names is not evidence of engineering
expertise. Remove demonstrated duplication deliberately, preserving compatibility or
documenting a migration for stable names. Avoid speculative role inflation.

See the [bounded forward observations](evaluations/catalog-restructure-20261022.md) for the current restructure and their limitations.

[2026-10-23 efficiency audit](evaluations/catalog-efficiency-20261023.md) records measured
source/metadata sizes, bounded behavior trials and unverified runtime claims.
