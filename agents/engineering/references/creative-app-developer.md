# Creative application specialist handoffs

Use the [role](../creative-app-developer.agent.md) for a bounded editing, music,
art or media-tool increment. The [creative application skill](../../../skills/engineering/creative-app-patterns/SKILL.md)
owns document, command, rendering and recovery procedures.

## Useful assignment

Supply the primary creative action, existing document format, representative media,
input devices, supported platforms and writable scope. Identify the latency or memory
budget that matters to that action and the user's expected undo/save behavior.

Return a working interaction and evidence for the affected edit, undo/redo, save/open
and interrupted-write paths. Separate measured interaction or audio timing from visual
inspection. Without representative media or runtime access, name the untested case and
provide a concrete replay; a mockup does not establish media-processing performance.

## Choose a focused boundary

- Document corruption or undo: inspect command ownership, history and persistence before
  adding a state library. Undoing an edit does not automatically reverse an exported file.
- Rendering or audio stalls: profile the critical path with realistic content; bound
  queues and allocations. Read the skill's media section for scheduling and recovery.
- Decorative motion: keep it optional and respect reduced motion; retain keyboard and
  nonvisual feedback for the core action. Add gamification only for an accepted product need.
- Export: check dimensions, format, color/audio expectations and failure cleanup against
  a real consumer. Keep original assets intact.

Use [frontend patterns](../../../skills/languages/frontend-patterns/SKILL.md) for web
interaction and [prototyping](../../../skills/engineering/prototyping/SKILL.md) when a
short experiment will resolve the creative or technical uncertainty.
