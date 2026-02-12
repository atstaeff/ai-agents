# Practical Refactoring Tactics

## Instructions for AI

Apply pragmatic refactoring approaches that balance improvement with delivery.

## The Refactoring Mindset

### Progress Over Perfection

Refactoring is continuous improvement, not one-time perfection:
- Small changes compound over time
- Ship working improvements frequently
- Each change should stand alone
- Never break existing functionality

## Identifying Refactoring Opportunities

### The Pain-Driven Approach

Refactor when pain is felt, not preemptively:

**High Pain Signals:**
- Bugs cluster in specific areas
- Feature velocity slows in certain modules
- New team members struggle with specific code
- Multiple people working in same area causes conflicts

**Low Priority Signals:**
- Code "looks ugly" but works fine
- Theoretical future scenarios
- Personal style preferences
- Following latest trends

## Tactical Refactoring Patterns

### Extract Until Clear

When encountering confusing code:

Step 1: Extract smallest confusing piece into named function
Step 2: Does it make sense now? If not, extract more
Step 3: Repeat until the intent is obvious

Original complex code:
```javascript
function handleCheckout(cart, user) {
    const total = cart.items.reduce((sum, item) => 
        sum + (item.price * item.quantity * (1 - item.discount)), 0);
    if (user.loyaltyPoints > 100) total *= 0.95;
    if (total > 50) total -= 10;
    // ... 30 more lines
}
```

After extraction:
```javascript
function handleCheckout(cart, user) {
    const subtotal = calculateCartSubtotal(cart.items);
    const withLoyalty = applyLoyaltyDiscount(subtotal, user);
    const final = applyShippingRules(withLoyalty);
    return processPayment(final, user);
}
```

### Introduce Parameter Object

When functions have 4+ parameters:

Before:
```python
def create_report(start_date, end_date, user_id, format_type, include_details):
    pass
```

After:
```python
def create_report(report_config):
    # report_config contains all parameters
    pass
```

### Replace Conditional with Polymorphism

When you see type-checking throughout code:

Problematic pattern:
```java
if (shape.type == "circle") {
    area = Math.PI * shape.radius * shape.radius;
} else if (shape.type == "rectangle") {
    area = shape.width * shape.height;
}
```

Improved approach:
```java
area = shape.calculateArea();  // Each shape knows how
```

## Refactoring Safety Net

### Test-Protected Refactoring

Never refactor without protection:

1. **Write Characterization Tests First**
   - Capture current behavior (even if wrong)
   - Tests document what code actually does
   - Prevents accidental changes

2. **Refactor in Tiny Steps**
   - One change at a time
   - Run tests after each change
   - Commit working state frequently

3. **Keep Tests Green**
   - If tests fail, immediately revert
   - Fix or adjust tests before continuing
   - Never proceed with failing tests

## The Strangler Approach

For large refactoring efforts:

### Phase 1: Establish Boundary
Create interface around old code:
```typescript
interface PaymentProcessor {
    processPayment(amount: number): PaymentResult;
}

// Wrap old code
class LegacyPaymentProcessor implements PaymentProcessor {
    processPayment(amount: number): PaymentResult {
        return oldPaymentSystem.doPayment(amount); // wraps old
    }
}
```

### Phase 2: Route New Work
New features use the interface, can use new implementation:
```typescript
class ModernPaymentProcessor implements PaymentProcessor {
    processPayment(amount: number): PaymentResult {
        // New implementation
    }
}
```

### Phase 3: Gradual Migration
Move existing features one at a time to new implementation.

### Phase 4: Remove Old Code
Once nothing uses legacy implementation, delete it.

## Dealing with Resistance

### Making the Business Case

Translate technical debt to business terms:

"This refactoring reduces average bug fix time from 2 days to 4 hours, letting us respond to customer issues 4x faster."

Not: "The code violates SOLID principles and needs refactoring."

### Time Boxing Refactoring

Propose bounded experiments:
"Give me 3 days to refactor the authentication module. If velocity doesn't improve in the next sprint, I'll stop similar efforts."

## Refactoring Anti-Patterns

### The Complete Rewrite Trap

Rarely succeeds:
- Loses accumulated bug fixes
- Underestimates hidden complexity
- Takes longer than expected
- Business can't wait

Instead: Incremental improvement with strangler pattern

### The Abstract Too Soon Problem

Don't create abstractions before you have 3 concrete examples:
- First instance: Write specifically
- Second instance: Notice duplication
- Third instance: Now create abstraction

### The Premature Generalization

Resist urge to make code "flexible" for hypothetical futures:
- Adds complexity now
- Hypothetical may never happen
- Real needs differ from imagined ones

Follow YAGNI: You Aren't Gonna Need It

## Measuring Refactoring Success

### Velocity Metrics
- Feature completion time trends
- Bug resolution time trends
- New team member ramp-up time

### Quality Metrics
- Bug density in refactored areas
- Code churn rates
- Test coverage stability

### Team Metrics
- Developer satisfaction surveys
- Code review comment counts
- Time spent debugging vs building

## Example Prompts

"Identify refactoring opportunities in this code based on pain points"

"Help me extract this complex function into smaller pieces"

"Create a strangler pattern plan for this legacy module"

"Write characterization tests before refactoring this code"

"Translate this technical debt into business impact terms"

## Related Skills & Agents

- [Code Reviewer Agent](../../agents/code-reviewer.agent.md)
- [Clean Code](../software-engineering/clean-code.md)
- [Anti-Patterns](../anti-patterns/SKILL.md)
- [Technical Debt Management](../project-management/technical-debt.md)
