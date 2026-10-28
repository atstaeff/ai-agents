# Bounded prototype and playtest

Use this reference to turn one uncertainty into an observation. Reuse the available
engine, UI stack or test harness; a prototype does not require a framework migration,
complete game template or production architecture.

## Write the experiment contract

State the decision, one assumption, time/resource budget, representative input and what
result would change the approach. Distinguish feasibility, usability and demand: a
working interaction can demonstrate one without proving the others.

Example: “Can a novice place and undo an edit on a large document without losing their
place?” Supply representative content, an observable task and the target environment.
Record actual behavior and timing; any success threshold is a proposed project target,
not a universal rule.

## Build enough of the boundary

Keep the interaction and feedback that determine the result. Replace secondary art,
navigation or external services only when that shortcut does not hide the uncertainty.
For a performance question, representative media, data size and hardware may matter
more than visual polish. For a physical device, a desktop simulation cannot establish
real timing or actuation behavior.

Isolate disposable code from production paths. Mark stubbed authentication, in-memory
persistence, missing cleanup or synthetic data so no one mistakes them for validated
behavior. Keep source/licensing for assets and explicit removal/retention conditions.

## Observe without inventing feedback

Give a participant a concrete task without revealing the intended solution. Record
what they attempted, where they paused or failed and whether recovery worked. Separate
observed behavior, quoted feedback and the author's interpretation. Do not claim a
participant session when only the author tried the prototype.

For a game, test one playable loop and ask a focused question about comprehension,
control or feedback. Keep the build, input device, seed/replay and relevant parameters
so the next iteration can reproduce the observation.

Collect only necessary permitted measurements. A local event log can support a specific
question; instrumentation must not silently add external analytics or private payloads.

## Decide and hand over

Return the runnable prototype or reviewable artifact, exact conditions, observations,
limitations and the next decision. Choose to discard, iterate or harden from the evidence.
For retained code, identify concrete production gaps: contracts, authorization, data
recovery, accessibility, resource use and actual integration checks as relevant.

A failed or unavailable runtime is still useful evidence about the experiment's limits;
provide a concrete replay and mark it unrun. Do not infer user demand, scalability or
production readiness from a successful local demo.

Use [product discovery](../../../delivery/product-discovery/SKILL.md) for value or demand,
[game design](../../game-design/SKILL.md) for playtest interpretation and
[performance](../../../quality/performance/SKILL.md) for a measured bottleneck.
