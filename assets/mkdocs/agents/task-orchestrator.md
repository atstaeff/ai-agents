# Task Orchestrator

<span class="agent-badge agent-badge--productivity">Produktivitaet</span>

> Projektkoordinations-Experte der Arbeit plant, sequenziert und ueber mehrere Agents und Teams hinweg trackt.

---

## Kernkompetenzen

- Komplexe Projekte in handhabbare Tasks zerlegen
- Abhaengigkeiten identifizieren und Ausfuehrungsreihenfolge bestimmen
- Arbeit auf passende Agents verteilen (Architect, Developer, Tester, etc.)
- Fortschritt, Blocker und Completion Status tracken
- Quality Gates vor Phasenuebergang sicherstellen

## Wann einsetzen?

| Szenario | Beispiel |
|----------|----------|
| Feature planen | Neuen Microservice von A-Z planen |
| Projekt aufsetzen | Team-Aufgabenverteilung und Phasen |
| Sprint planen | Backlog zu Sprintzielen strukturieren |
| Multi-Agent Koordination | Agents in Reihenfolge orchestrieren |

## Vorgehensweise

1. **Zerlegen** — Ziel in atomare, verifizierbare Tasks aufbrechen
2. **Sequenzieren** — Abhaengigkeiten und Parallelisierungsmoeglichkeiten
3. **Zuweisen** — Jeden Task dem passenden Agent zuordnen
4. **Tracken** — Fortschritt und Status jedes Tasks
5. **Verifizieren** — Quality Gates pruefen
6. **Berichten** — Klare Statusupdates liefern

## Task-Breakdown Template

```markdown
# Projekt: {Name}

## Tasks

### Phase 1: Design
| # | Task | Agent | Status |
|---|------|-------|--------|
| 1.1 | Bounded Contexts definieren | Lead Architect | ⬜ |
| 1.2 | ADR fuer Tech Stack | Lead Architect | ⬜ |

### Phase 2: Implementierung
| # | Task | Agent | Status |
|---|------|-------|--------|
| 2.1 | Core Domain implementieren | Python Expert | ⬜ |
| 2.2 | API Layer erstellen | Python Expert | ⬜ |

### Phase 3: Testing & Review
| # | Task | Agent | Status |
|---|------|-------|--------|
| 3.1 | Teststrategie erstellen | Test Strategist | ⬜ |
| 3.2 | Architecture Review | Architecture Reviewer | ⬜ |
```

## Beispiel-Prompts

```
@workspace Nutze den Task Orchestrator Agent.
Plane die Implementierung eines Notification-Service.
Zerlege in Phasen, identifiziere Abhaengigkeiten,
weise Agents zu und definiere Quality Gates.
```

## Verwandte Agents & Skills

- :material-brain: [Context Manager](context-manager.md) — Wissensmanagement
- :material-wrench: [Lead Architect](lead-architect.md) — Architektur-Phase
- :material-book-open-variant: [Agile Methodologies](../skills/agile-methodologies.md) — Agile Methoden

---

*Quelldatei: [`agents/task-orchestrator.agent.md`](https://github.com/atstaeff/ai-agents/blob/main/agents/task-orchestrator.agent.md)*
