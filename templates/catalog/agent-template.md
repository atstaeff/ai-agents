# Agent source template

Create `agents/<domain>/<name>.agent.md`. Give the role a clear selection situation and
bounded responsibility; actual tools and permissions belong to the host adapter.

```markdown
---
name: "replace-with-name"
description: "State the outcome this role owns and when to select it."
---

# Role title

## Responsibility

State the bounded outcome, when the lead can proceed without this role, and the
expected handoff. Link the adopted project workflow from this file's actual location.

## Procedure

1. Read the minimum inputs needed for this role.
2. Describe the role's concrete method and what to do when an input or tool is missing.
3. Return the named artifact or finding, verification evidence, limits and next action.

## Relevant skills

Link selected canonical skills rather than copying their instructions.
```

Before publishing, try a representative assignment and one that should bypass the
role. Record observed behavior separately from structural checks.
