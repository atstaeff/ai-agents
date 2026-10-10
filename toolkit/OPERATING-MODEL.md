# Work with AI as a teammate

Organize delivery around a clear outcome, an accountable owner and evidence. Give AI
context and action scope for the assignment. Keep customer knowledge in customer-controlled
systems so another person or agent can continue the work.

As implementation becomes faster with AI, goals, decision rights, feedback and shared
knowledge need to remain explicit. This model makes those handoffs visible without
asking people to maintain several copies of the same plan.

## From business value to useful knowledge

| Stage | Human responsibility | AI contribution | Evidence |
| --- | --- | --- | --- |
| Frame | Choose outcome, scope and acceptance | Inspect context and propose a bounded increment | A Ready assignment |
| Approve the plan when required | Verify assumptions, comment and approve the current revision | Revise the plan and preserve feedback | A receipt in the existing planning home |
| Deliver | Resolve consequential questions | Implement within scope and keep the plan accurate | Focused code and relevant checks |
| Review | Review and decide acceptance | Prepare a reviewable PR and explain remaining limits | Required review and acceptance |
| Learn and operate | Choose follow-up work and assess impact | Update affected knowledge and prepare iteration closeout | Current knowledge, significant ADRs and observed results |

These are activities, not mandatory separate agents, documents or meetings. Small
changes take a direct path. Larger assignments need a visible plan and the people who
can resolve consequential questions.

## Scale the process to uncertainty and consequence

| Assignment | Minimum useful flow |
| --- | --- |
| Clear, reversible small change | Inspect, implement, run relevant checks, report |
| Uncertain feature or several affected boundaries | Clarify the outcome, plan one complete slice, obtain required review, implement and verify |
| Consequential migration or operational change | Add the affected compatibility, rollout, recovery and observation checks; involve the accountable owner |

Use product discovery when user value or the solution is uncertain. Compare the
smallest software change with an existing capability or process improvement. State
what would disprove the idea before investing in a larger implementation. A prototype,
a passing build and a shipped feature each provide different evidence; none alone
proves customer value.

## Let each project choose its tools

The project defines the system of record for each information type in a small
[`workspace/project.yaml`](PROJECT-CONFIG.md), linked from `AGENTS.md`. Use an existing
equivalent configuration when already present. The YAML owns the tooling map; the
working agreement explains statuses, authority and process without duplicating locations.

| Information | Project specifies | Accountable role |
| --- | --- | --- |
| Priority, iteration, status and assignment | Tracker/board and project URL, e.g. Jira or GitHub Projects | Product owner |
| Live plan, acceptance and questions | Work-item URL and the permitted section/field | Work-item owner |
| Implementation and verification | Repository and PR/MR review location | Author and reviewers |
| Significant decisions and rationale | ADR directory or designated decision space | Decision maker |
| Current domain, architecture and operational knowledge | Repository, wiki or other customer-owned knowledge space | Domain/technical owner |
| Iteration outcomes | Existing project update or report location | Product owner |
| Questions and approval | Authorized channel, reviewer and scope of approval | Relevant stakeholder |

Name one authoritative location for each purpose and link related objects. Specify
which statuses mean ready, reviewable and done, who may update which fields, and which
access tools are available. A Jira ticket can own the entire live plan while GitHub
hosts only the code and PR. There is no requirement to create a matching GitHub issue.
Different ownership across tools is valid; two independently edited live plans are not.

Customer knowledge stays in customer-controlled systems. General expertise stays in
AI Agents, and personal Second Brain notes stay in the private PARA vault. `workspace/`
can contain the knowledge itself or a compact index of its authoritative external homes.
Docusaurus and the knowledge graph are optional views of the selected sources; external
wiki synchronization is not implemented by this toolkit.

## Choose the planning home once

Read the project tooling map and active assignment before selecting an integration or
creating records. Keep the plan, acceptance, questions and required approval receipt at
the designated home. Respect project-owned fields and preserve human feedback.

For larger local work with no assigned system, use one [work record](WORK-RECORDS.md).
For a small fix, inspect, change and verify directly. If the designated system is
unavailable, record the access limitation and prepare an unsent update in the current
conversation; continue independent work without inventing synchronization or creating
a competing source of truth. Resolve conflicting ownership before shared writes.

For planned work that needs approval, use [local Plannotator review](PLAN-REVIEW.md)
between Plan and Build when available. Comments go back to Plan; Build starts after
the current revision is approved. The review UI does not choose or replace the project’s
planning home. Choose a model and supported thinking variant for each phase when useful;
carry the approved scope and evidence across model changes.

## Questions improve the assignment

Bundle related questions with a recommendation, impact and the needed decision. Route
business questions to the Product Owner, design to the Technical Owner and operational
questions to Operations. Preserve original answers as evidence. Continue independent
work within scope while a consequential answer is pending.

Update the plan after a material increment or answer. Keep transient exploration and
full tool logs out of routine comments; link detailed evidence instead.

## Decisions are recorded during delivery

Draft an ADR when a significant choice arises, while alternatives and reasons are
available. The authorized decision maker accepts or rejects it. Preserve accepted
rationale; a substantive replacement gets a new ADR and an explicit supersedes relation.

Decision acceptance, implementation, merge, deployment and observed business impact are
separate states. Current knowledge describes behavior; historical ADRs explain choices.
At iteration close, prepare one concise report linking outcomes, evidence, existing ADRs
and material open work. Draft only missing significant decisions. Link the report from
the designated project update. Each completed issue does not need an ADR.

## Keep context and coordination small

- Start with the project config and three workspace pages: goal/entry points, working agreement, stakeholders.
- Load the active assignment and relevant knowledge, rather than the entire history.
- Reuse loaded guidance; reread mutable feedback before updates.
- Ask for a human decision when meaning, risk or authority requires one.
- Delegate only when supported, authorized and useful; give each writer a bounded scope.
- Archive completed work out of routine context and generate views from canonical sources.

Measure time to a reviewable increment, repeated questions, documentation effort and
customer outcomes using an actual baseline. File counts and text volume do not prove value.

## Make quality observable

Provide the agent with reproducible setup, start and check commands, representative
fixtures and access to the relevant UI, API or logs within its authorized scope.
Turn acceptance criteria into checks at the affected boundary. Derive expected behavior
from the requirement or contract, independently of the implementation. Use CI for
repeatable quality rules; request human judgment for consequential tradeoffs.

Deliver small complete increments. Review evidence and the diff. For operational
changes include the relevant rollout, recovery and post-deployment observation; keep
unrun checks and unknown impact visible. Promote recurring defects into a focused
regression check or a clarified rule instead of growing a universal instruction manual.

For a few comparable assignments, measure time to accepted result, human review effort,
rework or escaped defects, and the intended user outcome. Compare model/effort or
coordination changes against that baseline. Keep a change only when its benefit
justifies its operating cost; token consumption alone cannot measure delivery quality.

## Keep tools replaceable

Maintain the process and expertise once. Customer knowledge stays at the project-designated home,
shared expertise in canonical catalog files, and host-specific discovery/permissions
in generated adapters. Model changes do not rename project folders. Host changes
require checking capabilities and effective permissions. See [portability](PORTABILITY.md).

## What you can use today

The toolkit exports Jörg, Plan, Build, specialists and focused skills. It includes a
local dashboard and a [customer workspace starter](../templates/customer-workspace/README.md).
Your host runs models and tools and provides native delegation where supported. Provider
choice controls whether inference is local or remote.
The OpenCode 1 export can optionally configure Plannotator and separate Plan/Build models
and variants. Review happens locally; installed-host behavior needs a local smoke check.

The starter includes a local graph generator and an existing-site Docusaurus guide.
Its runner page is a design contract. Adopt the manual issue-to-PR flow first; recurring
execution needs an implemented runner and authorized host capabilities.

Continue with [runtime setup](RUNTIMES.md), the [working contract](WORKFLOW.md) or
[the worked assignment](../templates/customer-workspace/examples/issue-42.md).
