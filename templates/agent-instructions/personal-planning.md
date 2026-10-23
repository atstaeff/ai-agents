# Configure private Second Brain planning

Keep the actual path and vault name in user-local host configuration or an instruction
file outside the repository. These example values are placeholders; preserve existing
PARA folder names. The project root needs only the policy, not your machine's location.

Example private instruction:

```text
Store my working plans in the existing Second Brain project folder configured below.
Filesystem directory (WSL): /mnt/c/Users/USER/OneDrive/VAULT/Projects/PROJECT/Plans
Obsidian vault name: VAULT
Vault-relative plan directory: Projects/PROJECT/Plans
Use one plan per outcome. Preserve comments; after saving output an encoded Obsidian URI.
After implementation, preserve relevant decisions and current documentation in the project.
Do not copy the personal plan into an issue, PR or repository.
```

Configure Plan's write access explicitly when exporting the OpenCode 1 bundle:

```sh
python3 tools/ai_toolkit.py export --runtime opencode \
  --plan-directory '/mnt/c/Users/USER/OneDrive/VAULT/Projects/PROJECT/Plans' \
  --output "$HOME/.config/ai-agents/opencode"
```

The exporter resolves and requires an existing absolute directory. It grants Plan editing
only below that directory, grants external-directory access there, and writes a private
location instruction into the generated bundle. Keep that bundle outside source control.
It does not discover a vault, move notes or change permissions for other agents. Without
this option Plan stays read-only; use the coordinating writing agent to save a personal plan.
Do not point the option at an entire vault, home directory or repository.

For Obsidian links, encode the exact vault name and the path relative to that vault,
never the `/mnt/c/` path. See [the skill](../../skills/knowledge/obsidian-para/SKILL.md).
Link clicking still depends on the chat UI and Windows protocol registration; it is not
proved by a generated configuration. Check the installed host once with a harmless note.
