# Asynchronous progress examples

Use the existing assignment and source links. These are hypothetical shapes, not status
facts to copy. Include only what changes the audience's understanding or next action.
Do not create a second tracker, schedule a meeting or send a message by default.

## For the product or acceptance owner

State the user-visible outcome, evidence and decision needed:

> The save flow is implemented at [revision]. The success and denied-access scenarios
> passed in [environment/check]. Recovery after a timed-out write remains unverified.
> [Owner] needs to confirm the proposed recovery behavior in [assignment]. Next:
> exercise that case before requesting acceptance.

Distinguish implemented, verified, accepted, integrated and deployed. Include observed
benefit only when it was actually measured. Retain original stakeholder feedback and
link its disposition; do not silently turn an unanswered proposal into a decision.

## For an implementer or integrator

Provide the artifact, exact source/base revision, writable boundary and check evidence:

> [Change/branch] updates [contract/files]. [Commands] passed at [revision]. Integration
> depends on [upstream revision]; its error payload has changed since the brief.
> [Integrator] will reconcile that contract, then rerun [affected check]. No deployment
> has occurred.

If another writer overlaps, identify the owner and stop conflicting writes until the
claim/handover is resolved. Individual branch checks do not establish a combined result.

## For a blocked assignment or session handoff

Record current result, evidence/limits, blocker/owner, pending writes and one next action:

> [Revision] contains [completed slice]. [Check] failed with [relevant evidence]. Cloud
> credentials are unavailable, so the live plan was not run. [Owner] can resolve access.
> The external update timed out; its effect is unknown. Next: inspect [work home/run]
> before retrying the write.

Keep personal working steps and private source paths in their configured private home.
A shared handoff points to authoritative sources so the next worker can check for
intervening changes. Escalate a decision with alternatives and consequences only when
it exceeds the current scope or changes an accepted constraint.

Use [communication](../../../knowledge/communication/SKILL.md) for the audience's wording,
[project management](../../project-management/SKILL.md) for a demonstrated flow problem,
or [task orchestration](../../../../agents/delivery/task-orchestrator.agent.md) for a
useful bounded handoff. Another session is not required for a progress update.
