# Google Cloud workload guide

Read only the relevant section. Verify service details against the actual project,
installed provider/SDK and current official documentation before using them.

## Cloud Run API service

Trace caller identity, ingress, runtime service account, data access and outbound
connectivity. Compare the existing host with a managed container service using the
workload's latency, concurrency, background-work and regional constraints. A managed
runtime still needs an owner, deployment contract and recovery evidence.

Bound concurrency and maximum scaling against database connection capacity and cost.
Account for cold starts only where the journey is sensitive to them. Use the platform's
secret integration with scoped access; separate deployment identity from runtime
identity. Test an allowed caller and a denied caller, dependency failure and graceful
shutdown. Verify the current [Cloud Run documentation](https://cloud.google.com/run/docs)
for service-specific settings rather than copying a template.

## Pub/Sub event processing

Treat redelivery and duplicate publication as design inputs. Choose a durable business
idempotency key and make the deduplication record plus state change atomic where they
share a datastore. A check-then-process-then-mark sequence can race or repeat work after
a crash. For external effects, use the provider's idempotency key or an explicit outbox
and reconciliation path; a transaction alone cannot cover a remote system.

Acknowledge only after the required durable work. Bound retry/backoff and distinguish
transient errors from poison messages. Configure and exercise dead-letter handling and
replay when the workload needs them, including service-agent permissions. Test duplicate
and concurrent delivery plus a crash between effect and acknowledgment. Record what
was verified. See [subscriber guidance](https://cloud.google.com/pubsub/docs/subscribe-best-practices)
and [exactly-once scope](https://cloud.google.com/pubsub/docs/exactly-once-delivery) when
that guarantee is material; it does not establish exactly-once external effects.

## Data, cost and infrastructure

For analytical data, define event time, schema compatibility, retention, access and
partition/query patterns before choosing ingestion machinery. Estimate cost from
representative storage, queries, compute and egress; validate expensive assumptions
against observed usage. Alerts-only budgets notify; they do not establish a spending cap. Verify current
[cost controls](https://cloud.google.com/billing/docs/how-to/budgets) for the actual service.

Use [Terraform IaC](../../terraform-iac/SKILL.md) for state, module, IAM ownership and
plan review. Preserve environment isolation and review replacement/deletion effects.
A backup configuration is not restore evidence: exercise recovery against the agreed
data-loss and recovery-time targets when required.

## Select another boundary only when needed

- [GCP role](../../../../agents/architecture/gcp-architect.agent.md): service and operational tradeoffs.
- [DevOps role](../../../../agents/engineering/devops-agent.agent.md) and
  [CI/CD](../../devops-cicd/SKILL.md): build/promotion/release mechanics.
- [Cloud native](../../cloud-native/SKILL.md): provider-neutral deployment choices.
- [Security](../../../quality/security/SKILL.md): a concrete trust boundary.
- [Microservices](../../../architecture/microservices/SKILL.md): a justified service split.
