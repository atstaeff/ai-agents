---
name: "game-mechanics"
description: "Implement or tune a specific game mechanic such as movement, combat, inventory or progression."
---

# Game Mechanics

## Workflow

1. Specify inputs, state transitions, timing and observable player feedback for the mechanic.
2. Separate parameters from rule logic so tuning remains easy. Prefer deterministic tests for rules where possible.
3. Handle boundaries, interrupts, invalid actions and save/load behavior.
4. Return the implemented rule or tuned parameters and actual core-loop checks. Separate observed player feedback from measured timing; identify untested platform behavior.

## Focused references

- [Detailed examples](references/game-mechanics.md): load only the section relevant to the task.
