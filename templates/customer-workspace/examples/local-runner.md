# Local runner contract

This is a design contract, not implemented software or a started background job.
The initial manual workflow can use Jorg in the customer's checked-out repository.
A runner additionally needs authenticated access to the customer's Project, issues and
repositories and an AI host capable of performing the authorized actions.

## Minimal loop

1. Read the configured customer Project. Select current-iteration Ready issues assigned
   to the explicitly authorized worker identity; resume its existing active issue first.
2. Compare Project field changes and issue/comment revisions with the local cursor.
   Load the active issue's current body, open questions and relevant new feedback.
3. Claim one issue, create or resume its branch, and invoke the host with the issue and
   customer instructions. For multiple runner processes, use a shared claim mechanism.
4. For a review-required assignment, submit the concrete plan revision and await actual
   approval. Persist the revision, review reference, notes and decision before invoking
   Build with its configured model/variant. A rejection returns to Plan; cancellation,
   timeout or unavailable review stays blocked. Do not infer approval from a successful call.
5. Execute a bounded increment, verify it and publish a material update or draft PR.
   On a consequential blocker, record the question and await a relevant answer.
6. At iteration close, prepare one report from actual accepted work and unresolved items.
   Upsert its draft using the iteration identifier so retries do not create duplicates.

## Efficiency and recovery

Use a small metadata query before loading issue bodies. Cache unchanged guidance; reread
mutable assignments and feedback. Avoid loading every historical issue or archived decision.
Back off while idle or waiting. Work only within the issue's agreed time and action budget.

Keep per-customer credentials, checkpoints and claim state in local protected configuration.
Persist issue, branch and last processed comment identifiers for restart recovery. Deduplicate
questions and closeout drafts. On resume, compare the current plan with its approved revision;
material changes invalidate that approval and require review again. Keep credentials and model
settings local; keep the plan and receipt in the customer issue. Reconcile the host's actual
agent/model before implementation; no silent fallback to another model.
Do not mark Done solely because the host returned successfully.

Project field editing permissions are separate from repository editing permissions.
Report missing capabilities and prepare a reviewable result within the available scope.
