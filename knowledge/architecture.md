# Current architecture and knowledge layout

Owner: repository owner. Scope: the AI Agents repository and operating model.
State: implemented for review on the current branch; integration and publication are separate.

## Source ownership

AGENTS.md starts a person or AI session and links project context, contribution process,
current knowledge, decision history and the assigned work home. PROJECT.md owns project
facts; CONTRIBUTING.md owns detailed contribution procedure, tool routing and commands.
No YAML manifest is needed for this route.

Reusable agents and skills live in agents/ and skills/. toolkit/ owns reusable process,
quality, recovery and host-adapter guidance. templates/ supplies adaptable project entries,
AGENTS.md variants and engineering records. tools/ and tests/ implement and verify local
catalog, export and work-record behavior.

## Knowledge and decisions

knowledge/ owns this repository's current project knowledge and rationale.
Decisions remain in decisions/ with status, owner, context, alternatives, consequences and
source links. Accepted replacements link both records. Shared scope, acceptance and feedback stay
at the assigned issue or PR; personal execution steps stay private, subject to customer policy; a bounded handoff points to the relevant revisions.
See [ADR-0003](decisions/0003-agents-first-project-entry.md) for this proposed arrangement
and [knowledge lifecycle](../toolkit/PROJECT-KNOWLEDGE.md) for retention and retrieval.

## Native expertise and orchestration

Focused presets register only the selected native profiles. The Herd adapter emits
commander packages and portable schema-v2 import files, carrying selected skill bindings
and an on-demand catalog reference. Host configuration owns providers, worker routing,
permissions and execution; the toolkit is an exporter, not a fleet runtime.

The [orchestration guide](../toolkit/ORCHESTRATION.md) defines bounded task packets,
multiple lead responsibilities, integration and installed-host checks. The
[integration guide](../toolkit/INTEGRATIONS.md) separates native Ponytail/Graphify use
from curated Docusaurus publication. [ADR-0006](decisions/0006-native-orchestration-and-focused-expertise.md)
records the proposed adapter and expertise approach.

## Documentation and optional local tools

website/generate.py selects canonical Markdown for Docusaurus and rewrites local links.
The website is a derived reading view, with edit links to the maintained source. docs/ is
existing generated Pages output. A public website cannot expose private customer sources.

The example knowledge map starts with aggregate areas. Record lists and one-hop
neighborhoods use bounded JSON pages fetched on demand, with versioned snapshot URLs,
explicit result counts and retryable errors. Its build still processes the full published
Markdown collection. [ADR-0005](decisions/0005-bounded-knowledge-views.md) records the proposed
retrieval contract and the boundary to an indexed service for larger collections.

The optional workbench still stores records in ignored workspace/work/ and archives in
workspace/archive/. Its --workspace argument means the project root. Existing YAML
validation and customer examples remain compatibility tools; neither is required for a
new AGENTS.md project. The toolkit runs no models and provides no distributed work lock.

Update this page when source ownership, runtime storage, publication or entry behavior changes.
Validate using the [runbook](../toolkit/REPOSITORY-WORKFLOW.md) and CI on the affected revision.
