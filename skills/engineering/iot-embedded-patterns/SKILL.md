---
name: "iot-embedded-patterns"
description: "Develop or review firmware, embedded protocols, resource-constrained systems or device integration."
---

# IoT and Embedded Patterns

## Workflow

1. Identify hardware, memory, timing, power and toolchain constraints before changing firmware.
2. Separate hardware access from deterministic logic; document ISR/task ownership and bound allocations.
3. Specify protocol framing, retries, watchdog behavior, update recovery and safe failure states.
4. Return the changed device/protocol contract, exact target and executed checks. Distinguish measured hardware results from simulation or desktop-only tests; identify missing equipment and timing evidence.

## Focused references

- [Detailed examples](references/guide.md): load only the section relevant to the task.
