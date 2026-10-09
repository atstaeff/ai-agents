---
name: "agent-routing"
description: "Select skills and specialist agents for a user outcome, using progressive loading and explicit, verifiable handoffs."
---

# Agent Routing

1. Handle clear, small tasks directly. When routing helps, reuse available metadata and inspect only what is missing. Load selected skill bodies.
2. Use the narrowest relevant expertise: second-brain for PARA, product-manager for product uncertainty and domain experts for implementation. Skills can guide the current session without switching agents.
3. Check actual host capabilities and instructions. Delegate only when tools exist, authorization permits it and the benefit exceeds coordination cost. Otherwise apply specialist guidance in the current session.
4. Supply a bounded goal, context pointers, acceptance criteria, allowed files and expected evidence. Avoid concurrent writers to the same file.
5. Inspect returned changes and checks, resolve contradictions and update an existing work record when present. A successful tool call does not prove completion.

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
