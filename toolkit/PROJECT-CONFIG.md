# Project-owned tooling configuration

Use one `workspace/project.yaml` to declare where the project works. Link it from
`AGENTS.md`. If the project already has an equivalent configuration, keep that file
and declare its location instead; do not introduce a competing configuration.

The [GitHub example](../templates/customer-workspace/workspace/project.yaml) and
[Jira example](../templates/customer-workspace/examples/project-jira.yaml) demonstrate
one contract with different tools. The YAML is the canonical tooling map. Markdown
explains the process and links to it; avoid manually maintaining the same map twice.

## Small, explicit contract

| Field | Meaning |
| --- | --- |
| `version` | Configuration format version; currently integer `1` |
| `name` | Human-readable project name |
| `work` | Tracker/board containing the selected work item; that item owns its live plan and acceptance |
| `review` | Code review system and location, such as GitHub PRs or GitLab MRs |
| `knowledge` | Authoritative current domain and operational knowledge |
| `decisions` | Significant decision records, in a repository or customer knowledge system |
| `iteration_reports` | Existing home for iteration outcomes |
| `communication` | Permitted channel location; actual contact and action scope come from project rules |
| `working_agreement`, `stakeholders` | Project-root-relative paths or authoritative URLs for rules and owners |
| `commands` | Optional `setup`, `start`, `check` command strings or `null` when unspecified |

Each of the six location fields has a non-empty `system` and `location`. System names
are open strings, not an enforced vendor list. Locations may be URLs, project-relative
paths or clearly named dynamic locations such as `Assigned work item`. The actual task
supplies the selected ticket and linked review URL; do not overwrite the project config
for every assignment. Relative paths resolve from the project root, not the YAML folder.

Keep credentials, personal vault paths, model API keys and transient progress elsewhere.
This file describes ownership. It grants no access, configures no connector, sends no
messages and executes no commands. Host permissions and existing authorization still apply.
Different projects can use different tools without changing generic skills or agents.

## Agent behavior

1. Read project instructions and the declared config before selecting integrations or
   creating shared records. Load the working agreement and relevant owner information.
2. Read the actual assigned work item from `work`. Keep its plan, questions, acceptance
   and required approval receipt there. Link code review evidence from `review`.
3. Update only affected authoritative knowledge. If knowledge lives in Confluence,
   keep a pointer in `workspace/` rather than a separately maintained Markdown mirror.
4. Preserve project-owned status meanings and action scope. Plannotator is an optional
   review surface; save its actual approval receipt at the designated planning home.
5. If config is missing, use already explicit project instructions. If ownership is
   ambiguous or conflicting, resolve it before shared writes. Use a local record only
   when no assigned system owns the work; unavailable access is not such an absence.
6. If access is missing, prepare an unsent update and state the exact gap. Continue
   independent authorized work; never claim a remote update, approval or synchronization.

## Validate before adoption

Run the optional local validator from this toolkit:

```sh
uv run tools/project_config.py --config /path/to/project/workspace/project.yaml
```

It checks shape, version, required locations, unknown fields and duplicate YAML keys.
It does not access URLs, test credentials, execute commands or prove that a location
exists. PyYAML is isolated to this optional command; the main toolkit remains stdlib-only.
Replace example placeholders, confirm locations and perform the [host smoke check](PORTABILITY.md#verify-a-new-host-once).

The bundled graph generator reads local Markdown. A remote wiki requires a separately
authorized integration to generate a website or graph; this config does not implement one.
