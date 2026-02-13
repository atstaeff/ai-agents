# Marp Presentations

> Professionelle Praesentationen mit Marp (Markdown Presentation Ecosystem) — Syntax, Themes und Best Practices.

---

## Grundlagen

Marp verwandelt Markdown in Slide Decks (HTML, PDF, PPTX).

### Basis-Syntax

```markdown
---
marp: true
theme: default
paginate: true
---

# Slide 1: Titel

Content fuer die erste Folie.

---

# Slide 2: Naechstes Thema

- Punkt 1
- Punkt 2
```

## Directives

| Directive | Zweck |
|-----------|-------|
| `marp: true` | Marp aktivieren |
| `theme: default/gaia/uncover` | Theme waehlen |
| `paginate: true` | Seitenzahlen anzeigen |
| `header: "Text"` | Kopfzeile |
| `footer: "Text"` | Fusszeile |
| `backgroundColor: #fff` | Hintergrundfarbe |

## Layouts

```markdown
<!-- _class: lead -->
# Titelfolie
Zentriert, grosse Schrift

---

<!-- _class: invert -->
# Invertierte Folie
Dunkler Hintergrund, helle Schrift
```

## Verfuegbare Templates

Im Repository unter `marp-templates/`:

| Template | Zweck |
|----------|-------|
| Client Pitch | Kundenpraesentationen |
| Technical Deep-Dive | Technische Vortraege |
| Project Review | Sprint Reviews, Status Updates |

## Verwandte Agents

- :material-robot: [Presentation Agent](../agents/presentation-agent.md)

---

*Quelldatei: [`skills/marp-presentations/SKILL.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/marp-presentations/SKILL.md)*
