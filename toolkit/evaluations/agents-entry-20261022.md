# AGENTS.md entry: bounded model observations

Observed on 2026-10-22 in three fresh model threads using disposable local projects.
The threads received the repository-contribution skill path and a task, without the
expected answer or this assessment. They had separate fixture directories and no
authorization to publish or modify the AI Agents repository. Raw fixture/output
snapshots and instruction SHA-256 hashes are in
[the observation artifact](../../tests/fixtures/agents-entry-20261022.json).

| Case | Observed result | Root verification |
| --- | --- | --- |
| Account-scoped upload feature alongside another writer | Read accepted ADR, returned the exact account/attempt tuple, added account-isolation/value-preservation checks, retained the human note and saved evidence/handoff in the original TASK.md | Three tests passed; shared contract and ADR bytes preserved |
| Required web process unavailable | Named the exact required URL and absent fallback; identified the accepted-contract conflict, left implementation unchanged and saved the blocker/next action | Original implementation/tests/ADR/contract unchanged; existing baseline test failure reproduced and reported |
| Small typo correction | Corrected only the requested README word and verified exact content; preserved pre-existing instruction changes | README matched the intended result; other source/work files unchanged |

The feature trial used local work ownership declared in PROJECT.md and TASK.md; it did
not create a second tracker or require a YAML manifest. The unavailable-source case
explicitly withheld web/tracker capabilities as scenario input: it was no live outage,
authentication or remote-page retrieval test. The small-edit case had already-loaded
instructions and needed no separate work record.

These observations support bounded source routing, missing-source handling, preservation
and direct small-task behavior in these local fixtures. They do not establish throughput,
large-team performance, distributed locking, independent human acceptance, installed-host
discovery, cross-model reliability or actual web/issue integration. Parallel ownership
was represented by a preserved file and an explicit other owner; no simultaneous writer
race was exercised. The optional workbench HTTP/export/migration replay is separate
mechanical evidence.

Run the cold-session and real-host checks on an actual adopted project before making
claims about collaboration efficiency. Keep observation artifacts historical; do not
rewrite them to match later instructions.
