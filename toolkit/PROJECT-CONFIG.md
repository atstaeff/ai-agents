# Project manifest

Keep one small project.yaml at the repository root. It is a flat list of references:
one field, one path or URL. All Markdown names and content directories are project choices.
See the [complete example](examples/project-kernel.md) or
[lean starter](../templates/lean-project/README.md).

## Fields

| Key | Value |
| --- | --- |
| `schema_version` | Integer `2`; the manifest format, not the product release |
| `project_name` | Project name |
| `vision` | Markdown file/section explaining intended users, problem, direction, current goals and success signals |
| `stakeholders` | Markdown file/section identifying affected groups, accountable roles, decision rights and acceptance responsibility |
| `scope` | Markdown file/section defining project responsibility, inclusions, explicit exclusions and material constraints |
| `process` | Markdown file/section describing the agreed workflow for people and AI, including relevant skills and checks |
| `work_tracking` | URL, path or named home of assignments and their live plans |
| `knowledge_base` | URL or path to current project knowledge |
| `decision_records` | URL or path to significant decisions and their reasons |
| `code_review` | Optional URL, path or named review home |

All fields except code_review are required. Values are nonempty strings, apart from the
integer schema_version. The four context/role/process references are local Markdown,
optionally with heading anchors. Several fields may point to one document. Local entries
can link authoritative external detail; all relative paths resolve from the project root.

Vision, stakeholders, scope and process are the four entry points. Goals belong with
vision; scope explains both what the project owns and where it stops. Stakeholders
identifies affected users/groups and who sets priority, decides and accepts results.
A small team can name the same person in several roles. Keep this short and factual.
The remaining locations make assignments, current knowledge and decision history findable.
Architecture, ideas, concepts and incident records can be linked from knowledge_base
when needed; they require no additional manifest fields.

The document referenced by process describes the workflow, collaboration rules, commands,
quality gates and action boundaries, with links to relevant detailed instructions and skills.
Keep executable checks in existing CI. They need no parallel YAML configuration. That guide
also explains any integration-specific details, multiple repositories or reporting needs.
The actual request supplies the selected ticket/PR; transient progress stays in that work item.

## Use it

The host's agent instructions point to project.yaml. The session reads its required sources,
follows the contribution guide and selects only relevant skills and affected knowledge.
Keep plan, acceptance, feedback and handoff at work_tracking; review evidence belongs at
the chosen review home. Maintain knowledge and decisions at their declared locations.

A path or URL grants no tool access, approval, integration or delegation. If access is
unavailable, report the exact gap, prepare an unsent update and continue independent
work within actual authorization. Use the [recovery contract](CONTEXT-RECOVERY.md)
when resuming. A skill link requires installed-host discovery or an explicit source read.

## Validate before adoption

From the toolkit checkout:

```sh
uv run --locked --group validation python tools/project_config.py --config /path/to/project/project.yaml
```

The validator checks the [schema](workspace.schema.json), required fields, types, unknown
fields, duplicate keys and conflicting conventional maps. It also checks the four required
local Markdown references: files/headings must exist, sections must contain content and
recognizable prompts must be filled. Comments, frontmatter and fenced examples do not
count as content. Referenced local sources must stay inside the project root.

The starter intentionally fails completeness checks until filled. During setup,
--structure-only checks schema compatibility without source readiness. Use the normal
command in the adopted project's CI. --project-root can make the expected root explicit.

The validator never executes content or fetches URLs. It cannot establish prose quality,
truth, remote access, approval or implementation. Review sources and perform the
[host check](PORTABILITY.md#verify-a-new-host-once). Its optional PyYAML/jsonschema dependencies
belong to this toolkit; adopting the manifest does not require copying its pyproject.toml.

## Existing tooling maps

Version-1 [GitHub](../templates/customer-workspace/workspace/workspace.yml),
[Jira](../templates/customer-workspace/examples/workspace-jira.yml) and
[multi-repository](../templates/customer-workspace/examples/workspace-multi-repo.yml)
examples remain readable. Their richer system/location and policy objects are a legacy
contract, not required structure for a new project.

When adopting the flat format, preserve actual locations as strings and link existing
working instructions. Move useful commands/policy into the contribution guide instead
of carrying their YAML blocks. Do not mix formats or maintain a second conventional map.
The schema source remains toolkit/workspace.schema.json; validation uses that exact file.
