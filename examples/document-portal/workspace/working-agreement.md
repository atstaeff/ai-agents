---
title: Working agreement
description: One assignment, one owner, proportionate checks and customer-owned knowledge.
---

> Compatibility reference. New projects start at `AGENTS.md`. Personal execution plans
> belong in the configured private Second Brain; the structures below are optional
> existing-layout or shared-team examples, not requirements.


# Working agreement

Example policy to review and adopt with the customer before enabling automation.
This worked configuration uses the GitHub locations in the [project configuration](workspace.yml).
For another tracker/wiki, adapt locations, statuses, permitted fields and channels first;
the shared process does not mandate GitHub or a mirror issue.

## Ready and ownership

A Ready issue has an outcome, observable acceptance criteria, relevant links, an iteration
and an accountable assignee. Ready is a condition for starting work, not an extra required
flow state. The Product Owner chooses priority and scope. A runner takes only ready
assignments explicitly assigned to its customer-authorized identity.

Use one active issue per runner. Work in one branch per issue and avoid concurrent writers
to the same files. Assignment and status are coordination signals; multiple runners need
a shared claim mechanism rather than relying on an assignee field as a lock.

## Deliver an increment

1. Read the issue, relevant code and selected workspace pages. Reuse already loaded guidance.
2. Keep the plan in the issue's designated AI section. For planned delivery in this example,
   the Technical Owner reviews the concrete revision in local Plannotator before Build.
   Address requested changes and resubmit; record actual approval and notes in the issue.
3. Implement the smallest complete increment within the approved scope.
4. Run relevant checks and prepare a linked PR. Explain missing verification explicitly.
5. Move to Review when the result is reviewable. Done requires acceptance evidence, required
   review and the customer's agreed completion point. In this example, a human-approved merge.

Use the [plan review example](../examples/plan-review.md). While approval or a consequential
answer is pending, mark the item as blocked with reason, owner and resume condition;
preserve its underlying flow position and WIP. Cancellation, timeout or tool failure does
not authorize implementation. If the
review UI is unavailable, require explicit review through the existing issue or conversation.
Reopen review for material scope or design changes. Small direct tasks need a gate only
when the user or customer requires one. Plan approval does not accept an ADR, merge or deploy.

## Action scope

After this policy is adopted, the worker may edit its branch, prepare draft PRs, update
its own issue status section and ask bounded questions in that issue. It may notify only
the verified role contact listed in [stakeholders](stakeholders.md) through that channel.
Merging, deployment, deletion and changes to access rights require separate authorization.

## Questions and updates

Bundle related questions with a recommendation, impact and needed decision. Route business
questions to the Product Owner and design questions to the Technical Owner. Record a blocker
for unanswered consequential questions; continue independent authorized work.

Reread the issue before updates. Preserve human-owned sections and comments; update only
the bounded AI section. On the first assignment, append the `ai:status:start` and
`ai:status:end` section shown in the issue example if it is absent. Keep its plan, next
action and evidence there. Detect intervening edits and retry rather than overwrite them.
Post a new comment only for a question, material blocker or reviewable result.

## Knowledge and completion

The issue records the live plan; the PR records implementation and checks. Update current
process knowledge when accepted behavior changes. Draft significant decisions when they
arise, while alternatives and feedback are available. Record reasons, consequences and
the responsible decision maker.
The authorized decision maker accepts or rejects the decision; implementation evidence stays
in the PR. Preserve an accepted decision's rationale. To change the substantive decision,
create a new ADR with a supersedes relation and mark the old ADR superseded. Reviewed status,
replacement links and factual corrections may change; they do not silently rewrite history.
A proposed replacement does not revoke an accepted decision. Code records observed behavior,
not authorization to depart from accepted architecture. Resolve consequential conflicts
before dependent work; continue independent authorized work.

## Resume and hand off

Before following an old plan, read current assignment/feedback, applicable decisions,
contracts and relevant code. Compare with the [bounded handoff](handoff.md). Save source
revisions, each relevant repo commit, actual criterion-linked evidence, approval references,
open questions, unsaved work, pending writes and next action after material progress or
before a session/model switch. Use the existing issue section, not another live plan.
Material changes reopen affected planning, approval and checks; old evidence proves only
its tested revision. Preserve human content and inspect existing effects after API timeouts
before retrying. Local recovery data is not a second source of truth.

The example flow is Todo, In Progress, In Review, Done; blocked is an additional property.
Cancelled, duplicate and not-implemented closures do not count as delivered. Engineering
Done for code requires the agreed checks, required review and authorized integration.
Deployment and measured impact remain separate facts. Closed issue or host success alone
is insufficient. A different existing board mapping is allowed when equally explicit.

Use the [cold-session pilot](../examples/context-recovery-pilot.md) before claiming recovery
works in the chosen host. This template implements no tracker connector or distributed claim.

At iteration close prepare one short report from linked outcomes, open work and feedback.
Distinguish delivered, reviewed, deployed and measured results. Link detailed evidence.
A documentation site and graph are generated views; maintain the underlying Markdown and links.
Closeout links decisions already recorded and drafts only missing significant decisions.
Do not turn every completed issue or iteration report into an ADR. Rebuild the knowledge
index and map from relations before building Docusaurus; read workspace sources for AI work.
