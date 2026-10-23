# One record per outcome

> Compatibility reference. New projects start at `AGENTS.md`. Personal execution plans
> belong in the configured private Second Brain; the structures below are optional
> existing-layout or shared-team examples, not requirements.


Use `workspace/work/<slug>.md` for larger local work without a board-owned assignment.
For tracked delivery, the project-designated work item (such as Jira or GitHub) owns the live plan;
follow the [operating model](OPERATING-MODEL.md) and the project's working agreement.
The dashboard below manages files; Project updates use your host's authorized tools.

Keep acceptance criteria, plan, tasks,
feedback, decisions and evidence together. Small fixes need no record. Avoid separate
proposal, spreadsheet and decision logs unless the project already requires them.

```sh
python3 tools/ai_toolkit.py work --workspace /path/to/project new customer-portal \
  --title "Ship the first customer portal flow" --kind software
python3 tools/ai_toolkit.py work --workspace /path/to/project feedback customer-portal \
  --text "Keep the existing sign-in flow."
python3 tools/ai_toolkit.py work --workspace /path/to/project task customer-portal T1 \
  --status done --evidence "Acceptance scenario verified with the relevant test."
python3 tools/ai_toolkit.py work --workspace /path/to/project csv customer-portal
python3 tools/ai_toolkit.py work --workspace /path/to/project archive customer-portal
```

Add task rows in your editor with stable `T1`, `T2`… IDs and statuses `open`,
`in_progress`, `blocked`, `done`. Preserve the four-column table. The API updates only
the selected row or appends feedback with a stable `F1` ID. Completion needs evidence.
Archiving requires all parsed tasks complete; check acceptance criteria and feedback too.

`serve --workspace /path/to/project` opens the local dashboard. Markdown is displayed
as text. HTTP writes require the current ETag; in-process writes are serialized and
the file is rechecked before replacement. This handles normal stale updates but is
not a distributed transaction system for uncoordinated editors or OneDrive.

Existing work records are optional legacy state, not the default personal planning home.
Decide per repository whether to commit existing work records. This toolkit ignores them by
default; explicitly track sanitized records if useful. Private notes never belong in
public repositories. Extract only reusable conclusions into existing documentation
or the private PARA vault for an appropriate personal task. Archive completed records and load history on demand.

## Existing records and the project root

`--workspace` is the project root; the store appends `workspace/work/` or
`workspace/archive/`. It creates no project config or second tracker automatically.
Existing `.ai/work/` or `.ai/archive/` content produces an actionable migration error
instead of an empty dashboard or a duplicate record. Stop writers and use:

```sh
python3 tools/ai_toolkit.py work --workspace /path/to/project migrate --dry-run
python3 tools/ai_toolkit.py work --workspace /path/to/project migrate
```

Both destinations are checked before moves. Existing targets and symlinks stop migration;
reconcile conflicting directories manually. Contents are unchanged, including feedback,
evidence and timestamps. Relative links may need review. Unknown `.ai` files, previews
and exported bundles are left alone. The empty `.ai/` parent is removed after migration;
`legacy_directory_remaining` reports unknown content left for deliberate review. See the
[migration runbook](REPOSITORY-WORKFLOW.md).
