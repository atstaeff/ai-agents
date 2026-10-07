# Architecture and source of truth

| Component | Source | Responsibility |
| --- | --- | --- |
| Portable agents | `agents/*.agent.md` | Short roles, focused skill pointers and completion contract |
| Portable skills | `skills/` | Actionable instructions and optional reference examples |
| Shared workflow | `toolkit/WORKFLOW.md` | Proportionate planning, delivery, feedback and evidence |
| Runtime adapters | `tools/ai_toolkit.py export` | Native layout, permissions and rebased references |
| Work records | Each project's `.ai/work/` | One record per larger outcome |
| Local UI/API | `tools/web/`, Python loopback server | Catalog search, task evidence and comments |
| Website | MkDocs sources and `tools/docs_hook.py` | Render canonical instructions at build time |

Jörg selects relevant expertise from metadata. A native host may provide subagent
execution; otherwise the current session uses the selected guidance. The toolkit
itself does not call model APIs or manage chat sessions.

Exported bundles contain one shared catalog copy. Native skill directories include
only their entry instructions and links to shared references, avoiding a full library
copy in every skill. Ownership hashes protect edited and unmanaged export files.

Private vaults and workspaces remain separately configured. `docs/` retains its
existing GitHub Pages role; operational records live in `.ai/` when needed.
