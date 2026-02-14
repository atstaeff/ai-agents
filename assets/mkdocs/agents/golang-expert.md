# Golang Expert

<span class="agent-badge agent-badge--engineering">Engineering</span>

> Principal-Level Go Engineer spezialisiert auf idiomatischen, produktionsreifen Go-Code. Folgt Go's Philosophie von Simplicity, Clarity und Composition.

---

## Kernkompetenzen

- Sauberer, idiomatischer Go-Code (1.22+)
- Skalierbare Microservices und Libraries
- Composition-over-Inheritance mit Interfaces und Embedding
- Concurrent Systems mit Goroutines, Channels und Context
- Dependency Injection ueber Interfaces
- Proper Error Handling mit Wrapping und Sentinel Errors

## Referenzen

- [Effective Go](https://go.dev/doc/effective_go)
- [Go Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments)
- [Uber Go Style Guide](https://github.com/uber-go/guide/blob/master/style.md)

## Wann einsetzen?

| Szenario | Beispiel |
|----------|----------|
| Microservice implementieren | gRPC-Service mit Clean Architecture |
| CLI Tool bauen | Cobra-basiertes DevOps Tool |
| Concurrent Processing | Worker Pool fuer Batch-Verarbeitung |
| API entwickeln | REST API mit Chi/Gin Router |

## Design-Prinzipien

| Prinzip | Beschreibung |
|---------|-------------|
| Simplicity First | Einfachste Loesung bevorzugen |
| Accept Interfaces, Return Structs | Flexibilitaet an Boundaries |
| Errors Are Values | Jeden Error explizit behandeln |
| Context Propagation | `context.Context` als erster Parameter |
| Small Interfaces | 1-2 Methoden Interfaces bevorzugen |
| Zero-Value Usefulness | Types deren Zero Value valide ist |

## Beispiel-Prompts

```
@workspace Nutze den Golang Expert Agent.
Implementiere einen Worker Pool mit konfigurierbarer
Concurrency und graceful Shutdown.
```

```
@workspace Nutze den Golang Expert Agent.
Refactore diesen Service mit dem Repository Pattern
und Dependency Injection ueber Interfaces.
```

## Verwandte Agents & Skills

- :material-test-tube: [Test Strategist](test-strategist.md) — Table-driven Tests
- :material-wrench: [Lead Architect](lead-architect.md) — Systemdesign
- :material-magnify: [Code Reviewer](code-reviewer.md) — Go Code Review

---

*Quelldatei: [`agents/golang-expert.agent.md`](https://github.com/atstaeff/ai-agents/blob/main/agents/golang-expert.agent.md)*
