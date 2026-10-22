---
name: "cloud-native"
description: "Plan or review cloud deployment, managed services, runtime configuration and operational resilience."
---

# Cloud Native

## Workflow

1. List workload scale, latency, data residency, budget and recovery needs; check whether an existing host already meets them.
2. Prefer managed primitives with a clear ownership and exit path. Containers and Kubernetes are options, not prerequisites.
3. Externalize configuration and secrets; include health, readiness, graceful shutdown, resource limits and observable failure signals.
4. Describe deployment, rollback, backup restore and cost monitoring. Test the highest-impact failure path.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/cloud-native.md): load only the section relevant to the task.
