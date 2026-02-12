# Testing Patterns Skill

## Instructions for AI

Apply comprehensive testing best practices. Use this skill when designing test strategies, writing tests, or setting up testing infrastructure.

## Test Pyramid

```
         /\
        / E2E \          ~5%  — Critical user journeys
       /--------\
      / Contract  \      ~10% — API contracts
     /--------------\
    /  Integration    \  ~25% — DB, queues, external APIs
   /--------------------\
  /     Unit Tests       \ ~60% — Business logic, pure functions
 /------------------------\
```

## Unit Testing Patterns

### Arrange-Act-Assert

```python
class TestPriceCalculator:
    def test_applies_percentage_discount(self):
        # Arrange
        calculator = PriceCalculator()
        product = Product(price=100.0)
        discount = PercentageDiscount(rate=0.2)

        # Act
        result = calculator.calculate(product, discount)

        # Assert
        assert result == 80.0
```

### Parameterized Tests

```python
import pytest

@pytest.mark.parametrize("input_price,discount_rate,expected", [
    (100.0, 0.0, 100.0),
    (100.0, 0.1, 90.0),
    (100.0, 0.5, 50.0),
    (100.0, 1.0, 0.0),
    (0.0, 0.5, 0.0),
])
def test_discount_calculation(input_price, discount_rate, expected):
    result = calculate_discount(input_price, discount_rate)
    assert result == expected
```

### Fakes over Mocks

```python
class FakeEmailSender:
    """In-memory fake — captures sent emails for verification."""

    def __init__(self):
        self.sent_emails: list[Email] = []

    async def send(self, email: Email) -> None:
        self.sent_emails.append(email)

# In tests
async def test_order_confirmation_sends_email(fake_email_sender):
    service = OrderService(email_sender=fake_email_sender)
    await service.place_order(sample_order)
    
    assert len(fake_email_sender.sent_emails) == 1
    assert fake_email_sender.sent_emails[0].subject == "Order Confirmation"
```

### Factory Pattern for Test Data

```python
from polyfactory.factories.pydantic_factory import ModelFactory

class UserFactory(ModelFactory):
    __model__ = User
    
    @classmethod
    def admin(cls) -> User:
        return cls.build(role=UserRole.ADMIN)
    
    @classmethod
    def with_orders(cls, count: int = 3) -> User:
        user = cls.build()
        user.orders = OrderFactory.batch(count)
        return user
```

## Integration Testing Patterns

### Testcontainers

```python
import pytest
from testcontainers.postgres import PostgresContainer

@pytest.fixture(scope="session")
def db_container():
    with PostgresContainer("postgres:16-alpine") as pg:
        yield pg

@pytest.fixture
async def db_session(db_container):
    engine = create_async_engine(db_container.get_connection_url())
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    async with AsyncSession(engine) as session:
        yield session
        await session.rollback()
```

### API Testing (httpx)

```python
from httpx import AsyncClient, ASGITransport

@pytest.fixture
async def api_client(app):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        yield client

async def test_create_user_returns_201(api_client):
    response = await api_client.post("/users", json={"name": "Alice", "email": "alice@test.com"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Alice"
    assert "id" in data
```

## Quality Gates

```yaml
quality_gates:
  unit_tests:
    coverage: ">= 80%"
    max_duration: "120s"
    blocking: true
    
  integration_tests:
    coverage: ">= 60%"
    max_duration: "300s"
    blocking: true
    
  security_scan:
    tool: "bandit"
    severity: "medium"
    blocking: true
    
  type_checking:
    tool: "mypy --strict"
    blocking: true
    
  linting:
    tool: "ruff check"
    blocking: true
```

## Test Fixture Organization

```
tests/
├── conftest.py           # Shared fixtures
├── factories.py          # Test data factories
├── fakes.py              # Fake implementations
├── unit/
│   ├── conftest.py       # Unit-specific fixtures
│   ├── test_models.py
│   ├── test_services.py
│   └── test_validators.py
├── integration/
│   ├── conftest.py       # DB, containers
│   ├── test_repositories.py
│   └── test_api.py
└── e2e/
    ├── conftest.py       # Full stack setup
    └── test_user_journey.py
```

## Best Practices

✅ Name tests: `test_<action>_<scenario>_<expected>`
✅ One logical assertion per test
✅ Use `conftest.py` for shared fixtures
✅ Prefer fakes over mocks for domain dependencies
✅ Run unit tests in parallel (`pytest-xdist`)
✅ Tag slow tests: `@pytest.mark.slow`
✅ Keep test code clean — it's production code too

## Anti-Patterns

❌ Testing implementation details instead of behavior
❌ Shared mutable state between tests
❌ Ignoring flaky tests
❌ Over-mocking (if everything is mocked, what are you testing?)
❌ Missing error path tests
❌ Hard-coded test data (use factories)
❌ Skipping tests that "take too long"

## Example Prompts

- "Write unit tests for this OrderService using fakes and factories"
- "Set up integration tests with testcontainers and PostgreSQL"
- "Design a quality gate configuration for our CI/CD pipeline"
- "Refactor these tests to eliminate shared state and improve isolation"

## Related Skills

- [Test Strategist Agent](../../agents/test-strategist.agent.md)
- [Testing Strategies](../software-engineering/testing-strategies.md)
- [Python Patterns](../python-patterns/SKILL.md)
- [Golang Patterns](../golang-patterns/SKILL.md)
- [Flutter Patterns](../flutter-patterns/SKILL.md)
