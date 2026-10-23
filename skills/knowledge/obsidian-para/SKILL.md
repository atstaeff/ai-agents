---
name: "obsidian-para"
description: "Capture, retrieve and maintain notes in a private Obsidian vault organized as Projects, Areas, Resources and Archive, including Windows/WSL links."
---

# Obsidian Para

## Discover before writing

Confirm the actual vault path, exact Obsidian vault name and existing folder convention from the workspace or user context. Recognize names such as `Projects` or `01_Projects`; do not rename folders to match an example. On WSL, a Windows vault may be mounted under `/mnt/c/...`; use the accessible filesystem path for edits and the vault name for Obsidian links.

Read the destination note and nearby conventions before changing anything. If access is unavailable, produce a concrete proposed note or patch and state that it has not been applied. Do not claim that this catalog gives automatic access to a vault.

## Classify by actionability

| Folder | Meaning | Example |
| --- | --- | --- |
| Projects | A finite outcome with a completion condition | Ship the customer portal |
| Areas | An ongoing responsibility or standard | Personal finances; engineering quality |
| Resources | Reusable knowledge or a topic of interest | Python patterns; research notes |
| Archive | Material no longer active | Completed project; inactive responsibility |

1. Search for an existing relevant note before creating one. Prefer useful links and a focused update over duplicate summaries.
2. Capture the idea in the existing inbox when its purpose is unclear; classify when there is enough context.
3. Preserve the user's text, properties, aliases and note identity. Add a small sourced summary and explicit next action where useful.
4. Keep project status and actionable tasks in the existing project note or linked work record; avoid two manually maintained task lists.
5. Extract only reusable conclusions from work, including a source link and the date when it affects validity. Do not paste entire chat transcripts by default.

## Personal engineering plans

Keep one working plan per substantial outcome in the vault's existing project folder.
Store goal, acceptance, steps, actual checks and one resume point. Do not mirror it into
an issue or repository. Respect customer policy before storing project material privately.
After implementation, preserve significant decisions and current documentation in the
shared project, then close/archive the personal plan. If the vault is unavailable, state
that the plan is unsaved and continue in-session without a substitute repository file.

## Load for the requested operation

- [Maintenance and Windows links](references/maintenance-and-links.md): moves, archival,
  collision/concurrent-sync checks and encoded Obsidian links. Read before those operations.

Keep vault content, credentials and private paths outside public repositories. Report
applied changes and actual link checks; label unavailable access and unapplied proposals.
