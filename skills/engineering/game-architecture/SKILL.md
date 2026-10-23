---
name: "game-architecture"
description: "Structure an existing or new game for clear state ownership, engine integration and testable mechanics."
---

# Game Architecture

## Workflow

1. Inspect the engine and target platforms. Separate deterministic game rules from rendering, input and persistence.
2. Choose component or entity systems only when their costs fit the game; avoid an engine abstraction without a second consumer.
3. Define update order, save state, scene transitions and lifecycle ownership.
4. Measure frame time and allocation; test rules and state transitions with representative play scenarios.

## Focused references

- [Detailed examples](references/game-architecture.md): load only the section relevant to the task.
