# Testing Strategies

## Instructions for AI

Implement comprehensive testing strategies at multiple levels:

## Test Pyramid

### Unit Tests (Base - 70%)
- Test individual components in isolation
- Fast execution (milliseconds)
- Mock external dependencies
- High coverage of business logic
- One assertion per test when possible
- Follow AAA pattern: Arrange, Act, Assert

**Best Practices:**
- Test public interfaces, not implementation details
- Use descriptive test names (should_returnUser_when_validIdProvided)
- Test edge cases and error conditions
- Keep tests independent and idempotent
- Use test fixtures and builders for setup

### Integration Tests (Middle - 20%)
- Test interaction between components
- Include database, external APIs, file system
- Slower than unit tests (seconds)
- Use test databases or containers
- Verify correct integration behavior

**Best Practices:**
- Use test containers (Docker) for databases
- Clean state between tests
- Test actual integration points
- Mock only external services you don't control
- Verify data persistence and retrieval

### End-to-End Tests (Top - 10%)
- Test complete user workflows
- Exercise entire system
- Slowest tests (minutes)
- Run less frequently (CI/CD pipelines)
- Focus on critical business paths

**Best Practices:**
- Test happy path and critical scenarios
- Use page object pattern for UI tests
- Minimize flakiness with proper waits
- Run against production-like environment
- Keep tests maintainable

## Testing Approaches

### Test-Driven Development (TDD)
1. Write failing test first
2. Write minimal code to pass
3. Refactor for quality
4. Repeat

**Benefits:**
- Better design (testable code)
- Higher confidence
- Documentation through tests
- Regression prevention

### Behavior-Driven Development (BDD)
- Write tests in business language (Given-When-Then)
- Use tools like Cucumber, SpecFlow
- Collaboration between dev, QA, business
- Living documentation

### Property-Based Testing
- Test properties that should always hold
- Generate random test data
- Find edge cases automatically
- Use tools like QuickCheck, Hypothesis

## Test Doubles

### Mock
- Verify interactions (method calls)
- Example: Verify email service was called

### Stub
- Provide predetermined responses
- Example: Return fixed user data

### Fake
- Working implementation for testing
- Example: In-memory database

### Spy
- Record interactions for verification
- Partial mock of real object

## Testing Patterns

### AAA Pattern (Arrange-Act-Assert)

```python
# Python — pytest with AAA
async def test_create_order_calculates_total() -> None:
    # Arrange
    repo = FakeOrderRepository()
    service = OrderService(repo=repo, events=FakeEventBus())

    # Act
    order = await service.create_order(
        items=[LineItem(product_id="p1", quantity=2, unit_price=Decimal("10.00"))]
    )

    # Assert
    assert order.total == Decimal("20.00")
    assert order.status == OrderStatus.DRAFT
```

```go
// Go — table-driven test with AAA
func TestCalculateTotal(t *testing.T) {
	tests := []struct {
		name  string
		items []LineItem
		want  decimal.Decimal
	}{
		{
			name:  "single item",
			items: []LineItem{{Qty: 2, Price: decimal.NewFromInt(10)}},
			want:  decimal.NewFromInt(20),
		},
		{
			name:  "empty order",
			items: nil,
			want:  decimal.Zero,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			order := NewOrder(tt.items)
			got := order.Total()
			assert.True(t, tt.want.Equal(got))
		})
	}
}
```

```dart
// Flutter — widget test
testWidgets('OrderCard shows total', (tester) async {
  // Arrange
  final order = Order(id: '1', total: 42.0, status: OrderStatus.placed);

  // Act
  await tester.pumpWidget(MaterialApp(home: OrderCard(order: order)));

  // Assert
  expect(find.text('€42.00'), findsOneWidget);
  expect(find.text('Placed'), findsOneWidget);
});
```

### Builder Pattern for Test Data
```python
# Python — Factory for test data
def make_order(**overrides: Any) -> Order:
    defaults = {"status": OrderStatus.DRAFT, "lines": [make_line()]}
    return Order(**(defaults | overrides))
```

### Test Fixtures
- Shared setup for multiple tests
- Use [SetUp] / [TearDown] attributes
- Keep minimal to avoid test coupling

## Coverage Metrics

- **Line Coverage**: % of code lines executed
- **Branch Coverage**: % of decision branches taken
- **Path Coverage**: % of possible paths tested
- **Mutation Testing**: Test quality by changing code

**Target:**
- 80%+ overall coverage
- 100% coverage for critical paths
- Don't chase 100% blindly - quality over quantity

## Testing Anti-Patterns

❌ Testing implementation details
❌ Testing private methods directly
❌ Interdependent tests
❌ Slow test suites
❌ Flaky tests
❌ Testing everything through UI
❌ Mocking everything

## Example Prompts

"Write unit tests for this service using TDD approach"

"Create integration tests for this API endpoint"

"Design a testing strategy for this microservice"

"Review these tests and suggest improvements"

"Write property-based tests for this validation logic"

## Related Skills & Agents

- [Test Strategist Agent](../../agents/test-strategist.agent.md)
- [Testing Patterns Skill](../testing/SKILL.md)
- [Python Patterns](../python-patterns/SKILL.md)
- [Golang Patterns](../golang-patterns/SKILL.md)
- [Flutter Patterns](../flutter-patterns/SKILL.md)
