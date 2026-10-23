---
title: ADR-0005 Bounded knowledge views
knowledge_id: ADR-0005
slug: decisions/adr-0005
status: proposed
owner: repository-owner
relations:
  relates_to: [ADR-0004]
sources: []
---

# ADR-0005: Bounded knowledge views

## Situation

The graph demo imported every record and relationship into the browser and drew all
matching records. A global graph becomes difficult to read as the decision collection
grows; hiding nodes visually would still transfer and index the full corpus on the client.
The requested experience is a simpler overview that remains understandable at larger scale.

## Options

- Keep a global record graph and add visual filters.
- Cluster all records in the browser after downloading them.
- Publish area summaries and retrieve bounded record lists and direct neighborhoods.

## Proposed decision

Use one curated area per shared record. Start with aggregate counts and undirected
cross-area relationship counts. Open an area for type/status-filtered pages of records,
then open one record and a page of its explicitly recorded direct relationships. Show
complete result counts, pages and actual decision status. Preserve edge direction and
type in the detailed view. A summary line is not an inferred dependency.

For the static demo, generate snapshot-versioned JSON: an aggregate overview, twenty
records per area result page, one record per detail request and eight relationships per
neighborhood page. Render up to six area nodes or nine record nodes at once. Known IDs
open directly; query URLs support sharing and browser history. Cancel stale requests and
make retrieval failure visible and retryable. Keep source publication allowlists intact.

## Consequences and limits

The browser's initial graph data depends on area summaries instead of individual records.
A heavily connected record cannot expand the view into an unbounded diagram or payload.
Area taxonomy needs maintenance; pages explicitly omit nonselected records and connections.
Global title and semantic search are not implemented in this static demo.

The build still scans the full allowed Markdown corpus and publishes its documents.
Millions of ADRs require incremental indexing, authorized search and neighborhood queries,
stable cursor pagination and source document retrieval. The same view contract can be
served by a relational metadata/edge store or an existing knowledge platform. This change
does not implement, benchmark or claim that production backend.

Implementation and validation are prepared on the review branch. Owner acceptance,
merge and production deployment remain separate evidence.
