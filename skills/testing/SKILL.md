---
name: "testing"
description: "Design or improve behavior-focused tests and a practical verification strategy for a change."
---

# Testing

## Workflow

1. Identify high-impact behavior, realistic failure modes and existing test coverage.
2. Choose unit, integration or end-to-end checks based on the affected boundaries; reuse the repository's framework.
3. Prefer unittest for a new Python stdlib project. Keep fixtures small and tests independent of implementation details.
4. Exercise meaningful edge cases, errors and state transitions. Run the relevant suite and report what it establishes and what remains untested.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/guide.md): load only the section relevant to the task.
