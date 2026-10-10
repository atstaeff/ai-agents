---
name: "testing"
description: "Implement or improve tests that verify acceptance behavior and realistic regressions; report what executed checks establish and what remains unverified."
---

# Testing

1. Read the acceptance criteria, affected code and existing checks. Obtain expected
   behavior from the requirement, consumer contract or a reproduced defect, rather
   than deriving every assertion from the new implementation.
2. For a bug, reproduce it before the fix where practical and retain a focused
   regression check. Select unit, integration or end-to-end checks by the boundary
   at risk. Reuse the framework; prefer unittest for new Python stdlib projects.
3. Exercise the primary outcome and material failure/recovery behavior. Keep fixtures
   small and deterministic; mock external boundaries rather than the behavior under test.
4. Run the relevant checks. Inspect failures and fix their cause; do not weaken
   assertions, silently skip failures or change expected results merely to get green.
5. For UI work verify the running user journey and relevant responsive/keyboard states
   when tools allow. For APIs exercise consumer-visible responses and relevant access
   and compatibility boundaries. Syntax checks alone do not establish these outcomes.
6. Report commands, actual results, affected acceptance criteria and material gaps.
   Stop expanding checks once required coverage passes unless new changes, failures
   or unresolved concerns justify more. Do not add tests for wording-only changes.

## Focused references

- [Testing strategy](../software-engineering/testing-strategies.md): choose test levels when coverage is unclear.
- [Detailed examples](references/guide.md): load only the relevant section.
