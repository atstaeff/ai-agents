# Context recovery observation - 20 October 2026

This is a bounded local model/file observation, not a claim about live tracker integration
or an installed OpenCode/Claude environment. The [source artifacts](../../tests/fixtures/context-recovery-20261020.json)
contain task/decision revisions, produced code, handoff text and the task prompts with
machine-local paths normalized. Fixture approvals and commits belong to the isolated local
case; they are not customer approvals or commits in this repository.

## Setup

The updated [work-management skill](../../skills/work-management/SKILL.md) and
[shared recovery contract](../CONTEXT-RECOVERY.md) were supplied to fresh Work Mode agent
threads with no inherited conversation. Model choice was inherited from the host, not
independently version-pinned. Threads received the local assignment and raw project
artifacts, without the expected diagnosis or another thread's conversation. The coordinating
observer introduced the source revision between A and B and checked the resulting files.

The project used local Git, Python standard library, unittest and a Markdown task as the
explicitly designated planning home. External actions and further delegation were disabled
in the task. This controls source reasoning and handoff behavior; it does not exercise a
real Jira/GitHub connector, distributed lock or installed-host permission enforcement.

## Observed recovery

| Stage | Given source | Observed result |
| --- | --- | --- |
| Session A | Task r1; accepted ADR-0001 selected highest version, first occurrence on ties | Implemented only the assigned first increment, passed five tests and left the second decision open. Saved evidence/commits/next action in the existing task section. |
| Source change | Task r2 and accepted ADR-0002; ADR-0001 marked superseded | The observer authorized a local tie-policy change while leaving A's old handoff in place. The old substantive rationale remained in its ADR. |
| Fresh Session B | Current project sources and the same task; no A conversation or diagnosis | Identified the resolved dependency and replacement ADR, implemented version-first/timestamp-second behavior, updated seven tests and refreshed the existing handoff. |
| Observer | Six independent selection cases | Empty, unsorted, multi-document, timestamp-tie, exact-tie and version-precedence cases passed; original object identity and input non-mutation were preserved. |

The exact human preservation note and current human-owned scope remained intact. B linked
the new behavior to the accepted replacement and distinguished local verification from
acceptance, merge, deployment and impact. No competing planning record or external action
was observed. B's first startup attempt failed at model capacity before output; retry
completed without receiving A's conversation. This is reported rather than counted as a
successful first attempt or a latency measurement.

## Control cases

- **Unavailable designated tracker:** A separate fresh thread received a historical Jira
  snapshot with unresolved retry semantics and no current access. It returned an unsent
  Jira proposal, kept current approval/status unverified and created no local tracker or files.
- **Small direct edit:** A separate fresh thread corrected only the README heading.
  Observer file inspection confirmed no extra process record, ADR or other added file.

## Repository validation

Catalog/link validation retained 23 agents and 48 skills. The optional configuration
validator passed both GitHub and Jira examples. Seventy unittest checks passed in the
locked docs environment, including legacy filename support, conflicting defaults and
missing-file behavior. Skill validation, JavaScript syntax and strict MkDocs build passed.
These checks are separate from the observed model cases above.

## What remains unproven

One recovery example and two controls do not establish broad reliability or productivity.
No long-context stress test, cross-model comparison, user-installed OpenCode/Claude smoke
test, live tracker synchronization, API retry/claim integration or production rollout was
performed. Use the [pilot protocol](../../templates/customer-workspace/examples/context-recovery-pilot.md)
with the actual project to examine those boundaries before expanding autonomy.
