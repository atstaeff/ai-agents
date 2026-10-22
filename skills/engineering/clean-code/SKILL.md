---
name: "clean-code"
description: "Improve readability and changeability of code while preserving behavior and project conventions."
---

# Clean Code

## Workflow

1. Use concrete names and cohesive functions. Make data flow and side effects visible.
2. Remove unnecessary branches and duplication only when the shared behavior is actually stable.
3. Avoid style-only churn outside the change. Comments should explain constraints or intent, not restate syntax.
4. Verify behavior and show how the change reduces an actual maintenance cost.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/clean-code.md): load only the section relevant to the task.
