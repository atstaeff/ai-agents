# Contributing

This guide owns repository contribution requirements and tool references. The
[engineering process](engineering/process/README.md) owns phase procedures; start with
[AGENTS.md](AGENTS.md) and load only the relevant step. Keep shared artifacts English.

## Working process and skills

Use [PROJECT.md](PROJECT.md) for vision, boundaries, owners and real work/review homes.
The [working agreement](knowledge/working-agreement.md) defines acceptance and action
boundaries. Select the applicable procedure from the [process index](engineering/process/README.md);
it links focused skills for clarification, design, implementation, verification and retention.

For unfamiliar repository rules, use [repository contribution](skills/delivery/repository-contribution/SKILL.md).
Load selected skill bodies explicitly; a link does not install or execute a skill.
Use actual project tools and report missing access instead of creating a mirror tracker.

## Team ownership and integration

Apply [session rules](toolkit/SESSION-RULES.md#autonomous-team-default) for autonomous
startup and coordination. [Herdr](toolkit/HERDR.md) owns native execution and model routes;
[orchestration](toolkit/ORCHESTRATION.md) owns delegation, write scopes and integration.
The process's [plan](engineering/process/02-plan.md), [build](engineering/process/03-build.md)
and [verify](engineering/process/04-verify.md) steps cover the relevant handoffs.
Keep shared acceptance and evidence at the assignment and personal plans at their private home.

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
catalog/link, test, HTTP replay, legacy YAML, JavaScript/options and documentation checks.
Keep those commands and action rules in their existing sources, linked from the project entry.

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
After changing team profile metadata, regenerate the native checkout adapter with
`python3 tools/ai_toolkit.py opencode-config > opencode.json`; the catalog check detects drift.

Use [catalog management](toolkit/CATALOG-GUIDE.md), the
[quality standard](toolkit/QUALITY-STANDARD.md) and
[template chooser](templates/README.md) to keep new expertise specific and evidence-based.
