# Adopt the Markdown-first structure

For a new project, use the adaptable [Markdown-first project structure](../templates/markdown-project/README.md).
For an existing project, preserve its authoritative sources and adopt only the parts that
help with the next assignment. The compact [project starter](../templates/project-starter/README.md)
and [AGENTS.md variants](../templates/agent-instructions/README.md) remain useful for
smaller setups. Keep shared artifacts in English.

## Map the sources

Start with the project's existing `AGENTS.md` as the discovery entry. Link its real sources
for project facts, contributor process, issue and review homes, current knowledge,
decisions, roles and relevant skills. These can live in existing files, Markdown folders,
or authorized web documentation; the example structure is a starting point, not a required
folder tree. Keep existing owners and tool commands. Do not create empty directories or a
new manifest to match the example.

## Adapt the working process

Point contributors to the project's own process source and actual commands. Select and
adapt only the procedures that support the work; no fixed lifecycle or numbered sequence
is required. Keep assignment scope, acceptance, progress and review evidence at the
project's existing work and review homes. Record significant decisions when they arise,
and keep current verified behavior separate from decision history.

During adoption, verify that the chosen AI host discovers `AGENTS.md` and can load linked
sources. A link does not install instructions, guarantee retrieval or grant access. Replace
placeholder paths, URLs and roles, and preserve host-specific entry files such as
`CLAUDE.md` or `.github/copilot-instructions.md` when the project uses them.

## Adopt remote policy deliberately

A central process is optional. Record its immutable source URL and adopted SHA/version
in the project, explicitly read the body and verify access. Use only a declared fallback
with matching provenance when access fails; name the blocked action and continue
independent authorized work. Evolving technique links do not silently adopt policy.

## Verify a bounded assignment

Resolve source links, actual owners and commands, then try one real task and fresh-session
recovery. Check a missing required source and overlapping-writer handoff before scaling
parallel work. Static Markdown checks establish links, not acceptance, source quality or
host behavior. Follow the [runtime check](../templates/delivery/runtime-check.md) as needed.

## Keep personal and shared work distinct

Shared sources should let an authorized teammate understand the outcome, relevant evidence
and next action. Keep personal planning in the user's permitted private system, or unsaved
in-session when unavailable; do not publish private paths or notes in project guidance.
Docusaurus or another documentation site can provide a reading view of selected shared
Markdown, while the original source remains authoritative.

## Existing YAML and local workbench users

Keep an existing YAML configuration only when current tools depend on it. The optional
[project config](PROJECT-CONFIG.md) and local workbench remain compatibility paths; they
are not prerequisites for Markdown-first adoption. Preserve real data locations and avoid
contradictory copies of project policy.
