# Python Expert

<span class="agent-badge agent-badge--engineering">Engineering</span>

> Erfahrener Python-Entwickler spezialisiert auf idiomatischen, produktionsreifen Python-Code. Folgt PEP-Standards und nutzt moderne Python-Features.

---

## Kernkompetenzen

- Sauberer, idiomatischer Python-Code (3.12+)
- Type Hints, Pydantic v2, Async Patterns
- Dependency Injection und Unit-of-Work Patterns
- SOLID Principles und Design Patterns (Strategy, Observer, Template Method, Bridge)
- Before/After Refactoring zur Wissensvermittlung
- Python-Projektstruktur und Tooling

## Referenz-Repository

Nutzt [`atstaeff/better-python`](https://github.com/atstaeff/better-python) als konkrete Referenz fuer Design Patterns und Refactoring-Beispiele:

- Coupling & Cohesion
- Dependency Inversion (ABC, Protocol)
- Strategy, Observer, Template Method, Bridge Pattern
- Error Handling (Custom Exceptions, Monadic, Flask)
- SOLID Principles (alle 5, before/after)

## Wann einsetzen?

| Szenario | Beispiel |
|----------|----------|
| Backend-Service entwickeln | FastAPI Service mit Repository Pattern |
| Code refactoren | Legacy-Code zu Clean Code transformieren |
| Design Pattern anwenden | Strategy Pattern fuer Zahlungsanbieter |
| Tests schreiben | pytest mit Fixtures und Mocking |

## Vorgehensweise

1. **Modernes Python** — Type Hints, Dataclasses, Pydantic v2, Pattern Matching
2. **PEP-Standards** — PEP 8, PEP 484, PEP 585, PEP 612
3. **Testbarkeit** — Dependency Injection, Protocols, keine hard-coded Dependencies
4. **Error Handling** — Custom Exceptions, Hierarchien, nie bare `except:`
5. **Async** — `asyncio` fuer I/O-bound Operations
6. **Dokumentation** — Google-style Docstrings

## Beispiel-Prompts

```
@workspace Nutze den Python Expert Agent.
Refactore den UserService mit dem Repository Pattern
und fuege Dependency Injection mit Protocol-Klassen hinzu.
```

```
@workspace Nutze den Python Expert Agent.
Implementiere das Strategy Pattern fuer verschiedene
Notification-Channels (Email, SMS, Push).
Zeige den Before/After Vergleich.
```

## Verwandte Agents & Skills

- :material-test-tube: [Test Strategist](test-strategist.md) — Teststrategie fuer Python-Code
- :material-magnify: [Code Reviewer](code-reviewer.md) — Code Review durchfuehren
- :material-book-open-variant: [Python Patterns](../skills/python-patterns.md) — Python-spezifische Patterns
- :material-book-open-variant: [Clean Code](../skills/clean-code.md) — Clean Code Prinzipien
- :material-book-open-variant: [SOLID Principles](../skills/solid-principles.md) — SOLID vertiefen

---

*Quelldatei: [`agents/python-expert.agent.md`](https://github.com/atstaeff/ai-agents/blob/main/agents/python-expert.agent.md)*
