# AGENTS.md project collaboration and shared knowledge

## Contents

- [Entry and source ownership](#entry-and-source-ownership)
- [Local files and web documentation](#local-files-and-web-documentation)
- [Team coordination](#team-coordination)
- [Knowledge and decision lifecycle](#knowledge-and-decision-lifecycle)
- [Docusaurus publication](#docusaurus-publication)
- [Adoption and compatibility](#adoption-and-compatibility)
- [Validation and improvement](#validation-and-improvement)

## Entry and source ownership

Use AGENTS.md as the project collaboration entry for people and AI. It identifies the
sources and defines cross-cutting working rules. It can link local Markdown, a central
engineering site, a project wiki or a combination. No project.yaml, project.toml or
workspace/ hierarchy is required. Other document names and folders are project choices.

AGENTS.md is the conventional plural uppercase instruction filename. A catalog profile
such as agents/architecture/architect.agent.md defines a reusable role; it is a different
artifact. AGENT.md is not this model's alternate filename. Host support, nested scope,
imports and web access must be verified with the chosen host; see [portability](PORTABILITY.md).

| Concern | Authoritative home | AGENTS.md instruction |
| --- | --- | --- |
| Vision and goals | Project facts or product page | Read intended users, problem, direction and observable outcomes |
| Stakeholders | Project facts or role map | Identify affected groups, priority, decision and acceptance roles |
| Scope | Project facts or boundary page | Read included responsibilities, exclusions and constraints |
| Process | CONTRIBUTING.md or adopted central process | Follow workflow, tools, quality gates and relevant skill routing |
| Work and review | Assigned issue/ticket and linked PR | Keep shared scope, acceptance, feedback, evidence and team handoff |
| Current knowledge | Project-owned knowledge sources | Read affected contracts and update verified behavior |
| Significant reasons | Project-owned decision records | Read relevant status/scope and preserve rationale |

The [default starter](../templates/project-starter/README.md) provides AGENTS.md, PROJECT.md
and CONTRIBUTING.md. Reuse existing equivalents; several source links may point to one
page. There is no obligation to create seven documents. The [instruction templates](../templates/agent-instructions/README.md)
cover an existing repository, remote documentation, multi-repository coordination and
component-specific rules. [This repository's entry](../AGENTS.md) is a filled example.

## Local files and web documentation

For repository facts, local sources keep the document and implementation revisions together.
A web source is useful for a central process shared across repositories or knowledge already
owned by a wiki. State which source owns each fact; the rendered site is a reading view of
its source, not another editable process copy.

Write explicit instructions: read the named process, follow its applicable rules, then load
only relevant procedures and skill bodies. A bare link neither guarantees reading nor
installs a skill. The host needs a supported way to retrieve the page and actual access.
Links to skills must lead to the canonical body or an installed catalog entry.

Pin shared policy to an immutable source commit or an explicitly maintained documentation
version. A semantic version URL is only as stable as the publishing policy behind it. Record
the actual loaded revision/version in consequential plans and handoffs. This repository's
website currently publishes one main-line view; it does not claim versioned Docusaurus
releases. Use a verified GitHub commit permalink when immutable policy is needed.

If a required page is unavailable, name the URL and blocked decision/action. Use a declared
local copy only when its provenance and adopted version are known. Continue independent
authorized work; never treat remembered policy as a freshly read source. Summaries cannot
override their verified source. Project exceptions belong with the project and its owner.

## Team coordination

Use the [operating model](OPERATING-MODEL.md) and [shared working contract](WORKFLOW.md).
Every assignment has an accountable human, active writer, bounded outcome, acceptance,
dependencies and integration owner. Roles can be combined. One issue/ticket owns shared scope and acceptance; a linked PR owns code/review evidence. Personal execution plans stay in the Second Brain unless an explicitly shared plan is needed. Do not mirror editable plans across tools.

For parallel implementation, use separate branches and working directories, explicit write
scopes and agreed shared interfaces. Reserve overlapping work through the adopted shared
claim/handover mechanism; confirm a takeover after interruption and preserve other work.
An assignee, local file or Git worktree is no distributed lock. Without an effective shared
claim mechanism, serialize overlapping writes. This toolkit implements no claim service.

Agree consequential interface changes before dependent implementation. Keep small increments
and integration order visible. The integrator checks the combined result, including
cross-repository compatibility. Required reviews apply to the current revision. AI review
supports assessment but is not automatically independent human approval.

Routine reversible choices within the assignment proceed independently. Changed product
scope, incompatible contracts or material security, cost and operations consequences go to
the responsible owner. Continue unrelated authorized work while dependent work is blocked.

## Knowledge and decision lifecycle

Keep current facts, historical rationale and execution progress at distinct owners.
[Knowledge lifecycle](PROJECT-KNOWLEDGE.md) defines retention and retrieval;
[session recovery](CONTEXT-RECOVERY.md) defines checkpoints and contradictions.

| Event | Update | Keep |
| --- | --- | --- |
| New opportunity | Optional ideas intake | Disposition, reason and result link |
| Uncertain behavior or design | Existing concept/spec | One designated living contract or marked historical snapshot |
| Significant choice | Decision record | Context, alternatives, evidence, decision, consequences, owner and status |
| Changed implementation | Affected current knowledge | Actual behavior, boundaries, source revision and verification |
| Pause or writer/model switch | Private resume note, or existing work-item handoff for a teammate | Result, revisions, evidence/limits, blockers, pending writes and next action |
| Completed assignment | Close at agreed completion point | Personal plan history in the Second Brain; shared feedback, reusable knowledge and reasons remain findable |
| Significant incident | Existing incident review | Observed facts, recovery and owned follow-up issues |

A proposal does not supersede an accepted ADR. Accepted replacements preserve the old
reasons and link both records. Code shows behavior but does not authorize a policy change.
When sources conflict, resolve scope and accountable authority rather than choosing the
newest text. Do not require complete chat transcripts or every ADR in every session.

A useful example layout is knowledge/README.md, knowledge/current/ and knowledge/decisions/.
Only create directories when there is content. Projects may instead use an existing wiki.
See the [worked storage example](examples/project-kernel.md#knowledge-and-decisions-in-practice).

## Docusaurus publication

Maintain the original Markdown once and publish selected sources. For this repository,
website/generate.py maps sources to pages, rewrites local links and preserves edit links.
Public route names can stay stable when maintained files move. docs/ remains generated
Pages output and is never the editing home.

Recommended navigation is Project (vision, stakeholders, scope), Ways of Working (process,
AGENTS.md and tools), Knowledge (architecture and current behavior), Decisions, Templates,
and links to the actual work/review system. Private project facts stay in their authorized
source; a public central process site cannot grant access or publication permission.

Exclude local work, archives, exports, credentials and generated previews. A successful
build establishes rendering/link structure, not remote tool access, approval or product
behavior. The website may lag an unmerged revision; the current checkout owns its facts.

## Adoption and compatibility

Follow [project adoption](ADOPT-PROJECT.md). Merge into existing agent instructions and
source ownership rather than replacing human wording. Fill links, roles, real tool homes
and actual commands. Validate one real assignment and a fresh-session recovery before
expanding concurrency.

Earlier project.yaml/workspace.yml maps and the extended customer example remain optional
compatibility material. The [legacy configuration guide](PROJECT-CONFIG.md) explains the
validator; its source filename workspace.schema.json remains stable. There is no new YAML
schema for AGENTS.md and no YAML requirement in the default starter.

The optional Python workbench still stores ignored records in workspace/work/ and archives
in workspace/archive/. Its --workspace argument means the project root. Removing the
workspace concept does not authorize deleting work records or changing storage silently.

## Validation and improvement

Check local links, filled project facts, source authority, actual commands and relevant
behavior. Exercise a fresh session, an unavailable-source case and concurrent integration.
Static Markdown checks cannot establish semantic completeness or host discovery.
Observe time to accepted result, review/reconstruction effort, rework and escaped defects.
Improve repeated failure causes in their owning document, check or tool. Increasing the
number of agents or mandatory pages is no evidence of higher throughput.

Personal planning follows the [shared workflow](WORKFLOW.md). Keep private vault paths out of shared sources; an unavailable vault means an unsaved session plan, not an automatic repository fallback.
