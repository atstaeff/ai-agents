---
name: "testing-strategies"
description: "Choose meaningful unit, integration or end-to-end checks proportional to a software change."
---

# Testing Strategies

## Workflow

1. Identify likely regressions and important boundaries, then choose the smallest checks that observe them.
2. Use the existing test framework; default to unittest for new Python stdlib code.
3. Test error paths, permissions, concurrent writes and persistence when relevant. Mock external boundaries, not the implementation itself.
4. Do not mandate coverage percentages, one-assert rules or broad end-to-end suites for every change. Report exact checks and limitations.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/testing-strategies.md): load only the section relevant to the task.
