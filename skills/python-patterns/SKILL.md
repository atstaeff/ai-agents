# Python Patterns Skill

## Instructions for AI

Apply idiomatic Python patterns, modern best practices, and production-grade code standards. Use this skill when writing, reviewing, or refactoring Python code.

Reference: [`atstaeff/better-python`](https://github.com/atstaeff/better-python) for concrete before/after examples of all patterns below.

## Core Patterns

### 1. Repository Pattern

Abstraction over data access, enabling testability and swappable backends.

```python
from typing import Protocol
from uuid import UUID

class Repository[T](Protocol):
    async def get(self, id: UUID) -> T | None: ...
    async def save(self, entity: T) -> None: ...
    async def delete(self, id: UUID) -> None: ...
    async def list_all(self) -> list[T]: ...
```

### 2. Service Layer Pattern

Business logic encapsulated in services with injected dependencies.

```python
class OrderService:
    def __init__(self, repo: OrderRepository, events: EventBus) -> None:
        self._repo = repo
        self._events = events

    async def place_order(self, command: PlaceOrderCommand) -> Order:
        order = Order.create(command)
        await self._repo.save(order)
        await self._events.publish(OrderPlaced(order_id=order.id))
        return order
```

### 3. Domain Events

Decouple side effects from business logic.

```python
from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

@dataclass(frozen=True)
class DomainEvent:
    occurred_at: datetime = field(default_factory=datetime.utcnow)

@dataclass(frozen=True)
class OrderPlaced(DomainEvent):
    order_id: UUID
    customer_id: UUID
    total_amount: float
```

### 4. Result Pattern (Error Handling)

Explicit success/failure without exceptions for expected cases.

```python
from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")
E = TypeVar("E")

@dataclass(frozen=True)
class Ok(Generic[T]):
    value: T

@dataclass(frozen=True)
class Err(Generic[E]):
    error: E

type Result[T, E] = Ok[T] | Err[E]

# Usage
def divide(a: float, b: float) -> Result[float, str]:
    if b == 0:
        return Err("Division by zero")
    return Ok(a / b)
```

### 5. Configuration with Pydantic Settings

```python
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    database_url: str
    redis_url: str = "redis://localhost:6379"
    debug: bool = False
    log_level: str = "INFO"

    model_config = {"env_file": ".env", "env_prefix": "APP_"}

@lru_cache
def get_settings() -> Settings:
    return Settings()
```

### 6. Strategy Pattern (Functional)

Replace string-flag branching with callable strategies.

```python
from dataclasses import dataclass, field
from typing import Callable

@dataclass
class SupportTicket:
    id: str = field(init=False, default_factory=generate_id)
    customer: str
    issue: str

type Ordering = Callable[[list[SupportTicket]], list[SupportTicket]]

def fifo_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:
    return tickets.copy()

def filo_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:
    return list(reversed(tickets))

def random_ordering(tickets: list[SupportTicket]) -> list[SupportTicket]:
    return random.sample(tickets, len(tickets))

class CustomerSupport:
    def __init__(self) -> None:
        self.tickets: list[SupportTicket] = []

    def create_ticket(self, customer: str, issue: str) -> None:
        self.tickets.append(SupportTicket(customer=customer, issue=issue))

    def process_tickets(self, ordering: Ordering) -> None:
        for ticket in ordering(self.tickets):
            self._process_ticket(ticket)
```

### 7. Observer Pattern (Events)

Decouple side effects from core business logic via events.

```python
from collections import defaultdict
from typing import Callable, Any

subscribers: dict[str, list[Callable]] = defaultdict(list)

def subscribe(event_type: str, handler: Callable) -> None:
    subscribers[event_type].append(handler)

def post_event(event_type: str, data: Any) -> None:
    for handler in subscribers[event_type]:
        handler(data)

# Business logic stays clean:
def register_new_user(name: str, password: str, email: str):
    user = create_user(name, password, email)
    post_event("user_registered", user)

# Listeners wired up separately:
def setup_email_handlers():
    subscribe("user_registered", lambda u: send_welcome_email(u))

def setup_slack_handlers():
    subscribe("user_registered", lambda u: notify_sales(u))
```

### 8. Template Method Pattern

Define algorithm skeleton in base class, let subclasses override specific steps.

```python
from abc import ABC, abstractmethod

class TradingBot(ABC):
    def check_prices(self, coin: str) -> None:
        self.connect()
        prices = self.get_market_data(coin)
        if self.should_buy(prices):
            print(f"Buy {coin}!")
        elif self.should_sell(prices):
            print(f"Sell {coin}!")

    def connect(self) -> None:
        print("Connecting to exchange...")

    def get_market_data(self, coin: str) -> list[float]:
        return [10, 12, 18, 14]

    @abstractmethod
    def should_buy(self, prices: list[float]) -> bool: ...

    @abstractmethod
    def should_sell(self, prices: list[float]) -> bool: ...

class AverageTrader(TradingBot):
    def should_buy(self, prices: list[float]) -> bool:
        return prices[-1] < sum(prices) / len(prices)

    def should_sell(self, prices: list[float]) -> bool:
        return prices[-1] > sum(prices) / len(prices)
```

### 9. Error Handling — Custom Exceptions

Use domain-specific exceptions, never generic `Exception`.

```python
class NotFoundError(Exception):
    pass

class NotAuthorizedError(Exception):
    pass

def fetch_blog(blog_id: str) -> dict:
    blog = db_fetch(blog_id)
    if blog is None:
        raise NotFoundError(f"Blog {blog_id} not found")
    if not blog["public"]:
        raise NotAuthorizedError(f"Blog {blog_id} is private")
    return blog

# Flask: Map domain exceptions to HTTP status codes
@app.route("/blogs/<id>")
def get_blog(id: str):
    try:
        return jsonify(fetch_blog(id))
    except NotFoundError:
        abort(404, description="Resource not found")
    except NotAuthorizedError:
        abort(403, description="Access denied")
```

### 10. Coupling & Cohesion

Separate data, registration logic, and application orchestration.

```python
# ✅ GOOD: Each class has a single, clear responsibility
@dataclass
class VehicleInfo:
    brand: str
    electric: bool
    catalogue_price: int

    def compute_tax(self) -> float:
        rate = 0.02 if self.electric else 0.05
        return rate * self.catalogue_price

@dataclass
class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

class VehicleRegistry:
    def __init__(self) -> None:
        self.vehicle_info: dict[str, VehicleInfo] = {}

    def add_vehicle_info(self, brand: str, info: VehicleInfo) -> None:
        self.vehicle_info[brand] = info

    def generate_vehicle_id(self, length: int) -> str:
        return "".join(random.choices(string.ascii_uppercase, k=length))

class Application:
    def __init__(self, registry: VehicleRegistry) -> None:
        self.registry = registry

    def register_vehicle(self, brand: str) -> Vehicle:
        info = self.registry.vehicle_info[brand]
        vehicle_id = self.registry.generate_vehicle_id(12)
        license_plate = vehicle_id[:2] + "-" + "".join(random.choices(string.digits, k=4))
        return Vehicle(id=vehicle_id, license_plate=license_plate, info=info)
```

## Project Structure (Golden Repo)

```
src/
├── __init__.py
├── domain/
│   ├── __init__.py
│   ├── models.py        # Pydantic models, entities
│   ├── events.py        # Domain events
│   ├── services.py      # Domain services
│   └── exceptions.py    # Domain-specific exceptions
├── application/
│   ├── __init__.py
│   ├── commands.py      # Command handlers
│   ├── queries.py       # Query handlers
│   └── ports.py         # Abstract interfaces (Protocols)
├── infrastructure/
│   ├── __init__.py
│   ├── database.py      # Database setup & session
│   ├── repositories.py  # Repository implementations
│   └── event_bus.py     # Event bus implementation
├── api/
│   ├── __init__.py
│   ├── main.py          # FastAPI app
│   ├── routes/          # API route modules
│   ├── schemas.py       # API request/response models
│   └── dependencies.py  # FastAPI dependency injection
└── config.py            # Settings
```

## Best Practices

✅ Use `from __future__ import annotations` for PEP 604 syntax
✅ Prefer composition over inheritance
✅ Use `Protocol` for dependency interfaces (structural subtyping)
✅ Keep functions pure where possible
✅ Use `@dataclass(frozen=True)` for immutable value objects
✅ Apply the "Tell, Don't Ask" principle
✅ Use `match` statements for complex branching (Python 3.10+)

## Anti-Patterns

❌ God objects that do everything
❌ Circular imports between modules
❌ Business logic in API routes
❌ Hard-coded configuration values
❌ Using `dict` instead of typed models
❌ Catching exceptions too broadly
❌ String flags for strategy selection (`if mode == "fifo"`) — use callable/Protocol
❌ Side effects coupled to business logic (email in registration) — use events
❌ Hardcoded dependencies — inject via constructor
❌ Generic `Exception` in API layer — use domain-specific exception hierarchy

## Example Prompts

- "Refactor this code to use the repository pattern with dependency injection"
- "Create a domain model with Pydantic for a booking system"
- "Implement the Result pattern for error handling in this service"

## Related Skills

- [Clean Code](../software-engineering/clean-code.md)
- [SOLID Principles](../software-engineering/solid-principles.md)
- [Design Patterns](../software-engineering/design-patterns.md)
- [Reference: better-python](https://github.com/atstaeff/better-python)
