---
title: ADR-0002 Required project manifest and contribution routing
knowledge_id: ADR-0002
slug: decisions/adr-0002
status: proposed
owner: repository-owner
relations: {}
sources:
  - https://github.com/atstaeff/ai-agents/pull/8
---

# ADR-0002: Required project manifest and contribution routing

## Context

The project entry must identify vision, goals, boundaries, owners, key links, decisions
and the AI process. Free-form Markdown alone can silently omit a required area. Teams
also need to keep their existing document names and knowledge/decision directories.
Reusable procedures copied into every project would drift and grow session context.

## Proposed decision and alternatives

Require one project.yaml at the repository root. Version 2 adds explicit references
for vision, goals and boundaries to the existing role/process and tool-location map.
Check required keys, local Markdown files/sections and recognizable unfilled prompts.
A schema-only setup check must not claim source completeness. Preserve version-1 reading
for existing tooling maps and reject competing conventional configurations.

All Markdown names and content directories remain project choices. The starter uses
PROJECT.md and CONTRIBUTING.md as small defaults; several required references may point
to different sections of the same document. Host instructions load the manifest, the
relevant project sources and selected skills. Skills own reusable technique; the manifest
owns actual tool locations/commands. Existing workspace/ local-store paths remain an
optional tool convention, not a required project hierarchy.

## Consequences and status

Required areas become visible and mechanically checkable without forcing six documents
or a folder rename. Source checks cannot establish truth, sufficient quality, approval,
implementation or remote access. Required local entries may link authoritative external
detail. Project review and actual checks still establish those facts.

This proposal is implemented for review in draft PR #8. It refines ADR-0001's entry
placement and configuration without claiming owner acceptance, merge or deployment.
