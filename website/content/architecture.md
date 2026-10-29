# Source ownership and capabilities

Each source has one editing home. `AGENTS.md` makes those homes discoverable to people
and AI; runtime exports and the website publish selected views.

| Component | Canonical source | Responsibility |
| --- | --- | --- |
| Project collaboration | Root `AGENTS.md` | Rules and links to the authoritative project sources |
| Project facts | `PROJECT.md` or the project's existing equivalent | Goals, scope, stakeholders and ownership |
| Contribution process | `CONTRIBUTING.md` or an explicitly adopted process | Workflow, tools, checks and action boundaries |
| Shared assignment | Designated issue or ticket, with linked review | Scope, acceptance, questions, team handoff and evidence links |
| Implementation and review | Linked PR or equivalent | Changes, findings and actual check results |
| Current knowledge and decisions | Project-owned Markdown or authorized wiki | Behavior, contracts and significant reasons |
| Personal execution plan | Privately configured Second Brain | Personal steps and resume notes; an unavailable store means an unsaved session plan |
| Reusable expertise | This repository's `agents/` and `skills/` | Roles, handoffs and focused procedures |
| Shared guidance | This repository's `toolkit/` | Operating model, adoption and integration guides |
| Runtime adapters | `tools/ai_toolkit.py export` | Generated host layouts and references |
| Optional local workbench | Python loopback server and `tools/web/` | Local Markdown records, task evidence and comments |
| Website | `website/content/`, mapped canonical sources and `website/generate.py` | Published reading views; root `docs/` is compiled output |
| Knowledge publication selection | `website/knowledge.config.cjs` | One trusted, curated source set shared by document publication and graph generation |

## Execution belongs to your host

Relevant leads select expertise; one named integrator assembles and verifies the outcome.
Bounded specialists can use host-configured models suited to their work. Delegation,
session interaction, tools and inference belong to the host; see
[orchestration](getting-started/orchestration.md) and
[runtime setup](getting-started/installation.md).

## Sources and published views

Edit canonical Markdown, then regenerate affected indexes and the Docusaurus website.
Website-only introductions live in `website/content/`; generated profile pages are not
independent copies to maintain. The [website source guide](https://github.com/atstaeff/ai-agents/blob/main/website/README.md)
owns build and publication commands. The [customer publishing example](customer-workspace/docusaurus.md)
shows how a project can publish selected sources through an existing site.

A public site publishes only authorized sources. Private plans, customer facts, secrets,
exports and local work records stay outside its selected content. Projects can adopt the
three-file starter without adopting a particular knowledge folder, YAML map or workbench.
