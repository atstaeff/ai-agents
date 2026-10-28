---
name: "gcp-patterns"
description: "Design, review or troubleshoot Google Cloud workloads: service choice, IAM, Cloud Run, Pub/Sub, data, cost and recovery. Use terraform-iac for infrastructure state and plan mechanics."
---

# GCP Patterns

## Workflow

1. Confirm actual projects/environments, data residency, callers, workload shape, budget and recovery targets. Inspect existing resources and ownership when access permits; label unverified assumptions.
2. Compare the current deployment with the simplest adequate service. For Cloud Run, account for ingress, authentication, concurrency, scaling limits, cold starts and downstream connection capacity. Choose Kubernetes only for a concrete requirement.
3. Separate deployer, runtime and service-agent identities. Scope IAM to the needed action/resource, use managed secret delivery and prefer short-lived workload credentials. Verify denied access as well as the allowed path.
4. For Pub/Sub or asynchronous work, define durable idempotency, acknowledgment, retry/backoff, poison-message handling and replay. Make deduplication plus the business write atomic when possible; external side effects need their own idempotency or recovery contract.
5. Match storage/query design to data access, retention and compatibility. Estimate compute, storage and egress from a representative workload; define actionable alerts, operating owner and rollout/restore checks.
6. Verify affected service/provider limits and pricing in current official documentation. Report actual plan/deployment/access/restore evidence separately; a local validation cannot establish live cloud behavior.

## Focused references

- [Workload guide](references/guide.md): read the relevant Cloud Run, Pub/Sub or data section.
- [Terraform IaC](../terraform-iac/SKILL.md): state, module, IAM ownership or plan review.
