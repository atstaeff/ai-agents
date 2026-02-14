# Technical Debt

> Technische Schulden erkennen, bewerten, priorisieren und systematisch abbauen.

---

## Was ist Technical Debt?

Bewusste oder unbewusste Kompromisse in der Codequalitaet, die zukuenftige Aenderungen erschweren.

### Typen

| Typ | Beschreibung | Beispiel |
|-----|-------------|---------|
| Deliberate | Bewusst eingegangen | "Ship now, refactor later" |
| Inadvertent | Unbewusst entstanden | Fehlendes Wissen, schlechte Patterns |
| Bit Rot | Durch Alterung | Veraltete Dependencies, Legacy Code |
| Design Debt | Architektur-Schwaechen | Monolith statt Microservices |

## Bewertungsmatrix

| Dimension | Niedrig | Mittel | Hoch |
|-----------|---------|--------|------|
| Impact auf Velocity | Kaum spuerbar | Feature dauern laenger | Entwicklung blockiert |
| Risiko | Kein Ausfallrisiko | Gelegentliche Bugs | Produktionsfehler moeglich |
| Aufwand Behebung | < 1 Tag | 1-5 Tage | > 1 Woche |

## Abbau-Strategien

1. **Boy Scout Rule** — Code besser hinterlassen als vorgefunden
2. **Dedicated Sprint** — Regelmaessige Refactoring-Sprints
3. **20% Rule** — 20% der Kapazitaet fuer Debt-Abbau reservieren
4. **Strangler Fig** — Schrittweise durch neue Implementierung ersetzen

## Verwandte Skills

- [Practical Refactoring](practical-refactoring.md) — Refactoring-Taktiken
- [Clean Code](clean-code.md) — Praevention

---

*Quelldatei: [`skills/project-management/technical-debt.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/project-management/technical-debt.md)*
