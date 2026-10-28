# Go boundaries and concurrency

Use a focused section for the affected Go behavior. Match go.mod, the supported
toolchain and existing packages; verify version-dependent APIs before using them.

## Consumer contracts and errors

Define an interface where a consumer needs substitution or a stable boundary. Keep
methods small and meaningful to that consumer; avoid generating a full CRUD repository
for every type. A concrete struct or function may be sufficient. Use constructor
options only when actual optional configuration is clearer than a small config struct.

Return errors with useful operation context. Use errors.Is/errors.As for classifications
that callers are allowed to depend on; wrapping an implementation error can expose it
as part of that contract. Keep raw storage errors and secrets out of public responses.
Reserve panic for conditions the application cannot reasonably handle as ordinary input.

For database work, make transaction and commit ownership explicit. If a commit must
produce an event, record durable pending delivery in the same transaction where the
storage permits it, or define another recoverable contract. Logging a publish failure
after saving an order does not ensure eventual publication.

## Goroutine ownership

For each goroutine, identify its creator, cancellation signal, result/error path and
join point. Make channel closure the responsibility of the sending side. Handle a
consumer that stops early so producers cannot remain blocked forever.

Use request contexts through context-aware operations; a context parameter alone does
not cancel a blocking library call. Derive a bounded lifetime for independent background
work rather than accidentally tying it to a completed request. Call cancellation
functions and close resources on success, failure and early return.

For [errgroup](https://pkg.go.dev/golang.org/x/sync/errgroup), verify the installed API,
set a positive concurrency limit from actual capacity and ensure each task responds
to cancellation. Wait for all started work before returning. If zero means no work or
invalid configuration, handle it explicitly; do not silently start an unbounded batch.
Review blocked sends, full queues and slow dependencies as well as the success path.

## HTTP clients, servers and middleware

Use a reused client/transport with appropriate deadlines, propagate the caller's
context and close response bodies. Check response status before treating its body as
success; transport success alone does not mean the HTTP operation succeeded. Bound
response size where the peer is untrusted.

Configure server timeouts for the actual protocol and workload. During shutdown, stop
accepting new work, drain within a deadline and define cleanup for remaining workers.
Check how server errors reach the owning process; a background error must not disappear.

This middleware composition fragment preserves the order supplied by the caller:

```go
type Middleware func(http.Handler) http.Handler

func Chain(handler http.Handler, middlewares ...Middleware) http.Handler {
    for i := len(middlewares) - 1; i >= 0; i-- {
        handler = middlewares[i](handler)
    }
    return handler
}
```

It assumes the caller imports net/http and supplies valid middleware. Verify the
actual auth, timeout, request-ID and recovery ordering in the project's chain; a generic
wrapper does not establish authorization or a safe streaming contract.

## Tests and package organization

Use table-driven subtests for meaningful input classes and named failure cases. Derive
expected results from the requirement, not the implementation. A fake should preserve
the contract under test, including copying/ownership of mutable data and relevant errors;
it does not establish SQL, locking or network behavior.

Run gofmt and the established targeted tests. Use go vet and race checks when applicable
to the affected boundary; report unavailable platform/build checks. A race detector run
covers executed paths and is not proof that every race or leak is absent.

Follow [official module organization](https://go.dev/doc/modules/layout) as guidance,
not a required directory tree. Keep packages cohesive around behavior and ownership;
introduce internal packages or multiple commands when the project needs them. Do not
add a public pkg directory or service layer merely to match a sample.

## Official references

- [Effective Go](https://go.dev/doc/effective_go): language idioms; account for APIs added since its examples.
- [context](https://pkg.go.dev/context): lifetime and cancellation contract.
- [net/http](https://pkg.go.dev/net/http): client, server and shutdown behavior.
- [database/sql](https://pkg.go.dev/database/sql): query, transaction and resource lifetime.
- [Race detector](https://go.dev/doc/articles/race_detector): supported execution and limitations.
