# Flutter Patterns

> Flutter/Dart Patterns, Widget Composition, State Management und Clean Architecture fuer produktionsreife Mobile Apps.

---

## Ueberblick

Der Flutter Patterns Skill umfasst:

- **Widget Composition** — Kleine, fokussierte Widgets
- **State Management** — BLoC, Riverpod, Provider
- **Clean Architecture** — Presentation, Domain, Data Layer
- **Navigation** — GoRouter, Deep Linking
- **Testing** — Widget Tests, BLoC Tests, Integration Tests

## Kernthemen

### Architektur-Patterns

| Pattern | Anwendungsfall |
|---------|---------------|
| Clean Architecture | Feature-basierte Schichtentrennung |
| BLoC Pattern | Komplexe Zustandsverwaltung |
| Repository Pattern | Datenzugriff abstrahieren |
| Use Cases | Business-Logik kapseln |

### State Management

| Loesung | Wann verwenden |
|---------|---------------|
| BLoC/Cubit | Komplexe Business-Logik, Events |
| Riverpod | DI-zentrische Apps, einfache States |
| Provider | Einfache Apps, wenig Zustand |

### Performance

- `const` Constructors fuer statische Widgets
- `RepaintBoundary` fuer isolierte Widget-Bereiche
- Lazy Loading mit `ListView.builder`
- Image Caching und Optimierung

## Verwandte Agents

- :material-robot: [Flutter & iOS Expert](../agents/flutter-ios-expert.md)
- :material-robot: [Test Strategist](../agents/test-strategist.md)

---

*Quelldatei: [`skills/flutter-patterns/SKILL.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/flutter-patterns/SKILL.md)*
