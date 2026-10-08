# Issue 42: Prevent duplicate document handling after upload retries

Fictional issue body; create a real issue and use its actual identifier.
Project fields: Ready, Iteration I1, High priority, authorized customer worker assignee.

## Outcome and value

Service staff receive one document reference for an upload attempt even if a response
is lost and the client retries. Deliberate new uploads remain possible.

## Acceptance criteria

- [ ] A retry of the same attempt returns the same document reference and starts no duplicate processing.
- [ ] Concurrent requests for the same attempt result in one document.
- [ ] A deliberate new attempt can create a new document even for identical file content.
- [ ] Reusing an attempt key with different content is rejected with a clear error.
- [ ] Attempt keys are isolated between authenticated customers.
- [ ] Operations confirms the supported retry window; expiry behavior is documented and checked.

## Relevant context

[Customer workspace](https://github.com/CUSTOMER_ORG/CUSTOMER_REPO/blob/main/workspace/README.md)
and [decision draft](https://github.com/CUSTOMER_ORG/CUSTOMER_REPO/blob/main/workspace/decisions/0001-retry-safe-upload.md).
Inspect the actual upload endpoint, client and existing persistence boundary.

## Constraints

Reuse the existing stack. Scope this increment to retries, not general file deduplication.
Product Owner decides upload intent; Technical Owner reviews design; Operations decides the retry window.

<!-- ai:status:start -->
## AI work status

Plan: confirm attempt semantics and retry window; inspect the existing upload boundary;
implement one bounded change; verify acceptance cases; prepare a linked PR and knowledge update.
Next action: inspect existing handling and bundle consequential questions.
Evidence: none yet. Required checks and human acceptance are outstanding.
<!-- ai:status:end -->

Customer-owned text and feedback outside the bounded AI section must be preserved.
