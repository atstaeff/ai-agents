---
name: "golang-patterns"
description: "Write, review or debug idiomatic Go code, concurrency, interfaces and resource management."
---

# Golang Patterns

## Workflow

1. Respect the module's Go version and existing package conventions. Prefer small interfaces at the consumer boundary.
2. Return errors with useful context; avoid panic for ordinary failures and handle resource cleanup.
3. Make goroutine ownership, context cancellation and channel closure explicit. Bound parallel work.
4. Run gofmt, relevant go test checks and the race detector when concurrency changes. Test observable behavior and leaks.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/guide.md): load only the section relevant to the task.
