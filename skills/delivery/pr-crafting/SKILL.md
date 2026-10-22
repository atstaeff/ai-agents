---
name: "pr-crafting"
description: "Prepare a reviewable pull request description, scope and validation evidence for a code change."
---

# Pr Crafting

## Workflow

1. Lead with the concrete problem and resulting behavior.
2. Explain only implementation decisions a reviewer needs and list the checks actually run.
3. Include material limitations, migration steps or rollback needs when present.
4. Keep title and description aligned with the final diff. Do not merge or publish unless authorized.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/pr-crafting.md): load only the section relevant to the task.
