# Local Docusaurus knowledge publishing

These are integration instructions for an existing Docusaurus 3 website under `website/`.
The starter does not contain a complete website, a deployed portal or a background runner.

## Source, route and output are separate

- Canonical Markdown: `workspace/`; people and AI edit these files through reviewed changes.
- Website configuration: the existing `website/` directory.
- Docs plugin options: use [docusaurus-workspace.cjs](docusaurus-workspace.cjs) as an options fragment.
- Website route: `/workspace/`; keep each knowledge record's `slug` stable.
- Generated static output: Docusaurus defaults to `website/build/`. If root `docs/` is reserved
  for your compiled GitHub Pages output, build into `../docs` and keep that folder generated.

Never point the docs content plugin at a directory that also receives its compiled output.
Check that an output directory contains only replaceable generated files before building into it.

## Enable Mermaid in the existing configuration

Install `@docusaurus/theme-mermaid` at the version matching the website's Docusaurus packages.
Merge these top-level settings into the existing configuration; preserve all existing themes
and other Markdown options:

```js
markdown: {mermaid: true},
themes: ['@docusaurus/theme-mermaid'],
```

The docs fragment assumes `website/` and `workspace/` are sibling directories. If the
website is at the repository root, use `path: 'workspace'` instead.
If the website already reads another documentation source, preserve that plugin and add
a separate `@docusaurus/plugin-content-docs` instance with `id: 'workspace'` and this
fragment's options. Check that its route does not collide with an existing section.

## Generate the index and graph locally

From the repository root:

```bash
uv run examples/knowledge_graph.py workspace --json examples/knowledge-graph.json
```

Python 3.11+ and PyYAML are required. The script's dependency declaration lets uv resolve
the parser; an existing environment with PyYAML can invoke it with Python directly.
Generation reads only local Markdown. It makes no API requests and uses no graph service.

The generated page contains the record index, Mermaid diagram and clickable relationship
table. Metadata is the source for both the page and JSON; edit the underlying records.
The `relations` vocabulary is this starter's convention, not a MADR or Docusaurus standard.
Sources link to original issues and PRs without importing their comments into the graph.

The checked-in generated example lets you inspect the output immediately. In a real
project, regenerate before each website build and either commit generated views consistently
or ignore `workspace/knowledge-map.md` and the generated JSON. Do not edit them manually.

## Build and inspect the existing website

After generation, from the existing `website/` directory:

```bash
npm run build -- --out-dir ../docs
npm run serve -- --dir ../docs
```

These commands assume the usual package scripts map to `docusaurus build` and
`docusaurus serve`. An existing build-output arrangement may use another directory.
For branch-based GitHub Pages, keep its configured branch/folder; an artifact-based
deployment may publish `build/` without committing generated HTML. Publication follows
the customer's agreed process.

## Scaling the graph

Start with the generated page and relationship table. When a product has many records,
use a view by domain, status or the one/two-hop neighborhood of a selected ADR.
The generated JSON can support an optional local React/Cytoscape component in Docusaurus;
that interactive component is not implemented in this starter. Keep the accessible table.
Do not hand-maintain an independent graph database or infer authoritative edges from text similarity.

Website access must match customer requirements. A private repository does not automatically
make a published website private; configure hosting access separately. The JSON is published
data if embedded in the website, so apply the same content boundary to it.

## Official references

- [Docusaurus content directory and routes](https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs)
- [Docusaurus CLI output options](https://docusaurus.io/docs/cli)
- [Docusaurus Mermaid integration](https://docusaurus.io/docs/markdown-features/diagrams)
- [GitHub Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
- [MADR frontmatter](https://adr.github.io/madr/decisions/0013-use-yaml-front-matter-for-meta-data.html)
- [Cytoscape.js](https://js.cytoscape.org/)
