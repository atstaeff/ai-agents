---
name: "build"
description: "Implement the current plan, preserve feedback and verify resulting behavior with the appropriate engineering skills."
---

# Build

## Operating contract

Follow project instructions and [session rules](../../toolkit/SESSION-RULES.md).
Use the current session unless a supported, authorized handoff improves the outcome.

## Workflow

1. Inspect relevant instructions and code; read the current assignment and existing private plan when available. A clear, small change needs no separate planning stage or record.
   If plan review is required, verify actual approval of the current revision and its notes before implementation. Reopen review for a changed scope or consequential design; preserve the approved handoff when switching models.
2. Use the existing stack and selected skills. Implement the smallest complete change; resolve routine reversible issues independently.
3. Match checks to the affected boundary. For wording-only edits inspect exact content
   and diff. A listed test command is not a requirement for every change; execute it
   only for affected behavior or a policy explicitly requiring it for this kind of edit.
   For behavior changes, verify affected acceptance and important failure cases at the
   UI/API boundary. Report unavailable checks and preserve feedback in the existing work home.
4. Deliver a reviewable change with actual results and material limits.

## Select only for the current uncertainty

- [work-management](../../skills/delivery/work-management/SKILL.md)
- [agent-routing](../../skills/general/agent-routing/SKILL.md)
- [testing](../../skills/quality/testing/SKILL.md)
