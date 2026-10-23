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

Start with the **Knowledge map**: a few areas and counts summarize the project. Open an
area for its record list, filter by type/status, then open one record to see only its
direct relationships. Use a known ID for a direct lookup and share the resulting URL.
Open the source documentation for the full rationale. A keyboard-accessible area list
is available below the overview.

The view includes superseded decisions and visible proposal statuses. Summary lines are
undirected counts of explicit cross-area relationships; the focused view retains each
recorded direction and relationship type. Page controls make omitted results explicit.

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

Edit the Markdown frontmatter (`knowledge_id`, `title`, `slug`, `status`, `owner`, `area`,
`relations`) and run `npm --prefix website run generate` from the repository root; restart
the dev server after metadata changes. `npm --prefix website run build`
regenerates the graph automatically. Only the named shared folders are read; plans, work,
archives and symlinked files are excluded or rejected. The graph stores no embeddings,
calls no model and imports no Obsidian vault.

On small screens, area cards and relationship lists replace the diagram so that all
choices remain readable without horizontal panning. The same filters and source links
remain available.

## Large collections

Do not draw every ADR at once. Use a few curated domains/system areas for orientation,
then browse one area and inspect one decision. This demo shows up to six areas, twenty
matching records or eight direct relationships per page. Record data is loaded on demand;
counts make the size of the complete result visible. Search by a known ID is supported;
global title/semantic search is outside this static demo.

The browser no longer needs every record to show the overview. The static generator and
Docusaurus build still process the published sources. Millions of records need an
incremental index/search service with authorization and paginated neighborhood queries;
this demo does not implement or benchmark that backend. Keep the same simple navigation
and use the existing project documents as the source of truth.
