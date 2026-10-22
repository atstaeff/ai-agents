# Add or improve an agent

An agent owns a bounded role and handoff. Inspect the existing catalog before adding a
new role. Prefer improving an existing profile when the responsibility is already covered.

Create `agents/<domain>/<name>.agent.md` from the
[agent template](../templates/catalog/agent-template.md). Choose a discipline from the
[catalog guide](../catalog/maintain.md). Keep portable name/description metadata, project
and authority boundaries, a short procedure, selected skills and expected evidence.
Runtime tools and permissions belong in exporters.

Validate metadata and links, regenerate the agent index, exercise native exports and
build the docs. Consequential instruction changes need realistic behavior observations,
including failure and small-task bypass. Record limits and open a reviewable PR.

No website profile stub is needed: the build generates its page and catalog navigation.
