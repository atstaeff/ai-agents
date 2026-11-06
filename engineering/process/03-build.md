# 03 — Build

Use for authorized implementation. Read the bounded assignment, affected source/contracts
and applicable decisions; load only the relevant [engineering/language skill](../../skills/README.md).

1. Implement the smallest complete reviewable increment in the existing stack. Follow
   [session rules](../../toolkit/SESSION-RULES.md) for useful delegation, verified model
   routes and autonomous completion. Match instructions to the task, not an arbitrary team size.
2. Preserve human edits and comments. Coordinate overlapping writes through the adopted
   mechanism, isolate independent writers and agree integration order. Without an effective
   shared claim mechanism, serialize overlapping changes. A worktree is not a distributed lock.
3. Inspect returned changes and evidence. Reread before writes and use available version
   checks; after a remote timeout inspect existing effects before retrying the mutation.
4. Record newly significant reasons when they arise; return to [plan](02-plan.md) if a
   consequential assumption or shared contract changes. Do not silently override accepted ADRs.

Result: reviewable changes linked to the assignment. Continue to [verify](04-verify.md).
A dispatched task, idle worker or successful individual branch is not an integrated result.
