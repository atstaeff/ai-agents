---
name: "api-design"
description: "Design or review an HTTP API, consumer contract, errors, authorization, pagination or compatibility changes."
---

# Api Design

## Workflow

1. Identify consumers and concrete request/response examples before choosing endpoints. Reuse the existing framework and contract conventions.
2. Specify methods, status codes, content types, validation, error shape, authorization per resource and supported compatibility behavior.
3. Define pagination, retry/idempotency and concurrent-write behavior where consumers need them. Do not require JWT, version prefixes or microservices by default.
4. Keep secrets out of URLs and logs. Bound input size and expensive operations. Separate domain errors from transport errors.
5. Provide an OpenAPI contract when appropriate and test consumer-visible behavior, permissions and failure cases.
6. For a changed contract, inspect existing consumers and demonstrate compatibility or an explicit migration path. Verify representative requests against the implementation; a schema-valid document alone does not prove the API works.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/api-design.md): load only the section relevant to the task.
