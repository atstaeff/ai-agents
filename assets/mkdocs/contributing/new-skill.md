# Neuen Skill erstellen

Anleitung zum Erstellen einer neuen technischen Wissensdatenbank (Skill).

---

## Voraussetzungen

- Der Skill passt in eine bestehende Kategorie oder begruendet eine neue
- Es existiert kein Skill mit gleichem Fokus
- Der Skill ist breit anwendbar fuer AI-gestuetzte Entwicklung

## Schritt-fuer-Schritt

### 1. Kategorie waehlen

| Kategorie | Verzeichnis | Beispiele |
|-----------|------------|-----------|
| Sprach-Patterns | `skills/{sprache}-patterns/` | Python, Golang, Flutter |
| Software Engineering | `skills/software-engineering/` | Clean Code, SOLID |
| Architektur | `skills/architecture/` | Microservices, DDD |
| Projekt & Team | `skills/team-collaboration/` | PR Crafting, Incident Response |
| Weitere | `skills/{thema}/` | Anti-Patterns |

### 2. Datei anlegen

```
skills/{kategorie}/{skill-name}.md
# oder
skills/{skill-name}/SKILL.md
```

### 3. Template verwenden

Kopiere die Vorlage aus `templates/skill-template.md`:

```markdown
# {Skill Name}

## Instructions for AI
Klare Anweisungen fuer den AI-Agent.

## [Hauptthema 1]
Detaillierte Erklaerung mit Beispielen.

## Best Practices
✅ Good Practice 1
✅ Good Practice 2

## Anti-Patterns
❌ Bad Practice 1
❌ Bad Practice 2

## Example Prompts
"Beispiel-Prompt 1"

## Related Skills
- [Verwandter Skill 1]
```

### 4. "Instructions for AI" schreiben

Dieser Abschnitt ist **der wichtigste** — er steuert, wie der Agent den Skill anwendet.

!!! tip "Best Practice"
    - Spezifisch und handlungsorientiert formulieren
    - "Wie" beschreiben, nicht nur "Was"
    - Konkrete Beispiele einbinden
    - Edge Cases beruecksichtigen

### 5. Beispiele bereitstellen

- ✅ / ❌ Before/After Vergleiche
- Code in Python, Go oder TypeScript
- Praxisnahe Szenarien

## Checkliste

- [ ] Richtige Kategorie und Verzeichnis gewaehlt
- [ ] Template-Struktur eingehalten
- [ ] "Instructions for AI" klar formuliert
- [ ] Mindestens 2 Code-Beispiele (Good/Bad)
- [ ] Related Skills verlinkt
- [ ] PR mit Beschreibung erstellt
