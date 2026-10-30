# Documentation website

Docusaurus publishes the English catalog and operating model. This directory owns the
site; the engineering guidance stays in its canonical repository sources.

| Path | Edit here for |
| --- | --- |
| `content/` | Website-only guides and reference introductions |
| `src/pages/`, `src/css/`, `static/` | Homepage, presentation and local assets |
| `navigation.json` | Documentation sections and their order |
| `generate.py` | Canonical source mapping, link rebasing and catalog navigation |
| `docusaurus.config.js` | Site behavior, URL base and strict broken-link handling |
| `.generated/` | Generated Markdown, catalog metadata, area overview and paginated graph JSON; never edit or commit |
| `.docusaurus/`, `build/` | Framework cache and static output; never edit or commit |

`generate.py` reads the same catalog as the toolkit. Agents, skills, templates, operating
model and worked-project pages are generated, including edit links to their actual
sources. Add no profile placeholders or copied process documents under `content/`.

## Local development

Requirements: Python 3.11+, Node.js 22 or 24 LTS, and npm. Run from the repository root:

```sh
npm --prefix website ci
npm --prefix website start
```

Open http://localhost:3000/ai-agents/. The server binds to loopback. Website UI and
materialized document changes reload automatically. After editing canonical sources
outside this directory or navigation, run `npm --prefix website run generate` again;
restart the server after sidebar/configuration changes.

## Verify the static build

```sh
python3 tools/ai_toolkit.py check
python3 -m unittest discover -s tests -v
npm --prefix website run build
npm --prefix website run serve
```

The build automatically generates current pages and fails on broken links or anchors.
The pinned Docusaurus Faster package supplies SWC JavaScript minification; the rest of
the standard build pipeline stays explicit in the site configuration. The preview
uses the production `/ai-agents/` base path and trailing-slash routes. No hosted search,
analytics or external font service is required. Source pages use CommonMark; the homepage
uses JSX. Keep types, template placeholders and code examples literal in Markdown.

## Publication

The main documentation workflow installs the npm lockfile, builds the site and writes
its static output to the existing root `docs/` GitHub Pages directory. A PR only uploads
a build preview artifact. Keep Pages settings and generated-output changes separate from
source maintenance. Do not run a local build into `docs/` to prepare a source PR.

## Visual identity

The site follows [Stefan Poss](https://stefanposs.com): navy `#122E53`, white,
neutral gray surfaces, Heebo body text and Signika headings. The source reference is
[the website theme](https://github.com/stefanposs/sp-website-blog/blob/main/data/theme.json).
Pinned Fontsource packages bundle only the selected Latin weights locally; no external
font service is contacted. Dark mode uses charcoal surfaces and lighter navy accents
for legibility. Shared tokens in `src/css/custom.css` style the homepage, documentation,
navigation and graph; `src/css/knowledge-graph.css` owns only the graph's layout/components.
Keep focus indicators visible, text readable and page overflow contained on mobile.

The knowledge map imports an aggregate overview. Docusaurus copies
`.generated/static/knowledge-data/` into the build; the browser fetches versioned area
and direct-neighborhood pages only after navigation. The [demo guide](../examples/engineering-demo/README.md#large-collections)
describes the data contract and its production indexing boundary. `test:browser` checks
this navigation, request failures/retry, document links and mobile overflow. It saves
overview, focused and mobile screenshots to `.generated/browser-preview/`; CI uploads
them as the `knowledge-map-preview` artifact.

Curated knowledge slugs such as `decisions/adr-0042` are relative to the selected
content root. The Docusaurus frontmatter adapter resolves them from that root, including
records in nested folders, so graph links and document routes agree. Canonical Markdown
and unrelated documentation retain their original metadata.
The graph and document plugin share exclusions for `_` partials, hidden Markdown and
`*.test.md` files, so the graph cannot link to those unpublished pages.
