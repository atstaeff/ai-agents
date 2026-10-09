# Source ownership and capabilities

Separate reusable guidance, live work, durable knowledge and generated views.

| Component | Canonical source | Responsibility |
| --- | --- | --- |
| Agents and skills | This repository's `agents/` and `skills/` | Reusable roles and focused instructions |
| Operating model | `toolkit/OPERATING-MODEL.md` | Outcomes, ownership, handoffs and knowledge lifecycle |
| Customer work | Customer Project, issues and PRs | Priority, live plans, questions, implementation and evidence |
| Customer workspace | Customer repository's `workspace/` | Context, decision rights, ADRs and current knowledge |
| Local work records | Each project's `.ai/work/`, without a board-owned assignment | One record per larger local outcome |
| Private Second Brain | Existing Obsidian PARA vault | Personal projects, areas, resources and archive |
| Runtime adapters | `tools/ai_toolkit.py export` | Native profiles, permissions and references |
| Local dashboard/API | `tools/web/` and Python loopback server | Markdown records, task evidence and comments |
| This website | `assets/mkdocs/` and `tools/docs_hook.py` | MkDocs views of canonical guidance and examples |
| Customer documentation site | Existing Docusaurus configuration and workspace sources | Customer-controlled publishing |

## Execution belongs to your host

Jörg selects relevant expertise. Delegation depends on host capabilities and permissions;
the current session can otherwise use selected guidance directly. Inference may be
local or remote according to your provider configuration.

The toolkit exports profiles and manages files. Its dashboard does not run models or
update GitHub Projects. Recurring work needs an implemented runner and authorized host
tools; the [runner contract](customer-workspace/runner.md) describes the requirements.

## Sources and published views

Edit canonical Markdown, then regenerate the index, relationships and website. This
catalog site uses MkDocs. The [Docusaurus guide](customer-workspace/docusaurus.md) applies
to the customer's existing site. A root `docs/` used for compiled Pages output stays generated.

The site renders profiles, the operating model and worked examples from canonical sources.
The [knowledge map](customer-workspace/knowledge-map.md) uses explicit metadata and local links.
Customer facts and private vault paths do not belong in this public toolkit.
