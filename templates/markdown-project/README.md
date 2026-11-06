# Markdown-first project structure

Recommended for new projects that want adaptable AI collaboration without a workspace
manifest. Existing projects keep their authoritative sources. This is an adaptable
starter, not a fixed lifecycle, required folder hierarchy or executable workflow engine.

## Source map

| Example path | Owns |
| --- | --- |
| AGENTS.md | Short entry, source locations and context-loading rules |
| PROJECT.md | Vision, goals, boundaries, stakeholders and real work/review homes |
| CONTRIBUTING.md | Contributor setup, actual tools/commands and action boundaries |
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

1. Merge [the entry](AGENTS.md) into the project's existing AGENTS.md. Use the existing
   project facts and contributor guide, or adapt the [project facts starter](../project-starter/PROJECT.md)
   and [contributor starter](../project-starter/CONTRIBUTING.md).
2. Point CONTRIBUTING.md to [the process index](engineering/process/README.md) instead of
   copying the phase instructions. Keep real commands, tool access, authorization and
   policy adoption in that contributor guide. Replace its generic phase summary and
   generic Herdr/model-routing and coordination sections with a link to the process shared
   contract. Preserve project-specific exceptions, review requirements, commands and access.
3. Adapt the [process index](engineering/process/README.md) and relevant step pages.
   Each step states when to use it, required inputs, actions, evidence and next routing.
   Resolve all source pointers and roles before relying on them; no manifest is required.
4. Populate only useful skill/agent pointers and knowledge. Verify the host discovers
   AGENTS.md and can explicitly load linked bodies. Links do not install or run anything.
5. Try a real bounded task and a fresh-session handoff. Publish selected original Markdown
   through Docusaurus if useful; keep source ownership and links, and exclude private work.

Process pages describe reusable procedure. Issues/PRs hold actual assignments, progress,
review and evidence. ADRs retain significant reasons when decisions arise; current
knowledge describes verified behavior. Do not copy chat logs or every execution plan
into project memory. Personal planning follows the adopted project's privacy rules.

The existing [compact starter](../project-starter/README.md) remains useful when one
contributor guide is enough. This layout needs no project.yaml, workspace.yml or new
configuration parser. Optional ADR metadata supports publishing/graphs; it is not a
project manifest or a requirement for Markdown-only use.
