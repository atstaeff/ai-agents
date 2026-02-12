# Frontend Patterns

> TypeScript, Vue.js, Angular und moderne Web-Development Patterns fuer performante, barrierefreie Frontends.

---

## Ueberblick

Der Frontend Patterns Skill umfasst:

- **Component Architecture** — Composition, Smart/Dumb Components
- **State Management** — Pinia, NgRx, Signals
- **TypeScript Patterns** — Generics, Utility Types, Type Guards
- **Performance** — Lazy Loading, Code Splitting, SSR
- **Accessibility** — WCAG 2.1 AA, ARIA, Keyboard Navigation

## Kernthemen

### Component Patterns

| Pattern | Beschreibung |
|---------|-------------|
| Smart/Dumb | Container (Logik) vs. Presentational (UI) |
| Composables (Vue) | Wiederverwendbare Logik extrahieren |
| Render Props | Flexible Rendering-Delegation |
| Compound Components | Zusammengehoerige Komponenten-Gruppen |

### Framework-spezifisch

=== "Vue.js 3"
    - Composition API (`ref`, `computed`, `watch`)
    - Pinia Store Pattern
    - VueUse Composables
    - Dynamic Components

=== "Angular 17+"
    - Signals und RxJS
    - Standalone Components
    - Control Flow (`@if`, `@for`)
    - Dependency Injection

### Performance-Checkliste

- [x] Lazy Loading fuer Routes und Heavy Components
- [x] Code Splitting mit Dynamic Imports
- [x] Virtual Scrolling fuer grosse Listen
- [x] Image Optimization (WebP, responsive, lazy)
- [x] Memoization wo sinnvoll

## Verwandte Agents

- :material-robot: [Frontend Expert](../agents/frontend-expert.md)
- :material-robot: [Code Reviewer](../agents/code-reviewer.md)

---

*Quelldatei: [`skills/frontend-patterns/SKILL.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/frontend-patterns/SKILL.md)*
