# Project context and workspace: shared memory for people and AI

For a short explanation you can share with a team and a practical first setup, start
with [Adopt the workspace](ADOPT-WORKSPACE.md). Use the
[project setup prompt](../templates/customer-workspace/SETUP-PROMPT.md) to configure an
existing project. This page remains the detailed contract behind those entry points.

Use required root `project.yaml` as the manifest pointing to the project map: vision, goals, boundaries, owners, key sources
and working method. The default PROJECT.md and CONTRIBUTING.md explain context and
working policy; their names and folders are project choices. The host's entry makes the
manifest and its sources discoverable. This repository uses workspace/ for selected
records and optional local work; adoption requires no directory with that name.
People and AI use the same sources. Another person or a fresh session must be able to
continue an assignment without the previous conversation.

This concept combines the [operating model](OPERATING-MODEL.md),
[working contract](WORKFLOW.md), [configuration](PROJECT-CONFIG.md) and
[recovery contract](CONTEXT-RECOVERY.md). These documents provide focused operational
instructions; this page explains how their parts fit together.

## 1. Outcomes and principles

- Preserve why a significant choice was made, including alternatives and consequences.
- Keep one authoritative home for each fact and one live plan per assignment.
- Load relevant context from shared sources instead of growing a mandatory chat history.
- Make AI a sparring partner: inspect assumptions, propose alternatives and identify
  evidence that could change the recommendation. Work within the assigned decision rights.
- Keep customer knowledge with the customer and general expertise in the agent catalog.
- Scale ceremony to uncertainty and consequence. A clear small correction stays direct.

The workspace is a team convention, not a model memory API or a new project-management
system. Existing customer methods remain valid, including their own planning process,
Plan/Build/Review or another adopted method. Use an existing equivalent entry point
when the project already has one.

Start with the [lean starter](../templates/lean-project/README.md): AGENTS.md, PROJECT.md,
CONTRIBUTING.md and one config. Keep owner roles inline in the project map and working
rules in the contribution guide. Reuse existing equivalents without duplicate entries.
Only root project.yaml is a fixed file convention. All other paths below are examples,
not a mandatory folder hierarchy or checklist of files to create.

## Project facts, process and skills

The project entry answers six questions: what is the vision and goal, what are the
boundaries, who decides, where are the key sources, how do we work, and how does a
session resume? Keep short answers inline or link their existing detailed Markdown.
The same entry works at the main repository root or in a linked project repository.

The host instructions direct the session to root `project.yaml` and its referenced
entries. In the default starter, PROJECT.md owns project facts and navigation;
CONTRIBUTING.md owns the
project's contribution policy and maps activities to reusable skills. A skill explains
how to perform its focused activity and use the relevant tool contracts; YAML supplies
project source locations; the contribution guide supplies commands and working policy. Current user/host
instructions supply effective authority. A generic skill cannot override project policy.

For example, vision/scope uncertainty selects product-discovery; an ordinary larger
assignment selects work-management; implementation selects the relevant language or
engineering skill; testing and pr-crafting support verification and review. The
[repository-contribution skill](../skills/delivery/repository-contribution/SKILL.md)
resolves this route in an unfamiliar repository. Load only relevant skill bodies and
references, not every linked page recursively. Hosts must discover the installed skill
or the session must read it explicitly; Markdown links are navigation, not execution.

Reuse existing entries and a contribution guide. No separate VISION.md, process tree,
role directory or project/ folder is required. The name Project describes the shared
context; workspace/ remains the technical area used by the local tooling. Older
workspace entries and explicitly linked configurations remain valid.

## 2. Folder and information ownership

Only project.yaml is fixed. Other paths below illustrate this repository and the optional
local workbench, relative to the project root. Declare different document names and
directories in the manifest when they fit the project. Create only useful content.

| Path | Purpose | Update and publication rule |
| --- | --- | --- |
| `AGENTS.md` | Entry instructions, commands and pointer to workspace config | Preserve project rules; keep short |
| `PROJECT.md` | Vision, goals, scope, owners, key sources and process entry | Root project map; link existing detail |
| `CONTRIBUTING.md` | Working process, project rules and reusable skill selection | Project-specific policy; link shared technique |
| `project.yaml` | Required references for vision, goals, boundaries, roles, process and tool ownership | Root manifest; one configuration, no credentials |
| `workspace/working-agreement.md` | Optional detailed authority, review and completion policy | Link from CONTRIBUTING.md when already useful |
| `workspace/stakeholders.md` | Optional separate decision-role map | Keep roles in PROJECT.md initially; use verified contacts within scope |
| `workspace/ideas.md` | Optional opportunities and hypotheses | Disposition and links, not a second delivery backlog |
| `workspace/concepts/` | Optional concepts/specifications | Declare a living contract or historical snapshot; link current sources |
| `workspace/incidents/` | Optional material incident reviews | Preserve facts and link owned follow-up; explicitly review publication scope |
| `workspace/decisions/` | Significant ADRs and their historical rationale | Preserve accepted reasoning and replacement links |
| `workspace/knowledge/` | Current domain, architecture and operational knowledge | Update affected pages when behavior changes |
| `workspace/iterations/` | Outcomes, learning and open follow-up | Link evidence; no duplicate live task list |
| `workspace/work/` | Optional local record for an otherwise unassigned larger outcome | Local and ignored by default |
| `workspace/archive/` | Completed local work records | Local history, excluded from routine context |
| `workspace/generated/` | Replaceable previews and derived output | Ignored; never a source of truth |
| `workspace/exports/` | Optional generated host bundles | Ignored; edit canonical catalog sources |

The `--workspace` CLI option still means the **project root**. For a project at
`/path/to/project`, pass that root; the store writes `workspace/work/` beneath it.
Passing `/path/to/project/workspace` would create an unintended nested workspace.

The local store uses this conventional folder name. A customer can retain a different
knowledge directory through the declared locations, but the store does not provide a
configurable alternate record root. Resolve an existing conflicting `workspace/` before
using local records; adopting documentation never authorizes overwriting customer files.

## 3. One plan, even with several tools

| Project arrangement | Live assignment and plan | Code and proof | Durable knowledge |
| --- | --- | --- | --- |
| GitHub | Assigned issue; Projects owns adopted board fields | Repository, PR and checks | Project-selected repository or wiki |
| Jira with GitHub | Jira ticket; no mirror GitHub issue | Linked GitHub PR and checks | Repository ADRs and/or Confluence |
| Split product and engineering planning | Jira owns product/capacity; explicitly scoped engineering items own technical increments | Linked repository changes per increment | Shared customer-owned sources |
| Larger local request with no assigned tracker | One `workspace/work/<slug>.md` | Local changes and actual checks | Existing project documentation |

For split planning, use a stable delivery-object reference and explicit parent/child
relationships. Define ownership per field and work item before writing. Do not maintain
two editable copies of the same live plan. A missing connector does not change ownership.
Prepare an unsent proposed update and continue only independent authorized work.

## 4. The YAML contract

Use the [GitHub example](../templates/customer-workspace/workspace/workspace.yml),
[Jira example](../templates/customer-workspace/examples/workspace-jira.yml) or this
[repository's configuration](https://github.com/atstaeff/ai-agents/blob/main/project.yaml). All use the same
[JSON Schema](workspace.schema.json) and [validator](../tools/project_config.py).

Version 2 is a flat list: project_name; vision, goals and scope_and_boundaries references;
responsibilities and contribution_guide; work_tracking, knowledge_base and decision_records.
Only code_review is optional. Values are simple paths/URLs or named work/review homes.
The [manifest contract](PROJECT-CONFIG.md) defines validation and the schema-only setup check.

The contribution guide owns the method, commands, quality checks, communication and action
boundaries. Link existing CI, role documents, repository lists and reporting conventions
there instead of duplicating policy in YAML. The richer version-1 examples remain readable
for existing projects; their nested blocks are not the default kernel.

The YAML is declarative. Validation checks schema and version-2 local source completeness;
it makes no connection, creates no board or labels, executes no commands and grants no authority. Confirm actual access and adopted policy
in the chosen host. Do not invent GitHub Project IDs, Jira fields or reviewer approval.
Relative paths resolve from the project root, not from the configuration directory.

The older standalone v0.2 concept example used `schema_version`, `sources` and `paths`;
it was explicitly a separate example schema. Map those ownership values into this
contract rather than copying its YAML verbatim. Existing toolkit version-1 configs
remain readable without the new fields. New projects use one root project.yaml; keeping
a second conventional workspace map is rejected as ambiguous.

## 5. Initial project setup

1. Determine the outcome, scope, quality constraints and accountable people.
2. Inspect the existing tracker, repositories, instructions, contracts and decisions.
3. Adopt the minimum entry pages and map actual locations in the YAML. Preserve existing
   policies and private content; do not copy fictional customer details into production.
4. Agree which actions are allowed within an assignment, which require a decision and
   which tools or credentials the host actually has.
5. Record significant initial choices and unresolved assumptions. Architecture evolves
   during delivery; do not invent historical decisions or require all design up front.
6. Validate the config and perform the [host smoke check](PORTABILITY.md#verify-a-new-host-once).
7. Select one bounded real assignment and run the manual flow before adding orchestration.

## 6. Delivery and sparring

Start from an outcome and observable criteria. Inspect relevant constraints before
proposing the smallest complete increment. When uncertainty matters, compare alternatives,
state the recommendation and tradeoffs, and name what evidence would change it.

Follow the project's review policy. Routine reversible implementation details within the
assigned scope can proceed. An incompatible API change, changed data meaning, material
cost/security consequence or disputed architectural constraint needs the accountable role.
Do not ask for every routine step or silently reinterpret consequential requirements.

Implement, exercise the affected behavior and link criteria to actual results on a
specific revision. A second AI review is not automatically independent approval.
Update affected knowledge and significant decisions as they arise. The iteration report
links these outcomes and unresolved items; it is not the first place to reconstruct rationale.

| Trigger | Action | Result |
| --- | --- | --- |
| New assignment or resumed session | Read current sources and choose a bounded increment | Current scope and next step |
| Required decision or plan review | Obtain the accountable owner's decision on the current revision | Preserved decision or approval evidence |
| Authorized increment | Implement and verify criteria; save evidence and handoff | Reviewable result on a known revision |
| Changes requested | Revise the affected increment and repeat relevant checks | Updated result and feedback disposition |
| Acceptance at the completion point | Close work and link reusable learning | Verified outcome, with impact still separately measured |

## 7. Decisions, current knowledge and recovery memory

| Question | Read or update |
| --- | --- |
| Why did we choose this approach? | ADR with context, alternatives, evidence, decision and consequences |
| What currently applies? | Accepted decisions in scope and current contracts |
| What is actually implemented? | Code, tests and operational evidence |
| What are we trying to change? | Current assignment, criteria and human feedback |
| Where do we continue? | Bounded handoff in the existing planning home |

Use stable ADR IDs and explicit statuses. A proposed replacement cannot revoke an
accepted decision. A substantive replacement gets a new ADR, a `supersedes` relation
and an updated old status; preserve the old reasoning. Correct factual metadata without
silently rewriting accepted rationale. Resolve contradictions by scope and authority,
not by the newest file timestamp or the current code alone.

Record useful outcomes and reasons, not private reasoning traces or full chat dumps.
The workspace supports shared project memory; it does not make model-internal memory
reliable or replace the authoritative sources.

## 8. Context loading and fresh sessions

Load the short entry, config, applicable rules and actual assignment first. Follow links
to affected code, tests, contracts and decisions. Search the bounded project when a
relevant source is missing; an absent link does not prove that no decision exists.
Load full documents only as needed. Do not load the entire archive or every agent/skill.

Before resuming, compare the current sources with the last handoff: assignment revision,
relevant commits, ADR status, current approval and tested criteria. Refresh affected
context after material changes. An unrelated commit does not require rereading everything.
Do not omit relevant constraints merely to satisfy an arbitrary token budget.

Save the [bounded handoff](../templates/customer-workspace/workspace/handoff.md) after
material increments and before a known pause or session/model switch. Include unsaved
work and pending external writes. One current summary belongs inside the assigned work
item or existing local record; the template file is not another running plan.

## 9. Flow, completion and failure recovery

Map Todo, In Progress, In Review and Done to the adopted board. Blocked is an additional
property with reason, owner and resume condition; preserve underlying flow position and
WIP. A team's existing equivalent mapping may differ when explicit.

For code, Engineering Done requires criterion evidence, required review and authorized
integration at the agreed completion point. Acceptance, merge, deployment and measured
impact remain distinct facts. Cancelled, duplicate and not-implemented closures do not
count as delivered. An investigation can finish with a verified answer.

After a timeout, inspect the original system for the intended write before retrying.
Git, trackers and review systems are not one atomic transaction. Reconcile partial
effects and preserve intervening human edits. One writer owns an assignment or separate
bounded scope. Multiple workers need an effective shared claim and recovery policy;
an assignee field alone is not an atomic lock. Record each relevant repo revision and
integration order for multi-repository work.

The toolkit implements local record persistence, stale-write protection and exports.
It does not implement tracker polling, cross-system transactions, distributed claims
or an agent/session runner. The [runner example](../templates/customer-workspace/examples/local-runner.md)
describes an integration contract rather than an installed service.

## 10. Publication and privacy

One directory can hold several information types without granting them the same audience.
Local `work/`, `archive/`, `generated/` and `exports/` are ignored by default and excluded
from the example knowledge graph and Docusaurus publication. Git ignore rules alone
do not stop a website from reading files on disk.

The Docusaurus fragment publishes named root entry pages and the selected knowledge, decisions
and iteration directories. Review that allowlist and sources before adopting it. Do not
add local work directories to the site. Configuring `workspace/` as a broad content source
without exclusions would publish local notes. Keep secrets and personal material outside
public repositories, and enforce the customer's access requirements on the published site.

`docs/` remains generated Pages output in this repository. Its Docusaurus site reads explicit
canonical sources through `website/generate.py`; it does not recursively publish the root workspace.
The export manifest `.ai-toolkit-manifest.json` remains an adapter-ownership file so existing
bundles retain protection against overwriting human edits. It is not a project-memory folder.

## 11. Moving existing local work

Stop agents, dashboards and editors that write records. Back up the project. Then run:

```sh
python3 tools/ai_toolkit.py work --workspace /path/to/project migrate --dry-run
python3 tools/ai_toolkit.py work --workspace /path/to/project migrate
python3 tools/ai_toolkit.py work --workspace /path/to/project list
```

Migration moves `.ai/work/` and `.ai/archive/` into `workspace/` without changing file
contents. It checks both destinations before moving anything, refuses existing target
directories and rejects symlinks. It does not merge conflicts, rewrite relative links,
move unknown `.ai` content or grant permission to disclose records. Resolve conflicts
and update affected links deliberately. The empty old parent directory is removed;
remaining unknown content is preserved and reported by `legacy_directory_remaining`.

Each directory move is a separate filesystem operation. If interrupted, inspect both
locations and rerun after stopping writers; already-moved directories are left alone.
This is not a distributed migration lock. The store reports remaining legacy records
instead of hiding them or creating a second plan. Old ignored paths stay ignored during
transition. Regenerate disposable previews and bundles under the new paths, then update
host references deliberately; never delete edited bundles as part of a blind migration.

## 12. Evidence and adoption decision

Run the [cold-session pilot](../templates/customer-workspace/examples/context-recovery-pilot.md)
on real authorized work. Test a relevant decision change, unavailable tracker and small
bypass task. Separately exercise installed-host discovery, effective permissions, live
API retries and competing writers before expanding autonomy.

The [local observation](evaluations/context-recovery-20261020.md) records bounded recovery
behavior, not broad productivity or installed-host reliability. Compare a few similar
assignments for reconstruction effort, recovery errors, time to accepted outcome,
review/rework and intended user impact. State model/host and process versions, raw
evidence, failed attempts and unrun boundaries. Keep rules whose benefit exceeds their
maintenance cost; improve repeatable tooling instead of continually enlarging prompts.
