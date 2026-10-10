# Shared working contract

Follow the current user and host instructions, then project constraints. Use English
for shared repository artifacts and the user's language in conversation. Reuse this
guidance and catalog metadata already in context; load selected skills and focused
references only when they help the current task.

## Choose the shortest complete path

For a clear, small task: inspect the relevant files, make the change, run appropriate
checks and report the result. No work record, catalog scan or agent handoff is required.

For larger work, read the project’s tooling config (normally `workspace/project.yaml`,
or the equivalent linked from `AGENTS.md`) and working agreement first. See the
[project configuration contract](PROJECT-CONFIG.md). Use the
designated work item and planning home, whether Jira, GitHub, another tracker or a file.
Do not create a second issue, local record or wiki plan for the same assignment.
If no system owns the assignment, use one `.ai/work/<slug>.md` with the
[work template](../templates/work-item.md). Reuse existing work for the same outcome.
If ownership is ambiguous, resolve it before creating shared records. If the designated
system is inaccessible, report the access gap and prepare an unsent update; do not
silently switch systems. Continue independent authorized work.
Keep the goal, acceptance criteria, short plan, tasks, feedback, decisions and evidence
together. Keep `docs/` available for its existing purpose, including GitHub Pages.

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

## Finish with reusable knowledge

For local work records, archive in `.ai/archive/` after acceptance criteria are verified
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
