---
name: "architecture-planning"
description: "Produce a concise architecture plan with boundaries, alternatives, delivery steps and verification."
---

# Architecture Planning

## Workflow

1. Read the actual assignment, current architecture, relevant decisions and affected consumers.
   Distinguish intended behavior, implemented behavior and unresolved assumptions.
2. Identify the outcome and the few quality attributes that determine the choice. Use
   stimulus/response/measure scenarios instead of unsupported claims such as scalable or clean.
3. Compare the current design and the simplest viable alternative. Include data meaning,
   dependency direction, trust boundaries, compatibility, operating/change cost and recovery.
4. Make abstractions earn their indirection. Propose a replaceable boundary for real
   variation; do not add speculative frameworks or service splits by default.
5. Sequence small complete increments with checks derived from criteria and contracts.
   Name consequential uncertainties and the owner who can decide them.
6. Preserve the plan in its existing home. Draft significant rationale at the designated
   decision home while alternatives are known. An accepted ADR and its replacement status
   constrain dependent work; a proposal does not silently revoke them.

## Focused references

- [Detailed examples](references/architecture-planning.md): load only the section relevant to the task.
- [Quality standard](../../../toolkit/QUALITY-STANDARD.md) and
  [architecture review](../../../templates/architecture/architecture-review.md): use for the affected quality and decision boundary.
