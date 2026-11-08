# Background examples

Use focused sections only when needed. The current skill entry, project conventions and user constraints govern the work. Examples illustrate particular choices; they do not mandate a framework, test library or architecture.

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
# Before (the stored fields p and q are unit price in cents and quantity)
def calc(d: list[dict[str, int]]) -> int:
    t = 0
    for i in d:
        t += i["p"] * i["q"]
    return t

# After: preserve input and output contracts while making the units clear.
def calculate_order_total_cents(line_items: list[dict[str, int]]) -> int:
    total_cents = 0
    for item in line_items:
        unit_price_cents, quantity = item["p"], item["q"]
        total_cents += unit_price_cents * quantity
    return total_cents
```

```go
// ❌ Before
func proc(d []map[string]any) float64 { ... }

// ✅ After
func CalculateOrderTotal(items []LineItem) (decimal.Decimal, error) { ... }
```

## Functions
- Keep a coherent operation together and name its inputs and effects clearly.
- Split functions when callers need distinct operations, not to meet a line or parameter count.
- Keep a flag when it configures one coherent operation and callers can read its meaning.

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

# After: specific exceptions and contextual fields with standard Python logging
try:
    result = process_order(order)
except OrderValidationError:
    logger.warning("order_validation_failed")
    raise
except PaymentGatewayError as exc:
    logger.error("payment_failed", extra={"failure_kind": "gateway"})
    raise OrderProcessingError("Payment failed") from exc
```

Keep chained exception details internal; do not expose them to an API consumer or an
unapproved log destination.

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
- Check one scenario per test; include the assertions needed to verify its outcome
- Use descriptive test names that explain the scenario
- Follow AAA pattern: Arrange, Act, Assert
- Test edge cases and error conditions

## Example Prompts

"Review this code for clean code violations and suggest improvements"

"Refactor this function following clean code principles"

"Write this feature using TDD approach with clean code practices"

## Related Skills & Agents

- [Python Expert Agent](../../../../agents/languages/python-expert.agent.md)
- [Golang Expert Agent](../../../../agents/languages/golang-expert.agent.md)
- [SOLID Principles](../../solid-principles/SKILL.md)
- [Design Patterns](../../design-patterns/SKILL.md)
- [Practical Refactoring](../../practical-refactoring/SKILL.md)
- [Python Patterns](../../../languages/python-patterns/SKILL.md)
- [Golang Patterns](../../../languages/golang-patterns/SKILL.md)
