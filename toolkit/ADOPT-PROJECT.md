# Adopt AGENTS.md in a project

Use one discoverable collaboration entry and shared project sources. Start with the
[project starter](../templates/project-starter/README.md) or choose an
[AGENTS.md variant](../templates/agent-instructions/README.md). All shared artifacts are English.

## 1. Inspect and preserve

Read existing agent instructions, project docs, repository state, tracker, CI, architecture
and decisions. Identify the actual owner and access boundaries. Merge into existing files;
never replace human wording or create a competing live plan.

## 2. Link the project sources

Fill the AGENTS.md source table with local Markdown or real, accessible web URLs:

| Source | Required information |
| --- | --- |
| Vision | Intended users, problem, direction, current goals and success signals |
| Stakeholders | Affected groups, priority, technical decision and acceptance roles |
| Scope | Included responsibilities, exclusions and material constraints |
| Process | Working method, tools, checks, relevant skills and action boundaries |
| Work/review | Actual issue/ticket home and code-review home |
| Knowledge/decisions | Current knowledge and significant rationale, including record status |

Several links may point to the same page. The default uses PROJECT.md and CONTRIBUTING.md;
these names and all content folders are choices. AGENTS.md is the entry convention. Verify
how the selected host discovers it; adapt host imports without duplicating project rules.
No project.yaml, TOML file or workspace folder is required.

## 3. Adopt the process and coordination

Use Clarify, Plan, Build, Verify, Integrate and retain; an existing adopted process takes
precedence. Keep shared outcome, criteria, feedback and team handoff at one work item. Name
the accountable human, active writer, scope, dependencies and integration owner.
For parallel work, separate working directories and agree shared interfaces and effective
claims. Serialize overlapping changes if the project has no shared coordination mechanism.
Keep BMAD/Spec-Driven artifacts at their native authoritative homes when selected.

## 4. Choose local or remote instructions deliberately

Local sources keep facts tied to the checkout. Central web policy can serve several projects.
In AGENTS.md explicitly instruct the session to read and follow the adopted process.
Pin shared policy to a verified source commit or maintained documentation version and record
what was actually read. A link does not install skills, guarantee retrieval or grant access.
Use the [remote documentation template](../templates/agent-instructions/remote-docs/AGENTS.md)
for fallback and version handling. Its example.org addresses are fictional placeholders.

## 5. Make knowledge recoverable

Use an existing knowledge index or start one when needed. Link current architecture,
contracts and operations separately from decision history. Store significant reasons as
they arise. Keep personal plans historical in the Second Brain; retain shared outcomes in the project. Before pausing, save result,
revisions, evidence/limits, blockers, pending writes and one next action in the assignment.
The [worked example](examples/project-kernel.md) shows record placement and relationships.

## 6. Verify the adopted project

Resolve every local source link, replace placeholder roles/URLs and run actual project
checks. Review the prose for missing facts; link validation cannot prove completeness.
Try one bounded real task, a fresh session and a required-source access failure. Verify
that the session chooses the correct source, preserves others' edits and reports real
check evidence. Test parallel integration before increasing concurrency.

Docusaurus is an optional reading view of those same sources. Publish only explicitly
selected material; keep private sources and local work outside the published set.

## Existing YAML and local workbench users

Keep a legacy tooling map only if existing tools need it; see
[optional YAML compatibility](PROJECT-CONFIG.md). Preserve real locations while moving
human/AI navigation into AGENTS.md. Do not leave contradictory process copies.
The optional local toolkit still uses workspace/work/ storage; --workspace means project
root. It remains independent of adopting the documentation model.

Personal planning follows the [shared workflow](WORKFLOW.md). Keep private vault paths out of shared sources; an unavailable vault means an unsaved session plan, not an automatic repository fallback.
