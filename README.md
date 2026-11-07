# AI Agents

A practical engineering kit for building and maintaining software with AI. Use focused
[agents](agents/README.md), [skills](skills/README.md) and [templates](templates/README.md)
with the tools, permissions and tracker your project already uses.

[Documentation](https://atstaeff.github.io/ai-agents/) ·
[First task](website/content/getting-started/quick-start.md) ·
[Engineering process](engineering/process/README.md)

## Keep the tools ready locally

On Linux or WSL with systemd, install and configure Herdr and OpenCode, then run:

```sh
python3 scripts/local_agents.py doctor
python3 scripts/local_agents.py install
python3 scripts/local_agents.py status
```

This enables both user services for this checkout. Use `--project /path/to/project`
for another checkout. See [local runtime setup](scripts/README.md) for login startup,
ports, logs, connecting through Herdr and uninstalling. Use the native host and
[export a focused catalog](toolkit/RUNTIMES.md) when persistent services are unnecessary.

## Work from Markdown

Start with [AGENTS.md](AGENTS.md). It maps the project and routes a session to the
relevant [process step](engineering/process/README.md), skill, agent and decision.
Choose the steps and folders that fit your project using the
[Markdown project starter](templates/markdown-project/README.md). A small correction
can go directly from the affected source to a change and checks.

The existing issue or ticket owns scope and acceptance; the PR owns the changes and
review evidence. Record consequential decisions when they arise. Keep current behavior
and ADR rationale in their [project knowledge homes](knowledge/README.md). No workspace
manifest or local task tracker is required.

Use [Herdr](toolkit/HERDR.md) when available. A lead coordinates useful independent work,
chooses qualified model routes and verifies the combined result. The host owns model
execution and permissions. The [operating model](toolkit/OPERATING-MODEL.md) explains
the delivery responsibilities.

## Repository map

| Path | Purpose |
| --- | --- |
| `agents/`, `skills/` | Canonical roles and reusable techniques |
| `templates/` | Adaptable project layout, assignments, ADRs and reviews |
| `engineering/process/`, `knowledge/` | This repository's procedures, facts and decisions |
| `scripts/` | Local Herdr and OpenCode service management |
| `toolkit/`, `tools/` | Guidance and optional validation, export and compatibility tools |
| `examples/`, `reference-repos/` | Worked examples and reference implementations |
| `website/`, `docs/` | Docusaurus source and generated Pages output |

For maintenance, see [contributing](CONTRIBUTING.md) and the
[verification runbook](toolkit/REPOSITORY-WORKFLOW.md). The
[optional workbench](toolkit/WORK-RECORDS.md) and legacy project config are compatibility
features. Existing local records stay outside the tracked source. The catalog and tooling
are [MIT licensed](LICENSE).
