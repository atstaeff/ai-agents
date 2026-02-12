# Clean Code Principles

## Instructions for AI

When writing or reviewing code, apply these clean code principles:

## Core Principles

### DRY (Don't Repeat Yourself)
Every piece of knowledge should have a single source of truth.

### KISS (Keep It Simple, Stupid)
Prefer the simplest solution that works. Complexity is the enemy of reliability.

### YAGNI (You Aren't Gonna Need It)
Don't build features until they're actually needed. Speculation leads to bloat.

### Law of Demeter
A method should only call methods on: itself, its parameters, objects it creates, its direct components.

## Naming Conventions
- Use descriptive, intention-revealing names
- Avoid abbreviations unless universally understood
- Class names should be nouns, method names should be verbs
- Use consistent naming patterns across the codebase

```python
# ❌ Before
def calc(d: list[dict]) -> float:
    t = 0
    for i in d:
        t += i["p"] * i["q"]
    return t

# ✅ After
def calculate_order_total(line_items: list[LineItem]) -> Decimal:
    return sum(item.price * item.quantity for item in line_items)
```

```go
// ❌ Before
func proc(d []map[string]any) float64 { ... }

// ✅ After
func CalculateOrderTotal(items []LineItem) (decimal.Decimal, error) { ... }
```

## Functions
- Keep functions small (ideally < 20 lines)
- Functions should do one thing and do it well
- Minimize parameters (ideally ≤ 3)
- Avoid flag arguments — split into separate functions

```python
# ❌ Before: flag argument controls behavior
def create_user(name: str, email: str, is_admin: bool = False) -> User:
    user = User(name=name, email=email)
    if is_admin:
        user.role = "admin"
        send_admin_welcome(user)
    else:
        user.role = "member"
        send_member_welcome(user)
    return user

# ✅ After: separate functions, clear intent
def create_member(name: str, email: str) -> User:
    user = User(name=name, email=email, role="member")
    send_member_welcome(user)
    return user

def create_admin(name: str, email: str) -> User:
    user = User(name=name, email=email, role="admin")
    send_admin_welcome(user)
    return user
```

## Code Structure
- Follow the Single Responsibility Principle
- Organize code by feature/domain, not by technical layer
- Keep related code close together
- Remove dead code and commented-out code

## Error Handling

```python
# ❌ Before: generic exception, no context
try:
    result = process_order(order)
except Exception:
    print("error")

# ✅ After: specific exception, structured context
try:
    result = await order_service.process(order)
except OrderValidationError as exc:
    logger.warning("order_validation_failed", order_id=order.id, reason=str(exc))
    raise
except PaymentGatewayError as exc:
    logger.error("payment_failed", order_id=order.id, gateway=exc.gateway)
    raise OrderProcessingError(f"Payment failed for order {order.id}") from exc
```

```go
// ❌ Before
result, _ := processOrder(order)

// ✅ After
result, err := processOrder(ctx, order)
if err != nil {
    return fmt.Errorf("process order %s: %w", order.ID, err)
}
```

## Comments
- Code should be self-explanatory; minimize comments
- Use comments to explain "why", not "what"
- Document complex algorithms and business rules

## Testing
- Write tests first (TDD) when appropriate
- One assertion per test when possible
- Use descriptive test names that explain the scenario
- Follow AAA pattern: Arrange, Act, Assert
- Test edge cases and error conditions

## Example Prompts

"Review this code for clean code violations and suggest improvements"

"Refactor this function following clean code principles"

"Write this feature using TDD approach with clean code practices"

## Related Skills & Agents

- [Python Expert Agent](../../agents/python-expert.agent.md)
- [Golang Expert Agent](../../agents/golang-expert.agent.md)
- [SOLID Principles](../software-engineering/solid-principles.md)
- [Design Patterns](../software-engineering/design-patterns.md)
- [Practical Refactoring](../software-engineering/practical-refactoring.md)
- [Python Patterns](../python-patterns/SKILL.md)
- [Golang Patterns](../golang-patterns/SKILL.md)
