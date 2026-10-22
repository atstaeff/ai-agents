# Repository workflow pilot — 22 October 2026

The user requested a configured AI Agents workspace, removal of the old working
directory and a concrete replay. The pilot exercised actual CLI, exporter, HTTP server
and storage operations in generated fixtures. It made no tracker writes and used no model.

Reproduce with `python3 tools/workspace_smoke.py`. Source baseline:
`71733747354a43772877ca53778af8ee4a6717b8` plus the workflow-pilot changes under review.
Python 3.12, uv and Node were available. OpenCode and Claude were not installed.
Each execution writes its own JSON report; private local paths are unnecessary here.

## Observed results

| Stage | Operation and observed result |
| --- | --- |
| Plan | CLI created a record under `workspace/work/`; plan and three tasks saved |
| Dashboard | Loopback HTTP served HTML, CSS, JavaScript, API contract and 71 catalog entries |
| Feedback | Marked fixture comment appended and preserved |
| Conflicts | Stale PATCH returned HTTP 412; feedback without If-Match returned HTTP 428 |
| Build | Real OpenCode export contained 23 agents and 48 skills and selected `joerg` |
| Repeat/edit protection | Unchanged export changed zero files; edited generated profile was preserved and export rejected it |
| Handoff | A new store recovered the plan, feedback, completed criteria and remaining action from disk |
| Closeout | CLI archived completed work at `workspace/archive/workflow-pilot.md` |
| Migration | Dry-run preserved data; migration retained record bytes, removed the empty parent and safely repeated |

The real catalog was also exported into this checkout's ignored `workspace/exports/opencode/`
for local use. The configuration and runbook name actual repository locations and checks;
no GitHub Project or field IDs were invented. The pilot is included in CI and the
repository quality gates for future replay.

## Limits and next check

This demonstrates local storage, exports and workflow boundaries. It does not establish
productivity improvement, independent human approval, effective installed-host permission,
multi-process locking, model quality, live Jira/GitHub operation or production deployment.
HTTP resource checks are not visual browser acceptance. Fixture feedback does not mean
a human reviewed a plan.

Run the next real assignment in the user's installed OpenCode environment with its model
and authorized repository tools. Verify profile discovery, the actual planning home and
effective permissions. Keep that evidence on its own assignment; do not turn this fixture
into a parallel tracker.
