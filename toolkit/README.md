# Engineering toolkit guide

Start at [AGENTS.md](../AGENTS.md). This directory contains reusable guidance and data;
[tools/](../tools/README.md) contains executable implementations. Read the next relevant
page, not this whole directory at the start of each session.

## Repository responsibilities

| Location | Purpose | Example |
| --- | --- | --- |
| Root AGENTS.md | Short AI entry, essential boundaries and source links | Where to read project scope and process |
| PROJECT.md / CONTRIBUTING.md | This project's facts / contribution process | Goals, owners / checks and skill selection |
| agents/ / skills/ | Reusable roles / actionable procedures | Reviewer / review method |
| toolkit/ | Reusable engineering model, adoption and tool documentation | How any project retains decisions |
| knowledge/ | Durable facts and decisions about this repository | Why this catalog uses private plans |
| templates/ | Copyable starting documents | ADR, request or architecture review |
| examples/ / reference-repos/ | Runnable demonstrations / worked projects / illustrative code | Decision graph / document portal / architecture patterns |
| tools/ / tests/ | Executable local tooling / behavior checks | Runtime exporter / export protection tests |
| website/ | Docusaurus source, configuration, navigation and publisher | Source-to-page mapping |
| docs/ | Compiled GitHub Pages output | Generated HTML and assets |

Knowledge is project memory, not another skill library or personal task store. A customer
project owns its own facts and ADRs; they do not belong in this catalog's knowledge folder.
Private plans stay in the user's permitted Second Brain, or unsaved in-session when
unavailable. The shared result remains understandable without access to those plans.

## Choose a guide

| Question | Read |
| --- | --- |
| What rules are needed for a normal session? | [Session rules](SESSION-RULES.md) |
| How does delivery work? | [Operating model](OPERATING-MODEL.md), [detailed workflow](WORKFLOW.md) |
| How do I adopt this in a project? | [Adoption](ADOPT-PROJECT.md), [project concept](PROJECT-CONCEPT.md) |
| How are knowledge and decisions retained? | [Project knowledge](PROJECT-KNOWLEDGE.md), [recovery](CONTEXT-RECOVERY.md) |
| How do I select or maintain expertise? | [Catalog guide](CATALOG-GUIDE.md) |
| How do several leads and specialists work together? | [Orchestration](ORCHESTRATION.md) |
| How do Ponytail, Graphify and Herdr fit? | [Integrations](INTEGRATIONS.md) |
| How do I export to my AI host? | [Runtime adapters](RUNTIMES.md), [portability](PORTABILITY.md) |
| What quality or approval applies? | [Quality standard](QUALITY-STANDARD.md), [optional plan review](PLAN-REVIEW.md) |
| How do I develop this repository? | [Repository runbook](REPOSITORY-WORKFLOW.md) |
| How does the optional local workbench work? | [Work records](WORK-RECORDS.md), [API](API.md) |
| What about existing YAML configurations? | [Optional project config](PROJECT-CONFIG.md) |

`catalog-domains.json`, `catalog-presets.json` and `catalog-aliases.json` define catalog
organization, native export selections and retired-name replacements. `openapi.json`
describes the local API; `workspace.schema.json` supports optional existing YAML setups.
`examples/` contains worked documentation and `evaluations/` records dated observations
with evidence and limits. They are reference material, not mandatory startup context.

## Source and published view

Keep each document at one editable owner. Docusaurus can publish Markdown from toolkit,
knowledge, agents and skills without moving or copying their maintained sources. The
[website guide](../website/README.md) explains the mapping. Root docs/ is reserved for
compiled Pages output; website/ already provides a separate Docusaurus source directory.

AGENTS.md may link a maintained Docusaurus process URL for other projects. Keep essential
boundaries and project-specific commands locally, identify the applicable source revision
or documentation version, and read the relevant linked content explicitly. A URL alone
does not inject its contents into an AI session; browsing may be unavailable and a deployed
site can lag a checkout. Follow the existing [remote documentation template](../templates/agent-instructions/README.md)
and [project concept](PROJECT-CONCEPT.md) when adopting central guidance.

Preserve host entry filenames: `.github/copilot-instructions.md`, path-specific
`.github/instructions/*.instructions.md`, reusable `.github/prompts/*.prompt.md`, and
`CLAUDE.md`. Their contents can point to canonical guidance; do not rename these entry
files to imitate a repository's own documentation naming scheme.
