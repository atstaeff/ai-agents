# AI Agents project

This is the project map for contributors and AI sessions. Start here for purpose,
boundaries and owners; follow [CONTRIBUTING.md](CONTRIBUTING.md) for how to work.

## Vision and goals

Help a small accountable team build and maintain useful products with AI through
portable expertise, shared project knowledge and verifiable engineering.

- Maintain an English catalog of focused agents and skills across engineering disciplines.
- Make goals, significant decisions and current knowledge recoverable across sessions.
- Provide a lean delivery method, reusable templates and optional local tooling.
- Evaluate changes through working examples and actual checks. Claims about productivity
  or user benefit require observations in real projects.

## Scope and boundaries

This repository owns reusable expertise, its operating model, runtime exporters,
the local Markdown workbench and the documentation publisher. Customer facts,
decisions and live assignments remain in their customer-owned sources.

The workbench does not run models, synchronize trackers or coordinate distributed
writers. Preserve the existing stack, exported identifiers and public routes.
Keep private notes, secrets, local work and generated output outside public commits.
Merge and deployment require explicit authorization.

## Responsibilities

The [decision-role map](workspace/stakeholders.md) names the repository owner,
contributor and reviewer. The owner decides priority, consequential design and
acceptance. The assigned contributor implements and supplies evidence; the reviewer
assesses the current revision. A role does not grant tool access or action authority.

## Key sources and links

| Need | Authoritative source |
| --- | --- |
| Tools, work/review locations and check commands | [Project manifest](project.yaml) |
| Contribution process and skill selection | [Contributing](CONTRIBUTING.md) |
| Repository acceptance and action boundaries | [Working agreement](workspace/working-agreement.md) |
| Setup, startup and local process replay | [Repository runbook](toolkit/REPOSITORY-WORKFLOW.md) |
| Reusable delivery method | [Operating model](toolkit/OPERATING-MODEL.md) |
| Architecture and information ownership | [Detailed project concept](toolkit/WORKSPACE-CONCEPT.md) |
| Significant repository rationale | [Decision index](workspace/decisions/README.md) |
| Available expertise | [Skills](skills/README.md) and [agents](agents/README.md) |

## Working method and AI process

Read [AGENTS.md](AGENTS.md), this map and the
[contribution process](CONTRIBUTING.md#working-process-and-skills), then the relevant
project sources. Use **Clarify → Plan → Build → Verify → Integrate and retain**.
Load only the skills needed for the assignment; the contribution guide maps each
activity to its reusable procedure. Tool addresses and actual commands come from
the configuration, while effective permissions come from the current host and request.

An assigned issue owns its live plan and acceptance; the PR owns implementation and
checks. Reuse an existing PR for a direct request it already represents. Otherwise,
a larger direct request may use one ignored `workspace/work/` record. Small corrections
need no additional process record. Required review and integration determine completion.

## Knowledge and session continuity

Preserve significant rationale at the configured decision home; update affected current
knowledge from verified behavior. Keep completed plans at their original work home.
Before a pause, leave result, source revisions, evidence/limits, blockers, pending writes
and the next action there. Resume using the [recovery contract](toolkit/CONTEXT-RECOVERY.md).

`project.yaml` is the required project manifest; it points to this human and AI map.
This repository keeps optional records and local work in `workspace/`; other projects
choose their own knowledge and decision directories. The
[pilot observation](toolkit/evaluations/workspace-pilot-20261022.md) records actual tooling
results and limits; [iteration reports](workspace/iterations/README.md) are optional.
