# Python specialist handoffs

The [role](../python-expert.agent.md) owns a bounded Python change or review.
Use the [Python skill](../../../skills/languages/python-patterns/SKILL.md) for procedure;
read its [FastAPI section](../../../skills/languages/python-patterns/references/guide.md#fastapi-boundaries)
only for HTTP/dependency/async uncertainty. Shared examples live with the skill.

A useful handoff identifies the failing behavior, supported Python versions, affected
contract, writable files and expected evidence. Return the changed behavior and checks;
flag a transaction or compatibility decision for its accountable owner.

For a teaching request, [better-python](https://github.com/atstaeff/better-python)
can supply a concrete before/after example. Preserve the project's conventions and
explain why that boundary helps the specific change.

Load [testing](../../../skills/quality/testing/SKILL.md) for verification design,
[design patterns](../../../skills/engineering/design-patterns/SKILL.md) or
[clean code](../../../skills/engineering/clean-code/SKILL.md) for an actual refactoring
question, and [GCP](../../../skills/engineering/gcp-patterns/SKILL.md) for runtime concerns.
