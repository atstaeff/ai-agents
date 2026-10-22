# Contributing

This document is the shared working process for people and AI in this repository.
Follow linked procedures and skills when relevant to the assignment.

Improve a concrete workflow or verified behavior. Keep changes focused and English
instructions concise. Follow [AGENTS.md](AGENTS.md) and the
[shared workflow](toolkit/WORKFLOW.md).

## Working process and skills

Read [PROJECT.md](PROJECT.md) for vision, goals, boundaries, responsibilities and current
sources. The [working agreement](workspace/working-agreement.md) defines acceptance
and action boundaries; the [manifest](project.yaml) maps the authoritative source locations. Use **Clarify → Plan → Build → Verify → Integrate and retain**.
Keep the live plan in the assigned work home. Clear small corrections need no extra record.

| Need | Load when relevant |
| --- | --- |
| Establish how to contribute in an unfamiliar repository | [repository-contribution](skills/delivery/repository-contribution/SKILL.md) |
| Clarify vision, value, boundaries and acceptance | [product-discovery](skills/delivery/product-discovery/SKILL.md) |
| Coordinate a larger assignment and session handoff | [work-management](skills/delivery/work-management/SKILL.md) |
| Resolve consequential design choices | [principal-engineer-decisions](skills/architecture/principal-engineer-decisions/SKILL.md) |
| Implement in the existing stack | Relevant [engineering or language skill](skills/README.md) |
| Verify behavior and assess a change | [testing](skills/quality/testing/SKILL.md), [code-review](skills/quality/code-review/SKILL.md) |
| Prepare the contribution for review | [pr-crafting](skills/delivery/pr-crafting/SKILL.md) |

Load only the selected skill body and necessary references. A link does not install or
execute a skill; use the host's installed catalog or read its canonical source explicitly.
Skills provide reusable technique; project rules and current instructions determine
the assignment, authoritative tools and permissions. Use available integrations for those
tools. Report missing access and prepare an unsent update; do not create a mirror tracker.

## Agents and skills

- Canonical agents: `agents/<domain>/<slug>.agent.md`.
- Canonical skills: `skills/<domain>/<slug>/SKILL.md`. Choose one primary discipline
  from `toolkit/catalog-domains.json`; names stay unique within each kind. Older flat
  layouts remain loader-compatible, but new contributions use the domain layout.
- Required frontmatter: `name` (matching the file/directory) and `description`
  (capability and selection situations). Use lowercase slugs with single hyphens.
- Keep common metadata separate from host-specific modes, tools and permissions.
  Follow the [portability contract](toolkit/PORTABILITY.md); generated copies are never
  an independently maintained source.
- Give each skill a specific selection situation and observable result. Improve an
  existing skill before adding overlapping roles; keep shared policy in the workflow
  and focused procedures in skills.
- Evaluate consequential instruction changes on a small realistic task, a missing-tool
  case and a task that should bypass the skill. Report observed behavior separately
  from structural validation; do not claim a model was tested if it was not.
- Put substantial examples in `references/`, link from the entry and load on demand.
- Use [templates/catalog/skill-template.md](templates/catalog/skill-template.md). Remove placeholders,
  keep instructions actionable and verify realistic tasks, including failure cases.

## Checks and tools

Use the [repository runbook](toolkit/REPOSITORY-WORKFLOW.md) for setup, startup and
verification commands. The [CI workflow](.github/workflows/checks.yml) defines required
catalog/link, test, HTTP replay, manifest, JavaScript/options and documentation checks.
Keep those commands and action rules in their existing sources, not duplicated in YAML.

## Toolkit and documentation

Keep the toolkit standard-library-only at runtime. Add meaningful unittest checks for
persistence, export, API or permission changes. Update the applicable user guide.
The optional project YAML validator uses PyYAML in the docs environment; test it with
`uv run --locked --group validation python -m unittest discover -s tests -v`.
The Docusaurus site and publishing tools live in [website/](website/README.md); generated `docs/` is maintained by
the main documentation workflow. Reference examples do not mandate a framework or architecture.

## Pull requests

Create a branch and a reviewable PR. Explain the concrete problem, resulting behavior,
relevant tradeoffs and checks actually run. Run the `AGENTS.md` commands and identify
unavailable checks. Keep private data and generated bundles out of the diff.
Merging and deployment remain separate actions.

## Catalog and documentation views

Refresh `agents/README.md` and `skills/README.md` after metadata changes using the
commands in [catalog management](toolkit/CATALOG-GUIDE.md#generated-indexes-and-exports).
The catalog check detects stale indexes.
Profile pages, template pages and catalog navigation are generated at documentation
build time. Add no profile page stubs or copied instructions under `website/content/`.
Edit the canonical source; maintain website-specific layout and entry pages in `website/`.

Use [catalog management](toolkit/CATALOG-GUIDE.md), the
[quality standard](toolkit/QUALITY-STANDARD.md) and
[template chooser](templates/README.md) to keep new expertise specific and evidence-based.
