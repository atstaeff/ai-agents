# Evidence for maintenance investment

Use a focused section when a maintainability problem competes with other work. Keep
repayment at the existing backlog/work home; a catalog of hypothetical smells is not
an actionable debt plan.

## Describe the cost

State the concrete change or operating task that is slow, fragile or blocked. Link a
reproduced defect, repeated review/rework, difficult recovery or representative change
exercise. Distinguish known facts from an estimate; do not invent percentage slowdowns
or label every old dependency and duplicated line as debt.

A useful record contains:

- Affected behavior/boundary, source revision and accountable owner.
- Observed cost or risk, its evidence and the event that makes repayment useful.
- The smallest adequate repair and a feasible alternative, including doing nothing.
- Compatibility and rollout/recovery needs, expected effort and material uncertainty.
- Observable acceptance and the condition that would close or revisit the item.

## Compare repayment options

| Situation | Proportionate approach |
| --- | --- |
| One confusing local path | Clarify it in the next relevant change with behavior preserved |
| Repeated expensive change across a stable boundary | A bounded refactor with a realistic change exercise |
| Unsafe or unsupported dependency blocks delivery | Confirm advisory/compatibility, then plan upgrade or replacement |
| Large legacy boundary with active consumers | Incremental replacement with routing, reconciliation and removal criteria |
| Unused code or dependency | Verify consumers and data needs before removal |

Prioritize from frequency, impact, urgency, effort and uncertainty using available
project evidence. A risk score is an estimate, not a measured financial return.
There is no universal percentage of sprint capacity to reserve; the product and
engineering owners decide the investment against current goals and capacity.

## Make the change safe and bounded

Identify the observable behavior and compatibility to preserve. Reuse relevant checks;
add a focused regression or characterization case for a risky unprotected path. Separate
intentional behavior changes from restructuring. Keep increments reviewable and stop
when the demonstrated maintenance goal is met.

For a migration, define ownership during transition, old/new consumer compatibility,
data reconciliation and a removal condition. Carry temporary duplication as an explicit
cost rather than creating an indefinite second implementation.

## Verify the claimed benefit

Exercise the same representative maintenance task before/after where practical. Report
the actual diff, checks and observed change in review effort, rework or operating cost.
A lower line count, complexity score or higher coverage alone does not establish faster
delivery or fewer incidents. Label benefits that remain estimates.

Use [practical refactoring](../../../engineering/practical-refactoring/SKILL.md) for
execution, and [project management](../../project-management/SKILL.md) for a repeated
flow bottleneck across assignments.
