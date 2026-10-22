---
title: ADR-0003 AGENTS.md as the project collaboration entry
knowledge_id: ADR-0003
slug: decisions/adr-0003
status: proposed
owner: repository-owner
relations:
  relates_to:
    - ADR-0001
    - ADR-0002
sources:
  - https://github.com/atstaeff/ai-agents/pull/8
---

# ADR-0003: AGENTS.md as the project collaboration entry

## Starting situation

The user requested an AGENTS.md entry that links vision, stakeholders, scope, process,
knowledge and decisions, including centrally maintained web documentation. Several people
and AI sessions must coordinate work and recover context without a mandatory workspace
hierarchy or project.yaml.

## Insight and alternatives

A required YAML manifest makes fields mechanically visible but adds configuration and
limits direct web-backed context. A large self-contained AGENTS.md would duplicate project
facts and reusable procedure. A linked collaboration contract preserves discoverability
while keeping each fact at its owner. Markdown checks cannot prove prose completeness,
remote access or correct agent behavior; those still need review and a real host pilot.

## Proposed decision and consequences

Use root AGENTS.md for source navigation and collaboration invariants. Link project facts,
CONTRIBUTING.md, actual work/review homes, current knowledge and decision history. Local
Markdown and explicitly adopted web sources are both supported. Pin remote policy to an
immutable revision or a maintained version; record the actual source version used.

Keep project-specific facts with their project. Publish selected canonical Markdown through
Docusaurus. Use knowledge/ for this repository's durable records. Preserve historical
proposal rationale and stable public routes. Retain legacy YAML examples/validation and
optional workspace/ workbench storage without requiring them for new adoption.

Provide templates for a team repository, an existing repository, remote documentation,
multi-repository coordination and component-specific instructions. Distinguish these
AGENTS.md instruction files from catalog role definitions named *.agent.md.

This implements the requested direction for review in PR #8. It records no independent
approval, authorized merge, deployment or measured productivity benefit. Acceptance status
and implementation/publication evidence must be recorded separately.
