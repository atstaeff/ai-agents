# Verification specialist handoffs

Use the [role](../test-strategist.agent.md) for test design or a bounded verification
increment. The [testing skill](../../../skills/quality/testing/SKILL.md) owns the
procedure and its focused references own examples; keep one copy of each technique.

## Useful assignment

Supply the acceptance or reproduced fault, affected boundary, exact revision, existing
runner and fixtures, available services/devices and writable scope. A review-only task
returns findings and concrete cases without claiming to have changed or executed tests.

Return checks mapped to important criteria, actual command/results and material gaps.
Distinguish unit, contract, integration and running-user-journey evidence. Without a
runner or dependency, provide the proposed check and mark it unrun; do not replace a
required integration check with a mock and call the criterion verified.

## Choose by failure mode

| Risk | Useful evidence |
| --- | --- |
| Incorrect business rule | Small deterministic cases from a requirement or reproduced fault |
| Serialization, authentication or API mismatch | Consumer-visible request/response checks including denied and invalid input |
| Persistence or concurrent write | Real transaction, stale-write, restart or rollback behavior |
| UI state or navigation regression | The affected interaction and recovery path in a running interface |
| Device or timing behavior | Representative target, workload and measurement conditions |

Reuse established gates. Coverage reveals unexecuted code; fixed coverage percentages
or a prescribed unit/integration/end-to-end ratio do not establish acceptance. Add
checks for concrete risk and stop broadening after required evidence is sufficient.
