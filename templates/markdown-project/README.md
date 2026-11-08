# Markdown-first project structure

Recommended for new projects that want adaptable AI collaboration without a workspace
manifest. Existing projects keep their authoritative sources. This is an adaptable
starter, not a fixed lifecycle, required folder hierarchy or executable workflow engine.

## Source map

| Example path | Owns |
| --- | --- |
| AGENTS.md | Short entry, source locations and context-loading rules |
| [PROJECT.md](PROJECT.md) | Vision, goals, boundaries, stakeholders and real work/review homes |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contributor setup, actual tools/commands and action boundaries |
| engineering/process/README.md | Process routing and shared collaboration rules |
| engineering/process/01-clarify.md through 05-integrate-retain.md | Selected step instructions |
| engineering/skills/README.md | Project-specific techniques or canonical skill pointers |
| engineering/agents/README.md | Relevant lead/specialist roles and host bindings |
| engineering/decisions/README.md | ADR discovery, status and replacement links |
| engineering/knowledge/README.md | Current contracts, architecture and operating knowledge |

Rename engineering/, process/, skills/, agents/ or decisions/ as needed and update links.
Add, remove, combine or reorder steps for your project. Numbers support navigation; they
are not workflow state, stable decision IDs or mandatory sequential gates. A change may
return to design after verification. Do not create empty folders just to match this map.

## Adopt

1. In a new project, copy AGENTS.md, PROJECT.md, CONTRIBUTING.md and the engineering/
   directory into the project root. Leave this setup guide in the catalog. In an existing
   project, merge useful material and point to the current owners instead of replacing files.
2. Fill the [project map](PROJECT.md) with actual owners and work homes. Fill the
   [contributor guide](CONTRIBUTING.md) with real commands, tools, access and action
   boundaries. Keep phase instructions in the [process index](engineering/process/README.md)
   and step pages. If you already use the compact guide, preserve its project-specific
   requirements and replace repeated process or coordination guidance with a link.
3. Adapt the process steps and populate only useful skill, agent and knowledge pointers.
   Remove unused files or sections together with their links. Verify the host discovers
   AGENTS.md and can load the selected bodies. Links do not install or run anything.
4. Walk one real task through the applicable steps and try a fresh-session handoff.
   Confirm the required sources resolve and check a missing source before depending on it.
   If you publish, generate a reading view from selected shared Markdown and exclude private work.

Process pages describe reusable procedure. Issues/PRs hold actual assignments, progress,
review and evidence. ADRs retain significant reasons when decisions arise; current
knowledge describes verified behavior. Do not copy chat logs or every execution plan
into project memory. Personal planning follows the adopted project's privacy rules.

The existing [compact starter](../project-starter/README.md) remains useful when one
contributor guide is enough. This layout needs no project.yaml, workspace.yml or new
configuration parser. Optional ADR metadata supports publishing/graphs; it is not a
project manifest or a requirement for Markdown-only use.
