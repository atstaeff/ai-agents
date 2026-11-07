# Skill source template

Create `skills/<domain>/<slug>/SKILL.md`. Replace placeholders with actionable domain guidance;
host-specific fields belong in adapters.

```markdown
---
name: "replace-with-slug"
description: "Explain the capability and concrete situations in which to select it."
---

# Descriptive title

## When to use

Describe the trigger, required inputs and one situation that needs a different technique.

## Workflow

1. Read only the sources that supply those inputs.
2. Give concrete steps and explain the fallback for missing inputs or tools.
3. Produce the named output and verify an observable result. Report material limits.

## Focused references

Link optional reference files only when they provide useful details.
```

Try a representative case and one where the skill should be skipped. Keep domain
examples in references when they would obscure the main procedure.
