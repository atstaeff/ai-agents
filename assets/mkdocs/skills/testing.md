# Testing Patterns

> Testing Patterns, Test Fixtures, Mocking, Faking und testbare Architektur.

---

## Test-Patterns

### Arrange-Act-Assert (AAA)

Jeder Test folgt dem gleichen Aufbau: Setup, Ausfuehrung, Verifikation.

### Test Doubles

| Double | Zweck |
|--------|-------|
| Stub | Vordefinierte Antworten liefern |
| Mock | Interaktionen verifizieren |
| Fake | Funktionierende Implementierung (in-memory DB) |
| Spy | Aufrufe aufzeichnen, echte Implementierung nutzen |

### Fixture Patterns

| Pattern | Beschreibung |
|---------|-------------|
| Factory | Testdaten ueber Factories erzeugen |
| Builder | Komplexe Testobjekte schrittweise aufbauen |
| Mother | Benannte Presets fuer haeufige Szenarien |

## Testbarkeit sicherstellen

- Dependency Injection ueber Konstruktor
- Interfaces/Protocols fuer externe Abhaengigkeiten
- Pure Functions bevorzugen
- Side Effects isolieren
- Deterministische Daten (fixe Timestamps, Seeds)

## Sprachspezifisch

=== "Python"
    - `pytest` mit Fixtures und Parametrize
    - `unittest.mock` / `pytest-mock`
    - `factory_boy` fuer Test Factories
    - `hypothesis` fuer Property-Based Testing

=== "Go"
    - Table-Driven Tests
    - `testify` fuer Assertions
    - Interface-basiertes Mocking
    - `httptest` fuer HTTP Tests

=== "TypeScript"
    - Vitest / Jest mit `describe` / `it`
    - Testing Library fuer Komponenten
    - MSW fuer API Mocking
    - Playwright fuer E2E

## Verwandte Skills

- [Testing Strategies](testing-strategies.md) — Strategieebene
- [Clean Code](clean-code.md) — Testbarer Code

---

*Quelldatei: [`skills/testing/SKILL.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/testing/SKILL.md)*
