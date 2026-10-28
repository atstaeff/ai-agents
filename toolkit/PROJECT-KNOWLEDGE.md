# Project knowledge

Keep the information needed to understand and maintain the implemented system with the
project. Keep personal execution notes in the user's private Second Brain, subject to
customer policy. The [operating model](OPERATING-MODEL.md) defines that boundary once.

## What belongs in shared knowledge

- Product purpose, scope and responsible roles.
- Current interfaces, data meaning, important boundaries and operating instructions.
- Significant technical decisions: situation, alternatives, choice and consequences.
- Relevant verification and implementation references.

Update an existing page instead of adding a parallel summary. Routine implementation
choices can be explained in the PR; use an ADR when the rationale matters beyond the task.
For a replacement, create a new decision, link `supersedes` and preserve the old rationale.
A proposal does not revoke an accepted decision. Label proposed and implemented behavior
honestly; code demonstrates behavior, not decision authority.

## Retrieval

`AGENTS.md` links to the actual project sources, wherever they live. Follow the affected
links and inspect current code/tests. Search the bounded project when a relevant decision
is missing; an absent link is not proof that no decision exists. Do not load every ADR,
archive or conversation by default. Teammates must not need a private vault to continue.

## Dependency evidence

When Graphify is adopted, query the affected components and verify returned source
locations and snapshot freshness. Extracted and inferred relationships are evidence,
not approval. Promote useful reviewed relationships into the canonical project record;
retain significant reasons in ADRs. See [native integration](INTEGRATIONS.md) for the
source-to-graph-to-documentation path and provider/publication boundaries.

## Graph and documentation

Use stable IDs and a few meaningful relationships: `depends_on`, `supersedes`, `relates_to`
and `governed_by`. Connect decisions to affected components and relevant AI topics such
as retrieval, evaluation and observability. A graph is an index, not another decision log.

Generate website pages and graph data only from approved shared Markdown. Use an explicit
content allowlist, stable routes and validated references. Exclude private plans, work
records and generated exports even if they happen to be inside the repository. Git ignore
alone does not protect website publication. Never follow source symlinks into a vault.

At larger scale, start with curated domain/system areas and aggregate counts, then fetch
one area's paginated results and one decision's bounded direct neighborhood. Keep hidden
result counts visible, preserve direction/type at record level and include historical
statuses explicitly. Do not load an entire ADR collection into every AI session or browser.
A million-record estate needs an incremental authorized metadata/search index; a static
site is a demonstration of navigation, not proof of that storage/query scale.

The [Docusaurus demo](../examples/engineering-demo/README.md) provides a runnable example.
The older [customer graph](../examples/document-portal/examples/knowledge_graph.py)
remains available for projects already using that schema.
