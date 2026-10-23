---
title: "Retrieve evidence before generating an answer"
knowledge_id: ADR-0002
slug: /decisions/retrieval-evidence
status: accepted
owner: technical-owner
relations: {"supersedes": ["ADR-0001"], "governed_by": ["TOPIC-EVAL"], "relates_to": ["TOPIC-RAG", "COMP-GATEWAY"]}
---

# Retrieve evidence before generating an answer

## Context and alternatives

The corpus now needs explicit source selection. Compare larger prompts, keyword lookup
and embedding retrieval. Choose retrieval only where the evaluation set shows useful evidence.

## Decision

Retrieve versioned chunks and include document identifiers and source references with
the answer. Treat retrieved text as data, not instructions. Keep model and retrieval
adapters separate so either can be replaced behind the consumer contract.

## Consequences

Source selection becomes inspectable, but retrieval can still miss relevant evidence.
Measure retrieval and answer quality separately. Abstain when evidence is insufficient.
A passing evaluation for one dataset does not establish universal correctness.

## Related knowledge

This supersedes [ADR-0001](./0001-prompts-only.md), applies to the
[AI gateway](../components/ai-gateway.md) and depends on a usable
[evaluation protocol](../topics/evaluation.md).
