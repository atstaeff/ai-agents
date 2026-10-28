# Native tools, one engineering process

Choose tools by responsibility. Record the actual project choices and access paths in
`PROJECT.md` or the equivalent source linked by `AGENTS.md`. Available credentials and
connectors do not establish a project's source of truth or permission to publish.

| Responsibility | Tool or source | Contract |
| --- | --- | --- |
| Scope, priorities and acceptance | GitHub Issues/Projects or Jira | One authoritative assignment; PR/MR links it |
| Code, checks and review | Existing Git host and CI | Evidence refers to the tested revision |
| Fleet orchestration | Herd (NickGuAI) | Native commanders and host-managed workers; [adapter](ORCHESTRATION.md) |
| Terminal agent control | Herdr, if adopted | Native terminal lifecycle commands; no duplicate scheduler |
| Reduce unnecessary implementation | Ponytail, if installed | Native host rules alongside project acceptance and quality requirements |
| Dependency discovery | Graphify, if adopted | Scoped derived context with source/provenance checks |
| Decisions for people | Docusaurus | Published view of selected maintained Markdown |
| Project dependency map | Repository knowledge map | Curated areas, records and typed relationships |

## Herd, Herdr and other similarly named tools

The `herd` runtime exporter targets [NickGuAI/Herd](https://github.com/NickGuAI/Herd),
which imports commanders and coordinates workers. Export/import is described in
[orchestration](ORCHESTRATION.md); provider readiness and action policies belong in Herd.

[Herdr](https://herdr.dev/docs/agent-automation/) controls coding agents in terminal panes.
It can organize several leads and specialists without replacing their harnesses. Create
layout first, capture the returned pane IDs, then start named agents in available shell
panes. Check native help for the installed release:

```sh
herdr --help
herdr agent --help
herdr agent list
```

Use `agent start` with the chosen `--kind` and model arguments supported by that harness.
Use `agent prompt`, `agent read` and bounded `agent wait` to control the lifecycle. An
idle terminal does not prove a successful task: inspect the result, revision and checks.
For live names, pane creation, blocked prompts and state semantics, use the
[official CLI reference](https://herdr.dev/docs/cli-reference/).

[HerdOS](https://github.com/Herd-OS/herd) coordinates GitHub Actions workers, and
[herd-ag/herd-core](https://github.com/herd-ag/herd-core) supplies team governance.
These projects have separate installation and configuration contracts. Their files are
not interchangeable with this export. Adopt only the named tool the project actually uses.

## Ponytail: keep implementation proportionate

Use the official [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
installation for the selected host. Its [installation guide](https://github.com/DietrichGebert/ponytail/blob/main/INSTALL.md)
covers native plugins and instruction-based hosts. For example, a compatible OpenCode
installation supports:

```sh
opencode plugin add @dietrichgebert/ponytail
```

Install into the actual worker harness as well as the lead if those use separate
configurations. Check discovery with a harmless change. This exporter neither installs
Ponytail nor copies its rules into every skill. Preserve the project's acceptance,
security, accessibility and required checks when simplifying an implementation.
Keep plugin versions in the host's managed configuration; evaluate local outcomes rather
than inheriting another project's benchmark percentages.

## Graphify: retrieve dependency context

The official source is [Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify);
the package is `graphifyy`, and the executable is `graphify`. Install separately, then
register its native skill for the chosen host from the customer project:

```sh
uv tool install graphifyy
graphify install --project --platform opencode
```

This repository supplies `.graphifyignore` to skip generated views, exported catalogs
and local work. Projects must still define their permitted scan scope. Inspect installation
changes before integration. To start with local code extraction:

```sh
graphify extract . --code-only
graphify query "Which components depend on the changed API?"
graphify path "Component A" "Component B"
graphify explain "Component A"
```

The initial extraction is an explicit project action. Semantic document/media processing
uses the configured backend; choose permitted inputs and provider deliberately. Query a
small subgraph rather than loading the whole report. Retain the source revision, schema
version and edge provenance; distinguish extracted links from inferred suggestions.
Verify important findings in their source before changing a contract or decision.

See the [official command reference](https://docs.graphify.com/) for the installed release.
This guide documents native use; it does not run extraction, upload customer documents or
promise that a graph is complete or current.

## Docusaurus and the curated knowledge map

Keep shared facts and decisions in their project-owned Markdown locations. Publish an
allowlist through Docusaurus; `website/` owns this repository's publisher and root `docs/`
contains compiled Pages output. The [runnable example](../examples/engineering-demo/README.md)
contains stable IDs, areas and `depends_on`, `supersedes`, `relates_to` and `governed_by` links.

Graphify helps discover a candidate relationship. Confirm it and record it in the canonical
project source when useful. The Docusaurus map reads those reviewed sources; it does not
consume an unrestricted raw Graphify snapshot or turn inferred edges into accepted ADRs.
Private plans, transcripts, credentials and generated worker memory stay outside publication.

The map starts with area summaries and loads selected records and direct relationships
on demand. Static generation still processes the published corpus. At very large scale,
use an authorized incremental metadata/search service and retain the same bounded views;
rendering every decision at once is not the retrieval contract.
