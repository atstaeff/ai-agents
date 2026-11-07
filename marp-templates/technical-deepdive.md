---
marp: true
theme: default
paginate: true
---

<!-- Describe the actual system. The delivery example is illustrative; replace it if it is irrelevant. -->

# [System or change] technical deep dive

**Audience:** [consumers, maintainers or reviewers]

**Owner:** [role] · **Revision:** [source link and tested revision]

**Purpose:** [technical decision or capability the audience needs to understand]

---

## Context and constraints

- **Behavior:** [problem, intended users and measurable acceptance]
- **Boundary:** [what the system owns, including data and external dependencies]
- **Important constraints:** [compatibility, reliability, security or resource limit]
- **Out of scope:** [related behavior outside this decision]

---

## Components and contracts

| Boundary | Responsibility and contract | Owner and failure behavior |
| --- | --- | --- |
| [Component or interface] | [Inputs, outputs and data ownership] | [Role, timeout or retry behavior] |
| [External dependency] | [Guarantee, compatibility and trust boundary] | [Role and fallback, if any] |

If a diagram helps, add a checked image with alt text and keep the main relationships
readable in Markdown. Link the maintained contract rather than copying it.

---

## A concrete path through the system

**Illustrative example: durable event delivery after an order write**

1. Persist the order and pending event in one transaction.
2. After commit, a relay publishes the pending event and can retry if delivery is uncertain.
3. Consumers apply local changes and record the stable event ID in one transaction.
   For external effects, verify that the provider honors an idempotency key.

Exercise a crash after publication but before marking the event sent. Replay the event
and verify that irreversible effects occur only once.

---

## Tradeoffs and change boundaries

- **Decision:** [specific choice and accountable owner]
- **Alternatives:** [existing design and simplest viable alternative]
- **Consequences:** [likely change cost, operational burden and failure modes]
- **Revisit when:** [measurable trigger or changed assumption; link the ADR]

---

## Evidence at the affected boundary

| Criterion | Check and expectation | Observed result |
| --- | --- | --- |
| [Consumer behavior] | [Reproducible check and independent expectation] | [Evidence and tested revision] |
| [Important failure or recovery] | [Failure condition and expected response] | [Evidence, blocked or not run] |

Use representative conditions for latency, capacity or cost claims. State sample size,
time window and limits when they affect the conclusion.

---

## Rollout and recovery

- **Compatibility and rollout:** [consumer or data transition, sequence and owner]
- **Observe and stop:** [signal, threshold and observation window]
- **Recovery:** [rollback, restore or repair; irreversible effects and tested limits]
- **Operate:** [runbook, diagnostic evidence and accountable operator]

---

## Decision and next step

- **Recommendation:** [specific decision and why]
- **Open question:** [evidence still needed and owner]
- **Next action:** [authorized step and completion criterion]
- **References:** [source, ADR and verification links]
