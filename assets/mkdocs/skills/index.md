# Skills Catalog

Skills are **technical knowledge bases** that agents use to provide well-founded recommendations. Each skill contains best practices, patterns, code examples, and anti-patterns.

---

## Language Patterns

Language-specific patterns and best practices.

| Skill | Description | For Agent |
|-------|-------------|-----------|
| [Python Patterns](python-patterns.md) | Idiomatic Python, Design Patterns, SOLID | Python Expert |
| [Golang Patterns](golang-patterns.md) | Idiomatic Go, Concurrency, Interfaces | Golang Expert |
| [Flutter Patterns](flutter-patterns.md) | Dart/Flutter, BLoC, Clean Architecture | Flutter & iOS Expert |
| [Frontend Patterns](frontend-patterns.md) | TypeScript, Vue.js, Angular Patterns | Frontend Expert |

## Software Engineering

Cross-language engineering principles.

| Skill | Description |
|-------|-------------|
| [Clean Code](clean-code.md) | Naming, Functions, Error Handling, DRY |
| [SOLID Principles](solid-principles.md) | SRP, OCP, LSP, ISP, DIP with examples |
| [Design Patterns](design-patterns.md) | Strategy, Observer, Factory, Repository |
| [Code Review](code-review.md) | Review guidelines, checklists, feedback |
| [Testing Strategies](testing-strategies.md) | Test Pyramid, TDD, Mocking, Coverage |
| [Practical Refactoring](practical-refactoring.md) | Refactoring tactics and workflows |

## Architecture

Architecture patterns and design decisions.

| Skill | Description |
|-------|-------------|
| [Microservices](microservices.md) | Service boundaries, communication, resilience |
| [Domain-Driven Design](domain-driven-design.md) | Bounded Contexts, Aggregates, Events |
| [Cloud-Native](cloud-native.md) | 12-Factor, Containers, Serverless |
| [API Design](api-design.md) | REST, gRPC, Versioning, Error Handling |
| [Security](security.md) | AuthN/AuthZ, Input Validation, Encryption |
| [Performance](performance.md) | Caching, Indexing, Profiling, Optimization |

## Cloud & DevOps

Cloud infrastructure and operations.

| Skill | Description |
|-------|-------------|
| [GCP Patterns](gcp-patterns.md) | Cloud Run, Pub/Sub, BigQuery, Terraform |
| [IoT & Embedded Patterns](iot-embedded-patterns.md) | MQTT, OPC UA, Sensors, PLCs, Edge Computing |
| [Testing](testing.md) | Testing Patterns, Fixtures, Mocking |
| [DevOps & CI/CD](devops-cicd.md) | Pipelines, GitOps, Deployment Strategies |

## Project & Team

Collaboration, communication, and project management.

| Skill | Description |
|-------|-------------|
| [Agile Methodologies](agile-methodologies.md) | Scrum, Kanban, Sprint Planning |
| [Technical Debt](technical-debt.md) | Assessment, Prioritization, Reduction |
| [PR Crafting](pr-crafting.md) | Professional Pull Requests |
| [Progress Sync](progress-sync.md) | Standup, Status Updates, Reporting |
| [Feature Discovery](feature-discovery.md) | Requirements Gathering, Story Mapping |
| [Incident Response](incident-response.md) | Incident Management, Postmortems |

## Game Development

Patterns und Prinzipien fuer Game- und Creative-App-Entwicklung.

| Skill | Description |
|-------|-------------|
| [Game Design](game-design.md) | Core Loops, GDDs, Difficulty Curves, Progression |
| [Game Mechanics](game-mechanics.md) | Physics, AI (FSM, Behavior Trees), Procedural Generation |
| [Game Architecture](game-architecture.md) | ECS, Event Bus, Scene Management, Save/Load |
| [Prototyping & Playtesting](prototyping.md) | Rapid Prototypes, Game Jam Strategies, Metriken |

## Creative Apps

| Skill | Description |
|-------|-------------|
| [Creative App Patterns](creative-app-patterns.md) | Micro-Interactions, Generative Design, Gamification, Audio |

## Additional Skills

| Skill | Description |
|-------|-------------|
| [Anti-Patterns](anti-patterns.md) | Common mistakes and how to avoid them |
| [Marp Presentations](marp-presentations.md) | Marp Syntax, Templates, Styling |
| [Communication](communication.md) | Technical Communication |
| [Architecture Planning](architecture-planning.md) | Planning Methodology, C4 Model |
| [Principal Engineer Decisions](principal-engineer-decisions.md) | Senior-level decision making |

---

## Using Skills in Your Workflow

Skills are referenced together with agents:

```
@workspace Use the Python Expert agent with the following skills:
- Clean Code
- SOLID Principles
- Design Patterns

Refactor the UserService according to these principles.
```

!!! tip "Combining Skills"
    The more relevant skills you reference, the more well-founded
    the agent's recommendations will be.
