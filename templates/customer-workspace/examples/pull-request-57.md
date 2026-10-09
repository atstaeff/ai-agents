# Proposed PR 57: Reuse the document reference when an upload attempt is retried

Fictional draft PR description; no implementation or checks have been performed.

Refs #42.

The intended change reserves a customer-scoped attempt key before processing and reuses
the document reference when that attempt is retried. A deliberate new attempt uses a new key.
The final description must reflect the actual implementation and chosen expiry behavior.

## Verification required before review completion

- [ ] Link actual approval of the implemented plan revision and its review notes from issue 42.
- [ ] Establish each acceptance case from issue 42, including concurrent requests.
- [ ] Run the project's relevant checks and link actual results.
- [ ] Confirm the Product Owner's attempt semantics and Operations' retry window.
- [ ] Obtain required technical review.
- [ ] Validate the process knowledge update and decision status.

The decision draft explains alternatives; process knowledge explains current accepted behavior.
Add actual source and check links instead of copying full logs here.
Use the project's issue-closing convention only after its acceptance rule is satisfied.
