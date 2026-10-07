---
name: "frontend-patterns"
description: "Build or improve a web interface with accessible interaction, clear states, reusable components and API contracts."
---

# Frontend Patterns

## Workflow

1. Follow the existing framework and design language. For a new modest interface, consider server-rendered HTML or HTMX before a full client framework.
2. Define loading, empty, error and success states; make the primary action easy to find and give useful feedback.
3. Use semantic HTML, labels, keyboard interaction, visible focus, responsive layouts and appropriate contrast.
4. Render untrusted content safely; avoid injecting Markdown or API text into innerHTML without a trusted sanitizer.
5. Agree on the API contract and test the critical interaction, authorization boundary and failure recovery.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/guide.md): load only the section relevant to the task.
