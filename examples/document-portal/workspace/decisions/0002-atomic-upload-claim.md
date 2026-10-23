---
title: ADR-0002 Establish one owner for a concurrent upload attempt
knowledge_id: ADR-0002
slug: decisions/adr-0002
status: proposed
owner: technical-owner
relations:
  depends_on: ["ADR-0001"]
sources:
  - https://github.com/CUSTOMER_ORG/CUSTOMER_REPO/issues/42
---

# ADR-0002: Establish one owner for a concurrent upload attempt

Fictional decision draft. No storage product, approval or implementation is assumed.

## Context

[ADR-0001](0001-retry-safe-upload.md) proposes that retries share an attempt key within
one authenticated customer. Two workers may receive that key at the same time. A
read-then-write check alone cannot establish which worker owns processing.

## Options

- Read for an existing attempt, then insert without an atomic uniqueness guarantee.
- Atomically establish one owner using the existing durable storage boundary.
- Introduce a separate coordination service for upload attempts.

## Proposed decision

Use an atomic claim for the customer and attempt key at the existing durable storage
boundary, where that boundary supports the required guarantee. Record the stable document
reference and processing state. Concurrent losers reuse that state rather than begin a
second processing operation. Validate this against the actual stack before accepting it.

## Consequences and confirmation

The design must define recovery after worker failure, concurrent response behavior and
the retry/retention window. An atomic claim alone does not provide exactly-once downstream
processing. Recovery and side effects need separate verification.

The Technical Owner reviews storage capabilities and failure cases. Operations confirms
retention and recovery requirements. Remain proposed while those decisions are unresolved.
