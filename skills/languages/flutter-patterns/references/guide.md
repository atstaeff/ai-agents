# Flutter state and platform boundaries

Use the section that matches the change. Follow the application's current Dart/Flutter
version, state management, router and dependency lock; select a new package only for a
concrete unmet need. Examples in package documentation may target a different version.

## State ownership and requests

Distinguish local interaction state, navigation state and remotely owned data. Keep one
owner for each value and derive presentation values where practical. A StatefulWidget
can be sufficient for local state; BLoC, Riverpod, code generation and use-case classes
are choices for real ownership needs, not prerequisites.

Represent loading, empty, error and success deliberately. For search or filter changes,
ensure an older completion cannot overwrite newer intent. Define cancellation, request
identity and error handling in the existing data layer; check disposal and mounted
state before accessing a widget's context after an asynchronous gap.

Retain user input and useful previous data during failed mutations where the user
expects recovery. Distinguish an optimistic UI update from a committed server change;
define rollback/reconciliation and duplicate-submission behavior. An uncertain timeout
needs an operation-status/idempotency contract before retrying a side effect.

## Widgets, models and lifecycle

Keep build methods free of requests and other side effects. Dispose owned controllers,
subscriptions, focus nodes and other resources at their actual lifetime boundary. Do
not dispose a shared dependency from one consumer. Use immutable values where they
prevent aliasing bugs; preserve the project's equality and serialization conventions.

Move expensive work off the UI path when measurement shows a problem. Isolate work has
transfer, lifecycle and error costs; it is not a substitute for profiling. Use const
constructors where appropriate without presenting them as evidence of a speedup.

For offline behavior, specify freshness, pending writes, retry and conflict resolution.
Local persistence alone does not establish offline-first behavior. Preserve unsaved
changes through backgrounding, process restoration and navigation when required.

## Navigation and native integration

Trace deep links, back navigation, route restoration and authentication transitions
using the existing router. A route guard supplements server authorization. Define what
happens to an in-progress edit when identity changes or the route is replaced.

For a platform channel, document Dart/native argument and result types, thread/lifetime
rules, cancellation and error mapping. Exercise unavailable hardware, denied/revoked
permission and repeated calls. Native signing, entitlements and deployment targets
remain part of the platform contract.

## Accessibility and layout

Use built-in semantic controls and add semantics when the intended action is missing.
Verify labels, focus order, text scaling, contrast and keyboard/screen-reader behavior.
Check representative narrow/wide layouts and reduced motion. Preserve entered values
when layouts rebuild; do not infer accessible interaction from a screenshot alone.

## Verification examples

| Changed behavior | Useful check |
| --- | --- |
| State transition | Controlled success/failure and obsolete request completion |
| Form mutation | Retained input, duplicate submission, failed save and retry |
| Widget interaction | Tap/keyboard/focus action and resulting user-visible state |
| Navigation | Deep link, back, expired identity and unsaved-change handling |
| Native capability | Actual platform build plus permitted simulator/device journey |
| Layout | Representative text scales/viewports; golden test when stable visual output matters |

Use focused pumps or the established async test pattern. Waiting for all animations
to settle can hang with continuous animation; inspect why a test waits before extending
a timeout. Keep mocks at the dependency boundary and verify the real platform separately.
A golden image test establishes appearance under its environment, not behavior or accessibility.

Return changed sources and exact analysis, test, build and device results. Without the
platform/toolchain, identify the unrun checks and provide a concrete replay; do not
claim iOS or distribution readiness from a Dart-only test.

## Official references

- [Flutter architecture](https://docs.flutter.dev/app-architecture): options and ownership guidance.
- [Async context use](https://dart.dev/tools/linter-rules/use_build_context_synchronously): widget context across asynchronous gaps.
- [Platform channels](https://docs.flutter.dev/platform-integration/platform-channels): native message contracts.
- [Flutter testing](https://docs.flutter.dev/testing/overview): unit, widget and integration boundaries.
- [Accessibility](https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility): semantic and platform checks.
