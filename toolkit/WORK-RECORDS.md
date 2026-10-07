# One record per outcome

Use `.ai/work/<slug>.md` for larger work. Keep acceptance criteria, plan, tasks,
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

Decide per repository whether to commit work records. This toolkit ignores them by
default; explicitly track sanitized records if useful. Private notes never belong in
public repositories. Extract only reusable conclusions into existing documentation
or the private PARA vault. Archive completed records and load history on demand.
