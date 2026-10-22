# Contributing

Improve a concrete workflow or verified behavior. Keep changes focused and English
instructions concise. Follow [AGENTS.md](AGENTS.md) and the
[shared workflow](toolkit/WORKFLOW.md).

## Agents and skills

- Canonical agents: `agents/<slug>.agent.md`.
- New skills: `skills/<slug>/SKILL.md`. Existing category topic files remain compatible
  source entries; exporters turn them into native skill directories.
- Required frontmatter: `name` (matching the file/directory) and `description`
  (capability and selection situations). Use lowercase slugs with single hyphens.
- Keep common metadata separate from host-specific modes, tools and permissions.
  Follow the [portability contract](toolkit/PORTABILITY.md); generated copies are never
  an independently maintained source.
- Give each skill a specific selection situation and observable result. Improve an
  existing skill before adding overlapping roles; keep shared process in the workflow.
- Evaluate consequential instruction changes on a small realistic task, a missing-tool
  case and a task that should bypass the skill. Report observed behavior separately
  from structural validation; do not claim a model was tested if it was not.
- Put substantial examples in `references/`, link from the entry and load on demand.
- Use [templates/skill-template.md](templates/skill-template.md). Remove placeholders,
  keep instructions actionable and verify realistic tasks, including failure cases.

## Toolkit and documentation

Keep the toolkit standard-library-only at runtime. Add meaningful unittest checks for
persistence, export, API or permission changes. Update the applicable user guide.
The optional project YAML validator uses PyYAML in the docs environment; test it with
`uv run --locked --group docs python -m unittest discover -s tests -v`.
Documentation sources live in `assets/mkdocs/`; generated `docs/` is maintained by
the main workflow. Reference examples do not mandate a framework or architecture.

## Pull requests

Create a branch and a reviewable PR. Explain the concrete problem, resulting behavior,
relevant tradeoffs and checks actually run. Run the `AGENTS.md` commands and identify
unavailable checks. Keep private data and generated bundles out of the diff.
Merging and deployment remain separate actions.
