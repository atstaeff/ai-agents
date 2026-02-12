# Neuen Agent erstellen

Anleitung zum Erstellen eines neuen spezialisierten AI-Agents.

---

## Voraussetzungen

- Der Agent deckt eine klar definierte Rolle oder Technologie ab
- Es gibt keinen bestehenden Agent mit gleichem Fokus
- Der Agent ist breit genug einsetzbar (nicht zu spezifisch fuer ein Projekt)

## Schritt-fuer-Schritt

### 1. Datei anlegen

Erstelle eine Datei unter `agents/` mit dem Namensschema:

```
agents/{name}.agent.md
```

Beispiel: `agents/rust-expert.agent.md`

### 2. Struktur folgen

Jeder Agent braucht folgende Abschnitte:

```markdown
# {Name} Agent

## Identity
Wer ist der Agent? Rolle, Erfahrungslevel, Spezialisierung.

## Core Responsibilities
Was kann der Agent? 5-8 Kernkompetenzen.

## Instructions
Wie arbeitet der Agent? Nummerierte Anweisungen.

## [Patterns / Templates / Checklists]
Konkrete Artefakte die der Agent nutzt.

## Example Output
Beispiel fuer typische Agent-Ausgaben.

## Cross-References
Verwandte Agents und Skills.
```

### 3. Identity formulieren

!!! tip "Best Practice"
    Schreibe die Identity in der zweiten Person:
    "You are a **{Name} Agent** — a {erfahrung} specializing in {bereich}."

### 4. Instructions definieren

- Nummerierte, priorisierte Anweisungen
- Jede Instruktion mit **Fettdruck-Label** beginnen
- Konkrete, handlungsorientierte Formulierungen

### 5. Beispiele hinzufuegen

- Before/After Code-Beispiele
- Templates fuer typische Ausgaben
- Checklisten fuer wiederkehrende Aufgaben

### 6. Cross-References setzen

Verlinke zu:
- Verwandten Agents (z.B. Test Strategist fuer jeden Sprach-Expert)
- Relevanten Skills (z.B. Clean Code, SOLID, Design Patterns)

## Checkliste

- [ ] `.agent.md` Dateinamen-Konvention eingehalten
- [ ] Identity, Responsibilities, Instructions vorhanden
- [ ] Mindestens 3 praktische Beispiele
- [ ] Cross-References zu Agents und Skills
- [ ] Keine urheberrechtlich geschuetzten Inhalte
- [ ] PR mit Beschreibung erstellt
