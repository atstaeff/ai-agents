# Engineering collaboration contract

This repository maintains an English engineering agent/skill catalog, a shared operating
model and a local Python toolkit. Follow current user and host instructions and the
applicable project rules. Use the user's language in conversation.

## Project sources

Read these entry sources, then only the detail relevant to the assignment:

| Need | Authoritative source |
| --- | --- |
| Vision, goals and success signals | [Project](PROJECT.md#vision-and-goals) |
| Stakeholders and decision/acceptance roles | [Stakeholders](knowledge/stakeholders.md) |
| Scope, exclusions and constraints | [Scope](PROJECT.md#scope-and-boundaries) |
| Process, tools, skills and checks | [Contributing source](CONTRIBUTING.md), [published process](https://atstaeff.github.io/ai-agents/contributing/) |
| Current knowledge and significant decisions | [Knowledge index](knowledge/README.md) |
| Acceptance and action boundaries | [Working agreement](knowledge/working-agreement.md) |
| Assignment and live plan | Assigned GitHub issue or existing PR representing the request |

The [documentation website](https://atstaeff.github.io/ai-agents/) publishes the maintained
sources. This checkout is authoritative for its revision; the published site can lag an
unmerged change. Read the [project concept](toolkit/PROJECT-CONCEPT.md) when changing the
operating model, information ownership, knowledge layout or documentation publication.
No project.yaml or workspace folder is required to adopt this contract.

## Ownership and parallel work

Keep one authoritative work item and one live plan per assignment. Identify its accountable
human owner, active writer, bounded change scope, dependencies and integration owner.
Use separate branches and working directories for independent writers; agree changes to
shared contracts before dependent implementation. Coordinate overlapping scopes through
the project's shared claim/handover mechanism; an assignee or a branch is no atomic lock.
Preserve other contributors' changes and reread shared records before updating them.

Follow the [shared workflow](toolkit/WORKFLOW.md) and
[recovery contract](toolkit/CONTEXT-RECOVERY.md). Proceed with routine reversible choices
within the assignment; resolve consequential scope/design conflicts with the named owner.
Delegate only when supported, authorized and useful. Keep material progress, feedback,
check evidence and the next action at the same work home.

## Repository navigation and engineering rules

- Maintain canonical profiles in agents/<domain>/<name>.agent.md and skills/<domain>/<name>/SKILL.md.
  Use [catalog domains](toolkit/catalog-domains.json) and [catalog guidance](toolkit/CATALOG-GUIDE.md).
  Keep exported names unique and name/description frontmatter present.
- Read the selected skill body and relevant references; links neither install skills nor
  start sessions. Keep host-specific discovery and permissions in adapters;
  see [portability](toolkit/PORTABILITY.md).
- Preserve Python 3.11+ and the standard-library-only core. Keep the dashboard on loopback,
  its assets local, and its comment persistence and stale-write protections intact.
- Edit canonical sources. website/ owns Docusaurus; docs/ is generated GitHub Pages output.
  Preserve public routes. Keep private data, local work and generated bundles out of commits.

## Verification and completion

Use the [runbook](toolkit/REPOSITORY-WORKFLOW.md) and [CI](.github/workflows/checks.yml).
Run checks appropriate to the change:

```sh
python3 tools/ai_toolkit.py check
python3 -m unittest discover -s tests -v
uv run --locked --group validation python -m unittest discover -s tests -v
npm --prefix website ci
npm --prefix website run build
```

Verify combined changes after integration and associate evidence with the tested revision.
Report passed, failed, blocked and unrun checks honestly. Required review, acceptance,
integration and deployment are separate states. Do not merge or deploy without an explicit request.

## Shared memory and handoff

Maintain affected current knowledge and record significant rationale at
[knowledge/](knowledge/README.md). Preserve accepted reasons and replacement links.
Before pausing, save result, relevant revisions, evidence/limits, blockers, pending writes
and one next action at the existing work home. A fresh session checks current sources.
For otherwise unassigned larger local work, the optional toolkit uses ignored
workspace/work/ and workspace/archive/; those are storage details, not the project model.
