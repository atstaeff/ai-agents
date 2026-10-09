# AI Agents · Local work toolkit

Work with AI as a teammate using a shared [operating model](toolkit/OPERATING-MODEL.md),
an English catalog of **23 agents and 48 skills**, native exporters and a local dashboard.
Use **Jörg** as the general assistant. Keep board-managed plans in the assigned issue
and larger local work in one Markdown record. Load focused expertise as needed.

The toolkit runs on your computer with **Python 3.11+ and no runtime dependencies**.
It does not run models, create chat sessions or access your Obsidian vault automatically.
Your AI host provides model execution, tools and any native delegation capabilities.

## Start in WSL with OpenCode 1

Run in your WSL terminal:

```sh
git clone https://github.com/atstaeff/ai-agents.git ~/tools/ai-agents
cd ~/tools/ai-agents
python3 tools/ai_toolkit.py check
python3 tools/ai_toolkit.py export --runtime opencode \
  --output "$HOME/.config/ai-agents/opencode"
```

Start OpenCode Web from the project you want to work on:

```sh
cd /path/to/your/project
OPENCODE_CONFIG_DIR="$HOME/.config/ai-agents/opencode" \
OPENCODE_CONFIG="$HOME/.config/ai-agents/opencode/opencode.json" \
opencode web
```

The exported configuration selects `joerg` by default. It supplies custom `plan` and
`build` profiles, specialist subagents, all 48 native skills and `/work-plan`,
`/work-build` and `/brain` commands. No provider, model or third-party plugin is forced.
These are OpenCode 1 configuration files; web session navigation depends on your release.

Try these requests:

> Jörg, fix this small issue directly and run the relevant check.

> Jörg, improve this larger feature. Keep the plan and my feedback in one
> `.ai/work/` record, implement the first complete increment and verify it.

> Use the second-brain agent to propose where these notes belong in my existing PARA
> vault. Preserve my wording, aliases and links.

Re-export after updating the repository; unchanged files are skipped. Edited bundle
files are protected; change canonical sources here or select another destination.
See [runtime details](toolkit/RUNTIMES.md).

## Plans, tasks and your comments

Small changes need no process file. For a larger outcome, create one record:

```sh
python3 ~/tools/ai-agents/tools/ai_toolkit.py work --workspace . new onboarding \
  --title "Improve onboarding" --kind product
python3 ~/tools/ai-agents/tools/ai_toolkit.py serve --workspace .
```

Open **http://127.0.0.1:4097**. The dashboard searches the catalog, creates records,
shows plans, appends comments and updates task status/evidence. Edit plans in your
editor or AI host; the dashboard writes selected task rows and appended feedback.
Stale updates are rejected so you can reload before retrying.

The agent instructions ask agents to update the same record while working. There is
no background session watcher: a model must follow the instructions. The dashboard
does not start AI sessions or execute shell commands.

```text
.ai/work/onboarding.md       # Goal, plan, tasks, feedback, decisions, evidence
.ai/archive/old-outcome.md   # Completed records; load only when needed
```

`docs/` stays available for existing documentation or GitHub Pages. CSV is an optional
export, not a second task list. See the [workflow](toolkit/WORKFLOW.md) and
[work-record guide](toolkit/WORK-RECORDS.md).

## Customer-owned GitHub workspace

Use [templates/customer-workspace](templates/customer-workspace/README.md) when a
customer's GitHub Project coordinates delivery. The Project owns priority, iteration
and status; the issue owns the live plan and questions; `workspace/` keeps durable
decisions, process knowledge and iteration outcomes in the customer's repository.
Use that issue instead of a duplicate `.ai/work/` record for the same assignment.

Start with three workspace entry files and merge the example instructions into the
customer's existing `AGENTS.md`. The fictional worked example includes an issue form,
stakeholder questions, linked ADRs, a local knowledge graph generator and integration
with an existing Docusaurus site. Adopt only what the project needs; this template is
not an automatic installer or background runner.

## Jörg and your Second Brain

Jörg selects relevant skills and specialists from metadata. Delegation uses the host's
actual tools and permissions; otherwise he works in the current session using the
selected guidance. OpenCode reviewer profiles are restricted; Build can implement.

Second Brain uses your existing **Projects, Areas, Resources and Archive**, including
numbered folders. Provide an accessible private vault path to your host when needed.
Keep notes and local settings outside this public repository. Filesystem moves require
backlink and relative-link checks.

```sh
python3 tools/ai_toolkit.py obsidian-uri \
  --vault "My Second Brain" --file "Projects/Customer portal.md"
```

Whether an `obsidian://` link is clickable in OpenCode Web depends on its renderer.
Copy the URI to a Windows application that supports the protocol if needed.

## Other runtimes and APIs

```sh
# Export into another project; edited/unmanaged files are protected.
python3 tools/ai_toolkit.py export --runtime copilot --output /path/to/other-project
# Generic Agent Skills plus portable Markdown profiles.
python3 tools/ai_toolkit.py export --runtime portable --output /path/to/bundle
# Metadata only, useful for routing.
python3 tools/ai_toolkit.py catalog --kind skill
```

Canonical `agents/` is a source catalog, not an automatically discovered directory in
every host. The exporter creates native layouts and fields. See
[compatibility](toolkit/RUNTIMES.md) and the [local API](toolkit/API.md).

## Develop and verify

```sh
python3 tools/ai_toolkit.py check
python3 -m unittest discover -s tests -v
uv sync --group docs
uv run --group docs mkdocs build -f assets/mkdocs.yml --strict
uv run --group docs mkdocs serve -f assets/mkdocs.yml
```

Open **http://localhost:8000** after starting MkDocs. The
[local preview guide](assets/mkdocs/getting-started/local-preview.md) also covers static builds.
The Docusaurus guide integrates customer workspace sources into an existing customer site.
MkDocs sources for this catalog site are in `assets/mkdocs/`. The existing website is
[atstaeff.github.io/ai-agents](https://atstaeff.github.io/ai-agents/).
CI checks catalog, tests and docs on PRs; the main workflow rebuilds tracked `docs/`
for the existing Pages setup. Contributions: [CONTRIBUTING.md](CONTRIBUTING.md).
License: [MIT](LICENSE).
