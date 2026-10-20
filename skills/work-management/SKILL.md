---
name: "work-management"
description: "Maintain the plan, acceptance criteria, human feedback and verification for a larger assignment at the project-designated home, such as Jira, GitHub or one local Markdown record."
---

# Work Management

1. Inspect the assignment, project rules and existing work. Complete a clear small edit
   directly with appropriate checks; create no process file automatically.
2. Read the declared project config (normally `workspace/workspace.yml`) and working
   agreement. Choose the designated planning home: Jira ticket,
   GitHub issue or another work item. Only without an assigned system, reuse or create
   one `.ai/work/<slug>.md` per larger outcome. Never create a duplicate tracker item,
   local record, task CSV or wiki plan. If ownership is unclear, resolve it before writing.
3. State the user outcome, scope exclusions, observable acceptance and first verifiable
   increment. Reuse the home's task format; local records use stable T1-style IDs and
   `open`, `in_progress`, `blocked`, `done` states.
4. When required, follow [plan review](../../toolkit/PLAN-REVIEW.md). Preserve the current
   revision, actual approval and attached feedback. A session/model change carries that
   handoff forward; a consequential scope/design change returns to review.
5. Update after material progress, a decision or a blocker. Keep one bounded current
   summary; preserve human comments verbatim and track their disposition. Link detailed
   evidence rather than posting tool logs or every intermediate thought.
6. Distinguish implementation, verification, acceptance, merge, deployment and impact.
   Close board work by its working agreement. Archive a local record after its outcome
   is verified and unresolved feedback is reviewed. Update affected customer knowledge
   at its canonical home; private PARA notes require an explicitly appropriate task.

## Unavailable tools

The project’s source of truth remains authoritative even if this host lacks access.
State the missing capability, prepare an unsent update and continue independent work.
Do not invent current status, approval, assignment, synchronization or a fallback tracker.

## Safe updates and handoffs

- On start or resume, compare the current assignment, relevant decisions, contracts and
  repository revisions with the previous handoff before following its next action.
  Follow the [context recovery contract](../../toolkit/CONTEXT-RECOVERY.md) for larger
  work or a session/model switch; load only the sources relevant to the assignment.
- Record significant decisions when they arise, with alternatives, reasons, status,
  source and responsible role. A proposed replacement does not revoke an accepted ADR.
  Flag consequential conflicts instead of silently preferring the newest text or code.
- Reread mutable state before writing. Compare it with the version read, preserve
  intervening edits and retry or resolve conflicts. Use API version/precondition checks
  where available; a local reread alone is not an atomic remote lock.
- The local dashboard uses ETags for the same Markdown record. Filesystem clients
  must also preserve intervening edits and human feedback.
- Carry the outcome, planning-home revision, each relevant repository commit, applicable
  decisions, required approval, criterion-linked evidence, unsaved work, pending writes
  and next action in one bounded summary. Avoid copying the entire conversation.
- Reassess affected plans, approvals and checks after material scope, decision, contract
  or code changes. An old green check does not prove a new revision. After API timeouts,
  inspect existing effects before retrying; never claim an atomic cross-system update.
- Follow the project's blocked mapping without losing the underlying flow position or
  WIP accounting. Closed as cancelled, duplicate or not implemented is not delivered.
- If a required check cannot run, name the affected criterion, reason and next action.
  Keep verification outstanding unless other adequate evidence establishes it.
- Keep customer facts with the customer, `docs/` available for its existing purpose,
  and private vault paths and secrets out of public records.
