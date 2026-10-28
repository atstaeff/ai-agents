# Distributed service boundaries and recovery

Read the affected section when evaluating a service split or changing an existing
service. Keep the established deployment stack; this guide does not select a cloud,
message broker or framework.

## Justify the boundary

Identify a concrete independent deployment, ownership, scaling or isolation need.
Compare a module boundary in the current application before extraction. A separate
service adds network failures, schema evolution, operations and data reconciliation.

Specify the owner of each invariant and write. Separate logical data ownership from
physical database placement: a shared database is a coupling risk to assess, not a
reason to migrate automatically. Avoid allowing several services to update the same
invariant without an explicit concurrency and transaction contract.

## Requests and failure budgets

For each call, define deadline, cancellation, failure response and concurrency limit.
Keep the end-to-end time budget visible across nested calls. Bound retries to transient
failures and safe operations; use backoff/jitter and avoid retrying at every layer.

A timeout after sending a charge or command has an uncertain outcome. Query the
operation by a stable idempotency key before repeating it. A client timeout does not
prove that the server rolled back.

A retry repeats work. A circuit breaker tracks failures across calls and temporarily
rejects work while a dependency recovers. Choose an actual compatible implementation
when needed; a retry decorator alone is not a circuit breaker. Verify library APIs in
[their documentation](https://tenacity.readthedocs.io/), not an illustrative import.

## Durable workflows

When a local write must produce an event, define how both survive process failure.
A transactional outbox or equivalent supported mechanism can record the change and
pending publication together; consumers still need duplicate handling and schema rules.
Logging a publish failure after a commit does not ensure later delivery.

A multi-service workflow needs durable step state, stable operation identities,
retryable transitions and an owner for unresolved outcomes. Compensation is a new
business action: it can fail and may not restore the previous world. Define pending,
failed and manually repairable states; an in-memory try/except chain is insufficient
for recovery after a crash.

## Compatibility and extraction

1. Choose one consumer-visible path and agree its contract before parallel writers.
2. Define schema/API compatibility for old and new consumers during deployment.
3. Decide data backfill, concurrent-write ownership and the cutover condition. Avoid
   uncoordinated dual writes; compare/reconcile data before switching the owner.
4. Exercise a full scenario with the dependency unavailable, a duplicate request,
   a timeout after commit and a restart during workflow recovery where applicable.
5. Define stop/rollback signals, operating owner and residual data repair. Rolling back
   a binary does not reverse external side effects or an incompatible data migration.

## Evidence to return

Return the boundary rationale, changed contracts/data owners, migration order and
actual end-to-end/failure evidence for a named revision. Without live dependencies,
provide a reviewable design or local checks and identify the missing integration case.

Use [API design](../../api-design/SKILL.md) for consumer contracts,
[cloud-native](../../../engineering/cloud-native/SKILL.md) for runtime resilience and
[incident response](../../../quality/incident-response/SKILL.md) for an active outage.
