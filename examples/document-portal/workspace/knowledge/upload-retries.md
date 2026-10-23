---
title: Upload retry behavior
knowledge_id: PROCESS-UPLOAD
slug: knowledge/upload-retries
status: draft
owner: technical-owner
relations:
  governed_by: ["ADR-0001", "ADR-0002"]
sources:
  - https://github.com/CUSTOMER_ORG/CUSTOMER_REPO/issues/42
  - https://github.com/CUSTOMER_ORG/CUSTOMER_REPO/pull/57
---

# Upload retry behavior

Fictional knowledge draft. Validate against the implementation before accepting it.

One attempt key represents one upload intent within one authenticated customer.
Retries of that attempt return the same document reference. A deliberate new upload
uses a new key. A key must not be reused with different content.

The key's retention window is unresolved. The final document must state that window
and behavior after expiry so clients can implement recovery correctly.

The business flow remains document intake, validation, processing, case assignment
and staff decision. Stable document references reduce ambiguity during intake.

Rationale and alternatives are in [ADR-0001](../decisions/0001-retry-safe-upload.md).
The concurrent-ownership proposal is in [ADR-0002](../decisions/0002-atomic-upload-claim.md).
Implementation and verification belong to the [linked PR](https://github.com/CUSTOMER_ORG/CUSTOMER_REPO/pull/57).
Keep those details linked instead of copying code, test logs or the issue plan here.
