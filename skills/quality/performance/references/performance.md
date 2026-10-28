# Performance investigation and evidence

Read the affected boundary after a concrete latency, throughput, memory or capacity
problem is identified. Keep the current architecture until evidence justifies a change.

## Reproduce a representative workload

Record revision, hardware/runtime, data size/distribution, concurrency or arrival rate,
cache state, warm-up, duration and relevant dependency limits. Choose metrics that
represent the user's wait or failed work, including tail latency and errors where useful.
A lower average can hide a slower critical path or rejected requests.

Capture a baseline and profile the same workload. Separate CPU work, allocation/GC,
I/O wait, lock contention, database time and queueing. Follow the request's critical path;
a slow span or hot function is a lead, not proof of the root cause.

## Inspect the expensive boundary

| Observation | Inspect first | Verify after a change |
| --- | --- | --- |
| CPU grows with input | Algorithm, duplicate work and data structure | Representative small and large inputs; same result |
| Memory keeps growing | Retained references, queues, cache cardinality and lifecycle | Steady-state and post-work cleanup |
| Database wait dominates | Query plan, row counts, lock/pool wait and round trips | Read/write cost, cardinality and concurrent behavior |
| Tail latency rises with load | Saturation, queue length, downstream limits and retries | Latency plus throughput/errors at the same offered load |
| Browser interaction stalls | Main-thread work, layout, payload and rendering | Running interaction on a representative device |

## Queries and caches

Inspect the actual query plan and workload before adding an index. Account for write
cost, disk use, selectivity and the database's online-migration behavior. Fetch only
needed data and address demonstrated N+1 paths; eager loading can also overfetch.

For PostgreSQL, [EXPLAIN documentation](https://www.postgresql.org/docs/current/using-explain.html)
explains plan interpretation. EXPLAIN ANALYZE executes the statement: use a safe
environment and account for writes and nontransactional external effects. Select the
documentation version matching the deployed database.

A cache needs key scope, size/eviction, freshness and invalidation rules. Include tenant
or authorization context where results differ. Test stale values, failure recovery,
concurrent misses and cold start. A hit-rate improvement is insufficient if it serves
the wrong user's data or overloads the source after expiry.

## Concurrency and background work

Parallel I/O may reduce waiting, but unbounded fan-out can exhaust connection pools,
memory and downstream capacity. Define cancellation, deadlines, concurrency and queue
limits. Async syntax does not make blocking work nonblocking or CPU work free.

Moving work to a queue changes the completion contract. Measure time to the user's
actual outcome, backlog age and error/retry behavior rather than only enqueue latency.
Preserve ordering and idempotency where the business rule depends on them.

## Compare and report

1. Change one demonstrated bottleneck at a time; retain the correctness checks.
2. Repeat comparable runs with the same offered workload and measurement method.
   Report variability and warm/cold conditions; avoid attributing noise to the change.
3. Include absolute values, units, workload/revision and resource tradeoffs alongside
   any percentage. Distinguish a microbenchmark from end-to-end performance.
4. Check overload, recovery and compatibility when affected. Stop optimizing when the
   agreed target is met or another bottleneck makes the next change unhelpful.

Without a reproducible environment or profiler, return an investigation plan or bounded
hypothesis and the exact missing measurement. Do not invent baseline numbers, savings,
scalability or environmental impact from a smaller source file or faster local build.
