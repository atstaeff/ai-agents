# Repository instructions

Maintain this English engineering catalog, operating model and local Python toolkit.
Use the user's language in conversation. Follow current user/host and applicable project rules.

## Choose the relevant context

For a clear small correction, inspect affected files and apply the rules below; reuse
instructions already loaded. For substantial or unfamiliar work, read [PROJECT.md](PROJECT.md)
for outcome, scope, ownership and actual work homes, then [CONTRIBUTING.md](CONTRIBUTING.md)
for process, skill selection and checks. Read further sources only for the current uncertainty:

| Need | Source |
| --- | --- |
| Concise execution rules | [Session rules](toolkit/SESSION-RULES.md) |
| Current knowledge and significant reasons | [Knowledge index](knowledge/README.md) |
| Decision/acceptance or action boundary | [Stakeholders](knowledge/stakeholders.md), [agreement](knowledge/working-agreement.md) |
| Preferred Herdr execution, model tiers and tabs | [Herdr policy](toolkit/HERDR.md) |
| Lead/specialist coordination and model choices | [Orchestration](toolkit/ORCHESTRATION.md) |
| Native Herd, Herdr, Ponytail or Graphify | [Integrations](toolkit/INTEGRATIONS.md) |
| Catalog structure, consolidation or presets | [Catalog guide](toolkit/CATALOG-GUIDE.md) |
| Information ownership, entry or publication change | [Project concept](toolkit/PROJECT-CONCEPT.md) |
| Interrupted or conflicting state | [Recovery contract](toolkit/CONTEXT-RECOVERY.md) |

The [published process](https://atstaeff.github.io/ai-agents/contributing/) is a reading view;
this checkout owns its revision. Load the next relevant skill body, not every linked skill,
role profile, guide or historical ADR. Expand when needed without omitting governing constraints.

## Preserve these boundaries

- Treat the assigned outcome as standing authorization for routine internal team coordination
  within host/project limits; apply the [autonomous default](toolkit/SESSION-RULES.md#autonomous-team-default).
  Choose leads, specialists and qualified models, then carry work through review and checks
  without requiring the user to repeat orchestration instructions.
- Edit canonical agents/<domain>/<name>.agent.md and skills/<domain>/<name>/SKILL.md;
  keep portable name/description metadata and regenerate catalog indexes after changes.
- Preserve Python 3.11+, the standard-library core, loopback/local assets, comment
  persistence and stale-write protection. Export host permissions through adapters.
- website/ publishes canonical sources; docs/ is generated. Preserve public routes.
  Keep private content and generated bundles out of commits. No unsolicited messages.
- Use Herdr when available and usable; follow its [execution policy](toolkit/HERDR.md).
  Route complex judgment to strong models with high reasoning, bounded work to economical
  models, and mechanical coordination to native tools. Delegate useful independent ready
  slices by default within one shared capacity/budget; keep tabs and panes labelled.
- Keep shared scope and acceptance in the assignment; personal plans stay private. Preserve other writers' changes, coordinate overlapping
  scopes and shared contracts, and verify combined changes. Delegate only when supported,
  authorized and useful. Significant decisions and current knowledge stay at their owners.
- Before pausing, save result, revisions, evidence/limits, blockers, pending writes and
  one next action in the appropriate shared or private home. Do not merge or deploy without an explicit request.

## Verify the change

Use the [runbook](toolkit/REPOSITORY-WORKFLOW.md) and [CI](.github/workflows/checks.yml).
Run appropriate catalog/link, unittest, export and strict Docusaurus checks once; repeat
only after a relevant change, failure or unresolved concern. Distinguish actual evidence,
required acceptance, integration and deployment. Report unrun checks and material limits.
