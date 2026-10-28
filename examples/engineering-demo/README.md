# Engineering Atlas — the Docusaurus graph demo

A fictional Document Understanding project demonstrates shared decisions, components and
AI topics. The demo runs inside the existing Docusaurus website: one installation and
one build, with no second application or package manifest.

## Run locally

Requires Python 3.11+, Node.js 22+ and npm. From the repository root:

```sh
npm --prefix website ci
npm --prefix website start
```

Open http://localhost:3000/ai-agents/knowledge-graph/ in your Windows browser when the
server runs in WSL. Start with the area overview, browse records by type/status, then
inspect one record and its direct relationships. Open a known ID directly from the toolbar
or share the focused URL. Open the source documentation for its rationale. Keyboard selection and a record list provide an
alternative to pointer navigation. The server binds to loopback.

## Verify

```sh
uv sync --locked --group validation
npm --prefix website run test:graph
npm --prefix website run build
npx --prefix website playwright install chromium
npm --prefix website run test:browser
```

The graph tests also copy the actual ADR template through the legacy Python publisher.
They use the existing validation environment's Python and PyYAML; this adds no application
runtime dependency.

Package downloads require network access; the built graph calls no model, remote graph
service, font provider or CDN. All examples and statuses are fictional, not claims about
production quality, owner approval or deployed software.

## Sources and boundaries

- `content/decisions/`: context, alternatives, choice and consequences.
- `content/topics/`: retrieval, evaluation, observability and session context.
- `content/components/`: system responsibilities and interfaces.
- Each record has one curated `area` slug, such as `document-processing` or `retrieval`.
- Portable source `slug` values are relative, such as `decisions/adr-0042`. Existing values
  with one leading slash remain supported and resolve to the same route.
- Metadata links records by stable ID, route, status and explicit relationship.

The main site's `scripts/graph.cjs` generates disposable JSON before start/build.
It checks IDs, areas, routes, references, supersession status, cycles and source symlinks.
The initial page imports only aggregated area counts and cross-area relationship counts.
Record metadata and direct relationships are separate static JSON requests, loaded on demand.
The snapshot identifier includes the sources, data contract and page limits so that a
newly deployed page cannot silently mix its index with older JSON files. A failed request
is shown explicitly with retry; navigation cancels obsolete requests.
Only these three shared directories and `content/intro.md` are published by the demo
content plugin. Private plans, work records and vault content are outside that allowlist.
Git ignore alone is not a publication boundary. Restart the dev server after metadata
changes so graph data and document sources use the same snapshot.

### Use a customer-owned publication source

Edit `website/knowledge.config.cjs` deliberately to select the curated publication root,
route prefix and sidebar file together. The graph CLI and Docusaurus read this same
configuration; there is no environment-variable source override. Update its stable source
ID, title, description and `example` flag to match the actual source. The repository
default remains this fictional demo.

Keep only approved shared content in a dedicated publication directory with `intro.md`
and the three allowlisted subdirectories. Use `intro` as the introduction's slug and put
its sidebar definition in the configured file. The fixed allowlist also applies to a
customer source: it does not import the rest of a repository or a raw vault. Symlinks,
nested private/work/plans/archive directories and Markdown marked `private: true`,
`draft: true` or `visibility: private`/`internal` fail validation. A raw Obsidian vault
root is rejected. Export reviewed shared material into the publication directory first;
the configuration cannot determine whether ordinary prose contains confidential facts.
Keep private source paths out of shared configuration and logs. Source-configuration
validation reports availability without printing absolute customer paths.

Copy [the ADR template](../../templates/architecture/decision.md) into `decisions/`, replace
its ID/title/slug with unique values, and choose one existing curated area. Its relative
slug and proposed status work in both this graph and the legacy document-portal publisher.

The existing site also publishes the real catalog/project knowledge. This fictional
example is clearly labeled and uses separate `/demo-knowledge/` routes. No deployment
is configured by this change.

See the [engineering model](../../toolkit/OPERATING-MODEL.md) and
[AGENTS.md variants](../../templates/agent-instructions/README.md) to adopt the workflow.

On small screens, area cards and relationship lists replace the diagram so that all
choices remain readable without horizontal panning. The same filters and source links
remain available.

## Large collections

The default view contains areas, rather than one node per ADR. Use a small governed set
of domains or system areas; creating one area per ADR defeats the overview. The view shows
up to six areas per page. A line combines explicitly recorded relationships between two
visible areas; it does not infer a dependency or a direction. Counts include all statuses.

Open an area for paginated records, with type/status filtering over the entire area.
Open a record for its direct neighborhood: at most eight relationships and nine nodes.
The total relationship count and pagination stay visible, including for high-degree hubs.
The complete direction and relationship type are preserved here. Proposals and superseded
records remain discoverable. A known record ID opens directly; there is no global title or
semantic search in this static demo.

The generated data contract is:

| View | Data | Bound |
| --- | --- | --- |
| Overview | `.generated/knowledge-overview.json` | Aggregate areas and counts; no individual record metadata |
| Area results | `knowledge-data/<snapshot>/areas/<area>/<kind>-<status>/<page>.json` | 20 records per request |
| Record | `knowledge-data/<snapshot>/records/<id>/index.json` | One record and its total direct relationship count |
| Neighborhood | `knowledge-data/<snapshot>/records/<id>/<page>.json` | 8 explicit relationships and their endpoints |

Generated request data lives under `website/.generated/static/` and is copied into the
static build. Do not edit or commit it. The browser renders only the selected page and
loads no full-corpus graph. The generator still scans approved Markdown and constructs
its index in memory at build time; Docusaurus still builds each published document.

**Millions of ADRs require a different storage and indexing tier.** Keep the same bounded
views, backed by an incremental metadata/relationship index with scoped full-text search,
access control, stable cursor pagination and document retrieval. Index approved sources at
their owners; return authorized counts and links, then fetch only the chosen neighborhood.
A relational store with an edge table can implement this contract; a graph database is
not a requirement. Avoid rebuilding or sending the entire corpus for each session.

Tests cover aggregate counts for 50,000 synthetic records, a paginated high-degree hub
and a 30,000-record dependency chain. These establish the tested invariants, not an
end-to-end million-record performance measurement or a production backend implementation.
