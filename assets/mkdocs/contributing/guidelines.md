# Guidelines

> Qualitaetsstandards und Konventionen fuer Beitraege zum Copilot Expert Hub.

---

## Allgemeine Konventionen

### Dateinamen

- Kleinbuchstaben mit Bindestrichen: `mein-skill-name.md`
- Agents: `{name}.agent.md`
- Skills: `{name}.md` oder `SKILL.md` im Unterverzeichnis

### Markdown-Standards

- Ueberschriften: `#` fuer Titel, `##` fuer Abschnitte, `###` fuer Unterabschnitte
- Code-Bloecke mit Sprachkennung: ` ```python `
- Listen konsistent (entweder `-` oder `*`)
- Tabellen fuer strukturierte Informationen

### Sprache

- Agent- und Skill-Quelldateien: **Englisch**
- Dokumentationsseiten (MkDocs): **Deutsch** (Zielgruppe: Entwickler-Teams)
- Code-Beispiele und Kommentare: **Englisch**

## Inhaltliche Standards

### Agents

| Anforderung | Pflicht |
|------------|---------|
| Identity-Abschnitt | ✅ |
| Core Responsibilities (5-8) | ✅ |
| Nummerierte Instructions | ✅ |
| Code-Beispiele | ✅ |
| Before/After Demos | Empfohlen |
| Cross-References | ✅ |

### Skills

| Anforderung | Pflicht |
|------------|---------|
| "Instructions for AI" Abschnitt | ✅ |
| Best Practices (✅) | ✅ |
| Anti-Patterns (❌) | ✅ |
| Code-Beispiele | ✅ |
| Example Prompts | Empfohlen |
| Related Skills | ✅ |

## Code-Beispiele

### Sprachen

- **Python** — Primaersprache, fuer die meisten Beispiele
- **Go** — Fuer Concurrency, Microservices, CLIs
- **TypeScript** — Fuer Frontend-Beispiele
- **Dart** — Fuer Flutter/Mobile-Beispiele
- **Terraform** — Fuer Infrastructure-as-Code

### Format

```python
# ❌ Before: Problematischer Code mit Erklaerung
def bad_example():
    pass

# ✅ After: Verbesserter Code mit Erklaerung
def good_example():
    pass
```

## Pull Request Prozess

1. Fork erstellen und Branch anlegen
2. Aenderungen umsetzen und lokal testen
3. PR mit klarer Beschreibung erstellen
4. Review abwarten und Feedback einarbeiten
5. Nach Approval wird gemergt

---

*Quelldateien: [`CONTRIBUTING.md`](https://github.com/atstaeff/ai-agents/blob/main/CONTRIBUTING.md) · [`docs/GUIDELINES.md`](https://github.com/atstaeff/ai-agents/blob/main/docs/GUIDELINES.md)*
