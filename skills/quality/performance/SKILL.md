---
name: "performance"
description: "Investigate measured latency, throughput, memory or resource problems and validate an optimization."
---

# Performance

## Workflow

1. Capture a reproducible workload and a baseline with percentile latency, throughput or memory appropriate to the problem.
2. Profile the actual bottleneck before changing algorithms, storage, concurrency or caching.
3. Bound cache growth and define invalidation. Consider backpressure and query plans before scaling infrastructure.
4. Return before/after measurements with workload, environment, revision and correctness checks. Without a reproducible baseline or profiler, return a bounded hypothesis and missing measurement; promise no unmeasured speedup.

## Focused references

- [Detailed examples](references/performance.md): load only the section relevant to the task.
