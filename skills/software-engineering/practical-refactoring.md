---
name: "practical-refactoring"
description: "Refactor existing code incrementally while preserving behavior and keeping changes reviewable."
---

# Practical Refactoring

## Workflow

1. Identify the behavior to preserve and the next change the refactor should make easier.
2. Add a focused regression check if the behavior is not already protected.
3. Separate structural edits from intentional behavior changes and make small reversible steps.
4. Run appropriate checks after each risky step; stop when the concrete maintenance goal is met.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/practical-refactoring.md): load only the section relevant to the task.
