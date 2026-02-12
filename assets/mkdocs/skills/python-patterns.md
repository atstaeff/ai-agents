# Python Patterns

> Idiomatische Python-Patterns, Design Patterns und Best Practices fuer produktionsreifen Python-Code.

---

## Ueberblick

Der Python Patterns Skill umfasst:

- **Design Patterns** — Strategy, Observer, Repository, Factory, Template Method
- **SOLID Principles** — Alle 5 Prinzipien mit Python Before/After Beispielen
- **Error Handling** — Custom Exceptions, Monadic Error Handling, Flask Integration
- **Modern Python** — Type Hints, Protocols, Pydantic v2, Structural Pattern Matching

## Kernthemen

### Design Patterns

| Pattern | Anwendungsfall |
|---------|---------------|
| Strategy | Austauschbare Algorithmen (z.B. Zahlungsanbieter) |
| Observer | Event-basierte Entkopplung |
| Repository | Datenzugriffabstraktion |
| Factory | Objekterstellung ohne konkrete Klassen |
| Template Method | Algorithmus-Skelett mit variabler Implementierung |

### SOLID in Python

| Prinzip | Python-Konzept |
|---------|---------------|
| Single Responsibility | Ein Modul, eine Verantwortung |
| Open/Closed | Protocols und Strategy Pattern |
| Liskov Substitution | Protocol-konforme Implementierungen |
| Interface Segregation | Kleine Protocols statt grosse ABCs |
| Dependency Inversion | Injection ueber Konstruktor, Protocol als Interface |

### Error Handling

- Custom Exception Hierarchien mit `dataclass`-artigen Exceptions
- Monadic Error Handling mit `Result`-Type
- Flask/FastAPI Error Handler Integration

## Referenz-Repository

Detaillierte Before/After Beispiele unter [`atstaeff/better-python`](https://github.com/atstaeff/better-python).

## Verwandte Agents

- :material-robot: [Python Expert](../agents/python-expert.md)
- :material-robot: [Code Reviewer](../agents/code-reviewer.md)

---

*Quelldatei: [`skills/python-patterns/SKILL.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/python-patterns/SKILL.md)*
