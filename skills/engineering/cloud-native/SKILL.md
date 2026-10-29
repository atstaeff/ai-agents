---
name: "cloud-native"
description: "Define or review a cloud runtime contract: configuration, workload identity, scaling, health, failure handling and recovery. Use provider skills for service-specific behavior and devops-cicd for pipeline mechanics."
---

# Cloud Native

## Workflow

1. List workload scale, latency, data residency, budget and recovery needs; check whether an existing host already meets them.
2. Prefer managed primitives with a clear ownership and exit path. Containers and Kubernetes are options, not prerequisites.
3. Externalize configuration and secrets; include health, readiness, graceful shutdown, resource limits and observable failure signals.
4. Return the runtime contract, deployment/restore approach and actual failure-path evidence. Without access, label rollout and recovery unverified rather than inferring live state.

## Focused references

- [Detailed examples](references/cloud-native.md): load only the section relevant to the task.
