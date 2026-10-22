# Project manifest

Use one filled project.yaml at the repository root. It is the required machine-readable
entry for people and AI. All document names and content directories are project choices.
Start with the [complete project-kernel example](examples/project-kernel.md) or the
[lean starter](../templates/lean-project/README.md).

## Version 2: explicit required information

The manifest references project facts and procedures rather than copying their prose.
Several required fields may point to sections of one Markdown document. The starter's
PROJECT.md and CONTRIBUTING.md are defaults; neither filename nor a workspace/ folder
is required. The host's existing entry points the session to project.yaml.

| Required key | Meaning |
| --- | --- |
| `schema_version` | Integer `2`; the manifest format, not the product version |
| `project_name` | Human-readable project name |
| `context.vision` | Markdown source explaining the intended users, problem and direction |
| `context.goals` | Markdown source for current observable outcomes and success signals |
| `context.scope_and_boundaries` | Markdown source for included responsibilities, exclusions and constraints |
| `responsibilities` | Markdown source naming accountable roles and decision/acceptance responsibilities |
| `contribution_guide` | Markdown source defining how people/AI work, select skills, verify and complete work |
| `work_tracking` | System/location owning assignments, live plans, acceptance, status and feedback |
| `code_review` | System/location owning implementation review and check evidence |
| `knowledge_base` | System/location owning current domain, architecture and operational knowledge |
| `decision_records` | System/location preserving significant choices and their reasons |
| `communication` | Permitted collaboration location; actual contact/action scope follows project rules |

Each system/location field is an object with nonempty `system` and `location` strings.
System names are open, not a vendor allowlist. Locations can be URLs, project-relative
paths or explicit dynamic locations such as comments on the assigned work item.
Required context/role/process references are local Markdown files, optionally with
ATX heading anchors. They may link authoritative external detail. Paths resolve from
the manifest directory, which is the project root.

The actual request supplies the selected ticket and review URL. Do not change the
manifest for each assignment. Keep transient progress, credentials, personal notes and
model/provider settings outside it. The manifest installs no integration, grants no
permission and executes no command. Generic skills explain technique and tool contracts;
project sources supply actual ownership, commands and action boundaries.

## Agent behavior

1. Read host/project instructions, project.yaml and its required source references.
   Resolve context, responsible owners and contribution rules before dependent work.
2. Load only relevant skills and affected knowledge/contracts/decisions. Selecting a
   skill does not require another session; Markdown links require explicit reads or
   working installed-host discovery.
3. Read the actual assigned work item from work_tracking. Keep plan, questions,
   acceptance, feedback and handoff there; link code_review evidence without mirroring work.
4. Update affected knowledge_base and decision_records sources at their declared homes.
   If a wiki owns knowledge, retain a pointer rather than an independently edited copy.
5. Follow actual permissions and required review of the current revision. If ownership
   conflicts, resolve it before dependent shared writes. If access is unavailable, name
   the blocked operation, prepare an unsent update and continue independent authorized work.
6. Use the [recovery contract](CONTEXT-RECOVERY.md) across interruptions. A manifest,
   role or method label is not approval, delegation, synchronization or an atomic claim.

## Validate before adoption

From the toolkit checkout, run:

```sh
uv run --locked --group validation python tools/project_config.py --config /path/to/project/project.yaml
```

The validator checks the [JSON Schema](workspace.schema.json), required keys, types,
unknown/mixed-version fields, duplicate YAML keys and competing conventional maps.
Version 2 also checks the five required local Markdown references: files and ATX heading
anchors must exist; referenced sections need content and no recognizable prompt placeholders.
Frontmatter, comments and fenced examples do not count as content. Sources must stay
inside the project root; their directory names are unrestricted.

The starter intentionally fails source-completeness checks until its prompts are filled.
Use `--structure-only` during setup to inspect schema compatibility; it does not establish
source readiness. Run the normal command in the adopted project's CI. The optional
`--project-root /path/to/project` makes the expected root explicit; a version-2 manifest
must be that root's project.yaml.

The validator does not fetch URLs, judge prose quality/truth, test credentials or tool
access, execute commands or prove implementation. Review sources and perform the
[host smoke check](PORTABILITY.md#verify-a-new-host-once). PyYAML/jsonschema remain optional
validation dependencies; the main toolkit runtime stays standard-library-only.

## Optional fields

Add only the parts actually used by the project. Missing optional values are unspecified,
not permission to guess or create a board, reviewer notification or automation.

| Key | Content |
| --- | --- |
| `delivery_method`, `profile` | Adopted method and arrangement; contribution_guide defines the actual procedure |
| `progress_reporting` | Existing reporting system/location, only if separate reporting is useful |
| `repositories` | Unique name, location, optional local path and default_branch |
| `commands` | Optional setup/start/check strings or null; actual verified commands, never auto-executed |
| `quality_gates` | Name, command and boolean required for each actual project check |
| `planning` | Explicit priority/iteration/engineering-status ownership when genuinely split |
| `flow` | Actual board-state mapping, additional blocked property and completion policy |
| `handoff` | Existing assignment section and a shared template path |
| `labels`, `reviewers` | Real adopted coordination values; no implicit notifications or authority |
| `actions` | within_assignment, separate_authorization or forbidden for supported action categories |

Action categories are edit_assigned_branch, open_draft_pr, update_work_item, ask_questions,
merge, deploy, delete and change_access. Effective permissions and user authorization
still apply. The local task table retains its existing four states; flow is a project
board description, not a tracker implementation. See the
[detailed project concept](WORKSPACE-CONCEPT.md) for process, storage and publication.

## Existing version-1 tooling maps

The [GitHub](../templates/customer-workspace/workspace/workspace.yml),
[Jira](../templates/customer-workspace/examples/workspace-jira.yml),
[minimal](../templates/customer-workspace/examples/workspace-minimal.yml) and
[multi-repository](../templates/customer-workspace/examples/workspace-multi-repo.yml)
examples remain readable as legacy contracts. They use version: 1 and the older name,
work/review/knowledge/decisions/iteration_reports and working_agreement/stakeholders keys.
Their checks do not establish version-2 completeness.

For adoption, preserve actual values while mapping the old fields to the explicit keys
above; add the required context references and keep one root project.yaml. Never mix
old and new key names or keep a second conventional workspace map. Validation detects
conflicts without deleting or renaming files. The older standalone concept format
(schema_version with sources/paths) is a separate example, not another accepted contract.

Schema source: toolkit/workspace.schema.json. The validator reads that exact local schema,
with both version contracts; it neither fetches remote schemas nor maintains a hidden
second list of permitted fields.
