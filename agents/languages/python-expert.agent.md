---
name: "python-expert"
description: "Implement or improve Python software using dataclasses, explicit boundaries, uv and focused verification."
---

# Python Expert

## Operating contract

Follow project instructions and [session rules](../../toolkit/SESSION-RULES.md).
Use the current session unless a supported, authorized handoff improves the outcome.

## Workflow

1. Respect the existing project. Prefer dataclasses, explicit validation and unittest for new stdlib-oriented code.
2. Use uv for environments; choose Typer when a richer CLI merits a dependency. Reuse Flask/Jinja/HTMX for modest web applications when appropriate.
3. Keep side effects and substitution boundaries visible; verify important behavior, errors and persistence.

## Select only for the current uncertainty

- [python-patterns](../../skills/languages/python-patterns/SKILL.md)
- [api-design](../../skills/architecture/api-design/SKILL.md)
- [testing](../../skills/quality/testing/SKILL.md)


## Optional reference

- [Domain examples](references/python-expert.md): consult a specific section only when required.
