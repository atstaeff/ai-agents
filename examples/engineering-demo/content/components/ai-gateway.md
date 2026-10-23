---
title: "AI model gateway"
knowledge_id: COMP-GATEWAY
slug: /components/ai-gateway
status: current
owner: ai-owner
area: retrieval
relations: {"governed_by": ["ADR-0002"], "relates_to": ["TOPIC-EVAL"]}
---

# AI model gateway

## Responsibility

Expose a stable model boundary for the document pipeline. Keep provider choice, request
limits, error translation and model versions inspectable. Avoid letting a provider-specific
response become an implicit domain contract.

## Change boundary

Compare compatible implementations through the same contract and representative evaluation
set. Separate retrieval evidence from provider instructions. Record actual model and prompt
versions with evaluation results; changing providers does not automatically preserve behavior.
