---
name: "software-engineering"
description: "Implement a bounded change across modules or languages: trace the existing behavior, preserve contracts and verify the integrated result. Prefer the language skill for language-specific syntax or tooling."
---

# Software Engineering

1. Trace the affected entry point, business rule, state ownership and consumers. Read the
   contract and observed defect/acceptance before choosing files or abstractions.
2. Implement the smallest complete change in the established stack. Keep business rules
   separate from volatile boundaries when that makes a real change/test cheaper.
3. Preserve compatibility, error semantics and other writers' work. Resolve consequential
   interface changes with the owner; isolate concurrent work and verify combined changes.
4. Derive checks from acceptance or a reproduced defect. Exercise affected consumers and
   important failure/recovery cases. Report actual commands, tested revision and limits.
5. Update affected current knowledge and significant rationale; retain progress and the next
   action at the existing work home. Add no speculative framework or generic process report.

Load a language skill for syntax/tooling, [refactoring](../practical-refactoring/SKILL.md)
for structural changes, or [testing](../../quality/testing/SKILL.md) for verification design.
