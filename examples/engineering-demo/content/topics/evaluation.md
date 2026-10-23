---
title: "Evaluation before confidence"
knowledge_id: TOPIC-EVAL
slug: /topics/evaluation
status: current
owner: quality-owner
relations: {"relates_to": ["COMP-GATEWAY"]}
---

# Evaluation before confidence

## What AI and maintainers need to know

Use a versioned representative dataset and acceptance criteria derived from user needs.
Separate extraction accuracy, retrieval relevance, grounded answering and failure behavior.
Include abstention, invalid input and insufficient evidence. Record the tested code/model
revision and actual result; never equate a green build with acceptable model behavior.

## Decision trigger

Revisit the design when repeatable evaluations show a material quality or cost regression.
Keep actual measurements in review evidence. This demo provides no measured production score.
