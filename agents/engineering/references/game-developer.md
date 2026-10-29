# Game specialist handoffs

Use the [role](../game-developer.agent.md) for one playable increment. Keep engine and
framework conventions from the actual project; a new game does not require an ECS,
global event bus, object pool or separate abstraction around every engine API.

## Useful assignment

Supply the player action, expected feedback, existing engine/version, target platform,
input devices, representative scene and writable scope. Name the measurable timing or
resource constraint and the playtest question. Retain a replay or deterministic seed
when it helps reproduce a defect.

Return a playable change, relevant rule/transition checks and observed playtest results.
State which build, device and performance checks actually ran. Without an engine or
target device, return the reviewable code and a concrete replay; desktop tests cannot
establish console, mobile or controller behavior.

## Choose one procedure

- [Game design](../../../skills/engineering/game-design/SKILL.md): player goals, core
  loop, balance or evidence from playtesting.
- [Game mechanics](../../../skills/engineering/game-mechanics/SKILL.md): movement,
  combat, inventory, pathfinding or another specific rule.
- [Game architecture](../../../skills/engineering/game-architecture/SKILL.md): update
  order, ownership, scene lifecycle, persistence or engine boundaries.
- [Prototyping](../../../skills/engineering/prototyping/SKILL.md): an isolated experiment
  with a time budget, observation and disposal decision.

For a frame-time issue, measure the representative scene before pooling or partitioning.
Check pause/resume, scene replacement and save/load when those transitions affect the
increment; avoid adding unrelated polish or progression systems.
