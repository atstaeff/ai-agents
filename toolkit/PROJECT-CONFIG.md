# Project configuration

`AGENTS.md` is the shared entry point. Describe the project's purpose, scope, owners,
process, source locations, commands and review policy there, linking existing documents
instead of duplicating them. Local Markdown and authoritative web URLs are both valid.
A project YAML is optional. Do not require both formats to describe the same facts.

Minimal legacy `project.yaml` example (optional):

```yaml
schema_version: 2
project_name: Example
vision: PROJECT.md#vision
scope: PROJECT.md#scope
stakeholders: knowledge/stakeholders.md
process: CONTRIBUTING.md
work_tracking: Current request
knowledge_base: knowledge/README.md
decision_records: knowledge/decisions/
```

## Private plan settings

Keep personal plan paths, vault names, provider settings and credentials in user-local
host instructions/configuration. See [personal planning](../templates/agent-instructions/personal-planning.md).
The shared project needs only the policy that personal plans stay private. Respect
project restrictions before placing customer information outside approved systems.

## Existing YAML users

The [legacy schema](workspace.schema.json) and [validator](../tools/project_config.py)
remain supported for current tooling. Existing `workspace/workspace.yml` or linked
`project.yaml` maps locations; it grants no permission, installs no connector and executes
no commands. Do not add it to a new project merely to satisfy an AI workflow.

```sh
uv run tools/project_config.py --config /path/to/project/workspace/workspace.yml
```

The [minimal](../templates/customer-workspace/examples/workspace-minimal.yml),
[GitHub](../templates/customer-workspace/workspace/workspace.yml),
[Jira](../templates/customer-workspace/examples/workspace-jira.yml) and
[multi-repo](../templates/customer-workspace/examples/workspace-multi-repo.yml) examples
retain their existing format. The validator checks required fields, duplicate keys and
schema, not access or integrations. Do not keep competing default YAML files.

When reading an older configuration, interpret its work location as the shared assignment
home. Personal execution steps can remain in the Second Brain unless the project explicitly
requires a shared plan. Migrate optional metadata only when a real consumer needs it.
