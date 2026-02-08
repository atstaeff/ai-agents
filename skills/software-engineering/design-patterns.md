# Design Patterns

## Instructions for AI

Apply appropriate design patterns to solve common software design problems. Reference [`atstaeff/better-python`](https://github.com/atstaeff/better-python) for concrete Python before/after examples.

## Creational Patterns

### Singleton
- Use when exactly one instance is needed (e.g., configuration manager)
- Implement thread-safe lazy initialization
- Consider alternatives like dependency injection

### Factory Method
- Create objects without specifying exact class
- Use when object creation logic is complex
- Example: DocumentFactory creates PDFDocument, WordDocument

### Abstract Factory
- Families of related objects
- Example: UIFactory creates Button, TextBox for different themes

### Builder
- Construct complex objects step by step
- Use for objects with many optional parameters
- Example: QueryBuilder, HttpRequestBuilder

### Prototype
- Clone existing objects
- Use when object creation is expensive

## Structural Patterns

### Adapter
- Convert interface of a class into another interface
- Example: Adapt legacy API to new interface

### Decorator
- Add responsibilities to objects dynamically
- Alternative to subclassing for extending functionality
- Example: LoggingDecorator wraps service calls

### Facade
- Provide simplified interface to complex subsystem
- Example: PaymentFacade abstracts multiple payment processors

### Proxy
- Provide surrogate for another object
- Use for lazy loading, access control, logging
- Example: LazyLoadingProxy, CachingProxy

### Composite
- Treat individual objects and compositions uniformly
- Example: File/Folder tree structure

## Behavioral Patterns

### Strategy
- Define family of algorithms, make them interchangeable
- **Class-based**: Use ABC with concrete implementations
- **Functional** (preferred in Python): Use `Callable` type aliases
- Example: Ticket ordering strategies

```python
# ❌ Before: String flag controls behavior
class CustomerSupport:
    def __init__(self, strategy: str = "fifo"):
        self.strategy = strategy
    def process(self):
        if self.strategy == "fifo": ...    # Branching = OCP violation
        elif self.strategy == "filo": ...

# ✅ After: Callable strategy injected at call site
type Ordering = Callable[[list[Ticket]], list[Ticket]]

def fifo(tickets: list[Ticket]) -> list[Ticket]: return tickets.copy()
def filo(tickets: list[Ticket]) -> list[Ticket]: return list(reversed(tickets))

class CustomerSupport:
    def process(self, ordering: Ordering) -> None:
        for ticket in ordering(self.tickets): ...
```

### Observer
- Define one-to-many dependency between objects
- Decouple publishers from subscribers via event system
- Example: User registration with email, Slack, logging listeners

```python
# ❌ Before: register_new_user() directly calls email, Slack, logging
# ✅ After: post_event("user_registered", user) — listeners handle side effects
subscribers: dict[str, list[Callable]] = defaultdict(list)
def subscribe(event: str, handler: Callable): subscribers[event].append(handler)
def post_event(event: str, data: Any):
    for handler in subscribers[event]: handler(data)
```

### Command
- Encapsulate request as object
- Enable undo/redo, queuing
- Example: Transaction commands

### Template Method
- Define skeleton of algorithm in base class
- Let subclasses override specific steps
- Example: TradingBot with connect/analyze/decide steps

```python
class TradingBot(ABC):
    def check_prices(self, coin: str) -> None:
        self.connect()
        prices = self.get_market_data(coin)
        if self.should_buy(prices): print(f"Buy {coin}!")
        elif self.should_sell(prices): print(f"Sell {coin}!")

    @abstractmethod
    def should_buy(self, prices: list[float]) -> bool: ...
    @abstractmethod
    def should_sell(self, prices: list[float]) -> bool: ...

class AverageTrader(TradingBot):
    def should_buy(self, prices): return prices[-1] < sum(prices) / len(prices)
    def should_sell(self, prices): return prices[-1] > sum(prices) / len(prices)
```

### Chain of Responsibility
- Pass request along chain of handlers
- Example: Validation chain, middleware pipeline

### State
- Object behavior changes when internal state changes
- Example: Order states (Pending, Confirmed, Shipped)

### Iterator
- Access elements sequentially without exposing structure
- Usually built into language (foreach)

## When to Apply

- Don't force patterns — use when they solve actual problems
- Patterns should simplify, not complicate
- Consider pattern combinations for complex problems
- Document which patterns are used and why
- **Always show before/after** — demonstrate why the pattern improves the code
- In Python, prefer functional approaches (callables) over class-based where simpler

## Reference

See [`atstaeff/better-python`](https://github.com/atstaeff/better-python) for complete before/after examples of:
- Coupling & Cohesion (folders `1 - coupling and cohesion`)
- Dependency Inversion (`2 - dependency inversion`)
- Strategy Pattern (`3 - strategy pattern`)
- Observer Pattern (`4 - observer pattern`)
- Template Method & Bridge (`6 - template method & bridge`)
- Error Handling (`7 - dealing with errors`)
- MVC (`8 - mvc`)
- SOLID Principles (`9 - solid`)
- Object Creation (`10 - object creation`)

## Example Prompts

"Implement a caching mechanism using Proxy pattern"

"Design an extensible validation system using Chain of Responsibility"

"Create a document generation system using Strategy and Factory patterns"

"Refactor this code to use appropriate design patterns"
