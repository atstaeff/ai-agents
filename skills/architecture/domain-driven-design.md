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

```
class Order {
    private OrderId id;
    private OrderStatus status;
    // Identity is the defining characteristic
}
```

### Value Objects
- Immutable objects defined by attributes
- No identity, only values matter
- Examples: Money, Address, DateRange

```
class Money {
    private readonly decimal amount;
    private readonly string currency;
    // Immutable, equality by value
}
```

### Aggregates
- Cluster of entities and value objects
- One entity is the aggregate root
- External objects hold references only to root
- Enforce business invariants
- Transaction boundary

```
class Order { // Aggregate Root
    private List<OrderLine> orderLines;
    
    public void AddOrderLine(Product product, int quantity) {
        // Business rule: validate and maintain consistency
    }
}
```

### Repositories
- Abstraction for data access
- One repository per aggregate root
- Provides collection-like interface
- Hides persistence details

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
- Example: TransferMoneyService, PricingService

### Domain Events
- Something significant that happened in domain
- Immutable
- Past tense naming
- Enable decoupling and eventual consistency

```
class OrderPlacedEvent {
    public OrderId OrderId { get; }
    public DateTime OccurredAt { get; }
    public CustomerId CustomerId { get; }
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
- ❌ Anemic: Data classes with getters/setters, logic in services
- ✅ Rich: Behavior in domain objects, encapsulate business logic

### Aggregate Design Rules
- Keep aggregates small
- Reference other aggregates by ID only
- Use eventual consistency between aggregates
- One transaction modifies one aggregate

### Value Object Usage
- Use for money, dates, measurements
- Make immutable
- Implement equality by value
- No side effects in methods

### Domain Events Usage
- Publish after transaction commits
- Use for loose coupling between contexts
- Enable auditing and event sourcing
- Name in past tense (OrderPlaced, PaymentProcessed)

## Common Patterns

### Specification Pattern
```
interface ISpecification<T> {
    bool IsSatisfiedBy(T entity);
    ISpecification<T> And(ISpecification<T> other);
}
```

### Repository Pattern
```
interface IRepository<T, TId> where T : IAggregateRoot {
    T FindById(TId id);
    void Save(T aggregate);
    void Delete(T aggregate);
}
```

### Unit of Work Pattern
```
interface IUnitOfWork {
    void BeginTransaction();
    void Commit();
    void Rollback();
}
```

## DDD with Modern Architecture

### DDD + Microservices
- Each microservice = One bounded context (or few)
- Services communicate via events
- Anti-corruption layers at boundaries

### DDD + CQRS
- Separate read and write models
- Commands modify aggregates
- Queries use optimized read models
- Event sourcing stores domain events

### DDD + Event Sourcing
- Store events instead of current state
- Reconstruct state by replaying events
- Complete audit trail
- Temporal queries

## Anti-Patterns

❌ Anemic domain model
❌ Aggregates too large
❌ Direct aggregate-to-aggregate references
❌ Business logic in application services
❌ Ignoring ubiquitous language
❌ One model for entire system

## Example Prompts

"Model an order management system using DDD tactical patterns"

"Design bounded contexts for a banking system"

"Implement an aggregate with business invariants"

"Create domain events for an e-commerce checkout process"

"Refactor this anemic model to a rich domain model"
