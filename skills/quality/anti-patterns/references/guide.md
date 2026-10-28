# Background examples

Use focused sections only when needed. The current skill entry, project conventions and user constraints govern the work. Examples illustrate particular choices; they do not mandate a framework, test library or architecture.

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

**Problem:** A service cannot change or recover independently because shared contracts,
write ownership or synchronous dependencies are tightly coupled.

**Check:** Reproduce the deployment/failure constraint. Compare a local module boundary,
a smaller contract change and a service/data split; choose the smallest adequate repair.

### 2. Competing Data Ownership

**Problem:** Several writers change the same invariant without an explicit transaction,
compatibility or concurrency contract. Sharing a database alone is not proof of a defect.

**Repair:** Clarify the invariant's owner and permitted reads/writes. A physical database
split needs migration, consistency and operating evidence; asynchronous events do not
automatically remove coupling.

### 3. Big Ball of Mud

**Problem:** No clear architecture, everything depends on everything.

**Fix:** Introduce bounded contexts, layered architecture, dependency rules.

### 4. Over-Engineering / Premature Abstraction

**Problem:** Building for imaginary future requirements.

**Fix:**
- YAGNI (You Aren't Gonna Need It)
- Start simple, refactor when complexity justifies it
- Extract shared meaning only when stable behavior and actual consumers justify it

### 5. Chatty Communication

**Problem:** Repeated remote calls add measured latency or coupled failure to a user path.

**Repair:** Inspect the critical path and data ownership first. Batch, cache, aggregate
or move a boundary only when it preserves freshness and business semantics. Making all
steps asynchronous changes the completion contract and is not an automatic repair.

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

```

A check-then-credit-then-mark sequence can race or crash between writes. For a local
business effect, claim a unique operation identity and apply the effect atomically in
one transaction where storage permits. For external effects, use a stable idempotency
key and a durable outcome/reconciliation contract; marking locally cannot roll back a
remote charge. Exercise duplicate, concurrent and interrupted processing.

### 3. Unbounded or Lost Failed Work

**Problem:** Failed messages disappear silently or retry forever.

**Repair:** Bound attempts, backoff, queue size and message age. Use a dead-letter or
other durable failure/replay mechanism when required, with an owner and alert. Select
limits from the actual contract; do not prescribe a universal retry count.

### 4. Event Schema Coupling

**Problem:** Consumers break when event schema changes.

**Fix:**
- Schema registry / versioning
- Compatibility during rollout, with an explicit migration for a breaking change
- Consumer-driven contract tests

### 5. Temporal Coupling in Events

**Problem:** Assuming events arrive in a specific order.

**Fix:**
- Define the required ordering scope and handle late/duplicate input
- Use sequence or causal identity where the invariant needs it; timestamps alone may not establish order
- Persist multi-step workflow state and recovery when required

## Detection Checklist

| Anti-Pattern | How to Detect | Action |
|--------------|--------------|--------|
| God Object | Unrelated changes repeatedly affect one module | Separate the demonstrated responsibilities |
| Distributed Monolith | Coupled deployment or cascading failure | Repair the responsible contract or ownership boundary |
| Missing Idempotency | Retry duplicates a business effect | Atomic local effect/deduplication or recoverable external operation |
| Competing Data Ownership | Writers violate a shared invariant | Define write/transaction ownership; justify any migration |
| Chatty Services | Remote calls dominate the measured critical path | Reduce waits while preserving completion/data semantics |
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

- [Architecture Reviewer Agent](../../../../agents/architecture/architecture-reviewer.agent.md)
- [Code Reviewer Agent](../../../../agents/quality/code-reviewer.agent.md)
- [Design Patterns](../../../engineering/design-patterns/SKILL.md)
- [SOLID Principles](../../../engineering/solid-principles/SKILL.md)
- [Microservices Architecture](../../../architecture/microservices/SKILL.md)
- [Python Patterns](../../../languages/python-patterns/SKILL.md)
- [Golang Patterns](../../../languages/golang-patterns/SKILL.md)
- [Flutter Patterns](../../../languages/flutter-patterns/SKILL.md)
