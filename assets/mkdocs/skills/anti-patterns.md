# Anti-Patterns

> Haeufige Softwardesign-Fehler erkennen und beheben — mit konkreten Before/After Beispielen.

---

## Haeufige Anti-Patterns

### God Class

| Problem | Loesung |
|---------|---------|
| Eine Klasse macht alles | Single Responsibility, Extract Class |

### Primitive Obsession

| Problem | Loesung |
|---------|---------|
| Strings/Ints fuer Domain-Konzepte | Value Objects nutzen |

### Feature Envy

| Problem | Loesung |
|---------|---------|
| Methode nutzt mehr Daten einer anderen Klasse | Move Method zur richtigen Klasse |

### Magic Numbers

| Problem | Loesung |
|---------|---------|
| Hardcoded Zahlen ohne Erklaerung | Benannte Konstanten |

### Shotgun Surgery

| Problem | Loesung |
|---------|---------|
| Kleine Aenderung erfordert viele Dateien | Zusammengehoerige Logik buendeln |

### Spaghetti Code

| Problem | Loesung |
|---------|---------|
| Keine klare Struktur, verschachtelte Logik | Funktionen extrahieren, Schichten einfuehren |

## Architektur-Anti-Patterns

| Anti-Pattern | Beschreibung | Alternative |
|-------------|-------------|-------------|
| Big Ball of Mud | Keine erkennbare Struktur | Bounded Contexts, Layered Architecture |
| Distributed Monolith | Microservices ohne echte Entkopplung | Echte Service-Boundaries, Async Communication |
| Golden Hammer | Ein Tool/Pattern fuer alles | Passendes Tool pro Problem |
| Premature Optimization | Optimieren ohne Messung | Messen → Identifizieren → Optimieren |

## Verwandte Skills

- [Clean Code](clean-code.md) — Praevention
- [Practical Refactoring](practical-refactoring.md) — Anti-Patterns beheben
- [Design Patterns](design-patterns.md) — Richtige Patterns

---

*Quelldatei: [`skills/anti-patterns/SKILL.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/anti-patterns/SKILL.md)*
