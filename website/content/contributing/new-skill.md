# Add or improve a skill

A skill provides a focused procedure for a recognizable selection situation. Read the
[contribution process](index.md) and existing skill metadata first. Improve an existing
skill when it already covers the need.

Create `skills/<domain>/<name>/SKILL.md` using the
[skill template](../templates/catalog/skill-template.md). Include portable `name` and
`description` metadata, actionable steps and observable completion evidence. Put substantial
examples in `references/` and link them from the entry so they load only when needed.
Keep project facts, host permissions and private planning locations at their actual owners.

Follow the [catalog guide](../catalog/maintain.md) and
[repository runbook](../getting-started/repository-workflow.md) for the applicable metadata,
link, export and website checks. Observe substantial changes on realistic inputs, missing
access and a small task that should bypass the skill. Report the checks and behavior
actually observed, including limits.

Open a focused PR. The website generates skill pages and navigation from canonical
metadata; add no copied skill body or placeholder page under `website/content/`.
