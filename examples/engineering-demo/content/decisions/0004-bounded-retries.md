---
title: "Bound retries for document processing"
knowledge_id: ADR-0004
slug: /decisions/bounded-retries
status: proposed
owner: platform-owner
relations: {"relates_to": ["COMP-PIPELINE", "TOPIC-OBS"], "depends_on": ["ADR-0002"]}
---

# Bound retries for document processing

## Context

Transient model or storage errors can trigger repeated processing. Unbounded retries
increase cost and obscure failures. Compare manual replay, fixed retries and a bounded
retry policy with explicit terminal outcomes.

## Proposed decision

Use a bounded retry budget with backoff and a terminal failed state. Make replay a
separate authorized action. Record document ID, attempt, stage and reason.

## Consequences and open evidence

The policy limits amplification and improves diagnosis but needs a tested recovery path.
This proposal has no implementation or owner acceptance evidence yet. It cannot supersede
an accepted decision or be presented as deployed behavior.
