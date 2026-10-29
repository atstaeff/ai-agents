# Go specialist handoffs

Use the [role](../golang-expert.agent.md) for a bounded service, tool or review.
The [Go skill](../../../skills/languages/golang-patterns/SKILL.md) owns language and
concurrency procedure. Match the module's supported version and package structure;
there is no catalog-mandated project layout or linter bundle.

## Useful assignment

Supply the observed behavior, affected consumer, module/toolchain, concurrency or
resource limits, writable packages and expected check. Return the focused diff or
prioritized findings, commands actually run and unresolved race/integration limits.

## Focused review questions

- Who starts each goroutine, cancels it and waits for it? What happens when one worker
  fails, the consumer stops reading or the caller's deadline expires?
- Who owns channel closure, response bodies, database rows and transaction completion?
  Is cleanup reached on errors and early returns?
- Does the error contract let callers distinguish absence, conflict and operational
  failure without exposing credentials or raw database details?
- Is an interface defined around an actual consumer need? A small concrete function or
  configuration struct can be simpler than a repository layer or functional options.
- Is a database change plus event publication durable? Logging a publish error after
  committing data requires an explicit delivery/recovery contract.

Use [official module organization](https://go.dev/doc/modules/layout),
[Effective Go](https://go.dev/doc/effective_go),
[context](https://pkg.go.dev/context) and
[HTTP server documentation](https://pkg.go.dev/net/http) for the specific uncertainty.
Run race checks for affected concurrency when supported; a clean run covers executed
paths and does not prove the absence of every race or goroutine leak.
