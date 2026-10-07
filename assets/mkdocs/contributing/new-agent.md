# Add an agent

Create `agents/<slug>.agent.md` with common YAML `name` and `description`. Write a
short role, concrete workflow, focused skill links and completion criteria. Keep
host-specific modes, tools and permissions in the exporter. Add valuable examples
under `agents/references/` only when they are useful.

Add a thin website page at `assets/mkdocs/agents/<slug>.md`; the documentation hook
renders the canonical profile. Add navigation when appropriate, then run the checks
in the repository instructions. See the [contribution guide](index.md).
