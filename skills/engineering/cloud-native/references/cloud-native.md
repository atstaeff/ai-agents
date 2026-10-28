# Runtime resilience and delivery boundaries

Use the relevant section for a deployment or recovery decision. Start from the actual
host and workload; containers, Kubernetes, a service mesh and distributed services each
need a concrete reason.

## Deployment unit and identity

Identify the artifact digest, configuration revision, runtime identity, secret delivery
and operating owner. Keep builds separate from environment configuration and promote
the tested artifact. Confirm where state lives and what happens when an instance is
replaced; a stateful workload needs explicit durability, scheduling and recovery.

Separate startup, readiness and liveness semantics. A temporary downstream failure may
warrant removing traffic or degrading a feature rather than restarting every instance.
Drain accepted work on shutdown within the platform's actual deadline; decide how
unfinished jobs are recovered after forced termination.

## Timeouts, retries and isolation

| Mechanism | Purpose | Failure case to check |
| --- | --- | --- |
| Deadline/cancellation | Bound waiting and abandoned work | Caller leaves while downstream work is active |
| Retry with backoff/jitter | Recover from a transient failure | Duplicate side effect or synchronized retry storm |
| Circuit breaker | Stop repeatedly calling a failing dependency | Open/half-open transition and recovery |
| Concurrency/queue limit | Bound memory and downstream demand | Full queue, overload response and drain |
| Resource isolation | Protect important work from another workload | One pool exhausts while the protected path remains useful |

Choose limits from the workload and service contract. Account for multiplied connection
pools when instances scale. A retry library is not automatically a circuit breaker;
check the chosen library's actual API and avoid retrying non-idempotent side effects.

## Messages and data

Define acknowledgment, durable state, duplicate handling, ordering scope and replay.
Acknowledge only at the durability point promised to the producer. Retrying a message
must not blindly repeat an external charge or command. Bound backlog size, message age
and poison-message handling; assign the owner who can replay or repair failures.

Choose consistency from the user rule. Keep each invariant's write ownership clear;
introduce event sourcing, CQRS or an extra database only for a demonstrated requirement.

## Observe, release and restore

Use signals that reveal the user's outcome: errors, latency distributions, completed
jobs and data freshness, with resource saturation for diagnosis. Correlate requests
without exposing secrets or private payloads. An alert needs an owner and useful action.

Define rollout scope, stop condition, rollback/forward-repair path and compatible
schema versions. Exercise backup restoration against the stated recovery objective;
a successful backup job alone does not demonstrate that recovery works. Review compute,
storage, logging, idle capacity and egress using representative usage.

## Select a focused procedure

- [GCP patterns](../../gcp-patterns/SKILL.md): actual Google Cloud workload and service limits.
- [Terraform IaC](../../terraform-iac/SKILL.md): state, resource ownership and reviewed plans.
- [CI/CD](../../devops-cicd/SKILL.md): trusted artifact flow and release automation.
- [Performance](../../../quality/performance/SKILL.md): a measured capacity bottleneck.

Return the changed runtime contract, actual rollout/failure/restore evidence and gaps.
Use current provider documentation for affected limits and pricing. Without access,
label deployment and recovery unverified; local validation cannot establish live state.
