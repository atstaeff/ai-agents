---
name: "iot-embedded-patterns"
description: "Develop or review firmware, embedded protocols, resource-constrained systems or device integration."
---

# Iot Embedded Patterns

## Workflow

1. Identify hardware, memory, timing, power and toolchain constraints before changing firmware.
2. Separate hardware access from deterministic logic; document ISR/task ownership and bound allocations.
3. Specify protocol framing, retries, watchdog behavior, update recovery and safe failure states.
4. Validate on the available simulator or hardware and distinguish measured device results from desktop-only tests.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/guide.md): load only the section relevant to the task.
