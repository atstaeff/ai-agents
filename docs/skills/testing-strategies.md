# Testing Strategies

> Teststrategien, Test Pyramid, TDD und sprachuebergreifende Testing Best Practices.

---

## Test-Pyramide

```
        ╱╲
       ╱ E2E ╲           ~5% — Kritische User Journeys
      ╱────────╲
     ╱ Contract  ╲       ~10% — API-Vertraege
    ╱──────────────╲
   ╱  Integration    ╲   ~25% — DB, externe Services
  ╱────────────────────╲
 ╱      Unit Tests       ╲ ~60% — Business-Logik
╱──────────────────────────╲
```

## Test-Arten

| Art | Scope | Speed | Zweck |
|-----|-------|-------|-------|
| Unit | Einzelne Funktion/Klasse | < 1s | Business-Logik verifizieren |
| Integration | Module + externe Systeme | < 10s | Zusammenspiel pruefen |
| Contract | API-Grenzen | < 5s | API-Kompatibilitaet |
| E2E | Gesamtsystem | < 60s | Kritische User Flows |

## Best Practices

### Arrange-Act-Assert (AAA)

```python
def test_discount_applied_for_premium_users():
    # Arrange
    user = User(tier="premium")
    cart = Cart(items=[Item(price=100)])

    # Act
    total = calculate_total(cart, user)

    # Assert
    assert total == 90  # 10% premium discount
```

### Testbare Architektur

- Dependency Injection statt hard-coded Dependencies
- Interfaces/Protocols fuer externe Systeme
- Pure Functions wo moeglich
- Deterministische Tests (keine Zufallswerte, fixe Timestamps)

## Coverage-Ziele

| Bereich | Ziel | Begruendung |
|---------|------|-------------|
| Business-Logik | 80%+ | Kernwertschoepfung schuetzen |
| API-Endpunkte | 90%+ | Schnittstelle stabil halten |
| UI-Komponenten | 70%+ | Regressions vermeiden |
| Infrastruktur | 50%+ | Grundlegende Funktion sichern |

## Verwandte Skills

- [Testing](testing.md) — Testing Patterns Skill
- [Clean Code](clean-code.md) — Testbarer Code

---

*Quelldatei: [`skills/software-engineering/testing-strategies.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/software-engineering/testing-strategies.md)*
