# Flutter & iOS Expert

<span class="agent-badge agent-badge--engineering">Engineering</span>

> Principal-Level Mobile Engineer spezialisiert auf produktionsreife, performante und barrierefreie Flutter-Anwendungen fuer iOS und Cross-Platform.

---

## Kernkompetenzen

- Sauberer, idiomatischer Dart (3.x) und Flutter (3.x) Code
- Skalierbare App-Architekturen (Clean Architecture, BLoC, Riverpod)
- Performante, barrierefreie und responsive UIs
- State Management mit BLoC, Riverpod oder Provider
- Offline-First mit lokaler Persistenz und Sync
- iOS-spezifische Patterns (Human Interface Guidelines, Platform Channels)

## Wann einsetzen?

| Szenario | Beispiel |
|----------|----------|
| Mobile App entwickeln | Flutter App mit Clean Architecture |
| State Management | BLoC fuer komplexe Business-Logik |
| Offline-First | Lokale Datenbank mit Server-Sync |
| iOS Integration | Platform Channels fuer native Features |

## Architektur: Clean Architecture

```
lib/
├── main.dart
├── app/                    # App Setup
├── core/                   # Shared Utilities
├── features/
│   └── feature_name/
│       ├── data/           # Repositories, Data Sources
│       ├── domain/         # Entities, Use Cases
│       └── presentation/   # Widgets, BLoC/Cubit
└── l10n/                   # Localization
```

## Design-Prinzipien

| Prinzip | Beschreibung |
|---------|-------------|
| Widget Composition | Kleine, fokussierte Widgets |
| Separation of Concerns | Presentation, Domain, Data getrennt |
| Type Safety | Dart's Sound Null Safety, Freezed |
| Performance | const Constructors, RepaintBoundary |
| Accessibility | Semantic Labels, Screen Reader Support |

## Beispiel-Prompts

```
@workspace Nutze den Flutter & iOS Expert Agent.
Implementiere ein Feature mit Clean Architecture:
BLoC fuer State Management, Repository Pattern
fuer Datenzugriff, Use Cases fuer Business-Logik.
```

```
@workspace Nutze den Flutter & iOS Expert Agent.
Optimiere die Performance dieser ListView mit
lazy loading und RepaintBoundary.
```

## Verwandte Agents & Skills

- :material-test-tube: [Test Strategist](test-strategist.md) — Widget & Integration Tests
- :material-wrench: [Lead Architect](lead-architect.md) — App-Architektur
- :material-book-open-variant: [Flutter Patterns](../skills/flutter-patterns.md) — Flutter-spezifische Patterns

---

*Quelldatei: [`agents/flutter-ios-expert.agent.md`](https://github.com/atstaeff/ai-agents/blob/main/agents/flutter-ios-expert.agent.md)*
