---
name: "frontend-patterns"
description: "Implement or debug React, JavaScript and web UI behavior: state ownership, effects, forms, accessible interaction and API failure recovery."
---

# Frontend Patterns

## Workflow

1. Inspect the existing framework, router, dependency lock and design system. Trace the user journey and API contract; preserve JavaScript/TypeScript conventions. Choose a new client framework only when the interaction requires it.
2. Keep one owner for each state. Separate local interaction, URL state and server data. Derive values instead of duplicating state; use stable item identity and immutable updates. Introduce a shared store only for actual shared ownership.
3. In React, keep render pure and Hooks unconditional. Use Effects for external synchronization; include dependencies and cleanup subscriptions/timers or obsolete requests. Put user-triggered mutations in event handlers or the established framework action.
4. Define loading, empty, error and success states. For forms, retain entered data after failure, show field/global errors and prevent accidental duplicate submission. Handle HTTP errors, stale responses and cache invalidation using the existing data layer.
5. Use semantic controls, labels, keyboard operation, visible focus and responsive layouts. Render untrusted content as text or use the project's trusted sanitizer. Keep secrets out of the client; UI guards supplement server authorization.
6. Verify the critical journey and relevant failure recovery in the running interface. Check keyboard/focus and representative viewports; add a focused interaction regression when behavior warrants it. Report browser/backend checks separately from build, lint and type checks.

## Focused references

- [React state and effects](references/guide.md#react-state-and-effects): for ownership, cleanup or stale-response bugs.
- [API and interaction checks](references/guide.md#api-and-interaction-checks): for forms, transport failures and browser evidence.
