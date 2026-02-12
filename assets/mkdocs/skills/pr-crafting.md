# PR Crafting

> Professionelle Pull Requests erstellen — klare Beschreibung, sinnvolle Commits, hilfreiche Reviews.

---

## PR-Struktur

```markdown
## Was
Kurze Beschreibung der Aenderung.

## Warum
Motivation, Ticket-Referenz, Business-Kontext.

## Wie
Technischer Ansatz, Architekturentscheidungen.

## Testing
Wie wurde getestet? Welche Testfaelle?

## Screenshots
Bei UI-Aenderungen: Vorher/Nachher.

## Checklist
- [ ] Tests geschrieben und gruen
- [ ] Dokumentation aktualisiert
- [ ] Keine Breaking Changes
- [ ] Security-Review (falls relevant)
```

## Best Practices

| Praxis | Beschreibung |
|--------|-------------|
| Klein halten | < 400 Zeilen, ein logischer Change |
| Selbst-Review | PR vor dem Erstellen selbst reviewen |
| CI muss gruen sein | Nie reviewen wenn CI rot |
| Commit Messages | Conventional Commits Format |
| Draft PRs | Fuer fruehes Feedback nutzen |

## Commit-Konvention

```
feat(user): add password reset functionality
fix(auth): handle expired token gracefully
docs(api): update endpoint documentation
refactor(payment): extract strategy pattern
test(order): add edge case for empty cart
```

## Verwandte Skills

- [Code Review](code-review.md) — Review-Seite
- [Agile Methodologies](agile-methodologies.md)

---

*Quelldatei: [`skills/team-collaboration/pr-crafting.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/team-collaboration/pr-crafting.md)*
