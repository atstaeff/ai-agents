# Background examples

Use focused sections only when needed. The current skill entry, project conventions and user constraints govern the work. Examples illustrate particular choices; they do not mandate a framework, test library or architecture.

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

### Extract a Cohesive Rule

Give a rule its own name when that makes it easier to read or exercise. Keep steps
together when splitting them would hide the data flow or add unhelpful navigation.

Original checkout calculation (all amounts are integer cents and the coupon applies
to orders of at least $25):
```javascript
function checkoutTotal(items, couponCents) {
    let subtotal = 0;
    for (const item of items) subtotal += item.unitPriceCents * item.quantity;
    if (subtotal < 2500) return subtotal;
    return Math.max(0, subtotal - couponCents);
}
```

After extraction:
```javascript
function checkoutTotal(items, couponCents) {
    let subtotal = 0;
    for (const item of items) subtotal += item.unitPriceCents * item.quantity;
    return applyCoupon(subtotal, couponCents);
}

function applyCoupon(subtotal, couponCents) {
    if (subtotal < 2500) return subtotal;
    return Math.max(0, subtotal - couponCents);
}
```

This extraction helps when the coupon rule needs to be checked or changed separately.
Check an order just below the minimum, one at the minimum, and a coupon larger than
the subtotal in both versions.

### Introduce Parameter Object

Group parameters when they describe a cohesive value with a shared meaning or
validation rule. Argument count alone does not justify a wrapper:

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

Reuse checks that protect the behavior. Add a focused characterization check when a
risky path is unprotected:

1. **Establish the Behavior to Preserve**
   - Capture observable behavior at the relevant boundary.
   - Document known defects separately; changing them is a behavior change.

2. **Refactor in Tiny Steps**
   - One change at a time
   - Run affected checks after a risky step
   - Commit working state frequently

3. **Investigate Failures**
   - Find the cause and preserve the expected contract. Change an expectation only
     when evidence shows it was wrong or an authorized behavior change requires it.

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

"The last two fixes required coordinated edits in three modules. Try the same
representative fix after consolidation and compare the number of coordinated edits."

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

Keep similar code local while its meaning is still diverging. Extract shared behavior
when callers need the same rule to change together, or when an actual substitution
boundary makes the added indirection useful. A fixed example count cannot decide that.

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

- [Code Reviewer Agent](../../../../agents/quality/code-reviewer.agent.md)
- [Clean Code](../../clean-code/SKILL.md)
- [Anti-Patterns](../../../quality/anti-patterns/SKILL.md)
- [Technical Debt Management](../../../delivery/technical-debt/SKILL.md)
