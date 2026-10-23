---
title: ADR-0004 Private plans and shared project knowledge
knowledge_id: ADR-0004
slug: decisions/adr-0004
status: proposed
owner: repository-owner
relations:
  relates_to: [ADR-0003]
sources: []
---

# ADR-0004: Private plans and shared project knowledge

## Situation

The operating model repeated workflow rules across many pages and profiles. It required
workspace/YAML setup and put execution plans in shared assignments by default. A personal
contributor instead needs one planning home across repositories, while the team needs
maintainable results and consequential rationale.

## Options

- Keep all execution details in issues or repository work records.
- Store both personal plans and team knowledge in a private vault.
- Keep personal execution in the Second Brain and durable project knowledge with the team.

## Proposed decision

Use `AGENTS.md` as the short project entry, linking existing vision, owners, process,
commands and knowledge. Require no new workspace directory or YAML. Keep personal plans
in the privately configured Second Brain project folder, subject to project storage policy.
Issues own shared scope/acceptance and PRs own changes and actual verification. After
implementation, preserve significant decisions and affected current documentation in
shared project sources. A teammate must not depend on access to the author's private plan.

Generate optional Docusaurus pages and a graph from allowlisted shared Markdown. Preserve
proposals and superseded rationale visibly. Keep private plans, vault paths and exports
outside publication. Retain existing local store/schema interfaces for compatibility.

## Consequences

The default process needs fewer documents and less repeated context. Personal planning
requires explicit host-local configuration; an inaccessible vault produces an unsaved
session plan, not a second repository record. Team execution plans remain appropriate
when contributors actually need shared steps. Existing bundle users must re-export;
Plan is read-only until a narrow external plan directory is explicitly configured.

The changes and demo are prepared for PR review. This proposal records the new design;
owner acceptance, merge, deployment and installed-host behavior are not claimed here.
