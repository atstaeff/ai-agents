# Work with AI as a teammate

Use a small accountable team, shared project knowledge and AI for bounded delivery.
People own product direction, consequential decisions and acceptance. AI helps discover,
model, implement, verify and explain the result through the project's actual tools.
The aim is less reconstruction and rework, with useful products that can evolve safely.

The model has two connected parts: an [expertise catalog](CATALOG-GUIDE.md) maintained
centrally and a [project workspace](WORKSPACE-CONCEPT.md) owned by each project.
The catalog says how to do a class of work. The workspace says what this project needs,
what has been decided and where its authoritative sources live.

## Start from the outcome

Define the user, problem, expected behavior and observable success. Compare an existing
capability or process improvement with the smallest useful software increment. Name
assumptions and what evidence could disprove the proposal. A prototype, passing tests,
accepted code, deployed behavior and demonstrated value are different results.

Use the [project brief](../templates/project/project-brief.md) inside the existing intake
or assigned work item when needed. A clear reversible fix can go directly from inspection
to implementation and appropriate checks.

## The delivery loop

| Activity | Accountable decision | AI contribution | Evidence and existing home |
| --- | --- | --- | --- |
| Frame and discover | Product owner chooses outcome and priority | Inspect sources, compare alternatives, test uncertainty | Criteria and bounded increment in the assignment |
| Decide and plan | Technical/domain owner resolves consequential tradeoffs; review the plan when required | Model boundaries, select quality scenarios and propose the next slice | Current plan, feedback and significant ADRs |
| Build | Assigned contributor works within scope | Implement, preserve comments and update affected knowledge | Focused change and actual repository revisions |
| Verify and review | Required reviewer assesses meaning and evidence | Exercise criteria and failure cases; prepare actionable findings | Checks, current diff and acceptance references |
| Integrate and operate | Authorized owner approves integration/release | Prepare rollout, recovery, diagnostics and observation | Integrated/deployed state and operating evidence |
| Learn | Product/technical owners choose improvements | Link results, decisions, unresolved work and learning | Iteration report and measured user outcomes |

These are activities and accountabilities, not six mandatory agents, meetings or documents.
One person may hold several roles. Keep one accountable owner for each decision and one
integrator for the increment. Use the [template chooser](../templates/README.md) only
where the project lacks an adequate existing format.

## Let each project choose its tools

Read `AGENTS.md`, the workspace entry, working agreement and
[workspace/workspace.yml](PROJECT-CONFIG.md). Preserve existing customer conventions.
The YAML maps actual repositories, work/review/knowledge homes, optional board fields,
quality gates and action scope. It grants no permission and runs no workflow.

| Information | Authoritative home |
| --- | --- |
| Priority, iteration and assignment | The adopted board or tracker fields |
| Active scope, plan, questions and acceptance | One assigned issue/ticket or existing local work record |
| Implementation and checks | Relevant repository revisions and linked PR/MR |
| Significant rationale | Customer-owned ADR or decision space |
| Current domain, architecture and operations | Project-owned contracts, implementation and knowledge |
| Recovery state | Bounded handoff at the same planning home |
| Iteration outcomes | Existing project update/report |
| General reusable expertise | Canonical agents, skills and focused references |

A Jira ticket can own the entire plan with a linked GitHub PR and no mirror issue.
For split product/engineering planning, define stable delivery references and field/item
ownership; do not duplicate the same live plan. Missing access means an unsent proposed
update and an explicit gap. Continue independent authorized work.

For a larger direct request without an assigned system, use one [work record](WORK-RECORDS.md).
Personal Second Brain material stays private; customer facts remain with the customer.
Docusaurus, indexes and knowledge graphs are optional derived views.

## Make engineering quality concrete

Select the important quality attributes and turn them into observable scenarios.
Use the [quality standard](QUALITY-STANDARD.md) for correctness, maintainability,
replaceability, testability, security, reliability, usability, compatibility, operations
and resource efficiency. Compare realistic alternatives and justify the tradeoffs.

Optimize for understandable change boundaries and evidence. The most abstract design,
largest agent roster or highest coverage number is not automatically best. Small
complete increments make review and recovery practical. Reuse the existing stack and
make additional infrastructure or abstraction earn its operating and change cost.

A required plan review concerns the concrete current revision. Preserve actual feedback
and approval before dependent implementation. Follow the customer's review policy;
Plannotator is one optional [local review surface](PLAN-REVIEW.md), not a new planning home.
Routine details within approved scope do not reopen every gate. Material scope or design
changes reassess affected decisions, approval and checks.

## Preserve decisions while they are available

Record a significant choice when it arises: situation, alternatives/evidence, decision,
consequences, scope and responsible role. The accountable role accepts or rejects it.
An accepted decision's substantive rationale remains historical. A later accepted ADR
can supersede it with explicit links; a proposed replacement cannot revoke it.

Current knowledge describes intended or implemented behavior with that distinction
visible. Code proves observed implementation, not authorization to ignore architecture.
Resolve consequential contradictions by scope and authority, not the newest timestamp.
See [project knowledge](PROJECT-KNOWLEDGE.md) for retrieval, ownership and maintenance.

## Work with a small team and bounded concurrency

Start with one session and the narrowest relevant skills. Use specialists for a clear
uncertainty or deliverable; delegate only through supported authorized host capabilities.
Give each worker selected sources, acceptance, action/file scope and expected evidence.
Keep concurrent writers separate and verify the integrated result.

Review and decision capacity constrain WIP. Adding agents cannot create extra human
acceptance capacity or remove accountability. Several workers need an effective shared
claim, expiry/recovery behavior and an integrator; assignment alone is not a lock.
Multi-repo work records each relevant revision and integration order. Partial integration
is not a completed cross-repo feature. The toolkit implements no distributed claim or runner.

Use Todo, In Progress, In Review and Done or the project's explicit equivalent. Blocked
is an additional property with reason, owner and resume condition; retain flow position
and WIP. Distinguish delivered from cancelled, duplicate and not-implemented closures.

## Continue when people, sessions and models change

The [recovery contract](CONTEXT-RECOVERY.md) starts from current shared sources, relevant
contracts/code/decisions and the last bounded handoff. Compare assignment revision,
commits, applicable decisions, approval and tested evidence before following an old plan.
Save progress after material increments and before a known pause; include unsaved work,
pending external writes, unresolved questions and one executable next action.

Do not require the full conversation, every ADR or the entire catalog. Search the bounded
project if a relevant source is missing. Reconcile partial writes before retrying after
a timeout, and preserve intervening human edits. Grow domain indexes and retrieval only
when actual project scale requires them.

## Define completion and learn from use

For code, Engineering Done requires the agreed criteria, required review and authorized
integration at the defined completion point. An investigation may finish with a verified
answer. Deployment and measured user benefit require their own evidence. A closed issue
or successful host exit does not prove acceptance.

Observe comparable assignments for time to accepted result, human reconstruction/review,
rework, escaped defects and intended user impact. Record model/host, process revision,
actual results and limits. Keep practices that justify their maintenance cost. No staffing
reduction or universal productivity gain is established by this repository.

## Adopt incrementally

Start with [adoption](ADOPT-WORKSPACE.md) and [the worked assignment](../templates/customer-workspace/examples/issue-42.md).
Run one authorized real assignment, including a fresh-session handoff, before increasing
autonomy. Add domain ownership, multi-repo coordination and concurrency controls as the
need appears. Reuse the [customer starter](../templates/customer-workspace/README.md),
[runtime setup](RUNTIMES.md), [working contract](WORKFLOW.md) and
[repository replay](REPOSITORY-WORKFLOW.md) for concrete steps.
