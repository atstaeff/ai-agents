---
name: "code-review"
description: "Review a change for correctness, regression risk, security and maintainability with actionable findings."
---

# Code Review

## Workflow

1. Read the acceptance criteria, diff, surrounding call sites, tests and project instructions. Trace the intended behavior independently of the author’s completion claim.
2. Trace concrete scenarios and prioritize defects by impact. Identify the file/location, failure trigger and minimal repair.
3. Separate blocking bugs from optional preferences. Avoid hypothetical issues without a plausible path.
4. Honor read-only tool restrictions. Execute reproductions only when permitted; otherwise give the executor a concrete check. Report checks performed and remaining uncertainty; if no material issues were found, say so plainly.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/code-review.md): load only the section relevant to the task.
