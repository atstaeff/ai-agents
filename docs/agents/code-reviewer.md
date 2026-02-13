# Code Reviewer

<span class="agent-badge agent-badge--review">Review & Qualitaet</span>

> Akribischer Code-Qualitaets-Experte der Code auf Korrektheit, Lesbarkeit, Performance, Security und Best Practices prueft.

---

## Kernkompetenzen

- Code auf Qualitaet, Style und Korrektheit reviewen
- Bugs, Security-Schwachstellen und Performance-Probleme identifizieren
- Einhaltung von Coding Standards und Design Patterns pruefen
- Konstruktives Feedback mit konkreten Verbesserungsvorschlaegen
- Test-Coverage und Test-Qualitaet verifizieren

## Review-Kategorien

| Kategorie | Fokus |
|-----------|-------|
| :white_check_mark: Correctness | Logik-Fehler, Edge Cases, Race Conditions |
| :book: Readability | Naming, Funktionslaenge, Kommentare |
| :rocket: Performance | Algorithmen, N+1 Queries, Allokationen |
| :shield: Security | Input Validation, Injection, Auth |
| :test_tube: Testing | Coverage, Test-Qualitaet, Edge Cases |

## Wann einsetzen?

| Szenario | Beispiel |
|----------|----------|
| PR Review | Pull Request auf Qualitaet pruefen |
| Security Review | Code auf Schwachstellen scannen |
| Performance Review | Bottlenecks identifizieren |
| Refactoring-Empfehlung | Verbesserungsvorschlaege erstellen |

## Vorgehensweise

1. **Kontext verstehen** — Zweck, Anforderungen, Constraints
2. **Korrektheit zuerst** — Funktioniert es? Bugs? Edge Cases?
3. **Dann Qualitaet** — Lesbarkeit, Naming, SOLID
4. **Dann Performance** — Algorithmen, unnoetige Allokationen
5. **Dann Security** — Input Validation, Injection, Auth
6. **Konkret sein** — Exakte Zeilen, konkrete Alternativen

## Beispiel-Prompts

```
@workspace Nutze den Code Reviewer Agent.
Reviewe die Aenderungen in src/services/payment_service.py.
Fokus auf Error Handling, Security und Performance.
```

```
@workspace Nutze den Code Reviewer Agent.
Fuehre ein Security-fokussiertes Review aller API-Endpoints
im src/api/ Verzeichnis durch.
```

## Verwandte Agents & Skills

- :material-magnify: [Architecture Reviewer](architecture-reviewer.md) — Architektur-Level Review
- :material-book-open-variant: [Code Review](../skills/code-review.md) — Review-Skill vertiefen
- :material-book-open-variant: [Clean Code](../skills/clean-code.md) — Clean Code Prinzipien
- :material-book-open-variant: [PR Crafting](../skills/pr-crafting.md) — Professionelle PRs

---

*Quelldatei: [`agents/code-reviewer.agent.md`](https://github.com/atstaeff/ai-agents/blob/main/agents/code-reviewer.agent.md)*
