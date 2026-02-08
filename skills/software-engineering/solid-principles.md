# SOLID Principles

## Instructions for AI

Apply SOLID principles when designing and implementing code. Reference [`atstaeff/better-python`](https://github.com/atstaeff/better-python) for concrete Python before/after examples.

### Single Responsibility Principle (SRP)
- A class should have only one reason to change
- Each class/module should have a single, well-defined purpose
- Separate concerns into different classes

```python
# ❌ Before: Order handles data, price logic, AND payment
class Order:
    def add_item(self, name, quantity, price): ...
    def total_price(self): ...
    def pay(self, payment_type, security_code):  # SRP violation!
        if payment_type == "debit": ...
        elif payment_type == "credit": ...

# ✅ After: Order is data only, PaymentProcessor handles payments
class Order:
    def add_item(self, name, quantity, price): ...
    def total_price(self): ...

class PaymentProcessor:
    def pay_debit(self, order: Order, code: str): ...
    def pay_credit(self, order: Order, code: str): ...
```

### Open/Closed Principle (OCP)
- Software entities should be open for extension, closed for modification
- Use interfaces, abstract classes, and dependency injection
- Prefer composition over inheritance

```python
# ❌ Before: Adding PayPal = modifying PaymentProcessor
class PaymentProcessor:
    def pay_debit(self, order, code): ...
    def pay_credit(self, order, code): ...

# ✅ After: New payment methods = new classes, no modification
class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order: Order, security_code: str) -> None: ...

class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code): ...

class CreditPaymentProcessor(PaymentProcessor):
    def pay(self, order, security_code): ...

class PaypalPaymentProcessor(PaymentProcessor):  # Just add a new class
    def pay(self, order, security_code): ...
```

### Liskov Substitution Principle (LSP)
- Derived classes must be substitutable for their base classes
- Don't strengthen preconditions or weaken postconditions
- Subtypes should enhance, not limit, base behavior
- Example: Square should not extend Rectangle if it violates LSP

### Interface Segregation Principle (ISP)
- Clients should not depend on interfaces they don't use
- Create small, focused interfaces
- Split fat interfaces into multiple specific ones

```python
# ❌ Before: PaymentProcessor forces SMS auth on all implementations
class PaymentProcessor(ABC):
    @abstractmethod
    def auth_sms(self, code): ...   # Credit card doesn't need this!
    @abstractmethod
    def pay(self, order): ...

# ✅ After: Separate Authorizer from PaymentProcessor
class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool: ...

class SMSAuthorizer(Authorizer):
    def verify_code(self, code): self.authorized = True
    def is_authorized(self) -> bool: return self.authorized

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order) -> None: ...

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, code: str, authorizer: Authorizer): ...
    def pay(self, order):
        if not self.authorizer.is_authorized(): raise Exception("Not authorized")
        ...
```

### Dependency Inversion Principle (DIP)
- Depend on abstractions, not concretions
- High-level modules should not depend on low-level modules
- Use dependency injection to provide implementations

```python
# ❌ Before: Switch hardcodes LightBulb
class ElectricPowerSwitch:
    def __init__(self):
        self.bulb = LightBulb()  # Concrete dependency

# ✅ After: Switch depends on Switchable abstraction
class Switchable(ABC):
    @abstractmethod
    def turn_on(self): ...
    @abstractmethod
    def turn_off(self): ...

class LightBulb(Switchable): ...
class Fan(Switchable): ...

class ElectricPowerSwitch:
    def __init__(self, device: Switchable):  # Inject abstraction
        self.device = device
```

## Application Guidelines

When designing systems:
1. Start by identifying responsibilities
2. Define abstractions (interfaces) before implementations
3. Use dependency injection containers
4. Apply SOLID at the appropriate level (class, module, service)
5. Balance purity with pragmatism
6. **Always show before/after** to demonstrate the improvement

## Reference

See [`atstaeff/better-python`](https://github.com/atstaeff/better-python) folder `9 - solid/` for complete before/after Python implementations of all 5 SOLID principles.

## Example Prompts

"Design this feature following SOLID principles"

"Refactor this code to comply with the Single Responsibility Principle"

"Create an extensible architecture using Open/Closed Principle"

"Review this class hierarchy for SOLID violations"
