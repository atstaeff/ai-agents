# Principal Engineer Decisions

> Entscheidungsfindung auf Senior / Principal Engineer Level — strategisch denken, pragmatisch handeln.

---

## Entscheidungsframework

### Decision Matrix

| Kriterium | Option A | Option B | Gewicht |
|-----------|----------|----------|---------|
| Time-to-Market | ++ | + | Hoch |
| Wartbarkeit | + | ++ | Hoch |
| Skalierbarkeit | + | ++ | Mittel |
| Teamkompetenz | ++ | + | Mittel |
| Kosten | ++ | + | Niedrig |

### Entscheidungsprinzipien

| Prinzip | Beschreibung |
|---------|-------------|
| Reversible Decisions | Schnell entscheiden, spaeter aendern |
| Irreversible Decisions | Gruendlich analysieren, breit konsultieren |
| Two-Way Door | Entscheidung leicht rueckgaengig machbar → schnell treffen |
| One-Way Door | Schwer rueckgaengig → sorgfaeltig abwaegen |

## Senior-Level Denkweisen

- **Think in Systems** — Gesamtsystem betrachten, nicht nur die Komponente
- **Optimize for Change** — Code aendert sich, Architektur evolviert
- **Make the Right Thing Easy** — Pit of Success fuer das Team schaffen
- **Measure Before Optimizing** — Daten statt Bauchgefuehl
- **Teach, Don't Just Decide** — Team befaehigen, nicht bevormunden

## Wann eskalieren?

| Situation | Aktion |
|-----------|--------|
| Reversible, low impact | Selbst entscheiden, dokumentieren |
| Reversible, high impact | Team konsultieren, dann entscheiden |
| Irreversible, low impact | ADR schreiben, Review einholen |
| Irreversible, high impact | Breit konsultieren, ADR + Review |

## Verwandte Skills

- [Architecture Planning](architecture-planning.md) — Planungsmethodik
- [Communication](communication.md) — Entscheidungen kommunizieren

---

*Quelldatei: [`skills/general/principal-engineer-decisions.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/general/principal-engineer-decisions.md)*
