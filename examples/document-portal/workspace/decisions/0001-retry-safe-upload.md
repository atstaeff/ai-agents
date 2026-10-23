---
title: ADR-0001 Retry-safe document upload
knowledge_id: ADR-0001
slug: decisions/adr-0001
status: proposed
owner: technical-owner
relations: {}
sources:
  - https://github.com/CUSTOMER_ORG/CUSTOMER_REPO/issues/42
---

# ADR-0001: Retry-safe document upload

Fictional decision draft. No customer approval or implemented behavior is claimed.

## Context

A client may retry an upload after a lost response. Staff need a stable document reference
for that attempt. A deliberate new upload of the same file may have a different business purpose.
See [issue 42](https://github.com/CUSTOMER_ORG/CUSTOMER_REPO/issues/42).

## Options

- Treat every request as a new upload.
- Deduplicate globally by file content.
- Reuse a client-generated upload-attempt key scoped to the authenticated customer.

## Proposed decision

Use one upload-attempt key for retries of the same attempt. A deliberate new attempt uses
a new key. Return the existing document reference on a retry. Reject reuse of the same
key with a different payload. [ADR-0002](0002-atomic-upload-claim.md) proposes how the
server establishes one owner for concurrent attempts; that decision depends on this semantic choice.

This preserves legitimate new uploads while preventing duplicate work for one attempt.
The key retention period is an open decision; ask Operations about the retry window before acceptance.

## Consequences and evidence

The client must retain its attempt key across retries. The server needs an atomic claim,
customer isolation and a bounded retention policy. Verify retries, concurrent same-key requests,
different keys, changed payloads and cross-customer separation.

Decision owner: Technical Owner. Business meaning: Product Owner.
Status remains proposed until the required decisions and evidence are recorded.
[Process knowledge](../knowledge/upload-retries.md) is updated after the accepted behavior is implemented.

Acceptance records the authorized decision maker's agreement. Implementation, test results
and deployment are tracked separately; an accepted decision does not prove deployed behavior.
