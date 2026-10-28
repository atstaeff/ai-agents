---
name: "python-patterns"
description: "Write, review or debug Python and FastAPI code with typed boundaries, safe async/resource lifetimes and behavior-focused tests."
---

# Python Patterns

## Workflow

1. Inspect the supported Python versions, pyproject, lockfile, entry points and current test commands. Reuse the project's environment manager; use uv for a new project when appropriate. Keep syntax and dependencies compatible with the declared minimum.
2. Model rules with small functions and explicit types. Use dataclasses for suitable internal data and boundary validation where required. Add protocols or layers only for a real substitution or transaction boundary.
3. For FastAPI, define request/response contracts and error semantics; enforce authorization for the resource and action. Keep transport schemas distinct where exposure or domain rules differ. Scope clients/sessions through dependencies and application lifespan.
4. Match sync/async code to the libraries in use. Keep blocking I/O and CPU work out of the event loop; bound external calls with timeouts and handle cancellation. Close resources on success and failure.
5. Make transaction ownership and commit points explicit. Preserve atomicity, uniqueness and stale-write behavior; retry only safe operations. Keep secrets and personal data out of error responses and logs.
6. Run the established checks at the affected boundary. Exercise success, validation/authorization failure and relevant cleanup or rollback. Reset dependency overrides between tests; distinguish HTTP contract evidence from actual database/integration evidence.

## Result

Deliver the focused diff and executed checks, including supported-version or integration limits.

## Focused references

- [FastAPI boundaries](references/guide.md#fastapi-boundaries): for routes, dependency lifetime and async behavior.
- [Persistence and refactoring](references/guide.md#persistence-and-refactoring): for transaction or design changes.
