# Repository instructions

This repository is a portable English agent/skill catalog and a local Python toolkit.
Canonical agents live in `agents/*.agent.md`; skills are either `skills/*/SKILL.md`
or existing category topic files. Runtime adapters materialize every skill in a native
`<name>/SKILL.md` directory. Edit the canonical sources, not generated bundles.

Read [toolkit/WORKFLOW.md](toolkit/WORKFLOW.md) for shared working guidance. Keep
instructions concise and use `references/` for examples. Every catalog entry requires
YAML `name` and `description`; avoid runtime-specific fields in canonical frontmatter.

Verify relevant changes with:

```sh
python3 tools/ai_toolkit.py check
python3 -m unittest discover -s tests -v
uv run --group docs mkdocs build -f assets/mkdocs.yml --strict
```

The toolkit uses Python 3.11+ and the standard library at runtime. Keep it local: bind
the dashboard to loopback, serve no external assets, and preserve comments and stale-write
protection. The dashboard manages Markdown work records; it does not execute AI agents.

`assets/mkdocs/` contains website sources. `docs/` is existing GitHub Pages output:
the documentation workflow rebuilds it after changes reach main. Do not use `docs/`
as a scratch directory or commit generated bundles, vault contents or private paths.

Keep larger work in `.ai/work/` and archive verified work in `.ai/archive/` when useful.
Do not merge or deploy as part of repository maintenance unless explicitly requested.
