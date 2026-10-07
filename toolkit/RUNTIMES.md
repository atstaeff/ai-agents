# Runtime adapters

Canonical entries use common `name` and `description` frontmatter. Exporters add
host fields and layout and rebase links into one shared `catalog/` copy.

| Runtime | Exported layout | Behavior |
| --- | --- | --- |
| OpenCode 1 | `agents/*.md`, `skills/<name>/SKILL.md`, `commands/`, `opencode.json` | Jörg, Plan and Build are primary; specialists are subagents |
| VS Code / Copilot | `.github/agents/*.agent.md`, `.github/skills/<name>/SKILL.md` | Project-native profiles; select in the host |
| Portable | `.agents/skills/<name>/SKILL.md`, `agents/*.agent.md` | Agent Skills plus portable profiles; agent discovery is host-specific |

## OpenCode in WSL

Export into a dedicated directory, then set both variables when starting from a project.
`OPENCODE_CONFIG` loads JSON; `OPENCODE_CONFIG_DIR` loads agents, skills and commands.
Your provider setup stays separately configured. Project configuration and permissions
can affect the final merged setup.

The exported configuration permits access to its own reference catalog outside the
project and denies editing that catalog. It does not grant access to other external
directories or a private vault. Configure those separately in your host when needed.

```sh
python3 tools/ai_toolkit.py export --runtime opencode \
  --output "$HOME/.config/ai-agents/opencode"
cd /path/to/project
OPENCODE_CONFIG_DIR="$HOME/.config/ai-agents/opencode" \
OPENCODE_CONFIG="$HOME/.config/ai-agents/opencode/opencode.json" opencode web
```

The adapter uses `mode` and singular `permission`, with no fixed model or plugin.
Reviewers deny edit, shell and task tools. Plan has edit exceptions for `.ai/work/**`
and `.ai/archive/**`. This is a planning guardrail, not an OS sandbox: consider other
installed tools and project configuration. Build and Jörg use normal host permissions.
Do not install unrestricted write tools on a profile intended to be read-only.

Use `/work-plan`, `/work-build` or `/brain`. Native delegation and interaction with
child sessions in OpenCode Web depend on your release. The toolkit adds no session
orchestration plugin.

## Copilot

Export into another project. Existing edited/unmanaged files, including
`.github/copilot-instructions.md`, are protected. If you maintain those already,
export separately and integrate deliberately. Keep `catalog/` with the profiles;
their focused reference links point into it.

VS Code aliases `read` and `search` restrict reviewers and Plan to proposed changes.
Use a writing profile to apply a plan. Permissions and tool availability are
host-specific; other Copilot surfaces may interpret frontmatter differently.

## Updates and privacy

Re-export after source updates. `.ai-toolkit-manifest.json` tracks owned paths and
hashes. Edited or unmanaged files are not silently overwritten. `--dry-run` checks
without writing; `--force` explicitly permits replacing files at planned paths.
Updates write only changed files and remove obsolete owned files. Identical files,
including the manifest, keep their timestamps. JSON output reports `changed`,
`unchanged` and `removed` file counts; the manifest is excluded. With `--dry-run`,
these counts describe the proposed update. Use a dedicated destination.

Keep model keys and private vault paths in local configuration. The catalog/dashboard
uses no remote runtime service; AI provider calls are managed by your host.

Sources: [OpenCode agents](https://opencode.ai/docs/agents/),
[configuration](https://opencode.ai/docs/config/), [skills](https://opencode.ai/docs/skills/),
[VS Code custom agents](https://code.visualstudio.com/docs/agent-customization/custom-agents).
Structural checks do not establish model behavior or installed web UX compatibility.
