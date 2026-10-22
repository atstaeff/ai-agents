---
name: "flutter-patterns"
description: "Build, review or debug a Flutter application, including platform integration and widget behavior."
---

# Flutter Patterns

## Workflow

1. Inspect the current Flutter/Dart versions and state management before proposing changes.
2. Keep domain logic testable outside widgets. Choose the simplest state solution consistent with the existing app.
3. Handle loading, empty, error, cancellation, lifecycle and navigation states explicitly.
4. Check semantics, text scaling, keyboard/focus behavior and platform-specific permissions.
5. Run relevant Dart analysis, unit/widget tests and the available platform build; report unavailable device validation.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/guide.md): load only the section relevant to the task.
