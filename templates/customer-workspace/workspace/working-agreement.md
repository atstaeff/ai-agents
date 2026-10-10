---
title: Working agreement
description: One assignment, one owner, proportionate checks and customer-owned knowledge.
---

# Working agreement

Example policy to review and adopt with the customer before enabling automation.
This worked configuration uses the GitHub locations in the [project configuration](project.yaml).
For another tracker/wiki, adapt locations, statuses, permitted fields and channels first;
the shared process does not mandate GitHub or a mirror issue.

## Ready and ownership

A Ready issue has an outcome, observable acceptance criteria, relevant links, an iteration
and an accountable assignee. The Product Owner chooses priority and scope. A runner takes
only Ready issues explicitly assigned to its customer-authorized GitHub identity.

Use one active issue per runner. Work in one branch per issue and avoid concurrent writers
to the same files. Assignment and status are coordination signals; multiple runners need
a shared claim mechanism rather than relying on an assignee field as a lock.

## Deliver an increment

1. Read the issue, relevant code and selected workspace pages. Reuse already loaded guidance.
2. Keep the plan in the issue's designated AI section. For planned delivery in this example,
   the Technical Owner reviews the concrete revision in local Plannotator before Build.
   Address requested changes and resubmit; record actual approval and notes in the issue.
3. Implement the smallest complete increment within the approved scope.
4. Run relevant checks and prepare a linked PR. Explain missing verification explicitly.
5. Move to Review when the result is reviewable. Done requires acceptance evidence, required
   review and the customer's agreed completion point. In this example, a human-approved merge.

Use the [plan review example](../examples/plan-review.md). While approval or a consequential
answer is pending, use Blocked with the reason and next action; no extra board field is
needed. Cancellation, timeout or tool failure does not authorize implementation. If the
review UI is unavailable, require explicit review through the existing issue or conversation.
Reopen review for material scope or design changes. Small direct tasks need a gate only
when the user or customer requires one. Plan approval does not accept an ADR, merge or deploy.

## Action scope

After this policy is adopted, the worker may edit its branch, prepare draft PRs, update
its own issue status section and ask bounded questions in that issue. It may notify only
the verified role contact listed in [stakeholders](stakeholders.md) through that channel.
Merging, deployment, deletion and changes to access rights require separate authorization.

## Questions and updates

Bundle related questions with a recommendation, impact and needed decision. Route business
questions to the Product Owner and design questions to the Technical Owner. Set Blocked
for unanswered consequential questions; continue independent authorized work.

Reread the issue before updates. Preserve human-owned sections and comments; update only
the bounded AI section. On the first assignment, append the `ai:status:start` and
`ai:status:end` section shown in the issue example if it is absent. Keep its plan, next
action and evidence there. Detect intervening edits and retry rather than overwrite them.
Post a new comment only for a question, material blocker or reviewable result.

## Knowledge and completion

The issue records the live plan; the PR records implementation and checks. Update current
process knowledge when accepted behavior changes. Draft significant decisions when they
arise, while alternatives and feedback are available. Record reasons, consequences and
the responsible decision maker.
The authorized decision maker accepts or rejects the decision; implementation evidence stays
in the PR. Preserve an accepted decision's rationale. To change the substantive decision,
create a new ADR with a supersedes relation and mark the old ADR superseded. Reviewed status,
replacement links and factual corrections may change; they do not silently rewrite history.

At iteration close prepare one short report from linked outcomes, open work and feedback.
Distinguish delivered, reviewed, deployed and measured results. Link detailed evidence.
A documentation site and graph are generated views; maintain the underlying Markdown and links.
Closeout links decisions already recorded and drafts only missing significant decisions.
Do not turn every completed issue or iteration report into an ADR. Rebuild the knowledge
index and map from relations before building Docusaurus; read workspace sources for AI work.
