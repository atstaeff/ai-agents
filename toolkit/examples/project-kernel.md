# AGENTS.md project kernel: a worked example

The kernel is an instruction entry linking owned sources. This fictional customer portal
example shows a complete route; substitute real files, URLs, roles and checks. It asserts
no actual project access, approval, implementation or published result.

## AGENTS.md entry

```markdown
# Customer Portal collaboration contract

## Read these sources

- Vision and goals: product/overview.md#vision-and-goals
- Stakeholders and decision rights: team/roles.md
- Scope and constraints: product/overview.md#scope
- Process and checks: CONTRIBUTING.md
- Work: the assigned issue in our actual project tracker
- Review: the linked pull request in our actual repository
- Current knowledge: knowledge/README.md
- Significant decisions: knowledge/decisions/README.md

Read the source bodies and affected contracts before substantial changes.
Follow CONTRIBUTING.md; load only relevant skill bodies and references.

## Coordinate work

Keep one live plan at the assigned work item. Identify the accountable human,
active writer, bounded scope, dependencies and integration owner.
Use separate branches/working directories. Agree shared contracts and coordinate
any overlapping scopes through the project's adopted claim/handover mechanism.
Preserve other work and reread shared records before updates.

## Deliver, verify and retain

Proceed with routine reversible work in scope. Resolve consequential conflicts
with the responsible owner. Use actual project commands and verify behavior
against observable acceptance. Verify the combined result after integration.
Record evidence against the tested revision and follow required review/action policy.
Update affected current knowledge and preserve significant decision reasons.
Before pausing, save result, revisions, evidence/limits, blockers, pending writes
and one concrete next action in the same assignment.
```

The conventional filename is AGENTS.md. Other document names and directories are choices.
Use the [remote-documentation variant](../../templates/agent-instructions/remote-docs/AGENTS.md)
when a web source owns the process or facts; pin the adopted policy revision/version.
A path or URL neither grants access nor guarantees loading; explicitly read its content.

## Referenced project content

| Source | Smallest useful content |
| --- | --- |
| Vision and goals | Users/problem, desired future, current outcome and success signal |
| Stakeholders | Affected groups, priority owner, technical decision owner, acceptance/review roles |
| Scope | Included system responsibility, exclusions and material constraints |
| Process | Clarify/plan/build/verify/integrate, tools/checks, relevant skills and action boundaries |
| Work item | Outcome/criteria, current plan, owner/writer scope, dependencies, feedback and handoff |
| Knowledge index | Links to current contracts, architecture, operations and relevant decision records |

These sections may share a file. PROJECT.md and CONTRIBUTING.md in the
[starter](../../templates/project-starter/README.md) are adaptable defaults.

## Knowledge and decisions in practice

For a change that makes repeated uploads safe, use these example homes:

| Location | What belongs there |
| --- | --- |
| Assigned issue | Acceptance: retry returns the same reference; current plan, progress, feedback and next action |
| knowledge/decisions/ADR-0001-upload-idempotency.md | Why an idempotency key was chosen, alternatives, concurrency consequences, owner and decision status |
| knowledge/current/uploads.md | Actual upload contract, key scope/lifetime, failure behavior, operating limits and verified source revision |
| knowledge/README.md | Links to the upload contract and decision; concise topic navigation |
| Linked PR | Implementation, criterion-linked checks, tested revision and actual review |

An illustrative decision can start as:

```markdown
# ADR-0001: Scope upload idempotency by account and key

Status: proposed. Owner: product and technical decision owner.
Scope: upload retries in the current portal increment.

## Starting situation
Network retries can create duplicate documents. Concurrent retries must not race.

## Insight
Client-only deduplication misses concurrent requests and restarts.
A server-side claim keyed by account and idempotency key can preserve one result,
but needs atomic acquisition, retention rules and recovery after a partial write.

## Proposed decision and consequences
Use the server-side claim if the owner accepts its contract and operating cost.
Define payload-conflict behavior, key lifetime and recovery before implementation.
Link the work item and current upload contract. Record actual acceptance separately.
```

After accepted and integrated implementation, update the current upload page from actual
code/check evidence. Preserve the accepted rationale. A changed key-scope policy gets an
explicit decision and replacement links; avoid rewriting old reasons to match new code.
The old plan remains historical in its completed issue. An incident review links owned
follow-up work and affected current knowledge rather than becoming another task tracker.

## Parallel delivery example

One contributor owns the API implementation; another owns the client behavior. They agree
the request, response, conflict and retry contract before implementation. Use separate
working directories and a shared assignment/dependency view. Give a shared contract file
one coordinated writer at a time. The integrator verifies the API/client interaction and
failure behavior on the combined revision before claiming the feature complete.

## Publication and recovery

Docusaurus publishes explicitly selected source pages as Project, Ways of Working,
Knowledge and Decisions. Source Markdown is maintained once; private/local work is
excluded. The website can lag an unmerged branch. Before a session switch, save the work
item's bounded handoff and source revisions. A new session checks current sources and
reads only relevant history. See the [knowledge guide](../PROJECT-KNOWLEDGE.md).
