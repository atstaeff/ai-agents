# Repository instructions

This repository is a portable English agent/skill catalog and a local Python toolkit.
Canonical agents live in `agents/<domain>/<name>.agent.md`; skills use
`skills/<domain>/<name>/SKILL.md`. Select among the disciplines in
`toolkit/catalog-domains.json`. Keep stable exported names unique. Edit canonical
sources, not generated bundles. See [catalog management](toolkit/CATALOG-GUIDE.md).

Start with the required [project manifest](project.yaml), then its referenced
[project map](PROJECT.md) and [contribution process](CONTRIBUTING.md). Read the
[detailed concept](toolkit/WORKSPACE-CONCEPT.md) when changing information ownership,
workspace layout, migration or knowledge publication.

Read [toolkit/WORKFLOW.md](toolkit/WORKFLOW.md) for shared working guidance. Keep
instructions concise and use `references/` for examples. Keep shared rules tool-neutral;
see [portability](toolkit/PORTABILITY.md) when changing host integration. Every catalog entry requires
YAML `name` and `description`; avoid runtime-specific fields in canonical frontmatter.

Verify relevant changes with:

```sh
python3 tools/ai_toolkit.py check
python3 -m unittest discover -s tests -v
npm --prefix website ci
npm --prefix website run build
```

The toolkit uses Python 3.11+ and the standard library at runtime. Keep it local: bind
the dashboard to loopback, serve no external assets, and preserve comments and stale-write
protection. The dashboard manages Markdown work records; it does not execute AI agents.

`website/` owns the Docusaurus site and canonical-source publisher. `docs/` is existing GitHub Pages output:
the documentation workflow rebuilds it after changes reach main. Do not use `docs/`
as a scratch directory or commit generated bundles, vault contents or private paths.

For larger work, follow the project-designated planning home or use one `workspace/work/`
record when no assigned system owns the plan. Archive verified local work in `workspace/archive/` when useful.
Do not merge or deploy as part of repository maintenance unless explicitly requested.
