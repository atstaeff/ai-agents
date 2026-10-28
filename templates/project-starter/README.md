# Team project starter

Use AGENTS.md as the collaboration entry, PROJECT.md for project facts and CONTRIBUTING.md
for the working process, tools and relevant skills. Reuse equivalent existing sources.
No project.yaml or workspace folder is required. Shared artifacts are English.

## Adopt

1. Inspect existing instructions, ownership, tracker, code, CI, architecture and decisions.
   Preserve existing human text and use its authoritative homes.
2. Merge [AGENTS.md](AGENTS.md) into the host's project instructions. Fill its source links.
   Adapt [PROJECT.md](PROJECT.md): vision/goals, stakeholders, scope, repository/code locations,
   actual work/review homes, current knowledge and decisions. Adapt
   [CONTRIBUTING.md](CONTRIBUTING.md): workflow, skills, tools/access, setup/check commands,
   review and action boundaries.
3. For a centrally maintained process or project wiki, replace the relevant source with
   its adopted URL and revision/version. Use the [instruction variants](../agent-instructions/README.md)
   for remote documentation, existing repositories, multiple repositories or a component.
4. Merge [.gitignore](.gitignore) only when using the optional local workbench. Create no
   empty knowledge tree, fictional work items or duplicate plan. Do not copy this README
   as the customer's project facts.
5. Resolve source links, fill prompts and review the content. Run actual project checks.
   Verify host discovery and required web access; no Markdown check proves source quality.
6. Take one bounded real assignment through the process and try fresh-session recovery.
   Before parallel delivery, exercise ownership, overlapping-work recovery and integration.

## Keep information at its owner

| Information | Home |
| --- | --- |
| Stable product context and roles | PROJECT.md or existing project pages |
| Workflow, tools, commands and skill selection | CONTRIBUTING.md or adopted central process |
| Personal steps, experiments and resume notes | User-configured private Second Brain, subject to project policy; unsaved session plan if unavailable |
| Shared scope, acceptance, feedback and handoff | Actual issue/ticket or explicitly adopted shared local work record |
| Shared execution plan when collaborators need one | One agreed home linked from the assignment |
| Current architecture, contracts and operations | Linked project knowledge |
| Significant rationale | Linked decision records with status and acceptance evidence |
| Implementation and verification | PR and actual checks on the tested revision |

The three starter documents have different jobs; use their links instead of maintaining
several copies of a fact. Roles may be combined, but each assignment needs an accountable
human, bounded writer scope and integration responsibility. Follow AGENTS.md for coordination.

## Add knowledge when work produces it

For example, create knowledge/README.md as an index, knowledge/current/upload-behavior.md
for verified behavior and knowledge/decisions/ADR-0001-upload-idempotency.md for rationale.
Choose any equivalent existing paths or wiki sources. Use these focused templates:

| Need | Template |
| --- | --- |
| Opportunity | [Ideas](../knowledge/ideas.md) |
| Feature/design contract | [Concept/spec](../knowledge/concept.md) |
| Significant choice | [Decision](../knowledge/decision.md) |
| Current behavior | [Current knowledge](../knowledge/current.md) |
| Material failure learning | [Incident review](../quality/incident-review.md) |
| Bounded delivery | [Assignment](../delivery/assignment.md) |

Keep completed personal plans private; shared coordination history stays at its work home.
Preserve accepted reasons and replacement links. A
significant decision can begin in PROJECT.md's decision section; move it to a separate
record only when useful and update references together. Docusaurus publishes the selected
canonical sources as a reading view, excluding private/local work and generated exports.

## Use it

Ask your host to read AGENTS.md, follow its referenced project sources and process, and
work on the assigned issue/outcome. A clear small correction needs no extra plan record.
When the project explicitly chooses a shared local work record, the optional CLI uses
workspace/work/:

```sh
python3 /path/to/ai-agents/tools/ai_toolkit.py work --workspace /path/to/project new upload-retries \
  --title "Make upload retries safe" --kind software
```

The --workspace argument means project root. The documentation convention works without
this toolkit. Installing profiles and [runtime adapters](../../toolkit/RUNTIMES.md) is optional.
See the [operating model](../../toolkit/OPERATING-MODEL.md),
[project concept](../../toolkit/PROJECT-CONCEPT.md) and
[knowledge lifecycle](../../toolkit/PROJECT-KNOWLEDGE.md) for the full working agreement.
