# Shared working contract

Follow the current user and host instructions, then project constraints. Use English
for shared repository artifacts and the user's language in conversation. Reuse this
guidance and catalog metadata already in context; load selected skills and focused
references only when they help the current task.

Use AGENTS.md as the project entry and follow its declared local/web sources.
The [project concept](PROJECT-CONCEPT.md) explains ownership, coordination and publication.
Optional local workbench records still use workspace/ storage; local work, archives,
generated previews and exports remain outside knowledge publication.

## Choose the shortest complete path

Use the [lean operating model](OPERATING-MODEL.md) as the default. Keep
owner roles inline in PROJECT.md and working rules in CONTRIBUTING.md, or their
existing equivalents. Use that contribution guide to select relevant skills; load only
the required procedures and focused references. Add ideas, concepts, significant decisions and incident reviews only when actual work needs them.

For a clear, small task: inspect the relevant files, make the change, run appropriate
checks and report the result. No work record, catalog scan or agent handoff is required.

For larger work, read applicable AGENTS.md instructions, referenced project sources,
process and working agreement first. Read optional tooling configuration only when
the project declares it authoritative. See the [project concept](PROJECT-CONCEPT.md). Use the
designated work item and planning home, whether Jira, GitHub, another tracker or a file.
Do not create a second issue, local record or wiki plan for the same assignment.
If no system owns the assignment, use one `workspace/work/<slug>.md` with the
[work template](../templates/delivery/work-item.md). Reuse existing work for the same outcome.
If ownership is ambiguous, resolve it before creating shared records. If the designated
system is inaccessible, report the access gap and prepare an unsent update; do not
silently switch systems. Continue independent authorized work.
Keep the goal, acceptance criteria, short plan, tasks, feedback, decision references
and evidence together; preserve significant rationale at its designated decision home. Keep `docs/` available for its existing purpose, including GitHub Pages.

Reuse the project's technology. For new Python work prefer dataclasses, explicit
validation, uv and unittest; add Typer only for a CLI that merits it. For a modest new
web interface consider HTML, Flask/Jinja or HTMX. Preserve an established stack.

## Implement and verify

If the user, project or selected planning flow requires plan review, prepare the
concrete plan first. Use available Plannotator review, or explicit review in the current
conversation if unavailable. Preserve feedback, revise after requested changes and wait
for actual approval of the current revision before Build. Record the approval in the
existing planning home. A changed scope or consequential design reopens review; routine
details within approved scope do not. See [plan review](PLAN-REVIEW.md) for setup and
model handoff. Approval does not grant merge, deployment or broader tool permissions.

1. Define observable acceptance criteria. Resolve routine reversible choices
   independently; ask only when missing information changes a consequential decision
   or an action needs authorization not already given.
2. Implement the smallest complete increment. Delegate only when the host supports
   and authorizes it and the benefit exceeds coordination cost. Give bounded goals,
   context pointers, allowed files, acceptance criteria and expected evidence. Avoid
   concurrent writers to the same file; inspect and integrate returned work.
3. Check affected acceptance behavior and important failure cases. Derive expected
   results from requirements, consumer contracts or reproduced defects. Run the
   application at the relevant boundary; a build alone does not prove a user journey.
   Record actual results and limits; never claim an unrun check passed or weaken a
   check to obtain success. Repeat or broaden testing only for a new change, failure
   or unresolved concern.
4. Before updating a record, compare the current file with the version read. Preserve
   intervening edits and human comments verbatim; retry or resolve conflicts. Update
   task states, feedback disposition and consequential decisions with reasons.
5. Report the outcome, relevant files, actual checks and remaining limits. Never
   invent capabilities, sessions, background work or successful publication.

## Make verification executable

Read the project’s setup, start and check commands before substantial implementation.
Reuse a reproducible environment and existing checks. Identify missing dependencies,
fixtures, credentials or tools early; continue independent work and name blocked criteria.
For a defect, reproduce the behavior and add a focused regression check where useful.
For interfaces/APIs, exercise the consumer-visible flow and material failure/recovery
states. Apply existing CI checks before review; encode recurring deterministic rules
in tooling when that prevents repeated mistakes.

Select one bounded increment before increasing concurrency. A different model or a
second reviewer is useful only when it improves the result; carry the same requirements
and approval evidence across handoffs. Verify the integrated result after delegated work.
Use [portability guidance](PORTABILITY.md) when changing hosts, discovery paths or adapters.

## Resume from current shared sources

For larger work or a session/model switch, use the [context recovery contract](CONTEXT-RECOVERY.md).
Read current assignment and relevant decisions, contracts and code; compare them with the
last bounded handoff. Keep significant rationale at its designated decision home when it
arises. A newer comment does not automatically revoke an accepted decision; resolve the
responsible authority and preserve the history. Continue independent authorized work
while a consequential conflict blocks dependent steps.

Before switching, save source revisions, relevant commits, criterion-linked evidence,
open questions, unsaved work, pending writes and the next action at the existing planning
home. Reassess affected approvals/checks after material changes. Reread before updates;
inspect existing effects after API timeouts rather than blindly repeating them.
Do not create a second task store or carry an entire transcript as mandatory context.

## Finish with reusable knowledge

Update affected current knowledge from verified behavior. Keep completed plans at their
existing work home as history; preserve accepted decisions and replacement links. Before
replacing a derived plan, retain its still-important rationale. Mark historical concepts
and obsolete handoffs explicitly. See the [retention rules](PROJECT-KNOWLEDGE.md#choose-what-stays-current-and-what-becomes-history).

For local work records, archive in `workspace/archive/` after acceptance criteria are verified
and unresolved feedback is reviewed. Close tracked work according to the project agreement. Keep historical records out of routine context. Link reusable knowledge
into its existing customer documentation; use a private vault only when appropriate
to the requested personal task. Avoid duplicate task lists. CSV is
an optional generated export.

Keep secrets, vault paths and personal notes outside public repositories. Owners choose
whether to commit work records. Messages, publication, merging and destructive
reorganization require authorization appropriate to the action.

Use PARA: Projects for finite outcomes, Areas for ongoing responsibilities, Resources
for reusable knowledge and Archive for inactive material. Follow existing vault names
and conventions. Preserve properties, aliases, backlinks and human wording; verify
links after filesystem moves.
