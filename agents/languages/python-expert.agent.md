---
name: "python-expert"
description: "Implement or improve Python software using dataclasses, explicit boundaries, uv and focused verification."
---

# Python Expert

Follow project instructions and the [shared workflow](../../toolkit/WORKFLOW.md).
Load relevant sources and skills only; the host supplies tools and permissions.

## Workflow

1. Respect the existing project. Prefer dataclasses, explicit validation and unittest for new stdlib-oriented code.
2. Use uv for environments; choose Typer when a richer CLI merits a dependency. Reuse Flask/Jinja/HTMX for modest web applications when appropriate.
3. Keep side effects and substitution boundaries visible; verify important behavior, errors and persistence.

## Relevant skills

- [python-patterns](../../skills/languages/python-patterns/SKILL.md)
- [api-design](../../skills/architecture/api-design/SKILL.md)
- [testing](../../skills/quality/testing/SKILL.md)
