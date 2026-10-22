# Your AI can write code. Does it know where your team works?

A fictional team gives an agent an assignment. It changes the old service because the
README still links there. It updates a GitHub issue while the current requirements live
in Jira. Its tests pass, but the architecture owner rejected that approach last month.
Someone opens the team chat and starts scrolling.

Generating code faster has not made the team easier to understand. Adding more agents
can make the same misunderstanding happen in parallel.

This workspace model gives people and AI a shared starting point: outcomes, real tool
locations, accountable decisions and evidence. It is a proposed working convention,
not a universal standard or a claim of measured productivity improvement.

## Give the teammate an introduction

A new colleague needs to know what the product does, where assignments live, which
repository to change, whom to ask and what counts as complete. Make that information
available to a fresh AI session too. Humans retain accountability for consequential
decisions and acceptance; the agent operates within its actual assignment and access.

Start with the [three-file lean starter](../templates/lean-project/README.md), or reuse existing equivalents:

| File | Question it answers |
| --- | --- |
| `AGENTS.md` | Where should this host start, and which project rules apply? |
| `workspace/README.md` | What outcome matters and which sources explain this project? |
| `workspace/workspace.yml` | Which systems and repositories own which information? |


Keep the short working agreement and decision owners inline in `workspace/README.md`.
The required YAML fields `working_agreement` and `stakeholders` may both point there.
Use separate pages only when existing conventions or coordination complexity justify them.

The YAML is a map. Markdown explains policy and rationale. Keep actual locations in
one map and link to it rather than maintaining a second copy in prose.

## Choose a small, valid starting point

All these files use the same [version-1 schema](workspace.schema.json):

| Arrangement | Copy and adapt |
| --- | --- |
| Local work with inline rules and owners | [Lean starter configuration](../templates/lean-project/workspace/workspace.yml) |
| One repository, few rules | [Minimal configuration](../templates/customer-workspace/examples/workspace-minimal.yml) |
| GitHub Issues and Projects | [GitHub configuration](../templates/customer-workspace/workspace/workspace.yml) |
| Jira, GitHub reviews and Confluence knowledge | [Jira configuration](../templates/customer-workspace/examples/workspace-jira.yml) |
| Jira assignments, two GitHub repositories and BMAD | [Multi-repository configuration](../templates/customer-workspace/examples/workspace-multi-repo.yml) |

Choose one configuration. Do not copy the entire fictional example into a real project.
Replace placeholder URLs, branch names and role references with verified project values.
Omit optional systems and fields the team does not use. If an equivalent config already
exists, keep it and link it from the agent entry point.

GitHub Project links belong in the relevant work/planning locations. Repository URLs
belong in `repositories`. For Jira, point `work.location` at the actual project or board;
the assignment supplies the specific ticket. Discover real API field IDs, board state
values and transitions through the available integration before writing. A board URL
neither selects an assignment nor establishes write access.

The schema supports the declared locations and process mapping. It does not install
connectors, create boards, start sessions or execute YAML as a workflow. This repository's
local dashboard edits optional work records; it does not operate Jira or GitHub for you.

## Adopt it in an existing project

1. Read existing instructions, architecture, CI, tracker conventions and access rules.
2. Adapt one YAML example and the compact entry from the
   [lean starter](../templates/lean-project/README.md). Use the
   [extended customer example](../templates/customer-workspace/README.md) when useful. Merge a pointer into the
   existing agent instructions. Preserve human content and existing tool discovery rules.
3. Identify authoritative owners for tasks, priority, iteration, status, reviews and
   knowledge. Agree action scope with the project owner; YAML does not grant permissions.
4. Run the [configuration validator](PROJECT-CONFIG.md#validate-before-adoption) against
   the target config, then the [host smoke check](PORTABILITY.md#verify-a-new-host-once).
5. Select one bounded, authorized real assignment with observable acceptance criteria.
   Run it manually before adding polling, orchestration or extra agents.

You can give the [English setup prompt](../templates/customer-workspace/SETUP-PROMPT.md)
to your coding agent to do this work. It requires the current schema and examples from
your toolkit checkout, not an invented format from memory. Sharing this guide and prompt
is enough to start a team discussion; the full agent catalog is optional for adopting
the information model.

## Keep the method and the tools project-owned

BMAD, Plan/Build/Review or an existing customer method can operate within this framework.
The method describes the delivery procedure; the workspace makes its sources and rules
findable. Record the chosen method in `method` and explain it in the working agreement.
BMAD installation and its own artifacts remain a separate project choice.

If a method uses local specifications, define their relationship to the tracker: for
example, the specification owns design detail and Jira owns priority and assignment.
Keep one live plan per work item. Missing tracker access calls for an unsent proposed
update, not a replacement issue and a second status list.

When project policy requires plan approval, review the specific revision. Plannotator is
an optional local review surface. Preserve actual comments and approval evidence in the
designated planning home. A consequential revision reopens review; merge and deployment
follow their own authorization. Plan and Build may use different models and supported
thinking settings through the host adapter; see [plan review](PLAN-REVIEW.md).

## Preserve useful memory

| Information | Authoritative home |
| --- | --- |
| Current scope, plan, questions and acceptance | Assigned issue or ticket |
| Implementation, review and actual check results | Repository, PR/MR and linked evidence |
| Significant choice and its reasons | ADR at the customer's decision home |
| Current domain and operational behavior | Customer-owned knowledge source |
| Iteration outcome and open follow-up | Short report linking the original evidence |
| Reusable general expertise | Central agents and skills catalog |

An ADR is useful when the reason will matter later. Write it when the consequential
choice arises, while alternatives are still known. An iteration report is a different
artifact; every closed ticket does not need an ADR. Accepted rationale stays historical,
with explicit replacement links when a new decision supersedes it.

Keep a bounded handoff in the existing planning home before changing session or model.
The next session checks it against current tickets, commits and decisions. It does not
need the entire conversation. Use the [recovery contract](CONTEXT-RECOVERY.md) for detail.

For personal knowledge, PARA can organize Projects, Areas, Resources and Archives. A
short entry page and relevant links are enough to begin; do not create a new index for
every folder. Keep customer-specific decisions with the customer. Store only authorized
personal references and reusable, appropriately generalized learning in a private vault.
Common skills retain one maintained source rather than a manually copied vault edition.

## Publish a useful view and measure the result

An existing Docusaurus site can render selected Markdown knowledge and related ADRs.
Use explicit relationships for the knowledge map. Keep sources separate from generated
output; an existing `docs/` publication directory can retain that purpose. Local plans,
archives, exports and private notes stay outside published content. Follow the
[integration guide](../templates/customer-workspace/examples/docusaurus-integration.md).
This toolkit's own documentation site uses Docusaurus; see [website development](../website/README.md).

After a few assignments, ask whether the agent found the right requirement and repository,
preserved the important decisions and delivered evidence reviewers could use. Observe
reconstruction effort, review/rework, time to acceptance and actual user benefit.
Compare similar assignments and record limitations. More generated files are not a
substitute for those outcomes.

Start with one real assignment. Add structure only when it solves an observed problem.
The [detailed concept](WORKSPACE-CONCEPT.md) covers ownership, recovery, migration,
publication boundaries and limitations when you need the full contract.

## Share and reuse

The concept, prompt, templates and toolkit are covered by this repository's
[MIT license](../LICENSE). Keep its copyright and license notice when redistributing
copies or substantial portions. Retain customer content in customer-owned sources.
The repository documentation is the maintained source; a copied prompt should identify
which toolkit revision supplied its schema and examples.
