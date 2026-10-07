---
name: "work-management"
description: "Plan and execute a larger task with one compact Markdown record containing acceptance criteria, tasks, feedback, decisions and evidence."
---

# Work Management

1. Inspect project instructions and existing work. For a small edit, use the current conversation and existing tests; do not create process files automatically.
2. For larger work use `.ai/work/<slug>.md`, created from the toolkit template or CLI. Keep one record per outcome, not one per session or agent.
3. Write the goal, constraints and observable acceptance criteria. Make a short ordered plan and task rows with stable IDs.
4. Keep tasks `open`, `in_progress`, `blocked` or `done`. A completed task needs evidence: a result, changed file, check or an explicit manual observation.
5. Append human feedback with stable IDs. Preserve original wording and record its disposition; do not silently remove comments when replanning.
6. Record only consequential decisions with a reason. Update evidence as work happens and distinguish unrun checks from passing checks.
7. When the outcome is verified, move the record to `.ai/archive/`. Extract only reusable knowledge into the existing project documentation or private vault.

## Storage and handoffs

- Keep shared rules in the toolkit. Project `AGENTS.md` contains only project-specific constraints and verification commands.
- Keep `docs/` available for its existing purpose, including GitHub Pages. Do not turn it into an agent scratch folder.
- CSV is an export from the task table, not a second manually maintained task list.
- Read the current record and relevant files on a handoff; load historical work only when needed.
- Respect repository privacy rules. Never copy private vault notes into a public work record.
- A dashboard updates the same Markdown file. Use its ETag/concurrency check or reread the file before applying an update from another session.
- Before any rewrite, compare the current file with the version you read. Preserve intervening comments and changes, then retry or resolve the conflict explicitly. Never replace the whole record from an old session snapshot.
- Distinguish implementing a task from verifying its acceptance criterion. A changed file can establish implementation progress; verification needs an appropriate check or explicit observation.
- If a required check cannot run, record why, the affected acceptance criterion and the next action. Keep verification outstanding unless other adequate evidence establishes the criterion; do not archive an unverified outcome.

## Completion

Confirm acceptance criteria with evidence, preserve unresolved feedback, identify remaining limits and give the user a concise result.
