# Engineering quality standard

Choose the smallest design that meets the product's observable needs and can be changed
safely. Quality is a set of explicit tradeoffs supported by evidence. More abstraction,
files, agents, coverage or generated code does not establish a better product.

Use this standard when framing consequential work, reviewing architecture or agreeing
acceptance. Load the relevant section rather than adding the entire document to every task.

## Turn quality goals into scenarios

Select the qualities that matter to this increment. Use the
[quality scenario template](../templates/architecture/quality-scenario.md) to record a
stimulus, affected boundary, environment, expected response and measurable target.
Identify the owner, measurement method and revision. Treat sample thresholds as examples,
not universal project requirements.

| Quality | Useful question | Possible evidence |
| --- | --- | --- |
| Functional correctness | Does the behavior match the user's rule, including edge cases? | Consumer-visible acceptance and regression cases |
| Maintainability | Can a likely change be made without unrelated changes? | Focused diff, understandable ownership, change exercise |
| Modularity and replaceability | Can a volatile dependency be replaced behind a stable boundary? | Contract tests and a bounded substitution exercise |
| Testability | Can important rules and failures be exercised without brittle global setup? | Deterministic checks at the relevant boundary |
| Security and privacy | Are identity, authorization, trust boundaries and data handling enforced? | Denied-access cases, threat-specific checks, reviewed data flow |
| Reliability and recovery | What happens on timeout, duplicate input, partial write and restart? | Failure injection, retry/idempotency and restore exercises |
| Performance and capacity | Does realistic work meet its latency, throughput and resource budget? | Reproducible workload with hardware, data size and observed distributions |
| Usability and accessibility | Can the intended user complete the task and recover from mistakes? | Actual journey, keyboard access and relevant accessibility checks |
| Compatibility | Can existing consumers and stored data survive this change? | Consumer contracts, migration and rollback checks |
| Operability | Can someone deploy, diagnose, restore and own the result? | Runbook exercise, useful signals, rollout/recovery evidence |
| Cost and resource efficiency | Is the benefit worth compute, storage, network and maintenance cost? | Representative usage, cost estimate and measured resource consumption |

Resource consumption is a useful sustainability signal; token counts or CPU time alone
are not carbon measurements. Include embodied/operational context if making environmental
claims. Remove idle work and unnecessary retention without compromising the product.

## Make abstractions earn their place

Keep business rules distinct from volatile infrastructure where that protects a real
change boundary. Prefer cohesive modules, explicit contracts, small interfaces and
dependency direction that makes tests and changes practical. Reuse the established stack.

Introduce a shared abstraction when the common meaning is stable, variation is real and
the reduced change cost exceeds its indirection. Similar syntax alone is insufficient.
Prefer deliberate local duplication over a framework with speculative extension points.
Measure performance before optimizing; use simple data structures until evidence demands more.

For architecture, compare the existing design and the simplest viable alternative.
State compatibility, ownership, data meaning, operational burden and recovery. A modular
application is a valid solution; a service split needs a boundary and operating rationale.
Use the [architecture review](../templates/architecture/architecture-review.md) when a
consequential decision warrants it. Do not create a review document for every small fix.

## Scale checks to consequence

| Work | Minimum useful evidence | Additional consideration |
| --- | --- | --- |
| Clear reversible correction | Inspect the relevant behavior, make the change, run affected checks | No mandatory ADR, plan file or new test mirroring implementation |
| Feature or change across boundaries | Observable criteria, relevant contracts and failure cases, reviewable diff | Compare alternatives and preserve material decisions |
| Migration, security or operationally consequential change | Above plus compatibility, rollout, recovery and observation evidence | Obtain required accountable-owner decisions before affected actions |

Project policy and existing authorization determine the actual gates. A required check
may be passed, failed, blocked or not run. An omitted check needs an explicit applicability
reason; tool absence alone does not turn it into passed or not applicable.

## Trace evidence to the change

Link each important criterion to the check, result and tested revision. Derive expected
results from requirements, contracts or reproduced faults rather than copying the
implementation. Include representative input and important failure paths. Use
[verification evidence](../templates/quality/verification.md) when the existing PR or
issue format does not already capture it.

Automate repeatable deterministic checks in the project's CI. Human review addresses
consequential meaning, assumptions and tradeoffs; a second model can share the author's
mistake. A build proves buildability, not a user journey, safe deployment or business value.

Keep test suites readable, reasonably fast and deterministic. Do not add tests for
formatting-only changes or assertions that merely restate the implementation. Use a
focused regression check for a reproduced defect and broaden checks when a material
change, failure or unresolved concern justifies it.

## Review and operate

Return actionable findings with location, impact, evidence, priority and a minimal remedy.
Distinguish confirmed defects from questions. Review current revisions after material
changes; an old approval or green check is not proof for a new implementation.

For operational work, define release scope, rollout signals, stop/rollback conditions,
data repair and an accountable owner. Use the
[release and recovery template](../templates/quality/release-readiness.md) where needed.
Close work at the project's completion point; retain separate evidence for deployed
behavior and observed product benefit.

## Learn from outcomes

For comparable assignments, observe time to accepted result, human review/reconstruction
effort, escaped defects, rework and the intended user outcome. Keep the workload, model,
process revision and limitations. Improve repeated failure modes with a focused tool,
test or clarification instead of continually enlarging universal prompts.

This is an engineering convention, not a certification or a promise of defect-free
software. It complements an adopted customer standard. Useful primary references:
[arc42 quality requirements](https://docs.arc42.org/section-10/),
[quality scenarios](https://quality.arc42.org/articles/specify-quality-requirements),
[DORA small batches](https://dora.dev/capabilities/working-in-small-batches/) and
[WIP limits](https://dora.dev/capabilities/wip-limits/).
