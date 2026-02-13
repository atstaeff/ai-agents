# Clean Code

> Prinzipien fuer sauberen, lesbaren und wartbaren Code — sprachuebergreifend anwendbar.

---

## Kernprinzipien

### Naming

- Aussagekraeftige, aussprechbare Namen
- Suchbare Namen (keine Magic Numbers)
- Ein Konzept pro Name, konsistent im gesamten Codebase

### Funktionen

- Klein und fokussiert (Single Responsibility)
- Wenige Parameter (max. 3)
- Keine Flag-Argumente — separate Funktionen stattdessen
- Keine Seiteneffekte

### Error Handling

- Spezifische Exceptions mit Kontext
- Keine nackten `except:` / `catch`
- Error Handling von Business-Logik trennen

### DRY & KISS

- Don't Repeat Yourself — aber nicht auf Kosten der Lesbarkeit
- Keep It Simple — die einfachste Loesung ist meist die beste

## Beispiel: Before / After

=== "Before"
    ```python
    # ❌ Unklar, Magic Numbers, Flag Argument
    def calc(d, t, f=False):
        if f:
            return d * 0.9 * t
        return d * t
    ```

=== "After"
    ```python
    # ✅ Klar, benannte Konstanten, separate Funktionen
    DISCOUNT_RATE = 0.9

    def calculate_price(base_price: float, quantity: int) -> float:
        return base_price * quantity

    def calculate_discounted_price(base_price: float, quantity: int) -> float:
        return base_price * DISCOUNT_RATE * quantity
    ```

## Checkliste

- [x] Sprechende Variablen- und Funktionsnamen
- [x] Funktionen < 20 Zeilen, max. 3 Parameter
- [x] Keine Magic Numbers oder Strings
- [x] Spezifisches Error Handling
- [x] Kommentare erklaeren "warum", nicht "was"

## Verwandte Skills

- [SOLID Principles](solid-principles.md)
- [Design Patterns](design-patterns.md)
- [Practical Refactoring](practical-refactoring.md)

---

*Quelldatei: [`skills/software-engineering/clean-code.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/software-engineering/clean-code.md)*
