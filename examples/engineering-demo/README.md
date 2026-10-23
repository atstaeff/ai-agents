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
server runs in WSL. Search and filter records, select a node, inspect its relationships
and open the source documentation. Keyboard selection and a record list provide an
alternative to pointer navigation. The server binds to loopback.

## Verify

```sh
npm --prefix website run test:graph
npm --prefix website run build
npx --prefix website playwright install chromium
npm --prefix website run test:browser
```

Package downloads require network access; the built graph calls no model, remote graph
service, font provider or CDN. All examples and statuses are fictional, not claims about
production quality, owner approval or deployed software.

## Sources and boundaries

- `content/decisions/`: context, alternatives, choice and consequences.
- `content/topics/`: retrieval, evaluation, observability and session context.
- `content/components/`: system responsibilities and interfaces.
- Metadata links these records by stable ID, route, status and explicit relationship.

The main site's `scripts/graph.cjs` generates disposable JSON before start/build.
It checks IDs, routes, references, supersession status, cycles and source symlinks.
Only these three shared directories and `content/intro.md` are published by the demo
content plugin. Private plans, work records and vault content are outside that allowlist.
Git ignore alone is not a publication boundary. Restart the dev server after metadata
changes so graph data and document sources use the same snapshot.

The existing site also publishes the real catalog/project knowledge. This fictional
example is clearly labeled and uses separate `/demo-knowledge/` routes. No deployment
is configured by this change.

See the [engineering model](../../toolkit/OPERATING-MODEL.md) and
[AGENTS.md variants](../../templates/agent-instructions/README.md) to adopt the workflow.
