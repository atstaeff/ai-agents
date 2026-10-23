---
title: "Put document context directly into prompts"
knowledge_id: ADR-0001
slug: /decisions/prompts-only
status: superseded
owner: technical-owner
relations: {}
---

# Put document context directly into prompts

## Context

The first prototype had a small corpus and needed a fast way to validate the interaction.

## Decision

For the prototype only, supply a bounded collection of documents directly in the prompt.
This reduced setup effort but made source selection and versioning difficult to audit.

## Consequences

Prompt size grew with the collection. The shared record remains here as history;
[ADR-0002](./0002-retrieval-evidence.md) replaces the approach when the corpus grows.
No private implementation plan is required to understand that change.
