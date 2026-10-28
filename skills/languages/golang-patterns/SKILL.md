---
name: "golang-patterns"
description: "Write, review or debug idiomatic Go code, concurrency, interfaces and resource management."
---

# Golang Patterns

## Workflow

1. Respect the module's Go version and existing package conventions. Prefer small interfaces at the consumer boundary.
2. Return errors with useful context; avoid panic for ordinary failures and handle resource cleanup.
3. Make goroutine ownership, context cancellation and channel closure explicit. Bound parallel work.
4. Return the focused diff and actual gofmt/go test results; use the race detector for affected concurrency when supported. Check cancellation, cleanup and leaks; label missing toolchain or integration evidence.

## Focused references

- [Detailed examples](references/guide.md): load only the section relevant to the task.
