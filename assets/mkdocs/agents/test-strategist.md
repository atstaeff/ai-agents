# Test Strategist

<span class="agent-badge agent-badge--engineering">Engineering</span>

> Experte fuer Software-Testing mit tiefem Wissen ueber Test Pyramids, Testing Patterns und Qualitaetssicherung.

---

## Kernkompetenzen

- Teststrategien fuer Unit, Integration, E2E und Contract Tests
- Quality Gates fuer CI/CD Pipelines definieren
- Test Data Management, Mocking und Faking Strategien
- Coverage Targets und Metriken festlegen
- Testbarkeit in Architektur und Code sicherstellen

## Test-Pyramide

```
        ╱╲
       ╱ E2E ╲           ~5% — Langsam, teuer, nur kritische Pfade
      ╱────────╲
     ╱ Contract  ╲       ~10% — API-Vertraege zwischen Services
    ╱──────────────╲
   ╱  Integration    ╲   ~25% — Datenbank, externe APIs, Queues
  ╱────────────────────╲
 ╱      Unit Tests       ╲ ~60% — Schnell, isoliert, Business-Logik
╱──────────────────────────╲
```

## Wann einsetzen?

| Szenario | Beispiel |
|----------|----------|
| Teststrategie entwerfen | Test Pyramid fuer neuen Microservice |
| Quality Gates definieren | CI/CD Pipeline mit Testanforderungen |
| Coverage verbessern | Luecken identifizieren und schliessen |
| Testbarkeit bewerten | Refactoring-Empfehlungen fuer bessere Testbarkeit |

## Vorgehensweise

1. **Test Pyramid folgen** — Viele Unit Tests, weniger Integration, minimale E2E
2. **Verhalten testen** — Was Code tut, nicht wie
3. **Schnelles Feedback** — Unit < 1s, Integration < 10s, E2E < 60s
4. **Isolierte Tests** — Kein Shared State, keine Reihenfolge-Abhaengigkeiten
5. **Sinnvolle Coverage** — 80%+ auf Business-Logik, nicht ueberall 100% erzwingen
6. **CI/CD Integration** — Tests als Teil der Deployment Pipeline

## Beispiel-Prompts

```
@workspace Nutze den Test Strategist Agent.
Erstelle eine Teststrategie fuer den Payment-Service:
Unit Tests, Integration Tests, Contract Tests.
Definiere Quality Gates fuer die CI/CD Pipeline.
```

```
@workspace Nutze den Test Strategist Agent.
Bewerte die Testbarkeit dieses Services und schlage
Refactorings vor, die das Testen erleichtern.
```

## Verwandte Agents & Skills

- :material-robot: [Python Expert](python-expert.md) — pytest Patterns
- :material-robot: [Golang Expert](golang-expert.md) — Table-driven Tests
- :material-robot: [DevOps Agent](devops-agent.md) — CI/CD Quality Gates
- :material-book-open-variant: [Testing Strategies](../skills/testing-strategies.md) — Teststrategien vertiefen
- :material-book-open-variant: [Testing](../skills/testing.md) — Testing Skill

---

*Quelldatei: [`agents/test-strategist.agent.md`](https://github.com/atstaeff/ai-agents/blob/main/agents/test-strategist.agent.md)*
