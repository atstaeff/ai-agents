---
name: "agent-routing"
description: "Select skills and specialist agents for a user outcome, using progressive loading and explicit, verifiable handoffs."
---

# Agent Routing

1. Read catalog metadata first. Match the user outcome and existing technology to a small set of skills; load their bodies only when selected.
2. Prefer the narrowest relevant specialist. Jörg is the general entry point; use second-brain for PARA notes, product-manager for product uncertainty and language/domain experts for implementation.
3. Read the host capabilities and governing instructions. Native subagent/session tools must exist and delegation must be authorized. Otherwise use the specialist profile as guidance in the current session and say how the work is being performed.
4. Give a delegated task a goal, context pointers, acceptance criteria, allowed files, dependencies and expected evidence. Avoid concurrent writers to the same file.
5. Inspect returned changes and checks. Resolve contradictions and integrate the result into the current work record; a successful tool call alone is not proof of completion.

## Selection examples

| Outcome | Agent | Initial skills |
| --- | --- | --- |
| Add a Python API endpoint | python-expert | python-patterns, api-design |
| Improve an interface | frontend-expert | frontend-patterns |
| Clarify a product increment | product-manager | product-discovery |
| File notes in a private vault | second-brain | obsidian-para |
| Coordinate several deliverables | joerg | work-management, agent-routing |
| Review a risky change | code-reviewer | code-review |

## Host boundaries

- Exported profiles do not themselves create sessions. OpenCode's available native task/subagent tools determine delegation behavior.
- Do not promise that the user can type into a child session in every OpenCode Web release. Session visibility and interaction depend on the host UI.
- Do not invent tool names, models, account access or background execution. Select models by available capabilities and workload, not a hardcoded obsolete price table.
- Honor host permissions. A read-only reviewer must not become a writer merely because its Markdown describes a repair.
