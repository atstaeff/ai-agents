# Choose a first outcome

Start with one bounded assignment and the existing project's acceptance criteria.
Select expertise for the uncertainty that needs resolving.

| Team and outcome | Useful lead and expertise | Evidence and result |
| --- | --- | --- |
| Engineering: fix a defect or add a small API behavior | [Jörg, the general engineering coordinator](agents/joerg.md) or the relevant language specialist; Code Reviewer when useful | Changed behavior, representative tests and linked review |
| Product: decide whether to pursue a user problem | Product Manager with focused discovery expertise | Source observations, assumptions, a bounded experiment and a decision |
| Architecture: resolve a consequential interface choice | Lead Architect with relevant specialists and review | Alternatives, agreed contract, significant rationale and implementation evidence |
| Platform: improve deployment or recovery | Delivery coordinator with DevOps and reliability expertise | An exercised deployment or recovery path, constraints and owned follow-up |
| Quality: assess a risky change | Code Reviewer or Architecture Reviewer | Reproducible findings tied to the current revision |
| Knowledge: preserve an outcome for the next session | The assignment's owner with communication expertise | Updated current knowledge, significant decisions and a concise resume point |

The issue or ticket owns shared scope, acceptance and evidence links; the linked PR owns
implementation and review details. Personal execution plans stay private or explicitly
unsaved in-session. Follow the [adoption guide](getting-started/adopt-workspace.md) to name
these sources in `AGENTS.md`, `PROJECT.md` and `CONTRIBUTING.md`.

Use one session for a small clear change. For useful parallel work, agree interfaces,
give each writer a bounded scope and verify the combined result. Choose the relevant
leader and host-configured specialists using the [orchestration guide](getting-started/orchestration.md).
Profiles supply expertise; the host and project determine available tools and permissions.
