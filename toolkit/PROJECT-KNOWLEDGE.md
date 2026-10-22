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

## Maintain knowledge while delivering

Significant decisions preserve starting situation, alternatives/evidence, decision,
consequences, status and responsible role. This supports an AEK reading: situation,
insight and consequence. Use the [decision template](../templates/architecture/decision.md).
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
