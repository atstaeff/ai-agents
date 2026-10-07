---
name: "performance"
description: "Investigate measured latency, throughput, memory or resource problems and validate an optimization."
---

# Performance

## Workflow

1. Capture a reproducible workload and a baseline with percentile latency, throughput or memory appropriate to the problem.
2. Profile the actual bottleneck before changing algorithms, storage, concurrency or caching.
3. Bound cache growth and define invalidation. Consider backpressure and query plans before scaling infrastructure.
4. Compare before/after measurements under the same conditions and verify correctness. Document remaining limits without promising unmeasured speedups.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/performance.md): load only the section relevant to the task.
