---
name: "creative-app-patterns"
description: "Implement document models, undo/redo, real-time feedback or media processing in a creative application."
---

# Creative App Patterns

## Workflow

1. Define the editable document model, commands and reversible operations independently of the UI.
2. Make autosave and recovery explicit. Use versioned formats and do not corrupt the previous valid document on write failure.
3. Budget real-time work, move expensive computation off the interaction path and measure the critical loop.
4. Return the working edit and relevant undo/redo, recovery, accessibility and failure checks with representative media. Name unavailable runtime/media measurements rather than assuming responsiveness.

## Focused references

- [Detailed examples](references/creative-app-patterns.md): load only the section relevant to the task.
