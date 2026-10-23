# Vault maintenance and Windows links

Read the applicable section only for a move, archive or Windows/WSL link request.

## Safe maintenance

Before a move, inspect inbound wikilinks, Markdown links, embeds and relative paths. A plain filesystem move does not trigger Obsidian's automatic link update. Plan and verify link updates, or leave the note in place with an index link. Respect OneDrive synchronization and reread changed files before saving. Do not bulk rename, delete, flatten folders or install community plugins without a specific request.

Use the vault's existing completion convention to identify archive candidates; do not infer completion merely from an old date. Preserve heading/block fragments and recalculate outgoing relative links as well as inbound links. Build an old-to-new path map and follow the existing Archive layout. Never overwrite a destination collision. If a source changes after inspection, stop that move, reconcile the versions and recheck links before saving; do not overwrite a concurrent OneDrive edit.

Never commit private vault content, credentials or personal records to this public repository. Do not add a private absolute vault path to shared configuration. Keep vault settings in local environment variables or user configuration.

## Open a note on Windows

Construct `obsidian://open?vault=<encoded-vault-name>&file=<encoded-vault-relative-note-path>` using URI component encoding, including spaces, `&`, `#`, non-ASCII characters and slashes. Use the vault-relative path, not a `/mnt/c/...` path. The toolkit's `obsidian-uri` command performs this encoding.

Obsidian must be installed and have registered the protocol on Windows. Whether OpenCode Web renders a clickable custom-protocol link depends on its UI. Provide the URI for copying if it is filtered; do not promise a plugin-free clickable link in every release.

From the catalog checkout, run `python3 tools/ai_toolkit.py obsidian-uri --vault "Vault name" --file "Projects/Note.md"` to construct the URI. The helper is not an Obsidian plugin and does not open or modify the vault.
