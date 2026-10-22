# Project knowledge that survives growth and session changes

Build shared memory from owned sources. The project controls its requirements, decisions,
code and operating knowledge. The central catalog supplies reusable expertise. A model's
chat history is neither the authoritative record nor a required onboarding package.

## Start with a small entry

`AGENTS.md` points to the project config, workspace entry and working agreement. The
entry states the product outcome, important boundaries and relevant source links. The
YAML maps actual repositories, tracker and knowledge homes. Keep these short and current.

Use the [context recovery contract](CONTEXT-RECOVERY.md) for interruptions. This guide
adds the retrieval and maintenance choices needed as the project grows.

## Keep facts at their owners

| Fact | Authoritative home | Maintenance trigger |
| --- | --- | --- |
| Active scope, plan, questions and feedback | Assigned issue/ticket | Material progress, answer or scope change |
| Why a significant choice was made | Decision record | Decision arises or an accepted replacement is agreed |
| Current domain/architecture/operation | Relevant knowledge page, contract and implementation | Behavior or operating responsibility changes |
| Verification | PR and actual check artifacts | A relevant tested revision changes |
| Current recovery state | Bounded section in the existing assignment | Material increment or known session/model switch |
| Iteration outcome | Short linked report | An actual review period closes |
| General reusable method | Canonical skill or reference | Repeated evidence that it generalizes beyond one customer |

Do not copy customer facts into the global catalog. Preserve privacy and access boundaries
when sharing generalized learning. Websites and graphs are derived views, not independent
databases to edit. Keep local work, archives, exports and previews outside publication.

## Choose what stays current and what becomes history

This model uses current contracts/knowledge plus preserved decision history. Agree a
single authoritative contract for each topic; do not keep a concept and knowledge page
as competing editable descriptions. A concept may itself remain that living contract.

| Artifact | State and ownership | Retention rule |
| --- | --- | --- |
| Idea | Hypothesis with a disposition, not assigned delivery | Keep a short reason and result link; remove deliberate duplicates |
| Concept/spec | Draft/agreed contract, with delivery state recorded separately | Maintain the designated living source, or mark a completed snapshot historical and link its current successor |
| Plan/tasks | Current work item owns execution and status | Close in place after acceptance; preserve as historical execution context |
| Decision | Proposed/accepted/rejected/superseded with accountable owner and scope | Preserve accepted reasoning and explicit replacement links |
| Current knowledge | Intended/partial/verified behavior with sources | Update affected facts after integration and actual evidence |
| Incident review | Observed impact, recovery and owned learning | Retain history; track follow-up in the existing work system |
| Session handoff | Current continuation state in the existing assignment | Refresh during work; mark obsolete after completion |
| Generated output | Reproducible view/export/cache | Regenerate or remove deliberately; never the only rationale store |

Before discarding a derived plan, extract still-relevant choices into the designated
decision home. Retain important verification summaries, revision and evidence references
when temporary CI artifacts expire. Do not rewrite historical rationale to match today's
implementation. Git history is useful evidence, but current constraints need findable
entry links rather than only a commit search.

Use stable record IDs or paths, descriptive titles, status, scope, owner and source links
when the record warrants them. IDs support references, not a second numbering service.
Add a last-verified date/revision to consequential implementation claims. A date or the
word "current" alone does not establish correctness. Human acceptance references and
test evidence must be real.

## Choose a method without duplicating work

| Assignment | Default approach | Durable result |
| --- | --- | --- |
| Clear small correction | Inspect, change, verify | Result and relevant evidence in the existing conversation/review |
| Ordinary bounded feature | Lean clarification, short plan, build, verify | Assignment plus affected current knowledge and significant decisions |
| Complex behavior/contract | Spec-Driven Development if selected | One authoritative spec and checks; choose its retention convention |
| Broader discovery/product planning | BMAD or existing method if selected | Link its native artifacts and extract/preserve durable rationale |

Spec Kit explicitly permits historical feature snapshots, living specs and reconciled
artifact evolution; no retention strategy is forced. Our default keeps the current
contract trustworthy and completed work findable. A project may select another model
explicitly. Preserve important rationale before replacing derived plans/tasks. Accepted
implementation discoveries may change intent only through its responsible owner.

BMAD can support thinking and building independently. Reuse its native sources rather
than copying them into parallel workspace documents. If native `plan.md`/`tasks.md` owns detailed execution, the issue links that plan and owns
the agreed aggregate status/feedback; do not mirror editable checklists in both places.
Record the chosen method in the
project map/working agreement; per-assignment exceptions belong in that assignment.
This toolkit neither installs these methods nor executes their commands automatically.

Primary references: [Spec Kit artifact evolution](https://github.github.com/spec-kit/guides/evolving-specs.html)
and [BMAD starting points](https://docs.bmad-method.org/). The lean combination here is
this repository's recommendation, not a requirement imposed by those tools.

## Retrieve by assignment and scope

1. Read the current assignment, acceptance and new human feedback.
2. Identify affected repositories, domain boundaries, consumers and operational owners.
3. Follow relevant contract, knowledge and decision links. Inspect statuses, scope and
   replacement chains before treating a decision as current.
4. Search the affected domain when links are missing. Inspect relevant callers, tests,
   code ownership and ADR titles; an empty link list does not establish absence.
5. Load the smallest set of full sources that explains the constraint or uncertainty.
   Expand when necessary rather than cutting out an inconvenient requirement.
6. State missing/conflicting sources and resolve consequential uncertainty with its owner.

A useful context summary records the question, source pointers and relevant revisions,
not another full copy of the documents. Prefer explicit links and bounded domain indexes
before adding retrieval infrastructure. Add semantic search or a graph service only for
an observed retrieval need and evaluate its omissions, freshness and access filtering.

## Find knowledge and sessions again

The workspace entry links the current topics; each topic links its applicable decisions,
contract and verification. Add domain indexes only when the entry becomes difficult to
navigate. Keep history searchable but outside default context. An absent link is a reason
to search the affected sources, not proof that a constraint does not exist.

For a session change, preserve result, relevant revisions, evidence/limits, blockers,
pending writes and one next action at the current work home. If useful, add the actual
host, project and session ID/link there. Never invent a session reference or rely on a
provider session URL as the only project memory. No per-agent knowledge tree or complete
chat export is required. Concurrent sessions need real assignment/claim and integration
controls; naming a session in Markdown does not provide a lock.

## Maintain knowledge while delivering

Significant decisions preserve starting situation, alternatives/evidence, decision,
consequences, status and responsible role. This supports an AEK reading: situation,
insight and consequence. Use the [compact decision](../templates/knowledge/decision.md), or the
[architecture decision template](../templates/architecture/decision.md) when its richer metadata helps.
An accepted decision records agreement, not implementation or deployment.

Update affected current knowledge from the integrated behavior and actual evidence.
Keep intended behavior visibly distinguished while work is in progress. Record source
revision or evidence links for consequential statements and define a review trigger
when a contract, dependency, owner or environment changes. Time alone does not make an
ADR invalid, and a newer summary does not override an accepted decision.

When a person leaves or a component changes owner, update the entry and ownership links.
Archive inactive local work; do not remove the rationale of a superseded decision.
Correct known stale references as part of the affected work and leave explicit unresolved
gaps. A routine cleanup should not rewrite human history.

## Grow structure when it earns its cost

| Situation | Add when needed | Evidence it helps |
| --- | --- | --- |
| First increment | Entry, real config, first criteria and significant decisions | Fresh session finds the next authorized step |
| Several contributors | Domain entry pages, ownership, repeatable checks | Fewer repeated questions and conflicting edits |
| Several repositories | Stable repo names, cross-repo links and integration order | No missing dependency or partially claimed feature |
| Concurrent agents | Disjoint scopes, shared claim/recovery mechanism and integrator | Contention/retry cases are exercised |
| Large knowledge base | Scoped indexes, relationship neighborhoods, measured retrieval | Relevant constraints found with acceptable reconstruction effort |

These are adoption stages, not a mandatory maturity certification. Do not create a
folder tree for hypothetical future teams. Role accountability can be combined in a
small team; increasing agent count does not create more human review capacity.

## Prove recovery, including omissions

Run the [cold-session pilot](../templates/customer-workspace/examples/context-recovery-pilot.md).
Include an accepted decision change, a missing linked source that must be searched,
stale test evidence, an unavailable tracker and preserved human edits. At larger scale,
include relevant constraints among many unrelated ADRs and across repository boundaries.
Keep expected answers away from the fresh session's prompt.

Measure wrong-source choices, missed constraints, recovery time, repeated questions and
human reconstruction effort. Record failed attempts as well as successes. The existing
[local observation](evaluations/context-recovery-20261020.md) is a bounded example;
it does not establish large-project or cross-model reliability.
