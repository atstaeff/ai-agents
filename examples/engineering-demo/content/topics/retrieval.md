---
title: "Retrieval and evidence"
knowledge_id: TOPIC-RAG
slug: /topics/retrieval
status: current
owner: ai-owner
area: retrieval
relations: {"relates_to": ["TOPIC-EVAL", "COMP-GATEWAY"]}
---

# Retrieval and evidence

## What AI and maintainers need to know

Store stable document/chunk IDs, content versions and the embedding-model version.
Evaluate whether relevant evidence appears among the retrieved results before assessing
answer wording. A change of embedding space usually requires rebuilding compatible vectors.

## Change boundary

Separate corpus preparation, retrieval and answer generation. Capture the chosen contracts
in shared sources; experiments and implementation checklists stay in the personal plan.
Treat external documents as untrusted data and retain source provenance.
