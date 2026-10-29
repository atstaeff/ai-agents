# Consequential decision review

Use this reference when alternatives or decision authority remain unresolved. Routine
reversible choices can stay in the existing PR; use the project's ADR home for reasons
that future contributors must recover.

## Compare viable options

State the required user outcome, hard constraints, current revision and decision owner.
Include the current approach and the simplest adequate alternative. Compare only the
criteria that could change the choice: compatibility, data meaning, change/operating
cost, team capability, security, recovery and meaningful quality scenarios.

Separate observations from estimates and assumptions. Identify the uncertainty whose
answer would change the recommendation; choose a bounded experiment when its evidence
is worth the delay. Avoid invented information-completeness percentages, fixed innovation
budgets or claims that a technology will multiply delivery speed.

## Assess reversibility in this project

A library replacement can be expensive when it owns stored data or public contracts;
a database decision can be staged behind a real migration boundary. Assess consumer
commitments, data conversion, rollback/repair and switching cost rather than labeling
whole technology categories as inherently reversible.

For a hard-to-reverse choice, expose the material uncertainty and affected owners.
For a reversible experiment, define its budget, stop condition and what survives it.
Proceed with authorized routine work while the blocked decision is resolved.

## Record a recoverable decision

Use the existing format with:

- Context, outcome and source revision.
- Viable alternatives and the evidence or assumptions that distinguish them.
- Proposed or accepted choice, accountable decision owner and actual status.
- Consequences, compatibility/migration and operating or recovery responsibility.
- Verification and the condition that would justify revisiting or superseding it.

Draft reasons while alternatives are known, then reconcile them with implementation
and acceptance. Preserve an accepted record's history and explicit supersession; a new
proposal does not silently overrule it. A private plan is not the shared decision log.

## Resolve disagreement

Preserve the concern and evidence in the original feedback. State the concrete tradeoff,
recommendation and decision needed from the accountable owner. Do not invent consensus,
force a commitment or treat unanswered feedback as acceptance.

Return the recommendation, material alternatives, open uncertainty and next owner/action.
Use [architecture planning](../../architecture-planning/SKILL.md) to shape a cross-boundary
change, or [communication](../../../knowledge/communication/SKILL.md) to draft the decision request.
