# Golang Patterns

> Idiomatische Go-Patterns, Concurrency, Interface Design und Best Practices fuer produktionsreifen Go-Code.

---

## Ueberblick

Der Golang Patterns Skill umfasst:

- **Interface Design** — Accept Interfaces, Return Structs
- **Concurrency** — Goroutines, Channels, Worker Pools, Context
- **Error Handling** — Wrapping, Sentinel Errors, Custom Errors
- **Project Structure** — Standard Go Layout, Package Design
- **Testing** — Table-Driven Tests, Mocking mit Interfaces

## Kernthemen

### Interface-Prinzipien

| Prinzip | Beschreibung |
|---------|-------------|
| Kleine Interfaces | 1-2 Methoden bevorzugen |
| Accept Interfaces | Funktionsparameter als Interface |
| Return Structs | Konkrete Typen zurueckgeben |
| Composition | Interface Embedding fuer groessere APIs |

### Concurrency Patterns

| Pattern | Anwendungsfall |
|---------|---------------|
| Worker Pool | Parallelverarbeitung mit begrenzter Concurrency |
| Fan-Out/Fan-In | Arbeit verteilen und Ergebnisse sammeln |
| Pipeline | Datenverarbeitung in Stufen |
| Context Cancellation | Graceful Shutdown und Timeouts |

### Error Handling

- `fmt.Errorf("...: %w", err)` fuer Error Wrapping
- Sentinel Errors (`var ErrNotFound = errors.New(...)`)
- Custom Error Types mit `Is()` und `As()` Support

## Verwandte Agents

- :material-robot: [Golang Expert](../agents/golang-expert.md)
- :material-robot: [Code Reviewer](../agents/code-reviewer.md)

---

*Quelldatei: [`skills/golang-patterns/SKILL.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/golang-patterns/SKILL.md)*
