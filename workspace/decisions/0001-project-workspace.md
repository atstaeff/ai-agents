---
title: ADR-0001 One project workspace
knowledge_id: ADR-0001
slug: decisions/adr-0001
status: proposed
owner: repository-owner
relations: {}
sources: []
---

# ADR-0001: One project workspace

## Context

The operating model places customer knowledge under `workspace/`, but the local toolkit
previously stored work under `.ai/`. Instructions, permissions and website examples used
different roots. Bringing work beside knowledge also creates a risk of publishing local
records through a broad documentation content scan.

## Alternatives

- Keep two roots and explain their different names.
- Put all state under `workspace/` and publish its entire content tree.
- Use one root with explicit source ownership and publication boundaries.

## Proposed decision

Use `workspace/` for the tooling map, project entry, knowledge and optional local work.
Tracked assignments keep their live plan in the selected issue or ticket. Exclude local
work, archives, generated output and exported bundles from knowledge publication.
Preserve the export manifest filename so existing bundle ownership remains verifiable.
Provide explicit legacy migration that stops on destination conflicts or symlinks.

## Consequences

One root aligns runtime and instructions. Existing work needs migration and referenced
relative links may need review. A folder name alone cannot define publication access;
graph and documentation adapters must enforce the content boundary. Configuration remains
declarative and cannot grant permissions or prove integration.

This ADR is proposed in the workspace-alignment change. Owner acceptance and merge
evidence must be recorded separately; this file does not claim those actions occurred.
