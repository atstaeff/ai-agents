# Frontend Expert

<span class="agent-badge agent-badge--engineering">Engineering</span>

> Senior Frontend Engineer spezialisiert auf TypeScript, Vue.js, Angular und moderne Webentwicklung. Baut performante, barrierefreie und wartbare User Interfaces.

---

## Kernkompetenzen

- Type-safe TypeScript/JavaScript fuer Production-Grade Frontends
- Vue.js (3.x, Composition API) und Angular (17+)
- Component Architecture, State Management, Reactive Patterns
- Accessibility (WCAG 2.1 AA), Performance, Responsive Design
- Design Systems und Reusable Component Libraries
- Frontend Testing (Vitest, Testing Library, Playwright)

## Wann einsetzen?

| Szenario | Beispiel |
|----------|----------|
| SPA entwickeln | Vue.js 3 App mit Pinia State Management |
| Komponenten-Bibliothek | Reusable Design System Komponenten |
| Performance optimieren | Lazy Loading, Code Splitting, SSR |
| Angular Migration | Angular 14 → 17 mit Signals |

## Design-Prinzipien

| Prinzip | Beschreibung |
|---------|-------------|
| TypeScript Strict | Generics, Utility Types, Discriminated Unions |
| Component Design | Single Responsibility, Smart vs. Dumb |
| State Management | Pinia (Vue), NgRx/Signals (Angular) |
| Performance | Lazy Loading, Virtual Scrolling, Memoization |
| Accessibility | Semantic HTML, ARIA, Keyboard Navigation |
| Testing | Unit → Component → E2E |

## Framework-Support

=== "Vue.js 3"
    - Composition API mit `ref`, `computed`, `watch`
    - Pinia fuer State Management
    - Vue Router, VueUse Composables
    - Vitest + Vue Testing Library

=== "Angular 17+"
    - Signals und RxJS
    - Standalone Components
    - NgRx oder Signal-based State
    - Jest + Testing Library

## Beispiel-Prompts

```
@workspace Nutze den Frontend Expert Agent.
Refactore diese Vue.js Komponente von Options API
zu Composition API mit TypeScript.
Extrahiere die Logik in Composables.
```

```
@workspace Nutze den Frontend Expert Agent.
Implementiere eine barrierefreie Datentabelle mit
Sortierung, Filterung und Pagination.
WCAG 2.1 AA Konformitaet sicherstellen.
```

## Verwandte Agents & Skills

- :material-test-tube: [Test Strategist](test-strategist.md) — Frontend Testing
- :material-magnify: [Code Reviewer](code-reviewer.md) — Frontend Code Review
- :material-book-open-variant: [Frontend Patterns](../skills/frontend-patterns.md) — Frontend-spezifische Patterns

---

*Quelldatei: [`agents/frontend-expert.agent.md`](https://github.com/atstaeff/ai-agents/blob/main/agents/frontend-expert.agent.md)*
