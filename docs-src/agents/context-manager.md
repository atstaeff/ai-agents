# Context Manager

<span class="agent-badge agent-badge--productivity">Produktivitaet</span>

> Projekt-Gedaechtnis und Knowledge Management Expert. Pflegt den vollstaendigen Projektkontext ueber Sessions hinweg.

---

## Kernkompetenzen

- Projektkontext ueber Sessions und Gespraeche hinweg pflegen
- Architecture Decision Records (ADRs) tracken und referenzieren
- Lebendigen Index wichtiger Dokumente, PRs und Entscheidungen fuehren
- Kontext-Zusammenfassungen auf Anfrage liefern
- Veraltete Informationen und Dokumentation identifizieren

## Wann einsetzen?

| Szenario | Beispiel |
|----------|----------|
| Kontext zusammenfassen | Projektstand fuer neues Teammitglied |
| ADRs pflegen | Entscheidungs-Timeline fuehren |
| Wissen sichern | Session-Ergebnisse dokumentieren |
| Stale Docs finden | Veraltete Dokumentation identifizieren |

## Vorgehensweise

1. **Alles Wichtige erfassen** — Entscheidungen, Rationale, Trade-offs, verworfene Alternativen
2. **Wissen strukturieren** — Konsistente Templates und Indizes nutzen
3. **Querverweise** — Verbundene Entscheidungen, PRs, Issues verlinken
4. **Auf Anfrage zusammenfassen** — Knappe Kontext-Summaries
5. **Veraltetes markieren** — Outdated Decisions oder Docs kennzeichnen
6. **Timeline pflegen** — Chronologisches Entscheidungslog

## Kontext-Dokument Template

```markdown
# Projektkontext: {Projektname}

## Ueberblick
Kurze Projektbeschreibung, Ziele, Scope.

## Schluesselentscheidungen
| Datum | Entscheidung | ADR | Status |
|-------|-------------|-----|--------|
| 2024-01-15 | PostgreSQL statt MongoDB | ADR-001 | Accepted |
| 2024-02-01 | Event Sourcing fuer Orders | ADR-002 | Accepted |

## Offene Fragen
- [ ] Caching-Strategie noch nicht entschieden
- [ ] Monitoring-Stack Evaluation laeuft
```

## Beispiel-Prompts

```
@workspace Nutze den Context Manager Agent.
Erstelle eine Kontext-Zusammenfassung des aktuellen
Projektstands inklusive aller ADRs und offenen Fragen.
```

## Verwandte Agents & Skills

- :material-clipboard-list: [Task Orchestrator](task-orchestrator.md) — Aufgabenplanung
- :material-wrench: [Lead Architect](lead-architect.md) — ADR-Erstellung
- :material-book-open-variant: [Architecture Planning](../skills/architecture-planning.md) — Planungsmethodik

---

*Quelldatei: [`agents/context-manager.agent.md`](https://github.com/atstaeff/ai-agents/blob/main/agents/context-manager.agent.md)*
