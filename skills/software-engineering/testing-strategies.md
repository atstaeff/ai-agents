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
```
// Arrange: Setup test data and dependencies
var user = new User("John");
var service = new UserService(mockRepo);

// Act: Execute the behavior being tested
var result = service.CreateUser(user);

// Assert: Verify the outcome
Assert.True(result.Success);
```

### Builder Pattern for Test Data
```
var user = new UserBuilder()
    .WithName("John")
    .WithEmail("john@example.com")
    .Build();
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
