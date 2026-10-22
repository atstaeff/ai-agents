# Work with AI as a teammate

Run a project with one clear outcome, one current assignment and a small shared memory.
Use AI to explore, plan, build, verify and maintain that memory within actual permissions.
People own priorities, consequential decisions and acceptance. This is a practical default
built from established practices, not a claim of universally optimal productivity.

## Start with three entry files

Use the [lean project starter](../templates/lean-project/README.md). Merge it into existing
conventions; do not replace customer content or copy the larger fictional example.

| Entry | Maintain here |
| --- | --- |
| `AGENTS.md` | Where a session starts and the few rules it must follow |
| `workspace/README.md` | Product goal, boundaries, decision owner, working rules and links |
| `workspace/workspace.yml` | Authoritative tool locations and optional actual commands |

The starter keeps working agreement and role ownership inline in the workspace entry.
Separate pages become useful when ownership or policy outgrows that entry. Its local
configuration works without a tracker; adapt the map to the project's real GitHub/Jira
locations before tracked delivery. The YAML is a map, not an orchestrator or permission grant.

An [expertise catalog](CATALOG-GUIDE.md) supplies reusable skills. Project facts stay in
the project. Load the narrowest useful skill; another profile need not mean another session.

## Run one delivery loop

**Clarify → Plan → Build → Verify → Integrate and retain useful knowledge.**
These activities can happen in one conversation and issue. They require no phase documents.

| Activity | Smallest useful result |
| --- | --- |
| Clarify | Who needs what outcome, boundaries and observable acceptance |
| Plan | Next complete increment, important uncertainty and affected sources |
| Build | Focused implementation using the existing stack |
| Verify | Actual criterion-linked checks, relevant failure cases and practical limits |
| Integrate and retain | Required acceptance/integration, current knowledge and durable rationale |

For a clear reversible correction, inspect, change and check directly. For an ordinary
feature, use the [compact assignment](../templates/delivery/assignment.md) inside the
existing issue. For an uncertain or consequential change, add a concept/spec and the
necessary decisions. Each artifact must resolve an uncertainty or preserve useful knowledge.

Use Todo, In Progress, In Review and Done, or the project's equivalent. Track blocked
work with its reason, owner and resume condition; keep its flow position visible.
Cancelled, duplicate and declined work are not delivered. Engineering Done means the
agreed evidence, required review and authorized integration at the project's completion
point. A draft PR, passing tests, deployment and measured user benefit are distinct states.

## Control the project without a second management system

Choose one person accountable for priority and acceptance, plus a technical decision owner
when needed; one person can hold both roles. Select the next increment by value, risk,
dependencies and review capacity. Default to one active increment per accountable owner;
expand only when the team can integrate and review the additional work.

Keep priority, assignment, plan, feedback and progress at their designated work home.
Use a few tasks only when coordination needs them. On material progress or a blocker,
update the same assignment. At a useful review point, link delivered outcomes, unresolved
risks and the next choice there; a separate iteration report or recurring meeting is optional.

One session is the default. Add specialists only for a bounded uncertainty and through
supported, authorized host capabilities. Give disjoint file/action scopes, selected source
revisions, acceptance and expected evidence; name an integrator. Concurrent writers need
an effective shared claim and recovery mechanism. This toolkit implements no distributed
lock, tracker synchronization, model runner or automatic multi-session coordination.

## Keep a small, connected memory

Create only the records needed by actual work. The workspace entry links the current ones.

| Record | Create when | After the work |
| --- | --- | --- |
| [Idea](../templates/knowledge/ideas.md) | An opportunity needs capturing | Mark selected, deferred, declined or delivered; link its result |
| [Concept/spec](../templates/knowledge/concept.md) | A meaningful uncertainty or contract needs explanation | Keep the designated living contract current; otherwise mark it historical and link its current successor |
| [Decision](../templates/knowledge/decision.md) | A significant choice's reasons will matter later | Preserve accepted rationale and replacement links |
| [Current knowledge](../templates/knowledge/current.md) | Reusable behavior or operating knowledge would otherwise be lost | Update from verified implementation; show intended/partial states |
| [Incident review](../templates/quality/incident-review.md) | Impact, recurrence or uncertainty warrants learning | Preserve facts and link owned follow-up issues and knowledge changes |

An idea is not a commitment. An agreed concept is not evidence of delivery. Code changes
do not revoke accepted decisions. AEK makes rationale compact: starting situation,
insight from alternatives/evidence, and consequences of the chosen response.

Working plans and tasks remain with the completed assignment as history. Before replacing
or deleting a derived plan, preserve its still-important decisions. Remove disposable
generated output and genuine duplicates deliberately. Archive means searchable history
outside routine context; it does not mean losing the reasons. See the
[knowledge lifecycle and recovery rules](PROJECT-KNOWLEDGE.md).

## Resume from current sources

A new session reads the current assignment, workspace entry and affected knowledge,
contracts and decisions, then compares the last bounded handoff with current revisions.
Search the affected project if links are missing. Load historical plans only to answer a
specific question; never require the entire chat, catalog or every ADR.

Before interruption, save the current result, relevant revisions, actual check evidence,
blocker/decision owner, pending writes and one next action in the existing assignment.
An optional host/session link aids navigation; shared knowledge must remain usable without
it. Use the [recovery contract](CONTEXT-RECOVERY.md) for conflicts and incomplete writes.

## Let each project choose its tools

Jira can own the assignment and GitHub the code review. Do not create a mirror issue,
local work record or CSV task list. With no designated system, use one [work record](WORK-RECORDS.md).
If an authoritative system is unavailable, report the gap and prepare an unsent update;
continue independent authorized work without silently changing the work home.

Use lean Plan/Build/Verify by default. For larger requirements, a project may choose
Spec-Driven Development; BMAD can support discovery, planning and delivery. Keep their
required artifacts at their existing homes, link them here and state which source owns
requirements versus status. Select one primary delivery method per assignment. Choosing
a `method` in YAML installs nothing. Never reconcile intent by merely accepting whatever
code happened to be produced. See the [method selection and retention guide](PROJECT-KNOWLEDGE.md#choose-a-method-without-duplicating-work).

## Add rigor where it earns its cost

Make the relevant qualities measurable using the [quality standard](QUALITY-STANDARD.md).
For significant changes, cover affected consumer contracts, security/privacy boundaries,
recovery and maintenance cost. Prefer understandable boundaries; new infrastructure,
frameworks and abstractions need evidence of benefit.

Plan review is required when the user or project requires it. Preserve the actual approval
of that revision before dependent work. Material changes reassess affected approvals and
checks. Merge, deployment, messages and destructive actions follow their actual scope;
a role label, template or YAML file grants no authorization.

Start with the [lean worked example](examples/lean-project.md). For more elaborate customer
coordination, use [the worked assignment](../templates/customer-workspace/examples/issue-42.md)
and the [detailed workspace concept](WORKSPACE-CONCEPT.md). Observe reconstruction effort,
rework, review time and useful outcomes on real assignments before adding automation.

Practices behind this default include [DORA small batches](https://dora.dev/capabilities/working-in-small-batches/),
[short decision records](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
and [SRE incident learning](https://sre.google/sre-book/postmortem-culture/). Their combination
here is a project convention; its benefit still needs observation in the adopted project.
