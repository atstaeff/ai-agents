# Contributing

Read [AGENTS.md](AGENTS.md) and [PROJECT.md](PROJECT.md). This guide describes the project's
working process for people and AI. Adapt it to existing project policy.

## Working process and skills

Use **Clarify → Plan → Build → Verify → Integrate and retain**. A clear small correction
can go directly through inspection, change and relevant checks. Keep shared scope,
acceptance, feedback, evidence and coordination in the existing assignment. Keep personal
steps in the user-configured private Second Brain when permitted by project policy;
if unavailable, use a short unsaved session plan and continue authorized work. Share an
execution plan only when collaboration needs it, at one agreed home.

Select only relevant skills from the installed catalog or its canonical linked source.
Load the skill body explicitly when the host does not discover it; a Markdown link
does not install a skill or start an agent. Do not load the whole catalog for each task.

| Need | Reusable procedure |
| --- | --- |
| Establish contribution rules in an unfamiliar project | [repository-contribution](https://github.com/atstaeff/ai-agents/blob/main/skills/delivery/repository-contribution/SKILL.md) |
| Clarify vision, value, scope and acceptance | [product-discovery](https://github.com/atstaeff/ai-agents/blob/main/skills/delivery/product-discovery/SKILL.md) |
| Plan and coordinate a larger assignment | [work-management](https://github.com/atstaeff/ai-agents/blob/main/skills/delivery/work-management/SKILL.md) |
| Resolve consequential design choices | [principal-engineer-decisions](https://github.com/atstaeff/ai-agents/blob/main/skills/architecture/principal-engineer-decisions/SKILL.md) |
| Implement in the existing stack | Select the relevant engineering or language skill |
| Verify and prepare review | [testing](https://github.com/atstaeff/ai-agents/blob/main/skills/quality/testing/SKILL.md), [pr-crafting](https://github.com/atstaeff/ai-agents/blob/main/skills/delivery/pr-crafting/SKILL.md) |

## Tools and access

Link actual tools and their project-specific locations. Reuse an existing tooling map
when it already owns this information.

| Purpose | Authoritative project location | Integration and access |
| --- | --- | --- |
| Work, priority and acceptance | [Work home in PROJECT.md](PROJECT.md#key-sources-and-links) | [available connector/CLI and permitted updates] |
| Code and review | [Repository/review home in PROJECT.md](PROJECT.md#key-sources-and-links) | [available connector/CLI and review policy] |
| Current knowledge and decisions | [Knowledge homes in PROJECT.md](PROJECT.md#current-knowledge-and-decisions) | [local sources or authorized wiki; publication owner if applicable] |

Discover available host integrations for these tools. Report missing access and prepare
an unsent update in the response or handoff, naming its intended destination. Check existing effects after a timeout before
retrying a write. Keep credentials and personal filesystem paths in local configuration.

## Setup and checks

Use verified commands and working directories from the existing runbook or CI. Link that
source here, or fill only the applicable rows below. Discover unknown commands before
dependent work.

| Action | Verified command and working directory, or authoritative source |
| --- | --- |
| Setup and local run | [actual command/source] |
| Affected behavior, tests and static checks | [actual command/source] |
| Build and integration checks | [actual command/source] |

## Coordination and review

Identify the accountable human, active contributor, bounded write scope, dependencies
and integration owner at the assignment; roles may be combined. Isolate independent
writers in separate branches/working directories and agree shared contracts first.
Coordinate overlapping files through the project's effective claim/handover mechanism;
serialize overlap when none exists. Preserve human edits and reread shared records
before writes. Delegate only when supported, authorized and useful.

Start with one active increment. Preserve intervening edits and human feedback.
Capture significant rationale when it arises and update affected current knowledge from
evidence. Resolve consequential conflicts with the owner in PROJECT.md. Follow review
requirements and actual action permissions; a plan grants no merge/deployment authority.

Run actual checks on the combined revision, including affected behavior and important
failure cases. Required reviews apply to the current revision. Report unrun or blocked
checks and keep accepted, integrated, deployed and measured outcomes distinct.

Report the change, actual checks and remaining gaps. Save the bounded handoff described
in PROJECT.md before switching sessions. Shared artifacts use English; never invent
results, approvals, capabilities or successful writes.
