# Python boundary guide

Read the section that resolves the current uncertainty. The project version, dependencies
and contracts govern; examples are decision exercises, not a prescribed architecture.

## FastAPI boundaries

Trace one request through router, validation, identity, authorization, business rule,
transaction and response. A valid token does not establish permission for an object.
Check the denied case and ensure internal fields cannot escape through serialization.
Keep error codes and payloads compatible with consumers.

Use application lifespan for shared clients and dependencies for request-scoped
resources. Identify who opens, commits, rolls back and closes a database session;
a request must not share mutable session state with another request. Test cleanup
on failure as well as success.

Choose async handlers when their I/O is awaitable. A normal helper called directly
inside an async handler still blocks that handler if it performs blocking work;
framework scheduling of sync routes/dependencies does not automatically offload it.
Use the existing execution boundary for blocking calls and a worker for substantial
CPU work. Bound waits and preserve cancellation.

For a new endpoint, derive checks from its contract: valid input, invalid input,
missing identity, denied access, absent resource and the important downstream failure.
Use dependency overrides for narrow deterministic tests and restore them afterwards.
Exercise lifespan when the behavior relies on startup/cleanup. An overridden repository
does not verify the actual database transaction or migration.

Consult official [async guidance](https://fastapi.tiangolo.com/async/),
[lifespan](https://fastapi.tiangolo.com/advanced/events/) or
[testing dependencies](https://fastapi.tiangolo.com/advanced/testing-dependencies/)
only for the affected behavior and installed version.

## Persistence and refactoring

For an order write with a notification, identify the durability boundary before adding
an event bus. A commit followed by a publish can fail between the two; an in-memory
observer does not make delivery durable. Where reliable delivery is required, use the
project's transactional outbox or another explicit recovery mechanism. Verify a retry
cannot duplicate the business operation or external effect.

Before introducing a repository, protocol or service layer, name the variation or rule
that benefits. A simple function can be the right boundary. Compare the behavior before
and after, including exceptions and rollback; keep the refactor separate from semantic
changes where practical. Use precise money/time/identifier representations dictated by
the domain, rather than inferring them from sample code.

The optional [better-python reference](https://github.com/atstaeff/better-python)
contains before/after examples. Inspect its actual code only when an example answers
the task; it does not set this project's Python minimum, dependencies or layout.

## Select another boundary only when needed

- [Python role](../../../../agents/languages/python-expert.agent.md): a bounded implementation or review handoff.
- [Clean code](../../../engineering/clean-code/SKILL.md),
  [SOLID](../../../engineering/solid-principles/SKILL.md) and
  [design patterns](../../../engineering/design-patterns/SKILL.md): a demonstrated structural problem.
- [GCP](../../../engineering/gcp-patterns/SKILL.md): cloud runtime behavior.
- [Anti-patterns](../../../quality/anti-patterns/SKILL.md): checking a proposed abstraction.
