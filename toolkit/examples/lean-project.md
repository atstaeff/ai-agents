# A lean project from idea to the next session

This is a fictional walkthrough, not an implemented product, actual approval or passing
test report. It shows where information belongs and what another session should recover.
Use the [lean project starter](../../templates/project-starter/README.md) and
[operating model](../OPERATING-MODEL.md); skip steps that add no useful information.

## 1. Establish the project once

A small team maintains an existing document API and SQL database. Its next outcome is
fewer duplicate documents when an upload is retried. The actual setup/check commands
already live in the project's contributing guide.

The team merges the agent entry and fills PROJECT.md with that outcome, customer
isolation boundaries, and the owner who accepts product/technical choices. AGENTS.md
links those facts, the adopted process, existing Jira work, GitHub reviews and repository
knowledge/decision homes. Working rules and skill selection stay in CONTRIBUTING.md or
the explicitly adopted central process. No YAML is needed. No second GitHub issue or
local plan is created for the Jira assignment.

## 2. Capture an opportunity

In the existing ideas intake, IDEA-001 says:

> Retries may create duplicate documents. Explore whether attempt identity can reduce
> duplicate references. Evidence: reported cases; actual baseline is not established.

The idea has a short disposition and a link to exploration. It has no delivery tasks or
status copied from Jira. It could be declined without creating a concept or implementation.

## 3. Clarify one meaningful uncertainty

Here retries touch identity and customer isolation, so a small concept is useful.
CON-001 defines the intended behavior and acceptance boundaries:

- The same authenticated customer and attempt identity should reuse one document reference.
- Identical bytes from another customer must reveal no document existence/reference.
- A deliberate new attempt may create a new document.
- Retry retention/expiry semantics need the product owner's decision before dependent work.

The concept owns that feature contract and is declared living. It links applicable
accepted decisions and Jira work. A second knowledge page describing the same contract
is unnecessary. The agent searches existing decisions instead of assuming a missing link
means there is no prior constraint.

## 4. Preserve the consequential choice

The technical owner evaluates customer-scoped attempt identity against a global payload
hash. DR-001 records the starting situation, alternatives/evidence, chosen response and
consequences. In a real project it stays proposed until that owner actually accepts it.
An illustration here grants no implementation authorization.

The rationale includes preserving customer isolation and distinguishing a repeated attempt
from payload equality. SQL uniqueness/concurrency and recovery behavior require checks.
If an accepted existing ADR conflicts, resolve that scope/authority conflict first;
proposing CON-001 or DR-001 cannot silently supersede it.

## 5. Plan and build in one assignment

Jira UPLOAD-17 owns acceptance, short plan, status, feedback and the bounded handoff.
It links CON-001, the decision and the code repository. The next increment covers attempt
identity using the existing API/database; no workload evidence currently justifies new
services or a queue. One contributor session is enough to start.

The plan identifies affected interfaces, persistence and criterion-derived checks:
same-customer retry, cross-customer isolation, new attempts, simultaneous requests,
interruption/recovery and agreed retention boundaries. Unknown retention semantics block
only the dependent part; independent authorized investigation can continue.

A specialist is optional for a concrete concurrency uncertainty. Its scope, source
revisions, expected evidence and integration owner must be explicit. No session can claim
successful external synchronization when Jira is inaccessible: prepare an unsent update
and preserve the existing assignment's authority.

## 6. Verify, integrate and retain

In real delivery, the agent records actual checks against the changed revision, reviewer
feedback and gaps. Passing a build alone does not establish these behaviors. Required
review and authorized integration determine Engineering Done; deployment and measured
reduction in duplicates need separate evidence.

At completion:

| Artifact | Result |
| --- | --- |
| IDEA-001 | Disposition and link to the accepted outcome, or an honest partial/deferred result |
| CON-001 | The maintained intended contract; implementation state and evidence recorded separately |
| DR-001 | Actual accepted rationale retained, or proposed/rejected status preserved |
| UPLOAD-17 | Closed only at the agreed completion point; plan/tasks remain historical there |
| PR/checks | Actual revision, findings/results and durable summary if temporary logs expire |
| Project entry | Link CON-001 and the applicable decision; avoid a duplicate contract |

A runbook is added only if operators need a repeatable recovery procedure. A significant
incident later gets a factual review and owned follow-up; an ordinary defect can stay in
its issue. Neither every ticket nor every test failure needs a new document.

## 7. Resume and change safely

Before a pause, UPLOAD-17 holds result, current revisions, actual evidence, unresolved
retention decision, pending writes and one next action. An actual host/session link may
help navigation; the next worker does not depend on the old chat being accessible.

The next session reads UPLOAD-17 and new feedback, PROJECT.md, CONTRIBUTING.md, CON-001, applicable
decisions and relevant code/checks. It checks the handoff against those current sources.
An old plan proposing a global hash is historical context, not authority to bypass DR-001.
If source access is missing, state the gap; do not invent current status or approval.

For a later agreed change, update the living contract, open/use the next assigned work
item and preserve any significant new rationale in a related decision. Keep the old
execution plan historical. Tiny documentation corrections still go directly to editing
and relevant checks, with no obligatory concept or local work record.

## What this walkthrough does not prove

This is a coherent example of ownership and retention, not a fresh-model evaluation,
load test or claim of staffing savings. Validate the adopted process on one real authorized
assignment, including a session interruption, before adding automation or concurrency.
