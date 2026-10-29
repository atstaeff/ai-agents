# Delivery flow examples

Read the relevant section for an observed coordination problem. Preserve the project's
chosen work system and cadence; Scrum, Kanban, story points and scaling frameworks are
options rather than prerequisites for delivery.

## Slice and pull work

A useful increment has an outcome, observable acceptance, accountable owner and a
bounded change that can be reviewed. Split by a usable behavior or risk reduction;
separate technical layers only when their contracts and integration owner are clear.
Avoid opening many partially built slices that all wait for the same reviewer.

For a blocked assignment, retain its actual flow position, blocker, owner and next
unblock action. A blocker does not make the work delivered or free its review capacity.
Pull independent ready work within the team's real capacity instead of hiding blocked WIP.

## Choose a signal for the bottleneck

| Observed problem | Useful signal | Possible change to evaluate |
| --- | --- | --- |
| Work waits for review | Queue age and review turnaround | Smaller increments or protected review capacity |
| Many items start, few finish | WIP, cycle time and blocked age | Reduce concurrent starts and finish the oldest useful work |
| Integration repeatedly reopens work | Rework and contract failures | Agree shared interfaces and integrate complete slices earlier |
| Release batches grow | Time from accepted revision to release | Identify the real approval, automation or compatibility constraint |
| Scope frequently changes | Reopened criteria and decision delay | Resolve the uncertainty before committing the next slice |

Use comparable work, a stated time boundary and actual observations. Throughput and
cycle time describe flow; story points and model speed do not directly measure product
value, individual productivity or reliable delivery dates.

## Forecast without invented precision

Inspect dependencies, available capacity and historical variability. Separate a target
from a forecast and label assumptions. Update when scope, availability or a material
technical uncertainty changes. Treat an estimate as a decision input, not a commitment
made on behalf of another person. Avoid comparing teams by story points or velocity.

## Coordinate only the needed cadence

An existing planning/review meeting may already own priority and acceptance. Use an
async update when it resolves the decision. Add a ceremony only for an unmet coordination
need, with a useful input, decision owner and output; do not adopt a framework checklist
for a small assignment.

At the real review boundary, link accepted outcomes and evidence, unresolved work and
one useful process change to observe. Keep completed, integrated, deployed, cancelled
and duplicate outcomes distinct. Retain significant decisions at their existing homes.

For one assignment's progress or handoff use
[work management](../../work-management/SKILL.md); for a concrete maintenance investment,
use [technical debt](../../technical-debt/SKILL.md).
