````markdown
# Game Architecture Patterns

Architektur-Patterns fuer die Strukturierung von Game-Projekten: ECS, Event-Driven, Scene Management und mehr.

## Inhalt

- **Entity-Component-System (ECS)** — Daten von Logik trennen
- **Event Bus** — Signal-basierte Entkopplung von Game Systems
- **Game Loop** — Fixed + Variable Timestep
- **Scene/State Management** — Lifecycle Hooks, Transitions, Scene Stacking
- **Save/Load System** — Versionierung, Slots, Migration
- **Asset Management** — Zentraler Loader mit Progress Tracking

## ECS vs. Vererbung

| Ansatz | Pro | Contra |
|--------|-----|--------|
| **ECS** | Flexibel, performant, composable | Mehr Boilerplate |
| **Vererbung** | Einfach fuer kleine Projekte | Diamant-Problem, rigide |

## Quelle

:material-file-document: [`skills/game-development/game-architecture.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/game-development/game-architecture.md)
````
