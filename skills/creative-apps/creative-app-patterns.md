---
name: "creative-app-patterns"
description: "Implement document models, undo/redo, real-time feedback or media processing in a creative application."
---

# Creative App Patterns

## Workflow

1. Define the editable document model, commands and reversible operations independently of the UI.
2. Make autosave and recovery explicit. Use versioned formats and do not corrupt the previous valid document on write failure.
3. Budget real-time work, move expensive computation off the interaction path and measure the critical loop.
4. Prototype with representative media; test undo/redo, recovery, accessibility and empty/error states.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/creative-app-patterns.md): load only the section relevant to the task.
