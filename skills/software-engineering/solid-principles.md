---
name: "solid-principles"
description: "Evaluate responsibilities and dependencies using SOLID principles without unnecessary abstractions."
---

# Solid Principles

## Workflow

1. Look for concrete reasons a module changes and split responsibilities only when the boundary helps.
2. Depend on small consumer-facing contracts at real substitution points.
3. Check substitutability and avoid exposing methods consumers cannot use safely.
4. Prefer composition and direct implementations when inheritance or interface layers would add only ceremony.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/solid-principles.md): load only the section relevant to the task.
