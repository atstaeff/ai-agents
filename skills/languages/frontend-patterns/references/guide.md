# Frontend interaction guide

Read a section for a concrete uncertainty. Preserve the installed framework, existing
data layer and design system; this guide requires no new dependency or migration.

## React state and effects

For a searchable list, keep the query in component state or the URL according to the
navigation contract. Derive the displayed list from data plus query. Do not maintain a
second filtered copy with an Effect. Use stable domain keys so reordering cannot move
an input's local state to another item.

Keep transient state close to its consumer; lift genuinely shared state to its owner.
Reuse the framework's loader/query mechanism for server data when available. Cache
identity must include relevant parameters and authorization scope. Invalidate or update
affected queries after a successful mutation; prevent cross-user cached data reuse.

An Effect synchronizes with an external system: subscription, timer, widget or request.
List the values it reads as dependencies and undo its work on cleanup. Derive ordinary
rendered values during render and handle user mutations in events/actions. Test the
setup/cleanup/setup sequence when development Strict Mode exposes a leak; suppressing
the second run hides the defect.

For a rapid search, let request A start, then request B. Resolve B first and A last;
the screen must still show B. Abort obsolete requests or ignore stale results, with
loading/error state owned by the current request. Cancellation alone does not undo a
server mutation; use the backend's retry/idempotency contract for uncertain outcomes.

Consult React's [state guidance](https://react.dev/learn/choosing-the-state-structure),
[Effects](https://react.dev/learn/synchronizing-with-effects) or
[unnecessary Effects](https://react.dev/learn/you-might-not-need-an-effect)
only for the relevant behavior.

## API and interaction checks

Static TypeScript types do not validate an HTTP response. In JavaScript and TypeScript,
check status/error semantics and validate uncertain external data at the appropriate
boundary. Reuse an existing schema/client instead of inventing a parallel abstraction.
Keep credentials and sensitive diagnostics out of rendered errors and logs.

For a save form, exercise invalid input, pending submission, success and server failure.
Retain entered values after failure and associate errors with the relevant controls.
Prevent duplicate clicks while a request is pending; preserve recovery when the outcome
is unknown. Authentication, object authorization and business validation still belong
on the server even if the client hides a control.

Run the primary journey with realistic data. Verify labels, tab order, visible focus,
keyboard activation, modal focus return and relevant small/large layouts. Include
loading, empty and error states in the check. A screenshot checks appearance; a build
checks compilation. Neither establishes the interaction or accessibility by itself.

For Vue or Angular, apply the same state/cleanup and interaction contracts through the
project's established reactive APIs. Consult the installed framework's official docs
when a lifecycle or scheduler detail matters; do not transplant React Hooks.
