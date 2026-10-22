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
| `.generated/` | Generated Markdown, sidebars and catalog counts; never edit or commit |
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
