# Worked document portal example

This compatibility example retains a fictional document portal, optional YAML
configuration and graph helpers. It contains no actual customer data, approvals or
application implementation. It is an example, not the recommended project starter; do
not copy every file into a new project.

For new adoption, prefer the [instruction templates](../../templates/agent-instructions/README.md) and
[setup prompt](SETUP-PROMPT.md). Merge [AGENTS.md](AGENTS.md) into existing instructions;
link the project's actual vision, owners, process, code, decisions and check commands.
No mandatory workspace directory or YAML is needed.

## Ownership

Personal working plans live in the user's configured private Second Brain, subject to
customer policy. Shared issues own scope, acceptance and coordination. PRs own changes
and verification; shared knowledge/ADRs preserve the maintainable result. Copy no private
plan into the project merely because the tracker has a place for it.

When the team needs a joint execution plan, choose one shared home. The fictional
[worked assignment](examples/issue-42.md) shows such a case; it is not a required template
for personal execution. All CUSTOMER_* values, URLs, approvals and results are examples.

## Optional existing-layout examples

- [workspace/README.md](workspace/README.md), [owners](workspace/stakeholders.md) and
  [working agreement](workspace/working-agreement.md).
- [YAML](workspace/workspace.yml), [minimal](examples/workspace-minimal.yml),
  [Jira](examples/workspace-jira.yml) and [multi-repo](examples/workspace-multi-repo.yml) variants.
- [Bounded handoff](workspace/handoff.md) for actual collaborator handoffs.
- [Docusaurus integration](examples/docusaurus-integration.md) and
  [graph generator](examples/knowledge_graph.py) for the existing metadata schema.

For a complete running site, use the [new Docusaurus demo](../../examples/engineering-demo/README.md).
Both publishing approaches exclude local work and private plans. Git ignore alone is
not a publication boundary. Preserve the root project's README, policies and source layout.
