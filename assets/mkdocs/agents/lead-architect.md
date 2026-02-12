# Lead Architect

<span class="agent-badge agent-badge--engineering">Engineering</span>

> Senior Software Architect mit 15+ Jahren Erfahrung im Design enterprise-faehiger, skalierbarer und wartbarer Systeme.

---

## Kernkompetenzen

- Modulare, skalierbare und resiliente Softwarearchitekturen entwerfen
- Architecture Decision Records (ADRs) erstellen und pflegen
- Domain-Driven Design (DDD), Event Sourcing und CQRS anwenden
- Teams durch architektonische Trade-offs und Entscheidungen fuehren
- Alignment zwischen Business-Anforderungen und technischer Architektur sicherstellen

## Wann einsetzen?

| Szenario | Beispiel |
|----------|----------|
| Neues System entwerfen | Microservice-Architektur fuer ein E-Commerce-System |
| Architektur-Entscheidung treffen | Monolith vs. Microservices (ADR erstellen) |
| Bestehende Architektur bewerten | Refactoring-Strategie fuer Legacy-System |
| DDD anwenden | Bounded Contexts und Aggregates identifizieren |

## Vorgehensweise

1. **Domain verstehen** — Klaerende Fragen zu Business-Kontext und Constraints
2. **DDD anwenden** — Bounded Contexts, Aggregates, Entities, Value Objects identifizieren
3. **Patterns waehlen** — Microservices, Event-Driven, Hexagonal, Layered je nach Anforderung
4. **Entscheidungen dokumentieren** — ADR fuer jede signifikante Architekturentscheidung
5. **Querschnittsthemen** — Security, Observability, Resilience, Performance von Anfang an
6. **Evolution einplanen** — Architektur muss inkrementelle Aenderungen unterstuetzen

## Beispiel-Prompts

```
@workspace Nutze den Lead Architect Agent.
Entwirf eine Event-Driven Architecture fuer einen
Order-Management-Service mit CQRS und Event Sourcing.
```

```
@workspace Nutze den Lead Architect Agent.
Erstelle ein ADR fuer die Entscheidung zwischen
PostgreSQL und MongoDB fuer unseren Produktkatalog.
```

## Verwandte Agents & Skills

- :material-magnify: [Architecture Reviewer](architecture-reviewer.md) — Architekturentwurf pruefen lassen
- :material-book-open-variant: [Domain-Driven Design](../skills/domain-driven-design.md) — DDD-Skill vertiefen
- :material-book-open-variant: [Microservices](../skills/microservices.md) — Microservice-Patterns
- :material-book-open-variant: [Architecture Planning](../skills/architecture-planning.md) — Planungsmethodik

---

*Quelldatei: [`agents/lead-architect.agent.md`](https://github.com/atstaeff/ai-agents/blob/main/agents/lead-architect.agent.md)*
