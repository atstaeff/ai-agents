# Code Review

> Guidelines, Checklisten und Best Practices fuer effektive Code Reviews.

---

## Review-Prozess

1. **Kontext verstehen** — PR-Beschreibung, Ticket, Anforderungen lesen
2. **Big Picture** — Architektur, Abhaengigkeiten, Datenfluss pruefen
3. **Details** — Logik, Edge Cases, Naming, Error Handling
4. **Tests** — Coverage, Qualitaet, Edge Cases abgedeckt?
5. **Feedback** — Konstruktiv, spezifisch, mit Alternativen

## Review-Checkliste

### Korrektheit
- [ ] Logik ist richtig, Edge Cases behandelt
- [ ] Error Handling vollstaendig
- [ ] Keine Race Conditions oder Memory Leaks

### Qualitaet
- [ ] Sprechende Namen fuer Variablen, Funktionen, Klassen
- [ ] Funktionen sind kurz und fokussiert
- [ ] SOLID Principles eingehalten
- [ ] Keine Code-Duplizierung

### Performance
- [ ] Keine N+1 Queries
- [ ] Algorithmus-Effizienz angemessen
- [ ] Keine unnoetige Allokationen

### Security
- [ ] Input Validation vorhanden
- [ ] Keine SQL Injection / XSS Risiken
- [ ] Authentication/Authorization korrekt
- [ ] Keine Secrets im Code

### Tests
- [ ] Neue Logik hat Tests
- [ ] Edge Cases abgedeckt
- [ ] Tests sind lesbar und wartbar

## Feedback-Regeln

!!! tip "Konstruktives Feedback"
    - **Spezifisch**: "Zeile 42: `user_list` waere klarer als `ul`"
    - **Begruendet**: "Weil `ul` wie ein HTML-Element klingt"
    - **Mit Alternative**: "Vorschlag: `active_users`"

!!! warning "Vermeiden"
    - Vage Kritik: "Das ist nicht gut"
    - Persoenliche Angriffe: "Du machst immer..."
    - Bikeshedding bei unwichtigen Details

## Verwandte Skills

- [Clean Code](clean-code.md)
- [PR Crafting](pr-crafting.md)

---

*Quelldatei: [`skills/software-engineering/code-review.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/software-engineering/code-review.md)*
