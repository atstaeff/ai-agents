# Set up a shared workspace for people and AI

Copy the prompt below into a coding agent working in the target project. Make this
toolkit checkout available as reference, or provide the current linked schema, guide
and examples. Replace the bracketed input when known; the agent can discover the rest.

References: [adoption guide](../../toolkit/ADOPT-WORKSPACE.md),
[config contract](../../toolkit/PROJECT-CONFIG.md),
[schema](../../toolkit/workspace.schema.json), [lean starter](../lean-project/README.md)
and [extended example](README.md).
All are covered by the [repository license](../../LICENSE).

---

## Prompt

Set up this project so people and AI can collaborate efficiently using a small shared
workspace. Inspect the existing project first, then implement the necessary files and
references. Preserve customer conventions and minimize ongoing documentation work.
Use English for shared project artifacts and the user's language for conversation.

**Inputs**

- Project: the current checkout, plus any repositories explicitly in scope.
- AI Agents reference: [local toolkit checkout or repository URL and revision].
- Known tracker/board: [URL if available; otherwise discover or ask].
- Existing project instructions and the current user's authorization take precedence.

**1. Understand the project**

Read existing agent instructions, README, tooling configuration, relevant architecture
and decisions, setup/test commands and CI. Inspect known repositories and tracker links
with available read access. Determine the product outcome, relevant stakeholders and
the sources of truth for current work and durable knowledge.

Do not invent URLs, contacts, branch names, command results or permissions. Resolve
important missing information through a few specific questions; continue independent
setup work where possible. Preserve human wording and check for intervening edits.

**2. Use the actual configuration contract**

Read the reference toolkit's current `toolkit/PROJECT-CONFIG.md`,
`toolkit/workspace.schema.json` and matching YAML examples. Record the reference revision
in the setup report. Reuse a compatible existing project map. Otherwise adapt one example
as `workspace/workspace.yml` and link it from the project's agent entry point.

The version-1 contract uses six `system`/`location` mappings: `work`, `review`, `knowledge`,
`decisions`, `iteration_reports` and `communication`, plus `working_agreement` and
`stakeholders`. Use supported optional fields such as `method`, `repositories`, `planning`,
`flow`, `handoff`, `labels`, `reviewers`, `commands`, `quality_gates` and `actions` only
when useful. Do not invent a different schema or add unsupported `tools` or `sources`
sections. If the reference cannot be loaded, describe the gap and continue read-only
discovery; do not claim a configuration is compatible without its contract.

Map the real GitHub/GitLab repositories and review locations; use verified base branches.
Map the GitHub Project or Jira project/board to the relevant work and planning ownership.
If both systems exist, explain their distinct responsibilities and retain one live plan
per work item. Relative paths resolve from the target project root.

Keep credentials and local account/connector configuration outside the YAML. The file
declares locations and policy; it does not install an integration or grant authority.

**3. Create only useful entry pages**

Use the lean starter by default. Reuse or adapt `workspace/README.md` for the outcome,
boundaries, current sources, short working agreement and accountable decision roles.
Both required config fields `working_agreement` and `stakeholders` can point to this
entry. Add separate pages only when existing conventions or complexity justify them.
Together with the tooling map and agent entry, this is three maintained entry files.
Add ideas, concepts/specs, significant decisions, current knowledge and incident reviews
only when actual work needs them; create no empty folder hierarchy.

Merge a concise pointer into existing agent instructions, such as `AGENTS.md`. Respect
the host's actual discovery rules. Do not overwrite its instructions or assume that
an arbitrary Markdown file is loaded automatically.

Do not copy fictional ADRs, reports, customer names or issue numbers into production.
Create knowledge and decision pages when the work actually warrants them. Keep common
skills in their central maintained source, with host exports treated as generated output.

**4. Define how collaboration works**

Use lean clarification, short plan, build, verify and knowledge retention by default.
An existing project method takes precedence. Select BMAD or Spec-Driven Development
when useful, link their authoritative native artifacts and avoid a second live plan.
Keep completed execution as history, significant rationale in decisions and the current
contract/knowledge maintained. Add an actual optional host/session reference to a bounded
handoff; shared memory must remain usable without it.

Keep the project's chosen method: BMAD, Plan/Build/Review or its established procedure.
Do not introduce a second mandatory process beside it. A bounded assignment needs a
specific work-item reference, outcome, acceptance criteria and responsible decision role.
A board link alone is not authorization to process its backlog.

Document how the agent reads the assignment, keeps one concise current plan, asks
consequential questions, implements a small complete increment and links actual evidence
on a known revision. Derive expected checks from requirements and consumer behavior.
Missing access produces an unsent proposed update, not a mirror issue or invented sync.

If plan approval is required, preserve feedback and approval for the actual revision.
Use Plannotator only when available and adopted; record any manual review alternative.
Configure separate Plan/Build models or thinking settings only through supported host
options. A plan approval does not authorize merge or deployment.

Keep significant rationale in customer-owned ADRs as decisions arise. Update affected
current knowledge with behavior changes. Iteration reports link verified outcomes and
open work; they are not another live task list. Save a bounded handoff in the existing
planning home so a fresh session can resume from current shared sources.

**5. Respect action and publication boundaries**

Record already agreed actions and actual access. Do not infer customer permission from
a template value. During setup, do not post test comments, change tracker state, create
boards, merge or deploy without separate authorization for those actions.

Customer knowledge stays in customer-owned systems. A personal PARA vault may keep
authorized references and generalized learning, without becoming a customer-data mirror.
Publish only selected durable knowledge. Keep local work, archives, generated bundles
and private notes outside website content. Preserve an existing generated `docs/` directory.

**6. Validate and report**

Validate the target YAML using the toolkit's actual validator and schema. Check local
references and documented commands against the project; run appropriate agreed checks.
Report separately what passed, what was only inspected and what remains unverified.
Do not execute a command merely because it appears in a copied configuration.

Deliver the changed files, a concise information-ownership map, remaining questions and
access gaps, and one proposed real pilot assignment. Prepare a reviewable change through
the existing contribution workflow. Stop at the project's agreed review boundary.

Keep the setup small. No empty folder trees, duplicate trackers, copied chat histories
or large policy manuals without a concrete need.
