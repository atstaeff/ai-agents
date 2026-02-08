# Python Golden Repository

This directory contains the reference structure for a production-grade Python project.

## Structure

```
python-golden/
├── src/
│   ├── __init__.py
│   ├── domain/
│   │   ├── __init__.py
│   │   ├── models.py         # Pydantic models, entities, value objects
│   │   ├── events.py         # Domain events
│   │   ├── services.py       # Domain services
│   │   └── exceptions.py     # Domain-specific exceptions
│   ├── application/
│   │   ├── __init__.py
│   │   ├── commands.py       # Command handlers (write)
│   │   ├── queries.py        # Query handlers (read)
│   │   └── ports.py          # Interfaces (Protocols)
│   ├── infrastructure/
│   │   ├── __init__.py
│   │   ├── database.py       # DB setup, session factory
│   │   ├── repositories.py   # Repository implementations
│   │   └── event_bus.py      # Event bus implementation
│   ├── api/
│   │   ├── __init__.py
│   │   ├── main.py           # FastAPI application
│   │   ├── routes/           # Route modules
│   │   ├── schemas.py        # Request/response schemas
│   │   └── dependencies.py   # FastAPI DI
│   └── config.py             # Pydantic Settings
├── tests/
│   ├── conftest.py           # Shared fixtures
│   ├── factories.py          # Test data factories
│   ├── fakes.py              # Fake implementations
│   ├── unit/
│   │   ├── conftest.py
│   │   └── test_*.py
│   ├── integration/
│   │   ├── conftest.py
│   │   └── test_*.py
│   └── e2e/
│       └── test_*.py
├── pyproject.toml
├── Dockerfile
├── Makefile
├── README.md
└── .github/
    └── workflows/
        └── ci.yml
```

## Key Principles

1. **Hexagonal Architecture** — Domain at the center, infrastructure at the edges
2. **Dependency Injection** — All dependencies injected via constructors
3. **Protocol-Based Interfaces** — Structural subtyping for testability
4. **Pydantic Models** — Type-safe domain models with validation
5. **Async First** — Async I/O throughout (FastAPI, asyncio, httpx)
6. **Test-Driven** — Fakes > Mocks, factories for test data

## Design Patterns Reference

For concrete before/after Python examples of design patterns, see [`atstaeff/better-python`](https://github.com/atstaeff/better-python):

| Folder | Pattern |
|--------|---------|
| `1 - coupling and cohesion` | High cohesion, low coupling refactoring |
| `2 - dependency inversion` | ABC-based abstractions (`Switchable`) |
| `3 - strategy pattern` | Class-based & functional (`Callable`) strategies |
| `4 - observer pattern` | Event-based decoupling with listener setup |
| `5 - unit testing` | pytest-based testing examples |
| `6 - template method & bridge` | Algorithm skeleton + Bridge pattern |
| `7 - dealing with errors` | Custom exceptions, Flask, monadic (`returns`) |
| `8 - mvc` | Model-View-Controller with Strategy variant |
| `9 - solid` | All 5 SOLID principles, before/after |
| `10 - object creation` | Object Pool + context manager |

## Tooling

| Tool | Purpose | Config |
|------|---------|--------|
| `uv` | Package management | `pyproject.toml` |
| `ruff` | Linting & formatting | `pyproject.toml` |
| `mypy` | Type checking | `pyproject.toml` |
| `pytest` | Testing | `pyproject.toml` |
| `pre-commit` | Git hooks | `.pre-commit-config.yaml` |

## Getting Started

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Lint & format
uv run ruff check . --fix
uv run ruff format .

# Type check
uv run mypy src/

# Run locally
uv run uvicorn src.api.main:app --reload
```
