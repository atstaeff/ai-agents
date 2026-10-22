---
name: "microservices"
description: "Evaluate a service split or improve an existing distributed system with explicit ownership and failure handling."
---

# Microservices

## Workflow

1. First establish an independent deployment or ownership need. Compare against a modular monolith and identify migration cost.
2. Specify service contracts, data ownership, timeouts, retries, idempotency and degraded behavior.
3. Avoid shared mutable databases and synchronous call chains where a local boundary would suffice.
4. Plan observability, compatibility, rollback and operational responsibility before extraction. Verify one end-to-end scenario.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/microservices.md): load only the section relevant to the task.
