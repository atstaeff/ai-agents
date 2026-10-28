---
name: "solid-principles"
description: "Review a concrete responsibility, inheritance or interface contract using SOLID principles; identify substitutability and coupling problems without adding speculative abstractions."
---

# SOLID Principles

## Workflow

1. Look for concrete reasons a module changes and split responsibilities only when the boundary helps.
2. Depend on small consumer-facing contracts at real substitution points.
3. Check substitutability and avoid exposing methods consumers cannot use safely.
4. Return the concrete contract problem, smallest adequate remedy and behavior/substitution evidence. Prefer composition or a direct implementation when another layer adds only ceremony.

## Focused references

- [Detailed examples](references/solid-principles.md): load only the section relevant to the task.
