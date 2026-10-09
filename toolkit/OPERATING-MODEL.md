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

## One place for each kind of information

| Information | Canonical home | Maintained by |
| --- | --- | --- |
| Priority, iteration, status and assignment | Customer GitHub Project | Product owner and authorized workers |
| Live plan, acceptance and open questions | Assigned GitHub issue | Issue owner; AI updates its bounded section |
| Implementation and verification | Linked pull request | Author and reviewers |
| Goal, value chain, working rules and decision rights | Customer workspace entry pages | Responsible customer roles |
| Significant decision and rationale | `workspace/decisions/` ADR | Authorized decision maker |
| Current domain, architecture and operational knowledge | `workspace/knowledge/` | Technical or domain owner |
| Iteration outcomes and material open work | `workspace/iterations/` | Product owner with an AI-prepared draft |
| Documentation site and knowledge graph | Generated Markdown views | Build process |

General agents and skills live in AI Agents. Customer facts stay with the customer.
Personal Second Brain notes stay in the private PARA vault. Where Jira already owns
scope or capacity, preserve that ownership and link the engineering issue to its delivery object.

## Choose the planning home once

For customer delivery on a board, the assigned issue owns the plan. Follow the customer's
working agreement and preserve human feedback. Avoid a second `.ai/work/` record or task
spreadsheet for that assignment.

For larger local work without a board assignment, use one [work record](WORK-RECORDS.md).
For a small fix, inspect, change and verify directly. The local dashboard manages Markdown
records; Project and issue updates use authorized tools available in your AI host.

For planned work that needs approval, use [local Plannotator review](PLAN-REVIEW.md)
between Plan and Build. Comments go back to Plan; Build starts after the current
revision is approved. Keep the plan and approval receipt in the existing issue or record.
Choose a model and supported thinking variant for each phase when useful. Model changes
carry the approved scope and evidence forward; they do not restart the decision process.

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
the Project update. Each completed issue does not need an ADR.

## Keep context and coordination small

- Start with three workspace pages: goal and entry points, working agreement, stakeholders.
- Load the active assignment and relevant knowledge, rather than the entire history.
- Reuse loaded guidance; reread mutable feedback before updates.
- Ask for a human decision when meaning, risk or authority requires one.
- Delegate only when supported, authorized and useful; give each writer a bounded scope.
- Archive completed work out of routine context and generate views from canonical sources.

Measure time to a reviewable increment, repeated questions, documentation effort and
customer outcomes using an actual baseline. File counts and text volume do not prove value.

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
