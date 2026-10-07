---
name: "work-management"
description: "Plan and execute a larger task with one compact Markdown record containing acceptance criteria, tasks, feedback, decisions and evidence."
---

# Work Management

1. Inspect relevant instructions and existing work. A small edit uses the conversation
   and appropriate checks; create no process file automatically.
2. For larger work, reuse or create one `.ai/work/<slug>.md` per outcome using the
   template or CLI. Sessions and agents share it.
3. Define the goal, constraints, observable acceptance criteria and a short ordered plan.
   Use stable task IDs with states `open`, `in_progress`, `blocked` and `done`.
4. Update evidence as work happens. Implementation progress and acceptance verification
   are separate: a changed file alone does not prove resulting behavior.
5. Preserve human feedback verbatim with stable IDs and an explicit disposition. Record
   only consequential decisions and their reasons.
6. Archive in `.ai/archive/` when the outcome is verified and unresolved feedback is
   reviewed. Link reusable knowledge into existing documentation or the private vault.

## Safe updates and handoffs

- Read the current record and relevant files; load historical work only when needed.
  Before rewriting, compare against the version read and preserve intervening edits.
  Retry or resolve conflicts; never replace a record from a stale session snapshot.
- The dashboard edits the same Markdown file using ETag checks. Filesystem updates
  require the same reread and comparison discipline.
- A completed task needs evidence. If a required check cannot run, record why, the
  affected criterion and the next action. Keep verification outstanding unless other
  adequate evidence establishes it; never archive an unverified outcome.
- Keep shared rules in the toolkit and local constraints in project `AGENTS.md`.
  Keep `docs/` for its existing purpose. CSV is generated, not maintained separately.
- Follow repository privacy rules. Keep private vault notes and configuration out of
  public records. Report the outcome, actual checks and material limits concisely.
