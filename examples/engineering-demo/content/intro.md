---
title: A small engineering knowledge system
sidebar_position: 1
---

# Decisions outlast conversations

This fictional Document Understanding project demonstrates a lean engineering workflow.
It is a runnable Docusaurus site, not a transcript archive or a project-management system.

| Information | Source of truth |
| --- | --- |
| Personal working plans and resume notes | Private Second Brain; outside this demo |
| Shared scope and acceptance | Existing issue/ticket |
| Implementation and verification | Code and PR |
| Significant decisions and current knowledge | Reviewed shared Markdown |
| Website and graph | Generated views of the shared Markdown |

## Explore

Use the **Knowledge graph** to search records, filter by kind/status and inspect a node's
relationships. Open the source documentation from the detail panel. Superseded decisions
remain visible so you can see why the system changed. The record list below the graph is
an accessible alternative to the diagram.

The sample concerns [document processing](./components/document-pipeline.md),
[retrieval](./topics/retrieval.md), [evaluation](./topics/evaluation.md),
[observability](./topics/observability.md) and [context management](./topics/context.md).
All design statuses and roles in this demo are fictional examples, not claims about a
production system, completed reviews or measured model quality.

## Keep it small

Start with `AGENTS.md` and existing project documents. Add an ADR only when a significant
choice needs durable rationale. Add a knowledge page only when the implemented result
needs explanation. Never require a private plan for team continuity.

## Update the graph

Edit the Markdown frontmatter (`knowledge_id`, `title`, `slug`, `status`, `owner`, `relations`)
and run `npm run graph`; restart the dev server after metadata changes. `npm run build`
regenerates the graph automatically. Only the named shared folders are read; plans, work,
archives and symlinked files are excluded or rejected. The graph stores no embeddings,
calls no model and imports no Obsidian vault.
