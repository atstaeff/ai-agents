# Plan review for issue 42

Fictional walkthrough; no review, approval or implementation has occurred. Keep the
live plan in the customer's real issue. Configure local Plannotator using the
[toolkit guide](../../../toolkit/PLAN-REVIEW.md); it is a review interface, not an issue sync.

## Plan revision r1

Plan inspects the upload boundary, confirms upload intent and proposes a customer-scoped
attempt key with a persistence claim. It lists acceptance cases and asks Operations for
the supported retry window. Consequential unanswered questions keep this revision a draft.

Example reviewer comments:

- Technical Owner: explain how concurrent requests claim the attempt atomically.
- Product Owner: a deliberate new upload needs a new key even for identical content.
- Operations: define expiry using the actual supported retry window before approval.

The operator verifies role authority separately. Plannotator returns requested changes;
Plan incorporates the actual answers and submits r2. Answering questions alone does not
authorize Build. Preserve original human comments and summarize their disposition.

## Proposed issue update before approval

Update only the issue's existing bounded AI section. The example deliberately remains
unapproved; replace placeholders with actual answers and evidence.

```markdown
<!-- ai:status:start -->
## AI work status

Plan revision: r2, draft; awaiting the authorized reviewer's approval.
Plan: reserve a customer-scoped attempt key atomically; return the existing reference
for a retry; reject changed content; use the agreed expiry; check concurrent requests,
customer isolation and deliberate new attempts; prepare a linked PR and knowledge update.
Feedback: concurrency and upload intent incorporated; retry window still needs a real answer.
Plan review: required; approval evidence: none. Implementation has not started.
Next action: resolve the remaining question, verify assumptions and submit the revised plan.
Evidence: no implementation or checks yet.
<!-- ai:status:end -->
```

## Approval and Build handoff

After a real reviewer approves the settled revision, record its revision identifier,
actual reviewer, attached notes and available session/message or issue-comment reference
in that same section. Do not claim a reviewer or decision that the evidence does not identify.
Select Build and its configured model/variant; carry issue 42, the approved plan and notes,
acceptance criteria and relevant code/decision links into the implementation phase.

Build supplies actual check results and a linked PR. A new scope or consequential design
change returns to Plan and review. Approving the plan neither accepts ADR-0001 nor grants
merge or deployment. The [PR example](pull-request-57.md) records those separate checks.
The customer's knowledge remains in its issue and repository; leave private Obsidian
auto-save off for this assignment.
