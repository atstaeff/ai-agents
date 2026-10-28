# Choose an AGENTS.md template

Use the plural uppercase filename AGENTS.md for project instructions. A catalog
*.agent.md file is a reusable role profile, created from the separate
[agent profile template](../catalog/agent-template.md). Do not rename one into the other.
Host discovery, nested scope and imports vary; verify the selected host's behavior.
Use the [runtime and capacity check](../delivery/runtime-check.md) to record observed
discovery, effective permissions, model/effort and handoff before depending on them.

| Situation | Template | Adapt before use |
| --- | --- | --- |
| Team building in one repository | [Team contract](../project-starter/AGENTS.md) | Source table, roles, project locations, tools, commands and knowledge homes |
| Established repository with existing rules | [Existing repository](existing-repository/AGENTS.md) | Existing process, tooling, source locations, commands and ownership |
| Central process or project documentation over the web | [Remote documentation](remote-docs/AGENTS.md) | Real URLs, adopted revision, project locations, tools, access and fallback |
| One product spanning repositories | [Multi-repository coordinator](multi-repository/AGENTS.md) | Repo/tool map, commands, contract ownership and integration order |
| Package or component-specific details | [Component instructions](component/AGENTS.md) | Applicable root process/tools, component locations, knowledge and checks |

Copy or merge the chosen template into the intended instruction scope; these are alternatives
and scoped additions, not five files required in each project. Fill every prompt and replace
example.org URLs. The [project starter](../project-starter/README.md) supplies matching
context/process pages. Link an existing owning section for each concern; keep detailed
policy and commands there. [Adoption](../../toolkit/ADOPT-PROJECT.md) explains the checks.

Distinguish binding project process from evolving technique/reference links. For binding
external policy, record both its immutable source URL and an explicit adopted SHA/version
in the project's contribution guide. A `main` branch link or current documentation page
is a reference until deliberately adopted. Use the [starter policy fields](../project-starter/CONTRIBUTING.md#policy-adoption)
and replace the literal URL pattern with the verified revision; create no extra manifest.

AGENTS.md links project facts and the working process. Keep current knowledge and decisions
in project-owned sources; use the [worked example](../../toolkit/examples/project-kernel.md)
and [knowledge templates](../knowledge/current.md). Docusaurus can publish the same Markdown
sources without a second editable copy. Public central methods never own private customer facts.
