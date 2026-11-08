---
name: "build"
description: "Implement an authorized change, follow the applicable plan and verify behavior at the affected boundary."
---

# Build

## Operating contract

Follow project instructions and [session rules](../../toolkit/SESSION-RULES.md).

## Workflow

1. Inspect relevant instructions and code; read the current assignment and applicable shared or private plan when available. A clear, small change needs no separate planning stage or record.
   If plan review is required, verify actual approval of the current revision and its notes before implementation. Reopen review for a changed scope or consequential design; preserve the approved handoff when switching models.
2. Use the existing stack and selected skills. Implement the smallest complete change; resolve routine reversible issues independently.
3. Verify acceptance and important failure cases where the behavior is used, such as a
   CLI invocation, UI journey, API request or device operation. For wording edits, inspect
   the content and diff; run any checks the project requires.
4. Deliver a reviewable change with the tested revision, actual results and material limits.
   Preserve feedback and report blocked or unrun checks at the existing work home.

## Select only for the current uncertainty

- [work-management](../../skills/delivery/work-management/SKILL.md)
- [agent-routing](../../skills/general/agent-routing/SKILL.md)
- [testing](../../skills/quality/testing/SKILL.md)
