---
title: "Keep personal plans in the Second Brain"
knowledge_id: ADR-0003
slug: /decisions/private-plans
status: accepted
owner: engineering-owner
relations: {"relates_to": ["TOPIC-CONTEXT", "COMP-PIPELINE"]}
---

# Keep personal plans in the Second Brain

## Context and alternatives

A contributor benefits from one personal planning home across repositories. The team
needs implemented behavior and significant rationale, rather than every execution step.
Compare repository-local plans, issue task lists and a private project note.

## Decision

Keep personal execution plans in the user's configured Second Brain, subject to project
information policy. Issues own shared scope/acceptance and PRs own changes/checks.
Preserve significant decisions and affected current documentation in shared project sources.

## Consequences

The repository remains readable and the contributor has one place to resume. Shared
instructions contain no personal path. If a teammate must take over, provide a bounded
issue/PR handoff; do not make private note access a dependency. An unavailable vault means
an explicitly unsaved session plan, not an automatic repository copy.
