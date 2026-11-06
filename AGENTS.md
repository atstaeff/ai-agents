# Repository instructions

Maintain this English engineering catalog, operating model and local Python toolkit.
Use the user's language in conversation; current user/host instructions govern.
At session startup, load and apply [session rules](toolkit/SESSION-RULES.md), reusing a
matching loaded copy. Herdr discovery and autonomous team coordination are the default;
the user does not need to request them again.

## Repository map

| Source | Owns |
| --- | --- |
| [engineering/process/](engineering/process/README.md) | Applicable process step and next action |
| [skills/](skills/README.md), [agents/](agents/README.md) | Reusable techniques and role profiles |
| [knowledge/](knowledge/README.md), [decisions](knowledge/decisions/README.md) | Current facts and ADR rationale |
| [templates/](templates/README.md) | Adaptable project structures and records |

## Choose the relevant context

For a clear small correction, inspect affected files. For unfamiliar substantial work,
use [PROJECT.md](PROJECT.md) for scope, owners and actual work homes, then
[CONTRIBUTING.md](CONTRIBUTING.md) for the process. Reuse current loaded instructions;
follow further pointers only to resolve the assignment's uncertainty:

| Need | Source |
| --- | --- |
| Product AI intake and handoff to Engineering | [Product Intake workflow](toolkit/PRODUCT-INTAKE.md) |
| Current knowledge and significant reasons | [Knowledge index](knowledge/README.md) |
| Decision/acceptance or action boundary | [Stakeholders](knowledge/stakeholders.md), [agreement](knowledge/working-agreement.md) |
| Native execution and team coordination | [Herdr policy](toolkit/HERDR.md), [orchestration](toolkit/ORCHESTRATION.md) |
| Native Herd, Herdr, Ponytail or Graphify | [Integrations](toolkit/INTEGRATIONS.md) |
| Catalog structure, consolidation or presets | [Catalog guide](toolkit/CATALOG-GUIDE.md) |
| Information ownership, entry or publication change | [Project concept](toolkit/PROJECT-CONCEPT.md) |
| Interrupted or conflicting state | [Recovery contract](toolkit/CONTEXT-RECOVERY.md) |

The [published process](https://atstaeff.github.io/ai-agents/contributing/) is a reading view;
this checkout owns its revision. Load relevant skill bodies and source sections on demand.

For tasks explicitly in Product Intake, follow the [Product Intake workflow](toolkit/PRODUCT-INTAKE.md) before selecting agents. Product AI prepares and reviews requirements, but does not implement code or start engineering delivery. An authorized human approval is required before handoff to Engineering. This boundary does not restrict explicitly authorized engineering tasks outside Intake.

## Preserve these boundaries

- Edit canonical agents/<domain>/<name>.agent.md and skills/<domain>/<name>/SKILL.md;
  keep portable name/description metadata and regenerate catalog indexes after changes.
- Preserve Python 3.11+, the standard-library core, loopback/local assets, comment
  persistence and stale-write protection. Export host permissions through adapters.
- website/ publishes canonical sources; docs/ is generated. Preserve public routes.
  Keep private content and generated bundles out of commits. No unsolicited messages.
- Do not merge or deploy without an explicit request. The session rules own shared/private
  planning, coordination, verification and handoff; keep those policies at that source.

## Verify the change

Use the [runbook](toolkit/REPOSITORY-WORKFLOW.md) and [CI](.github/workflows/checks.yml).
Run checks appropriate to the changed boundary; repeat for a relevant change, failure or
unresolved concern. Report actual evidence and unrun checks against the tested revision.
