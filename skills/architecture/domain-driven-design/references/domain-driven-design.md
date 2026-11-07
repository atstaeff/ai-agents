# Background examples

Use focused sections only when needed. The current skill entry, project conventions and user constraints govern the work. Examples illustrate particular choices; they do not mandate a framework, test library or architecture.

# Domain-Driven Design (DDD)

## Instructions for AI

Apply Domain-Driven Design principles to model complex business domains:

## Strategic Design

### Ubiquitous Language
- Develop common language between developers and domain experts
- Use domain terminology in code (class names, methods, variables)
- Avoid technical jargon in business logic
- Keep language consistent across team and documentation

### Bounded Contexts
- Define explicit boundaries for models
- Each context has its own model and ubiquitous language
- Different contexts can have different models for same concept
- Example: "Customer" in Sales context vs Support context

### Context Mapping
- Define relationships between bounded contexts
- **Shared Kernel**: Shared code/database between teams
- **Customer/Supplier**: Downstream depends on upstream
- **Conformist**: Downstream conforms to upstream model
- **Anti-Corruption Layer**: Translate between contexts
- **Open Host Service**: Published API for multiple consumers
- **Separate Ways**: No integration, duplicate functionality

## Tactical Design

### Entities
- Objects with unique identity
- Identity persists across state changes
- Example: User, Order, Product (with ID)

The Python examples here assume a project that already uses Pydantic. Use the
project's existing model conventions; no new dependency is required for DDD.

```python
# Python — Entity with Pydantic
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class Order(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    status: OrderStatus = OrderStatus.DRAFT
    lines: list[OrderLine] = Field(default_factory=list)

    def add_line(self, product_id: UUID, quantity: int, unit_price: Decimal) -> None:
        if self.status != OrderStatus.DRAFT:
            raise OrderFrozenError(self.id)
        self.lines.append(OrderLine(product_id=product_id, quantity=quantity, unit_price=unit_price))

    @property
    def total(self) -> Decimal:
        return sum((line.subtotal for line in self.lines), Decimal(0))
```

```go
// Go — Entity with domain methods
type Order struct {
	ID     uuid.UUID
	Status OrderStatus
	Lines  []OrderLine
}

func (o *Order) AddLine(productID uuid.UUID, qty int, price decimal.Decimal) error {
	if o.Status != StatusDraft {
		return fmt.Errorf("order %s is frozen: %w", o.ID, ErrOrderFrozen)
	}
	o.Lines = append(o.Lines, OrderLine{ProductID: productID, Quantity: qty, UnitPrice: price})
	return nil
}
```

### Value Objects
- Immutable objects defined by attributes
- No identity, only values matter
- Examples: Money, Address, DateRange

```python
# Python — Immutable Value Object with frozen Pydantic model
class Money(BaseModel, frozen=True):
    amount: Decimal
    currency: str = "EUR"

    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise CurrencyMismatchError(self.currency, other.currency)
        return Money(amount=self.amount + other.amount, currency=self.currency)
```

```go
// Go — Value Object (immutable by convention)
type Money struct {
	Amount   decimal.Decimal
	Currency string
}

func (m Money) Add(other Money) (Money, error) {
	if m.Currency != other.Currency {
		return Money{}, fmt.Errorf("currency mismatch: %s vs %s", m.Currency, other.Currency)
	}
	return Money{Amount: m.Amount.Add(other.Amount), Currency: m.Currency}, nil
}
```

### Aggregates
- Cluster of entities and value objects
- One entity is the aggregate root
- External objects hold references only to root
- Enforce business invariants
- Transaction boundary

```python
# Python — Order as aggregate root
class Order(BaseModel):
    lines: list[OrderLine] = Field(default_factory=list)

    def place(self) -> OrderPlacedEvent:
        if not self.lines:
            raise EmptyOrderError(self.id)
        self.status = OrderStatus.PLACED
        return OrderPlacedEvent(order_id=self.id, total=self.total)
```

### Repositories
- Abstraction for data access
- Introduce a repository where it gives an aggregate a useful persistence boundary.
- Keep its operations focused on what actual consumers need.

```python
# Python — Repository protocol
class OrderRepository(Protocol):
    async def find_by_id(self, order_id: UUID) -> Order | None: ...
    async def save(self, order: Order) -> None: ...
```

```go
// Go — Repository interface
type OrderRepository interface {
	FindByID(ctx context.Context, id uuid.UUID) (Order, error)
	Save(ctx context.Context, order Order) error
}
```

```
interface IOrderRepository {
    Order GetById(OrderId id);
    void Save(Order order);
    List<Order> FindByCustomer(CustomerId customerId);
}
```

### Domain Services
- Operations that don't belong to any entity
- Stateless operations
- Coordinate between aggregates

### Domain Events
- Something significant that happened in domain
- Immutable, past tense naming
- Enable decoupling and eventual consistency

```python
# Python — Domain Event with Pydantic
class OrderPlacedEvent(BaseModel, frozen=True):
    order_id: UUID
    total: Decimal
    occurred_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
```

```go
// Go — Domain Event
type OrderPlacedEvent struct {
	OrderID    uuid.UUID       `json:"order_id"`
	Total      decimal.Decimal `json:"total"`
	OccurredAt time.Time       `json:"occurred_at"`
}
```

### Factories
- Create complex aggregates
- Encapsulate creation logic
- Ensure invariants from creation

### Specifications
- Encapsulate business rules for querying
- Reusable selection criteria
- Combine specifications with AND/OR

## Layers Architecture

### Presentation Layer
- UI, REST APIs, GraphQL endpoints
- Thin layer, delegates to application layer
- Handles serialization and HTTP concerns

### Application Layer
- Use cases and application workflows
- Orchestrates domain objects
- Transaction boundaries
- Thin layer, no business logic

### Domain Layer
- Business logic and rules
- Entities, value objects, aggregates
- Domain services and events
- Independent of infrastructure

### Infrastructure Layer
- Persistence (repositories implementation)
- External services
- Message queues
- Framework-specific code

## Best Practices

### Anemic vs Rich Domain Model
Keep invariants with the data they protect. A simple value and a focused function
can express a rule without a service or class hierarchy.

### Aggregate Design Rules
- Keep aggregates small
- Prefer stable identities across ownership boundaries.
- Let consistency requirements define the transaction boundary. Use eventual
  consistency only where the business accepts it and failure can be recovered.

### Value Object Usage
- Use for money, dates, measurements
- Make immutable
- Implement equality by value
- No side effects in methods

### Domain Events Usage
Name events after something that happened (`OrderPlaced`, `PaymentProcessed`). An
in-process event does not need a broker. When a committed write must reach another
system, persist the intent with the write or define an equivalent recovery mechanism.
Publishing after commit alone can lose the event if the process exits between them.
See [durable workflows](../../../architecture/microservices/references/microservices.md#durable-workflows).

## Common Patterns

### Specification Pattern
```python
class Specification(Protocol[T]):
    def is_satisfied_by(self, entity: T) -> bool: ...

class ActiveOrderSpec:
    def is_satisfied_by(self, order: Order) -> bool:
        return order.status == OrderStatus.ACTIVE
```

### Repository Pattern
```python
class Repository(Protocol[T]):
    async def find_by_id(self, id: UUID) -> T | None: ...
    async def save(self, aggregate: T) -> None: ...
    async def delete(self, aggregate: T) -> None: ...
```

### Unit of Work Pattern
```python
class UnitOfWork(Protocol):
    async def __aenter__(self) -> "UnitOfWork": ...
    async def __aexit__(self, *args: Any) -> None: ...
    async def commit(self) -> None: ...
    async def rollback(self) -> None: ...
```

## DDD with Modern Architecture

### DDD + Microservices
A bounded context can be a module. Split deployment only for a concrete ownership,
scaling or reliability need; choose communication according to the contract.

### DDD + CQRS
- Separate read and write models
- Commands modify aggregates
- Queries use optimized read models
- Event sourcing is a separate choice; CQRS can use ordinary persistence.

### DDD + Event Sourcing
- Store events instead of current state
- Reconstruct state by replaying events
- Complete audit trail
- Temporal queries

## Anti-Patterns

❌ Invariants duplicated across callers or bypassed by direct writes
❌ Aggregates too large
❌ Cross-boundary writes with unclear ownership or consistency
❌ Ignoring ubiquitous language
❌ One model for entire system

## Example Prompts

"Model an order management system using DDD tactical patterns"

"Design bounded contexts for a banking system"

"Implement an aggregate with business invariants"

"Create domain events for an e-commerce checkout process"

"Refactor this anemic model to a rich domain model"

## Related Skills & Agents

- [Lead Architect Agent](../../../../agents/architecture/lead-architect.agent.md)
- [Python Expert Agent](../../../../agents/languages/python-expert.agent.md)
- [Microservices Architecture](../../microservices/SKILL.md)
- [Python Patterns](../../../languages/python-patterns/SKILL.md)
- [Golang Patterns](../../../languages/golang-patterns/SKILL.md)
- [Clean Code](../../../engineering/clean-code/SKILL.md)
