---
name: "domain-driven-design"
description: "Model business rules, aggregates, bounded contexts or domain terminology in an existing or new application."
---

# Domain Driven Design

## Workflow

1. Build a small shared vocabulary from real user scenarios. Put business invariants close to the data they protect.
2. Define boundaries by behavior and ownership, not by copying database tables. Start with modules before distributed services.
3. Use dataclasses and explicit validation for new Python domain objects; use the project's established validation library at external boundaries.
4. Introduce aggregates, repositories or domain events only when they simplify invariants, persistence or a real integration.
5. Test business behavior without infrastructure; record the few decisions that constrain future changes.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/domain-driven-design.md): load only the section relevant to the task.
