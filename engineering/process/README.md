# Engineering process

This repository uses Markdown procedures selected by the work at hand. Start with
[AGENTS.md](../../AGENTS.md) and the assignment; load only the relevant step and source
sections. The numbers below aid navigation, not execution state or mandatory gates.
Add, combine, reorder or remove steps when the adopted project process changes.

| Situation | Procedure | Evidence at its existing home |
| --- | --- | --- |
| Unclear outcome, scope or acceptance | [01 Clarify](01-clarify.md) | Bounded outcome and observable acceptance |
| Consequential design or coordination | [02 Plan](02-plan.md) | Approach, contracts and ownership |
| Authorized implementation | [03 Build](03-build.md) | Reviewable increment |
| Check behavior and readiness | [04 Verify](04-verify.md) | Results and limitations on the combined revision |
| Integration, completion or handoff | [05 Integrate and retain](05-integrate-retain.md) | Authorized result, current knowledge and retained reasons |

A clear correction can proceed from affected source to build and verification. It needs
no process record or extra agent. Analysis-only assignments stay scoped. The existing
issue/current PR owns shared scope, acceptance and coordination; process pages describe
reusable procedure, not progress. Revisit an earlier step when new evidence requires it.

## Rules and source ownership

[Session rules](../../toolkit/SESSION-RULES.md) own startup, autonomous coordination and
cross-cutting execution rules. [Herdr](../../toolkit/HERDR.md) owns native readiness and
layout; [orchestration](../../toolkit/ORCHESTRATION.md) owns specialist packets and integration.
Apply those rules; do not duplicate them in every step. Use [recovery](../../toolkit/CONTEXT-RECOVERY.md)
for interrupted or contradictory state.

For this repository, [PROJECT.md](../../PROJECT.md) owns facts and work homes,
[CONTRIBUTING.md](../../CONTRIBUTING.md) owns contribution requirements and tool references,
and the [working agreement](../../knowledge/working-agreement.md) owns action boundaries.
[Skills](../../skills/README.md) supply technique, [agents](../../agents/README.md) define roles,
and [knowledge](../../knowledge/README.md) retains current facts and decision history.
These locations are choices, not a required directory hierarchy.

For another project, use its adopted process and permissions. The
[Markdown-first starter](../../templates/markdown-project/README.md) shows how to adapt
paths and steps without a workspace manifest. The [operating model](../../toolkit/OPERATING-MODEL.md)
explains responsibilities and value; this directory owns detailed phase procedures.
