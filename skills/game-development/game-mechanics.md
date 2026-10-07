---
name: "game-mechanics"
description: "Implement or tune a specific game mechanic such as movement, combat, inventory or progression."
---

# Game Mechanics

## Workflow

1. Specify inputs, state transitions, timing and observable player feedback for the mechanic.
2. Separate parameters from rule logic so tuning remains easy. Prefer deterministic tests for rules where possible.
3. Handle boundaries, interrupts, invalid actions and save/load behavior.
4. Test in the core loop and measure feel/performance on the intended platform.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/game-mechanics.md): load only the section relevant to the task.
