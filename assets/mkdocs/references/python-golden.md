# Python Golden Repository

> Referenzstruktur fuer ein produktionsreifes Python-Projekt mit Clean Architecture, FastAPI, SQLAlchemy und pytest.

---

## Projektstruktur

```
python-golden/
├── src/
│   ├── domain/              # Domain Layer
│   │   ├── models.py        # Pydantic Models, Entities, Value Objects
│   │   ├── events.py        # Domain Events
│   │   ├── services.py      # Domain Services
│   │   └── exceptions.py    # Domain-spezifische Exceptions
│   ├── application/         # Application Layer
│   │   ├── commands.py      # Command Handlers (Write)
│   │   ├── queries.py       # Query Handlers (Read)
│   │   └── ports.py         # Interfaces (Protocols)
│   ├── infrastructure/      # Infrastructure Layer
│   │   ├── database.py      # DB Setup, Session Factory
│   │   ├── repositories.py  # Repository Implementations
│   │   └── event_bus.py     # Event Bus Implementation
│   └── api/                 # API Layer
│       ├── main.py          # FastAPI Application
│       ├── routes/          # Route Modules
│       ├── dependencies.py  # FastAPI Dependencies (DI)
│       └── middleware.py    # Error Handling, Logging
├── tests/
│   ├── unit/               # Unit Tests
│   ├── integration/        # Integration Tests
│   └── conftest.py         # Shared Fixtures
├── pyproject.toml
├── Dockerfile
└── docker-compose.yml
```

## Architektur-Prinzipien

| Prinzip | Implementierung |
|---------|----------------|
| Clean Architecture | Domain → Application → Infrastructure → API |
| Dependency Inversion | Protocols als Interfaces in `ports.py` |
| CQRS Light | Commands (Write) und Queries (Read) getrennt |
| Domain Events | Event Bus fuer lose Kopplung |
| Testbarkeit | DI ueberall, keine harten Abhaengigkeiten |

## Tech Stack

| Komponente | Technologie |
|------------|------------|
| Framework | FastAPI |
| ORM | SQLAlchemy 2.0 |
| Validation | Pydantic v2 |
| Testing | pytest + pytest-asyncio |
| Linting | ruff |
| Type Checking | mypy |
| Container | Docker + docker-compose |

## Verwandte Agents

- :material-robot: [Python Expert](../agents/python-expert.md) — Nutzt diese Struktur als Referenz
- :material-robot: [Lead Architect](../agents/lead-architect.md) — Architekturentscheidungen

---

*Quelldatei: [`reference-repos/python-golden/README.md`](https://github.com/atstaeff/ai-agents/blob/main/reference-repos/python-golden/README.md)*
