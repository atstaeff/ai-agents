---
name: "python-patterns"
description: "Write, review or refactor Python using dataclasses, explicit boundaries, uv and behavior-focused tests."
---

# Python Patterns

## Workflow

1. Respect the project's Python version and existing conventions. For new code prefer dataclasses, type hints, pathlib and explicit validation.
2. Use uv for environments and dependency management; prefer unittest for a new stdlib-oriented toolkit and Typer for a richer CLI when an added dependency is justified.
3. Use a validation library at external boundaries when the project already uses it or requirements justify it; do not mandate Pydantic for every domain object.
4. Use small functions and protocols at real substitution boundaries. Avoid unnecessary repository, event-bus or inheritance layers.
5. Close resources, preserve tracebacks and use timezone-aware timestamps. Test behavior and boundary failures with minimal mocking.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/guide.md): load only the section relevant to the task.
