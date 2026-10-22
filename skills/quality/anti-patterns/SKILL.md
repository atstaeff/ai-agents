---
name: "anti-patterns"
description: "Spot avoidable complexity when reviewing architecture, code, processes or proposed dependencies."
---

# Anti Patterns

## Workflow

1. Check whether each abstraction solves a demonstrated problem. Prefer a direct implementation when extension points have no consumer.
2. Look for hidden coupling, mutable globals, swallowed exceptions, duplicated state, excessive mocking and premature distribution.
3. Describe the concrete failure mode and the smallest safer change. Preserve useful behavior with a regression check.
4. Separate a defect from a preference. Do not prescribe a rewrite or a new framework merely to match a pattern.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/guide.md): load only the section relevant to the task.
