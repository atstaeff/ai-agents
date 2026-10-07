# Shared working contract

Follow the current user and host instructions, then project constraints. Use English
for shared repository artifacts and the user's language in conversation. Reuse this
guidance and catalog metadata already in context; load selected skills and focused
references only when they help the current task.

## Choose the shortest complete path

For a clear, small task: inspect the relevant files, make the change, run appropriate
checks and report the result. No work record, catalog scan or agent handoff is required.

For larger work, keep one `.ai/work/<slug>.md` using the
[work template](../templates/work-item.md). Reuse an existing record for the same outcome.
Keep the goal, acceptance criteria, short plan, tasks, feedback, decisions and evidence
together. Keep `docs/` available for its existing purpose, including GitHub Pages.

Reuse the project's technology. For new Python work prefer dataclasses, explicit
validation, uv and unittest; add Typer only for a CLI that merits it. For a modest new
web interface consider HTML, Flask/Jinja or HTMX. Preserve an established stack.

## Implement and verify

1. Define observable acceptance criteria. Resolve routine reversible choices
   independently; ask only when missing information changes a consequential decision
   or an action needs authorization not already given.
2. Implement the smallest complete increment. Delegate only when the host supports
   and authorizes it and the benefit exceeds coordination cost. Give bounded goals,
   context pointers, allowed files, acceptance criteria and expected evidence. Avoid
   concurrent writers to the same file; inspect and integrate returned work.
3. Check affected behavior and important failure cases. Record actual results and
   limits; never claim an unrun check passed. Repeat or broaden testing only for a
   new change, failure or unresolved concern.
4. Before updating a record, compare the current file with the version read. Preserve
   intervening edits and human comments verbatim; retry or resolve conflicts. Update
   task states, feedback disposition and consequential decisions with reasons.
5. Report the outcome, relevant files, actual checks and remaining limits. Never
   invent capabilities, sessions, background work or successful publication.

## Finish with reusable knowledge

Archive in `.ai/archive/` after acceptance criteria are verified and unresolved feedback
is reviewed. Keep historical records out of routine context. Link reusable knowledge
into existing documentation or the private vault; avoid duplicate task lists. CSV is
an optional generated export.

Keep secrets, vault paths and personal notes outside public repositories. Owners choose
whether to commit work records. Messages, publication, merging and destructive
reorganization require authorization appropriate to the action.

Use PARA: Projects for finite outcomes, Areas for ongoing responsibilities, Resources
for reusable knowledge and Archive for inactive material. Follow existing vault names
and conventions. Preserve properties, aliases, backlinks and human wording; verify
links after filesystem moves.
