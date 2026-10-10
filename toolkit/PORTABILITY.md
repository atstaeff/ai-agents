# One workflow, several tools

Keep product intent, engineering knowledge and reusable instructions independent of
model vendors. Use a small adapter for each host's discovery paths and capabilities.
Switching the model within one host does not require moving repository files.

## Separate four concerns

| Concern | Canonical home | What changes when switching |
| --- | --- | --- |
| Customer outcomes, decisions and current knowledge | Project-designated tracker and knowledge space | Keep the same sources and ownership |
| Shared process and reusable expertise | This catalog's `toolkit/`, `agents/` and `skills/` | Update once, then regenerate adapters |
| Discovery, tools, permissions and review integration | Generated host configuration | Translate and verify for the target host |
| Model, effort, credentials and inference location | Host/provider settings | Choose supported capabilities for the task |

`workspace/` is our convention, not a reserved LLM directory. `AGENTS.md` is a useful
shared entry point, but supported names, precedence and imports vary by host/version.
A `.claude/` directory is a Claude Code discovery convention, not a requirement to
use a Claude model in another host. Renaming a discovery directory alone does not
configure a tool to read it.

## Use the project’s tooling map

Read the [project configuration](PROJECT-CONFIG.md), normally `workspace/project.yaml`,
and the [operating model](OPERATING-MODEL.md#let-each-project-choose-its-tools).
Resolve authoritative locations and permitted actions from the project, not from the
model name, the current host, an available connector or this catalog’s examples.

| Purpose | GitHub-oriented project | Jira-oriented project |
| --- | --- | --- |
| Assignment and current plan | GitHub issue, prioritized in Projects | Jira ticket, prioritized in the project’s board |
| Code and review evidence | Linked GitHub PR | Linked GitHub PR or GitLab MR |
| Decisions and knowledge | Customer repository `workspace/` | Project-selected Confluence space or repository ADRs |
| Questions and approval | Designated issue/review channel | Designated ticket/review channel |

These are examples, not automatic integrations. Read and write only through available,
authorized tools. If access is absent, prepare the proposed update and state the gap;
never create a substitute tracker or claim synchronization. Keep local reusable skills
independent of remote customer systems and provider inference settings.

## Maintain sources once

1. Keep a short project `AGENTS.md` with the project's commands, constraints and pointers
   to relevant customer knowledge. Preserve the existing instructions when adopting this toolkit.
2. Edit reusable profiles here. Common frontmatter contains `name` and `description`;
   host fields such as `tools`, `mode`, `permission` and model options belong in adapters.
3. Export only the host layout you use into a dedicated destination. Generated files
   are deployment artifacts; contribute durable improvements to the canonical source.
4. Read the active assignment and selected skill bodies. A catalog's size is not a
   reason to load every profile, archive or reference into every session.

The export contains a shared `catalog/` reference copy and native entry files with
rebased links. This is generated duplication, not another source to maintain. Keep
`catalog/` beside the exported profiles. Switching hosts preserves the customer
workspace; permissions, tool names, model support and approval UX need a fresh check.

See [runtime setup](RUNTIMES.md) for supported exports. This repository's `CLAUDE.md`
imports `AGENTS.md`; it does not maintain a second set of repository rules. A generated
Claude bundle imports the shared workflow from its own `catalog/`. If a customer already
has `CLAUDE.md`, export separately and deliberately add the import to the existing file.
Do not replace customer rules with the toolkit's generic workflow.

## Verify a new host once

Use a disposable project and a harmless task:

- Confirm the expected instructions, selected skill and profile are discovered.
- Confirm the desired model/effort and the effective tools, including restrictions on Plan/reviewers.
- Follow a referenced file; verify its path resolves from the deployed bundle.
- If plan approval is required, verify comments, revision and approval survive the handoff.
- Run a representative project check and distinguish actual results from unrun checks.

An export test proves generated structure and links. It does not prove an installed
host's behavior, a model's quality or an OS security boundary. Local configuration and
local plugins also do not imply local inference: the provider controls that separately.

## Compatibility references

Reviewed on 2026-10-10; verify against the installed version when adopting an adapter.

- [OpenCode rules](https://opencode.ai/docs/rules/) and
  [skills](https://opencode.ai/docs/skills/): rule precedence and discovery paths.
- [Claude Code memory](https://code.claude.com/docs/en/memory): shared imports and
  version-dependent direct `AGENTS.md` support.
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents) and
  [skills](https://code.claude.com/docs/en/skills): native layouts and tool allowlists.
- [VS Code custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents):
  native profile fields; other Copilot surfaces may differ.
