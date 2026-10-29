# Focused test design

Read the section that matches the affected boundary. Reuse the project's runner,
fixtures and required gates; a sample framework or coverage target is not a mandate.

## Expectations and test scope

Derive the expected result from acceptance, a consumer contract or a reproduced fault.
Choose representative equivalence classes and important boundaries, then exercise the
actual failure/recovery behavior. A concise test should make the condition, action and
observable result obvious without reproducing the implementation.

| Need | Useful boundary | Limit |
| --- | --- | --- |
| Business rule | Pure unit case with explicit inputs/results | Does not establish storage or transport behavior |
| Request/response contract | Actual routing, validation and authorization | In-process transport may omit network/server behavior |
| Transaction or stale write | Real persistence and competing operation | An in-memory fake may have different locking/constraints |
| Critical user interaction | Running browser/app journey and recovery | One environment does not establish every device/layout |
| Crash or restart recovery | Durable state plus interrupted workflow | A normal exception test may not exercise process loss |

## Doubles, data and cleanup

Use a fake for a boundary whose relevant behavior it can faithfully represent. Preserve
error, identity and mutable-data ownership contracts; avoid a fake that silently shares
objects when production returns independent records. Use real integration checks where
transaction, schema, authorization or library behavior is the risk.

Keep fixtures small and readable. Override only fields relevant to the scenario, avoid
hidden shared mutable defaults and give each test isolated state. Use explicit clocks,
seeds or IDs when nondeterminism obscures the rule. Clean up resources on assertion
failure as well as success; distinguish per-test and process/application lifetimes.

For async checks, use the runner's supported async integration and await started work.
Bound waits on observable conditions rather than arbitrary sleeps. Restore dependency
overrides, environment changes and subscriptions so order does not determine the result.

## HTTP and UI evidence

Exercise allowed, denied and invalid requests at the consumer-visible boundary. Assert
meaningful status/error/data behavior and side effects. Inspect relevant identity and
resource scope; a successful happy-path request does not prove authorization.

With an in-process ASGI transport, explicitly manage the application's expected lifespan
and dependencies according to the installed libraries. Distinguish that result from a
live server, real database and deployed integration. Use the project's established setup
rather than copying deprecated client arguments.

For UI behavior, check the actual action and visible recovery: loading/empty state,
validation, duplicate submission, failed mutation, navigation or stale request as affected.
Use stable semantic locators and controlled dependencies where practical. A screenshot
or successful build does not establish keyboard operation, focus or a completed journey.

## Failures, coverage and reporting

When a check fails, inspect the cause. Preserve the failure, fix a defective assumption
or implementation and rerun the affected check; do not weaken the expected result merely
to get green. If it is flaky, preserve a reproduction and isolate the nondeterminism.
Record unrelated pre-existing failures separately instead of claiming the suite passed.

Coverage identifies unexecuted code, not whether assertions are meaningful. Select
additional cases from risk and project gates; fixed test-type ratios and blanket
coverage percentages are not evidence of correctness. Property or mutation tests can
probe a consequential rule when they answer a real uncertainty.

Return the command, actual result, tested revision, linked criterion and material gap.
Mark blocked/unrun checks explicitly and give a concrete next verification action.
Stop expanding once required evidence is sufficient unless a new change, failure or
unresolved risk justifies more.

## Primary tool references

Use the installed version's [unittest](https://docs.python.org/3/library/unittest.html),
[pytest](https://docs.pytest.org/), [HTTPX transports](https://www.python-httpx.org/advanced/transports/),
[Flutter testing](https://docs.flutter.dev/testing/overview) or
[Playwright](https://playwright.dev/docs/intro) documentation only for the selected tool.
