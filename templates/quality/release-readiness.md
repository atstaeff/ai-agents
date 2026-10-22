# Release and recovery readiness

- Scope, release revision and owner: <exact changes and accountable operator>
- Dependencies and compatibility: <consumer/data/schema constraints and integration order>
- Required acceptance/review: <actual references or pending decisions>
- Verification and gaps: <linked evidence and explicit unrun criteria>
- Rollout: <bounded steps, exposure and observation window>
- Success and stop signals: <specific measures, thresholds and owner>
- Recovery: <rollback, restore or forward-repair procedure and tested evidence>
- Data consequences: <irreversible effects, backups, reconciliation and ownership>
- Operations: <alerts, diagnostics, runbook and on-call/response responsibility>
- Authorization and result: <actual release decision and observed state>

Do not fill a successful release in advance. Rehearse consequential recovery paths at
an appropriate boundary. A reversible code rollback may still leave changed data or
external effects requiring separate repair.
