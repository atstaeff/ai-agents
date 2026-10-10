# Frequently asked questions

## Must my repository use a .claude folder or change for every model?

No. Keep shared rules in `AGENTS.md`, customer knowledge in `workspace/` and reusable
expertise in the canonical catalog. A model change within a host needs no folder change.
Host tools have different discovery paths and permissions; exports generate those
adapters from the same sources. See [portability](getting-started/portability.md).

## Must every project use GitHub Issues or repository knowledge?

No. Each project defines its tracker, planning home, code review, decision and knowledge
locations in [`workspace/project.yaml`](getting-started/project-config.md). Jira can own the plan while GitHub holds only the PR;
Confluence or a repository can own knowledge. The customer starter uses GitHub as a
worked example. Missing tool access means an unsent proposed update, not a new tracker.

## Which hosts have native exports?

OpenCode 1, VS Code/Copilot and Claude Code. A portable export also provides Agent
Skills and generic agent profiles; generic profile discovery remains host-specific.
Permissions and review UI are not equivalent across hosts. See
[runtime setup](getting-started/installation.md) and perform a local discovery check.

## Is it an OpenCode session orchestration plugin?

No. It exports native agents, skills and commands. Delegation and session interaction
come from the installed host. The dashboard manages files and does not launch agents.

## Can Plan and Build be customized?

Yes. Edit their canonical profiles and re-export. OpenCode Plan has scoped edit
permissions for work records; its shell/task tools are denied. Review the final merged
host configuration and other installed tools before relying on a read-only boundary.

## Can I comment on and approve a plan before using another model for Build?

Use the optional [Plannotator plan review](getting-started/plan-review.md) in OpenCode 1.
Plan submits a concrete revision, receives comments and resubmits after requested changes.
Build starts after actual approval. Separate model and supported variant fields configure
the two phases; verify their selection in your installed Web version. The toolkit configures
the external plugin; it neither proves runtime switching nor synchronizes GitHub issues.

## Must every task create a document?

No. Small changes use the conversation and existing checks. Larger outcomes use one
planning home: the project-designated work item for tracked delivery, or `.ai/work/` for larger
local work without that assignment. CSV is an export only.

## Is this website Docusaurus?

The AI Agents catalog site uses MkDocs. The workspace starter integrates with a customer's
existing Docusaurus site. Both publish views of canonical Markdown; compiled `docs/`
output stays separate from editable workspace sources.

## Does an accepted ADR prove delivery?

It records the authorized decision maker's agreement. Implementation, verification,
review, merge, deployment and observed impact each need evidence. Write significant
decisions during delivery and link them at iteration close.

## Must I copy all the starter files?

Start with the project YAML config, workspace entry page, working agreement and stakeholders. Adopt relevant
instructions into the existing AGENTS.md. The worked files illustrate format; create
real ADRs and knowledge pages when the assignment warrants them.

## Is the recurring local worker implemented?

The manual host workflow, profile exports, dashboard and graph generator are available.
The runner page is a design contract. Recurring processing needs an implementation and
authorized tools for the customer's Project, issues and repositories.

## Does it upload my Obsidian vault?

The toolkit has no remote vault service. An AI host can read an explicitly accessible
vault using its own tools and provider configuration. Keep private notes and paths
outside this public repository.

## Do Obsidian links open from OpenCode Web?

The URI helper produces correctly encoded `obsidian://` links. Clickability depends
on the web renderer and Windows protocol registration. Copy the URI if it is filtered.

## How do I update profiles?

Update the repository and re-export to the same dedicated destination. Edited or
unmanaged files cause a clear error; integrate deliberately or choose another output.
