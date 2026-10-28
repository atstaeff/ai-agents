# Engineering with AI

Turn a product need into a verified change, then retain the knowledge needed to operate
and improve it. People own priorities, acceptance and consequential decisions. AI leads
coordinate bounded work; specialists contribute implementation and evidence.

## Start with a project map

Every adopted project has an `AGENTS.md` entry linking its purpose, boundaries, responsible
people, delivery process, tools, commands and knowledge. Keep facts in their existing homes:
`PROJECT.md`, `CONTRIBUTING.md`, repository Markdown or an accessible adopted web source.
The [starter](../templates/project-starter/README.md) provides a complete example.
Record which version of a central process applies. Read relevant linked content explicitly.

| Information | Authoritative home | Update when |
| --- | --- | --- |
| Vision, users, scope and decision rights | Project map and stakeholder sources | Product intent or responsibilities change |
| Outcome, acceptance, ownership, dependencies and progress | Existing GitHub issue, Jira ticket or current assignment | Shared coordination changes |
| Implementation and review evidence | Code and linked PR/MR | A reviewable increment is ready |
| Current architecture, operations and significant reasons | Project knowledge and decision home | Behavior or a consequential choice changes |
| Personal experiments, execution steps and resume notes | Permitted private Second Brain; otherwise unsaved in-session | Useful for personal continuity |
| Documentation and dependency map | Docusaurus and selected graph views | Regenerated from their maintained sources |

The team can continue from shared sources without accessing a personal vault. Use a shared
execution plan only when collaborators depend on its steps. Customer data policy governs
all storage and model use. No particular folder name, YAML manifest or extra tracker is required.

## The value stream

Use the smallest complete increment. A routine correction can move directly from the
request to implementation and relevant checks; it needs no new planning document.

| Stage | Work and accountable viewpoint | Evidence to continue |
| --- | --- | --- |
| Frame | Product: understand users, value, constraints and stakeholders | Observable acceptance and scope at the assignment |
| Shape | Engineering: inspect existing behavior, compare material options and agree interfaces | Bounded approach; significant choices recorded as proposed decisions |
| Build | Delivery coordinates; specialists implement independent slices | Reviewable changes, explicit ownership and executable checks |
| Verify | Check behavior, security and maintainability; use independent review when required or consequential | Criteria linked to actual results on the combined revision |
| Integrate and release | Integrator assembles changes; authorized owner controls release | Required acceptance, rollout and recovery evidence |
| Learn and retain | Contributors update current knowledge and decision status | Next session can recover the result; product outcome observed when available |

The assignment is the coordination home throughout. The PR links its evidence. Decisions
are captured when they arise and reconciled against the implemented result. Completed
plans remain historical at their original home; accepted decisions retain replacement links.
See the [working contract](WORKFLOW.md), [quality standard](QUALITY-STANDARD.md) and
[knowledge lifecycle](PROJECT-KNOWLEDGE.md) for the relevant detail.

## Leads and specialists

These are responsibilities, not a required headcount. A small task can use one session.
For substantial work, activate the lead viewpoints needed by the outcome and name one integrator.

| Viewpoint | Catalog role | Owns | Delegates for |
| --- | --- | --- | --- |
| Product lead | product-manager | User value, scope, stakeholder questions and acceptance proposal | Discovery, domain research and product uncertainty |
| Engineering lead | lead-architect | Technical approach, contracts and architectural tradeoffs | Python/FastAPI, React/JavaScript, GCP, Terraform and security |
| Delivery lead | task-orchestrator | Dependency order, writer scopes, blockers and integration coordination | Independent implementation slices and evidence collection |
| Independent review | code-reviewer, architecture-reviewer | Findings and assessment of the current revision | Tests, focused risk analysis and documentation review |
| Documentation | documentation-editor | Clear narrative, accurate instructions and useful navigation | A focused authoring pass followed by an independent editorial pass |

AI roles propose; the project's accountable humans retain decision rights. Leaders share
the assignment, interfaces and durable knowledge rather than their entire conversations.
Use [orchestration](ORCHESTRATION.md) for native Herd commanders, specialist packets,
concurrency and model selection. A role description alone starts no process and grants no tools.

## Work efficiently

Load the project entry, current assignment and next relevant skill. Search a scoped area
and expand for a concrete uncertainty. Keep large examples and reference guides on demand.
Use an economical evaluated model for a well-defined specialty; reserve stronger reasoning
for ambiguity, architecture, integration and consequential review. Escalate a failed approach
with its evidence rather than repeating blind retries or increasing the whole team's context.

Parallelize independent slices with clear contracts and isolated writers. Account for
coordination cost and provider limits; a larger team is useful only when accepted results
arrive sooner without excessive rework. Observe time to accepted change, review effort,
defects, model cost and resource use. Model price and token counts alone do not measure value.

## Adopt incrementally

1. Link the project's real sources from its [AGENTS.md](../templates/agent-instructions/README.md).
2. Deliver one assignment with the relevant [catalog preset](CATALOG-GUIDE.md).
3. Add [Herd or another supported host](RUNTIMES.md) when parallel work justifies it.
4. Publish selected shared knowledge through Docusaurus; use bounded graph views for dependencies.
5. Inspect one completed change and remove friction before expanding the process.

[Ponytail and Graphify](INTEGRATIONS.md) are optional native tools with distinct jobs:
reduce unnecessary implementation and retrieve useful dependency context. The repository's
[knowledge map](../examples/engineering-demo/README.md) publishes curated project records.
The optional [local workbench](WORK-RECORDS.md) manages files; it runs no models or team scheduler.
