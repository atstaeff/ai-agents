# Skills-Katalog

Skills sind **technische Wissensdatenbanken**, die Agents nutzten, um fundierte Empfehlungen zu geben. Jeder Skill enthaelt Best Practices, Patterns, Code-Beispiele und Anti-Patterns.

---

## Sprach-Patterns

Sprachspezifische Patterns und Best Practices.

| Skill | Beschreibung | Fuer Agent |
|-------|-------------|------------|
| [Python Patterns](python-patterns.md) | Idiomatisches Python, Design Patterns, SOLID | Python Expert |
| [Golang Patterns](golang-patterns.md) | Idiomatic Go, Concurrency, Interfaces | Golang Expert |
| [Flutter Patterns](flutter-patterns.md) | Dart/Flutter, BLoC, Clean Architecture | Flutter & iOS Expert |
| [Frontend Patterns](frontend-patterns.md) | TypeScript, Vue.js, Angular Patterns | Frontend Expert |

## Software Engineering

Sprachuebergreifende Engineering-Prinzipien.

| Skill | Beschreibung |
|-------|-------------|
| [Clean Code](clean-code.md) | Naming, Funktionen, Error Handling, DRY |
| [SOLID Principles](solid-principles.md) | SRP, OCP, LSP, ISP, DIP mit Beispielen |
| [Design Patterns](design-patterns.md) | Strategy, Observer, Factory, Repository |
| [Code Review](code-review.md) | Review-Guidelines, Checklisten, Feedback |
| [Testing Strategies](testing-strategies.md) | Test Pyramid, TDD, Mocking, Coverage |
| [Practical Refactoring](practical-refactoring.md) | Refactoring-Taktiken und -Workflows |

## Architektur

Architektur-Patterns und Design-Entscheidungen.

| Skill | Beschreibung |
|-------|-------------|
| [Microservices](microservices.md) | Service-Schnitt, Kommunikation, Resilience |
| [Domain-Driven Design](domain-driven-design.md) | Bounded Contexts, Aggregates, Events |
| [Cloud-Native](cloud-native.md) | 12-Factor, Containers, Serverless |
| [API Design](api-design.md) | REST, gRPC, Versionierung, Error Handling |
| [Security](security.md) | AuthN/AuthZ, Input Validation, Encryption |
| [Performance](performance.md) | Caching, Indexing, Profiling, Optimization |

## Cloud & DevOps

Cloud-Infrastruktur und Operations.

| Skill | Beschreibung |
|-------|-------------|
| [GCP Patterns](gcp-patterns.md) | Cloud Run, Pub/Sub, BigQuery, Terraform |
| [Testing](testing.md) | Testing Patterns, Fixtures, Mocking |
| [DevOps & CI/CD](devops-cicd.md) | Pipelines, GitOps, Deployment Strategies |

## Projekt & Team

Zusammenarbeit, Kommunikation und Projektmanagement.

| Skill | Beschreibung |
|-------|-------------|
| [Agile Methodologies](agile-methodologies.md) | Scrum, Kanban, Sprint Planning |
| [Technical Debt](technical-debt.md) | Bewertung, Priorisierung, Abbau |
| [PR Crafting](pr-crafting.md) | Professionelle Pull Requests |
| [Progress Sync](progress-sync.md) | Standup, Status Updates, Reporting |
| [Feature Discovery](feature-discovery.md) | Anforderungsermittlung, Story Mapping |
| [Incident Response](incident-response.md) | Incident Management, Postmortems |

## Weitere Skills

| Skill | Beschreibung |
|-------|-------------|
| [Anti-Patterns](anti-patterns.md) | Haeufige Fehler und wie man sie vermeidet |
| [Marp Presentations](marp-presentations.md) | Marp Syntax, Templates, Styling |
| [Communication](communication.md) | Technische Kommunikation |
| [Architecture Planning](architecture-planning.md) | Planungsmethodik, C4 Model |
| [Principal Engineer Decisions](principal-engineer-decisions.md) | Entscheidungsfindung auf Senior-Level |

---

## Skills im Workflow nutzen

Skills werden zusammen mit Agents referenziert:

```
@workspace Nutze den Python Expert Agent mit den Skills:
- Clean Code
- SOLID Principles
- Design Patterns

Refactore den UserService nach diesen Prinzipien.
```

!!! tip "Skills kombinieren"
    Je mehr relevante Skills du referenzierst, desto fundierter
    sind die Empfehlungen des Agents.
