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

## Safe maintenance

Before a move, inspect inbound wikilinks, Markdown links, embeds and relative paths. A plain filesystem move does not trigger Obsidian's automatic link update. Plan and verify link updates, or leave the note in place with an index link. Respect OneDrive synchronization and reread changed files before saving. Do not bulk rename, delete, flatten folders or install community plugins without a specific request.

Use the vault's existing completion convention to identify archive candidates; do not infer completion merely from an old date. Preserve heading/block fragments and recalculate outgoing relative links as well as inbound links. Build an old-to-new path map and follow the existing Archive layout. Never overwrite a destination collision. If a source changes after inspection, stop that move, reconcile the versions and recheck links before saving; do not overwrite a concurrent OneDrive edit.

Never commit private vault content, credentials or personal records to this public repository. Do not add a private absolute vault path to shared configuration. Keep vault settings in local environment variables or user configuration.

## Open a note on Windows

Construct `obsidian://open?vault=<encoded-vault-name>&file=<encoded-vault-relative-note-path>` using URI component encoding, including spaces, `&`, `#`, non-ASCII characters and slashes. Use the vault-relative path, not a `/mnt/c/...` path. The toolkit's `obsidian-uri` command performs this encoding.

Obsidian must be installed and have registered the protocol on Windows. Whether OpenCode Web renders a clickable custom-protocol link depends on its UI. Provide the URI for copying if it is filtered; do not promise a plugin-free clickable link in every release.

From the catalog checkout, run `python3 tools/ai_toolkit.py obsidian-uri --vault "Vault name" --file "Projects/Note.md"` to construct the URI. The helper is not an Obsidian plugin and does not open or modify the vault.

## Completion

Report the notes changed, classification decisions and link checks actually performed. Keep uncertain classifications and unapplied changes explicit.
