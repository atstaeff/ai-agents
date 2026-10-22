# Optional legacy YAML configuration

New projects use [AGENTS.md](../AGENTS.md) and its linked sources; see
[project adoption](ADOPT-PROJECT.md). No YAML file is required. This page preserves the
existing declarative configuration contract for tools/projects that still use it.
The validator does not discover or validate AGENTS.md and cannot establish prose quality.

## Version 2: optional flat manifest

An existing project may keep one root project.yaml when its tooling needs structured
references. This illustrative snippet requires real referenced sources before use:

```yaml
schema_version: 2
project_name: Customer Portal
vision: product/overview.md#vision-and-goals
stakeholders: team/stakeholders.md
scope: product/overview.md#scope-and-boundaries
process: CONTRIBUTING.md
work_tracking: https://github.com/example/customer-portal/issues
code_review: https://github.com/example/customer-portal/pulls
knowledge_base: knowledge/
decision_records: architecture/decisions/
```

All fields except code_review are required within this optional format. Values are
nonempty strings except integer schema_version. The four context/process references
must be local Markdown, with optional section anchors; they may link remote detail.
Work/review/knowledge/decision locations are strings. These restrictions belong to the
legacy YAML validator, not to the AGENTS.md entry: AGENTS.md may directly adopt web sources.

## Version 1: existing tooling maps

[GitHub](../templates/customer-workspace/workspace/workspace.yml),
[Jira](../templates/customer-workspace/examples/workspace-jira.yml) and
[multi-repository](../templates/customer-workspace/examples/workspace-multi-repo.yml)
examples remain readable. Their nested system/location and policy blocks are compatibility
material, not required project structure. The extended fictional example uses workspace/
so existing graph/adapter behavior and paths remain reproducible.

## Validate an existing map

From the toolkit checkout:

```sh
uv run --locked --group validation python tools/project_config.py --config /path/to/project/project.yaml
```

The validator checks schema, types, unknown/duplicate keys and conflicting conventional
maps. Version 2 also checks its four required local Markdown files/sections, emptiness,
obvious prompts and paths staying inside the declared project root. --structure-only is
a setup/schema check and does not establish source readiness. No content is executed or
URLs fetched. Optional PyYAML/jsonschema dependencies belong to the toolkit; customers do
not need its pyproject.toml to adopt AGENTS.md.

The source schema remains workspace.schema.json for compatibility. Existing YAML tests
remain in CI; the default repository/starter no longer needs a manifest. When retiring a
map, preserve real source locations in AGENTS.md or its linked project pages and first
check for external tools that depend on it. Do not keep contradictory process copies.
