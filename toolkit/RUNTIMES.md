# Runtime adapters

Canonical entries use common `name` and `description` frontmatter. Exporters add
host fields and layout and rebase links into one shared `catalog/` copy.
The [portability contract](PORTABILITY.md) separates shared content, host configuration
and model selection; keep customer knowledge independent of all three.

| Runtime | Exported layout | Behavior |
| --- | --- | --- |
| OpenCode 1 | `agents/*.md`, `skills/<name>/SKILL.md`, `commands/`, `opencode.json` | Jörg/Plan/Build are primary; Product/Engineering/Delivery leads use `all`; other specialists are subagents |
| VS Code / Copilot | `.github/agents/*.agent.md`, `.github/skills/<name>/SKILL.md` | Project-native profiles; select in the host |
| Claude Code | `.claude/agents/*.md`, `.claude/skills/<name>/SKILL.md`, `CLAUDE.md` | Native profiles; select Jörg explicitly; Plan/reviewers are read/search-only |
| Herd (NickGuAI) | `herd/commanders/`, `herd/imports/*.bundle.json` | Native lead packages and portable schema-v2 imports; workers run in the adopted harness |
| Portable | `AGENTS.md`, `.agents/skills/<name>/SKILL.md`, `agents/*.agent.md` | Startup entry plus portable profiles; native agent discovery is host-specific |

## Use available Herdr

Herdr is the preferred terminal execution surface when installed and usable; it runs
the selected harness rather than replacing its discovery layout. Follow the
[Herdr policy](HERDR.md) for readiness, strong/high reasoning for complex work, economical
specialists, labelled tabs and resource-aware parallel dispatch. Export the catalog for
the underlying harness, then verify discovery and effective model/effort in that session.
The `herd` exporter below targets a separate optional fleet product.

## Native startup in this checkout

The checked-in `opencode.json` selects `task-orchestrator`, automatically loads session
rules and registers the curated team's 13 agent profiles through canonical file references.
Start installed OpenCode from this repository in the intended Herdr pane. The lead discovers
Herdr once, uses its native skill/policy when available and usable, and coordinates useful
parallel work without another delegation instruction. Other hosts load the same startup
contract through AGENTS.md or their exported entry.

This configuration supplies no model, provider credentials, permission allowances or
installation. Nonconflicting private per-agent model routes remain in the merged host
settings; inspect the effective result once. Reviewers retain native edit/bash/task denies.
Canonical skills can be read explicitly from the project; native skill-menu discovery
still needs the installed host's discovery paths or an export.

Maintain this thin native adapter from canonical metadata:

```sh
python3 tools/ai_toolkit.py opencode-config > opencode.json
python3 tools/ai_toolkit.py check
```

The check rejects stale configuration; the generator prints deterministic JSON and changes
no files itself. Do not store personal routes in this generated project file. Use normal
host model settings or the exported routes below. A running session may need a supported
refresh/new session to load a changed project configuration.

## OpenCode in WSL

Export into a dedicated directory, then set both variables when starting from a project.
`OPENCODE_CONFIG` loads JSON; `OPENCODE_CONFIG_DIR` loads agents, skills and commands.
Your provider setup stays separately configured. Project configuration and permissions
can affect the final merged setup.

The exported configuration permits access to its own reference catalog outside the
project and denies editing that catalog. It does not grant access to other external
directories or a private vault. Configure those separately in your host when needed.

```sh
python3 tools/ai_toolkit.py export --runtime opencode --preset engineering \
  --output "$HOME/.config/ai-agents/opencode"
cd /path/to/project
OPENCODE_CONFIG_DIR="$HOME/.config/ai-agents/opencode" \
OPENCODE_CONFIG="$HOME/.config/ai-agents/opencode/opencode.json" opencode web
```

By default the adapter uses `mode` and singular `permission`, with no fixed model or plugin.
Reviewers and Plan deny edit, shell and task tools by default. An explicit
`--plan-directory /absolute/private/project/plans` grants Plan Markdown editing and external
access only below that existing folder; local instructions record the location. See
[private planning](../templates/agent-instructions/personal-planning.md). This is a planning guardrail, not an OS sandbox: consider other
installed tools and project configuration. Build and Jörg use normal host permissions.
Do not install unrestricted write tools on a profile intended to be read-only.

Use /work-plan and /work-build when their agents are selected. /brain is available
with --preset knowledge or --agent second-brain. See [preset selection](CATALOG-GUIDE.md#select-a-bounded-runtime-catalog). Native delegation and interaction with
child sessions in OpenCode Web depend on your release. The toolkit adds no session
orchestration plugin.

For plan comments and approval before implementation, add `--plannotator` to the export.
Use `--plan-model`, `--build-model`, `--plan-variant` and `--build-variant` for independent
phase settings. These are optional and OpenCode-specific. See [the local plan review
guide](PLAN-REVIEW.md) for WSL startup, privacy, review states and model handoff.

### Configure the autonomous team once

Use `--preset team` for the Product (`product-manager`), Engineering (`lead-architect`)
and Delivery (`task-orchestrator`) leads plus Python/React/GCP/Terraform, test, review and
documentation expertise. Delivery is this preset's default conversation; all three leads
are directly selectable and callable. The normal `all` export also starts with Delivery;
smaller focused presets retain their existing entry when that lead is not selected.
An ordinary authorized assignment activates their coordination loop without another
"use Herdr", "delegate" or model-selection prompt.

Set qualified routes once in private host configuration, or export native OpenCode
per-agent settings with the optional flags below. Replace example model IDs and variants
with approved installed values before use; a variant named `high` is not universal.

```sh
python3 tools/ai_toolkit.py export --runtime opencode --preset team \
  --lead-model provider/strong-model --lead-variant high \
  --worker-model provider/economical-model \
  --review-model provider/review-model --review-variant high \
  --output "$HOME/.config/ai-agents/opencode"
```

The lead route covers Jörg, the three leads, Plan/Build when selected, GCP architecture
and test strategy. The worker route covers other selected specialists; the review route
covers code-reviewer and architecture-reviewer. These are initial role defaults: an
unexpected complex worker task returns to the lead/strong route. Profile permissions stay
intact. `--plan-model`/`--build-model` override their route and replace its variant; an
omitted phase variant uses the new model's default. Without route flags, no model is forced.
OpenCode otherwise inherits the caller's model for subagents, so delegation alone does not
establish a cheaper route. See its [agent reference](https://opencode.ai/docs/agents/).

Ensure every Herdr worker harness discovers the same authorized catalog and local route
settings. A variable set only for the lead's launch does not automatically configure shells
created by an already running Herdr server. Prepare each worker's actual environment with
the established host setup and verify profile/model/effort before dispatch; remote workers
need reachable copies and their own valid paths. The lead performs this routine setup.

After changing canonical profiles, re-export with the same local route options, restart
or refresh affected host sessions using the installed version's supported flow, and verify
the loaded instructions and effective settings once. An existing bundle or active prompt
does not update merely because Git changed. Preserve edited files; export to staging and
integrate local changes when ownership checks stop an update. Host permissions can still
block automation; report that exact setup gap instead of repeatedly requesting orchestration.

## Copilot

Export into another project. Existing edited/unmanaged files, including
`.github/copilot-instructions.md`, are protected. If you maintain those already,
export separately and integrate deliberately. Keep `catalog/` with the profiles;
their focused reference links point into it.

VS Code aliases `read` and `search` restrict reviewers and Plan to proposed changes.
Use a writing profile to apply a plan. Permissions and tool availability are
host-specific; other Copilot surfaces may interpret frontmatter differently.

## Claude Code

Export into a customer project or a staging directory, not this source repository:

```sh
python3 tools/ai_toolkit.py export --runtime claude --output /path/to/customer-project
cd /path/to/customer-project
claude --agent joerg
```

The adapter generates native `.claude/agents/` and `.claude/skills/` from the same
canonical entries. `CLAUDE.md` imports `catalog/toolkit/SESSION-RULES.md`. Existing
`CLAUDE.md`, profiles and edited generated files are protected: export to staging
and integrate the import into existing instructions deliberately when necessary.
Keep the shared `catalog/` in the project. No model, effort, plugins, MCP servers or
permission bypasses are configured; the user's host settings remain responsible.

Plan, code-reviewer and architecture-reviewer allow only `Read`, `Grep` and `Glob`.
They return proposals/findings to the coordinating session; that session performs
record updates, required approval and executable checks under its own permissions.
Other profiles inherit host tool availability. A native subagent does not provide
the same interaction or plan-approval UI as an OpenCode primary agent. The optional
Plannotator/model/variant export switches remain OpenCode-only.

After installation, use `/agents` to inspect discovery and `/context` to inspect
loaded instructions. Run the [host smoke check](PORTABILITY.md#verify-a-new-host-once).
Adapter tests cover file formats, links, restrictions and safe updates; they do not
establish behavior in your installed Claude Code version.

## Herd fleet imports

Export selected lead commanders and skill bindings with `--runtime herd`. Import a
portable bundle through Herd Marketplace's **Install from file** action. Actual worker
execution, models, effort, budgets and permission policy remain configured in Herd and
its underlying harnesses. No running fleet, customer memory or scheduled automation is
created by export. Follow the [native orchestration guide](ORCHESTRATION.md) for commands,
pinned schema sources and an installed-host exercise.

Ponytail and Graphify are optional native integrations; [Herdr](HERDR.md) is the
preferred terminal surface when available and usable. See the
[integration guide](INTEGRATIONS.md) for their distinct responsibilities. A generated profile does not install a third-party tool.

## Updates and privacy

Re-export after source updates. `.ai-toolkit-manifest.json` tracks owned paths and
hashes. Edited or unmanaged files are not silently overwritten. `--dry-run` checks
without writing; `--force` explicitly permits replacing files at planned paths.
Updates validate manifest paths and content hashes, serialize cooperating exporters and
keep a recovery journal for a multi-file update. They write only changed files and
remove obsolete owned files. Identical files,
including the manifest, keep their timestamps. JSON output reports `changed`,
`unchanged` and `removed` file counts; the manifest is excluded. With `--dry-run`,
these counts describe the proposed update. Use a dedicated destination.

If a process was killed, preserve the destination and transaction journal. Check the PID
in `.ai-toolkit-export.lock` and confirm the owning exporter has stopped before removing
that lock. Rerun the same export to recover the unfinished transaction; preserve and
reconcile any reported intervening edit. Do not use `--force` as a recovery shortcut.
The lock coordinates toolkit exporters, not arbitrary editors or distributed hosts.

Re-export with the same optional phase settings; omitted options restore the defaults.

Keep model keys and private vault paths in local configuration. The catalog/dashboard
uses no remote runtime service; AI provider calls are managed by your host.

Sources: [OpenCode agents](https://opencode.ai/docs/agents/),
[configuration](https://opencode.ai/docs/config/), [skills](https://opencode.ai/docs/skills/),
[VS Code custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents),
[Claude Code subagents](https://code.claude.com/docs/en/sub-agents),
[skills](https://code.claude.com/docs/en/skills) and
[memory imports](https://code.claude.com/docs/en/memory).
Structural checks do not establish model behavior or installed web UX compatibility.
