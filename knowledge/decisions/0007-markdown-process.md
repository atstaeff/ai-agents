---
title: ADR-0007 Adaptable Markdown process
knowledge_id: ADR-0007
slug: decisions/adr-0007
status: proposed
owner: repository-owner
relations:
  relates_to:
    - ADR-0003
    - ADR-0004
sources:
  - https://github.com/atstaeff/ai-agents/pull/19
---

# ADR-0007: Adaptable Markdown process

## Context and alternatives

The owner requested a short AGENTS.md map, project-specific process steps in individual
Markdown files, separate skills and agents, and durable Architecture Decision Records.
A required workspace manifest makes navigation another configuration contract. A single
large guide is easy to start but mixes step procedures and repeated shared policy.

## Proposed decision

Use engineering/process/ for this repository's phase procedures. Its index selects the
applicable step; numbers are navigation, not workflow state or mandatory gates. Keep the
existing agents/, skills/ and knowledge/decisions/ homes and map them from AGENTS.md.
Other projects may rename folders and add, combine, remove or reorder steps.

Keep cross-cutting startup rules in toolkit/SESSION-RULES.md, detailed native execution
in the existing Herdr policy, project facts in PROJECT.md and contribution requirements
in CONTRIBUTING.md. toolkit/WORKFLOW.md preserves earlier links as a routing page.
Record significant decisions when they arise; current knowledge describes verified behavior.

## Consequences and evidence

The repository uses the same pattern it recommends. Selected sources publish through
Docusaurus and travel in runtime exports. Canonical source links and public routes must
remain valid; existing YAML/workbench storage stays compatible without becoming a new
project requirement. Product Intake's optional machine-executable configuration remains
separate from the Markdown collaboration process.

The implementation and verification are tracked in PR #19. This record documents the
requested direction and proposed change; it does not claim merge, deployment, independent
acceptance or measured productivity. Retain the actual acceptance and integration evidence
when available. Earlier proposed ADRs keep their recorded status and rationale.
