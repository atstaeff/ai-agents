# Anti-Patterns Skill

## Instructions for AI

Identify and avoid common anti-patterns in code, architecture, and event-driven systems. Use this skill when reviewing, refactoring, or designing systems to prevent common mistakes.

## Code Anti-Patterns

### 1. God Object / God Class

**Problem:** One class that knows too much and does too much.

```python
# ❌ Anti-pattern
class ApplicationManager:
    def create_user(self): ...
    def send_email(self): ...
    def process_payment(self): ...
    def generate_report(self): ...
    def validate_input(self): ...
    def connect_database(self): ...
```

```python
# ✅ Fix: Single Responsibility
class UserService:
    def create_user(self): ...

class EmailService:
    def send_email(self): ...

class PaymentService:
    def process_payment(self): ...
```

### 2. Primitive Obsession

**Problem:** Using primitives instead of domain types.

```python
# ❌ Anti-pattern
def create_order(customer_id: str, amount: float, currency: str): ...

# ✅ Fix: Value Objects
class CustomerId(BaseModel):
    value: UUID

class Money(BaseModel):
    amount: Decimal
    currency: Currency  # StrEnum

def create_order(customer_id: CustomerId, total: Money): ...
```

### 3. Feature Envy

**Problem:** A method that uses data from another class more than its own.

```python
# ❌ Anti-pattern
class InvoiceCalculator:
    def calculate_total(self, order: Order) -> float:
        total = sum(item.price * item.quantity for item in order.items)
        total -= order.discount_amount
        total *= (1 + order.tax_rate)
        return total

# ✅ Fix: Move method to the class that owns the data
class Order:
    def calculate_total(self) -> float:
        subtotal = sum(item.total for item in self.items)
        return (subtotal - self.discount_amount) * (1 + self.tax_rate)
```

### 4. Shotgun Surgery

**Problem:** A small change requires modifications in many classes.

**Fix:** Consolidate related behavior. Apply the "Open-Closed Principle" — extend via new code, not by modifying existing code.

### 5. Magic Numbers / Strings

```python
# ❌ Anti-pattern
if user.age > 18:
    if order.status == "COMPLETED":
        discount = amount * 0.15

# ✅ Fix: Named constants
MINIMUM_AGE = 18
LOYALTY_DISCOUNT_RATE = Decimal("0.15")

class OrderStatus(StrEnum):
    COMPLETED = "COMPLETED"
    PENDING = "PENDING"
```

## Architecture Anti-Patterns

### 1. Distributed Monolith

**Problem:** Microservices that must be deployed together, share databases, or have synchronous call chains.

**Symptoms:**
- Cannot deploy one service without deploying others
- Shared database between services
- Cascading failures across services
- High coupling between services

**Fix:**
- Clear bounded context boundaries
- Async communication via events
- Database per service
- API versioning

### 2. Shared Database

**Problem:** Multiple services reading/writing the same database.

```
# ❌ Anti-pattern
Service A ─┐
Service B ──┤──▶ Shared PostgreSQL
Service C ─┘

# ✅ Fix: Database per service + events
Service A ──▶ DB A ──▶ Events ──▶ Service B ──▶ DB B
```

### 3. Big Ball of Mud

**Problem:** No clear architecture, everything depends on everything.

**Fix:** Introduce bounded contexts, layered architecture, dependency rules.

### 4. Over-Engineering / Premature Abstraction

**Problem:** Building for imaginary future requirements.

**Fix:**
- YAGNI (You Aren't Gonna Need It)
- Start simple, refactor when complexity justifies it
- "Three strikes" rule: abstract after 3 repetitions

### 5. Chatty Communication

**Problem:** Services making many synchronous calls to each other.

```
# ❌ Anti-pattern: 5 sync calls for one operation
Order Service → User Service → Inventory Service → Payment Service → Notification Service

# ✅ Fix: Aggregate + async events
Order Service → Order Created Event → [User, Inventory, Payment, Notification] (parallel)
```

## Event-Driven Anti-Patterns

### 1. Event Sourcing Everything

**Problem:** Using event sourcing for simple CRUD where it adds complexity without benefit.

**When to use Event Sourcing:**
- Audit trail is a business requirement
- Time-travel / replay needed
- Complex domain with many state transitions

**When NOT to:**
- Simple CRUD operations
- Reference data (countries, currencies)
- Content management

### 2. Missing Idempotency

**Problem:** Processing the same event twice causes duplicate effects.

```python
# ❌ Anti-pattern: No idempotency
async def handle_payment(event: PaymentReceived):
    await credit_account(event.amount)  # Doubles on retry!

# ✅ Fix: Idempotent handler
async def handle_payment(event: PaymentReceived):
    if await is_already_processed(event.id):
        return
    await credit_account(event.amount)
    await mark_processed(event.id)
```

### 3. Missing Dead Letter Queue

**Problem:** Failed messages are silently dropped or retry forever.

**Fix:** Always configure:
- Dead letter topic/queue
- Max retry attempts (typically 5)
- Exponential backoff
- Alerting on DLQ messages

### 4. Event Schema Coupling

**Problem:** Consumers break when event schema changes.

**Fix:**
- Schema registry / versioning
- Backwards-compatible changes only
- Consumer-driven contract tests

### 5. Temporal Coupling in Events

**Problem:** Assuming events arrive in a specific order.

**Fix:**
- Design handlers to be order-independent
- Use correlation IDs and timestamps
- Implement saga pattern for multi-step processes

## Detection Checklist

| Anti-Pattern | How to Detect | Action |
|--------------|--------------|--------|
| God Object | Class > 200 lines, 10+ methods | Split by responsibility |
| Distributed Monolith | Services deployed together | Define boundaries, use events |
| Missing Idempotency | Duplicate processing on retry | Add idempotency key check |
| Shared Database | Multiple services, one DB | Database per service |
| Chatty Services | > 3 sync calls per request | Aggregate, use events |
| Over-Engineering | Unused abstractions | Remove, simplify |

## Best Practices

✅ Regular architecture reviews to catch anti-patterns early
✅ Use architecture fitness functions (automated checks)
✅ Code review checklist includes anti-pattern checks
✅ Document why things were done a certain way (ADRs)
✅ Refactor incrementally — don't try to fix everything at once

## Example Prompts

- "Review this codebase for common anti-patterns and suggest fixes"
- "Is this microservices architecture actually a distributed monolith?"
- "Check this event handler for idempotency and error handling issues"
- "Identify over-engineering in this project structure"

## Related Skills

- [Design Patterns](../software-engineering/design-patterns.md)
- [SOLID Principles](../software-engineering/solid-principles.md)
- [Microservices Architecture](../architecture/microservices.md)
