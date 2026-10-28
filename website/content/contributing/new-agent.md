# Add or improve an agent

An agent defines a bounded responsibility, procedure and handoff. Read the
[contribution process](index.md) and inspect existing metadata before adding a role.
Improve the current profile when it already owns that responsibility.

Create `agents/<domain>/<name>.agent.md` using the
[agent template](../templates/catalog/agent-template.md). Choose a discipline from the
[catalog guide](../catalog/maintain.md). Include portable `name` and `description`
metadata, selection situations, authority boundaries, relevant skills and completion
evidence. Configure host tools, permissions and models through the appropriate adapter
or host settings.

Follow the catalog guide and [repository runbook](../getting-started/repository-workflow.md)
for the applicable metadata, link, export and website checks. For consequential instruction
changes, observe a realistic task, missing access and a small task that should bypass the
role. Distinguish structural checks from behavior actually observed.

Open a focused PR with the result and evidence. The website generates the profile page
and navigation from its canonical source; add no website profile stub.
