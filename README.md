# Copilot Expert Hub

A complete, modular, and scalable repository of **AI Agents, Skills, Templates, and Reference Architectures** for GitHub Copilot and AI-assisted software development.

## Overview

The Copilot Expert Hub provides a full agent chain covering the entire software delivery lifecycle:

```
Architecture → Implementation → Quality → Deployment → IoT/Embedded → Creative → Communication
```

### What's Inside

| Category | Count | Description |
|----------|-------|-------------|
| **Agents** | 18 | Specialized AI agents for every role |
| **Skills** | 17+ | Technical knowledge bases |
| **Marp Templates** | 3 | Presentation templates |
| **Reference Repos** | 2 | Golden architecture examples |
| **Workflows** | 2 | CI/CD validation |

## Agents

### Core Engineering Agents

| Agent | Role | File |
|-------|------|------|
| **Lead Architect** | Architecture design, ADRs, DDD, Event Sourcing | [agents/lead-architect.agent.md](agents/lead-architect.agent.md) |
| **Python Expert** | Idiomatic Python, Pydantic, async, testing | [agents/python-expert.agent.md](agents/python-expert.agent.md) |
| **Golang Expert** | Idiomatic Go, interfaces, concurrency, clean architecture | [agents/golang-expert.agent.md](agents/golang-expert.agent.md) |
| **Flutter & iOS Expert** | Flutter, Dart, BLoC, Clean Architecture, iOS HIG | [agents/flutter-ios-expert.agent.md](agents/flutter-ios-expert.agent.md) |
| **Frontend Expert** | Vue, Angular, TypeScript/JS, component architecture | [agents/frontend-expert.agent.md](agents/frontend-expert.agent.md) |
| **GCP Architect** | Cloud Run, Pub/Sub, BigQuery, Terraform, IAM | [agents/gcp-architect.agent.md](agents/gcp-architect.agent.md) |
| **Test Strategist** | Test pyramid, quality gates, coverage, CI/CD | [agents/test-strategist.agent.md](agents/test-strategist.agent.md) |
| **DevOps Agent** | CI/CD pipelines, deployments, Docker | [agents/devops-agent.agent.md](agents/devops-agent.agent.md) |

### IoT & Embedded Agents

| Agent | Role | File |
|-------|------|------|
| **IoT & Embedded Expert** | MQTT, sensors, actuators, PLCs, Revolution Pi, Siemens, Beckhoff | [agents/iot-embedded-expert.agent.md](agents/iot-embedded-expert.agent.md) |

### Quality & Review Agents

| Agent | Role | File |
|-------|------|------|
| **Architecture Reviewer** | Review designs, identify risks & anti-patterns | [agents/architecture-reviewer.agent.md](agents/architecture-reviewer.agent.md) |
| **Code Reviewer** | Code quality, security, style, tests | [agents/code-reviewer.agent.md](agents/code-reviewer.agent.md) |

### Productivity Agents

| Agent | Role | File |
|-------|------|------|
| **Task Orchestrator** | Coordinate agents, plan tasks, track progress | [agents/task-orchestrator.agent.md](agents/task-orchestrator.agent.md) |
| **Context Manager** | Maintain project memory, track decisions | [agents/context-manager.agent.md](agents/context-manager.agent.md) |

### Creative & Games Agents

| Agent | Role | File |
|-------|------|------|
| **Game Developer** | Game design, mechanics, Godot/Phaser/Unity/PyGame | [agents/game-developer.agent.md](agents/game-developer.agent.md) |
| **Creative App Developer** | Creative coding, generative art, gamification, delightful UX | [agents/creative-app-developer.agent.md](agents/creative-app-developer.agent.md) |

### Customer-Facing Agents

| Agent | Role | File |
|-------|------|------|
| **Presentation Agent** | Create Marp slide decks for any audience | [agents/presentation-agent.agent.md](agents/presentation-agent.agent.md) |
| **Stakeholder Agent** | Translate technical → business language | [agents/stakeholder-agent.agent.md](agents/stakeholder-agent.agent.md) |
| **Proposal/Pitch Agent** | Roadmaps, milestones, proposals | [agents/proposal-pitch.agent.md](agents/proposal-pitch.agent.md) |

## Skills

### New Skills

| Skill | Description | File |
|-------|-------------|------|
| **Python Patterns** | Repository pattern, DI, domain events, Result type | [skills/python-patterns/SKILL.md](skills/python-patterns/SKILL.md) |
| **Golang Patterns** | Interfaces, error handling, concurrency, functional options | [skills/golang-patterns/SKILL.md](skills/golang-patterns/SKILL.md) |
| **Flutter Patterns** | BLoC, Riverpod, freezed, clean architecture, iOS HIG | [skills/flutter-patterns/SKILL.md](skills/flutter-patterns/SKILL.md) |
| **GCP Patterns** | Cloud Run, Pub/Sub, BigQuery, Terraform modules | [skills/gcp-patterns/SKILL.md](skills/gcp-patterns/SKILL.md) |
| **Testing** | Test pyramid, fakes, factories, quality gates | [skills/testing/SKILL.md](skills/testing/SKILL.md) |
| **Marp Presentations** | Slide design, Marp syntax, templates | [skills/marp-presentations/SKILL.md](skills/marp-presentations/SKILL.md) |
| **Anti-Patterns** | Code, architecture, and event-driven anti-patterns | [skills/anti-patterns/SKILL.md](skills/anti-patterns/SKILL.md) |
| **Frontend Patterns** | Vue/Angular patterns, composables, signals, testing | [skills/frontend-patterns/SKILL.md](skills/frontend-patterns/SKILL.md) |
| **IoT & Embedded Patterns** | MQTT, OPC UA, sensors, PLCs, edge computing | [skills/iot-embedded-patterns/SKILL.md](skills/iot-embedded-patterns/SKILL.md) |

### Existing Skills

| Category | Skills |
|----------|--------|
| **Software Engineering** | [Clean Code](skills/software-engineering/clean-code.md), [SOLID](skills/software-engineering/solid-principles.md), [Design Patterns](skills/software-engineering/design-patterns.md), [Code Review](skills/software-engineering/code-review.md), [Testing Strategies](skills/software-engineering/testing-strategies.md), [Practical Refactoring](skills/software-engineering/practical-refactoring.md) |
| **Architecture** | [Microservices](skills/architecture/microservices.md), [DDD](skills/architecture/domain-driven-design.md), [Cloud-Native](skills/architecture/cloud-native.md), [API Design](skills/architecture/api-design.md), [Security](skills/architecture/security.md), [Performance](skills/architecture/performance.md) |
| **Project Management** | [Agile](skills/project-management/agile-methodologies.md), [Technical Debt](skills/project-management/technical-debt.md), [DevOps/CI-CD](skills/project-management/devops-cicd.md) |
| **General** | [Communication](skills/general/communication.md), [Principal Engineer Decisions](skills/general/principal-engineer-decisions.md) |
| **System Design** | [Architecture Planning](skills/system-design/architecture-planning.md) |
| **Team Collaboration** | [PR Crafting](skills/team-collaboration/pr-crafting.md), [Progress Sync](skills/team-collaboration/progress-sync.md), [Feature Discovery](skills/team-collaboration/feature-discovery-session.md), [Incident Response](skills/team-collaboration/incident-response.md) |
| **Game Development** | [Game Design](skills/game-development/game-design.md), [Game Mechanics](skills/game-development/game-mechanics.md), [Game Architecture](skills/game-development/game-architecture.md), [Prototyping](skills/game-development/prototyping.md) |
| **Creative Apps** | [Creative App Patterns](skills/creative-apps/creative-app-patterns.md) |

## Marp Templates

| Template | Audience | Purpose | File |
|----------|----------|---------|------|
| **Client Pitch** | Business stakeholders | Sell a solution | [marp-templates/client-pitch.md](marp-templates/client-pitch.md) |
| **Technical Deep-Dive** | Engineers | Explain architecture | [marp-templates/technical-deepdive.md](marp-templates/technical-deepdive.md) |
| **Project Review** | Stakeholders | Sprint/project status | [marp-templates/project-review.md](marp-templates/project-review.md) |

## Reference Repositories

| Reference | Description | Directory |
|-----------|-------------|-----------|
| **Python Golden Repo** | Production-grade Python project structure | [reference-repos/python-golden/](reference-repos/python-golden/) |
| **Event-Driven Python** | Event-driven architecture patterns on GCP | [reference-repos/event-driven-python/](reference-repos/event-driven-python/) |

## How to Use

### With GitHub Copilot in VS Code

1. **Clone this repository:**
   ```bash
   git clone https://github.com/atstaeff/ai-agents.git
   ```

2. **Open in VS Code** — The `.github/copilot-instructions.md` provides global Copilot context.

3. **Reference agents in conversations:**
   ```
   @workspace Use the Lead Architect agent to design an event-driven
   architecture for our order management system.
   ```

4. **Use skills for context:**
   ```
   @workspace Apply the Python Patterns skill to refactor this service
   using the repository pattern and dependency injection.
   ```

### Recommended Workflow

```
 1. Task Orchestrator    → Break down project into tasks
 2. Lead Architect       → Design architecture, create ADRs
 3. Architecture Reviewer→ Review the design
 4. Python Expert        → Implement backend solution (Python)
 4b. Golang Expert        → Implement backend solution (Go)
 5. Flutter & iOS Expert  → Implement mobile app
 6. Frontend Expert       → Implement frontend/UI (web)
 6b. Game Developer       → Build games (Godot, Phaser, PyGame)
 6c. Creative App Dev     → Build creative apps (generative art, gamification)
 7. Test Strategist      → Design & implement tests
 8. Code Reviewer        → Review code quality
 9. DevOps Agent         → Set up CI/CD & deploy
 9b. IoT & Embedded Expert→ Implement IoT/edge solutions
10. Context Manager      → Document decisions
11. Presentation Agent   → Create client presentation
12. Stakeholder Agent    → Prepare status reports
13. Proposal/Pitch Agent → Create project proposals
```

## Repository Structure

```
agents/                        # 18 specialized AI agents
├── lead-architect.agent.md
├── python-expert.agent.md
├── golang-expert.agent.md
├── flutter-ios-expert.agent.md
├── frontend-expert.agent.md
├── gcp-architect.agent.md
├── iot-embedded-expert.agent.md
├── test-strategist.agent.md
├── devops-agent.agent.md
├── presentation-agent.agent.md
├── architecture-reviewer.agent.md
├── code-reviewer.agent.md
├── task-orchestrator.agent.md
├── context-manager.agent.md
├── stakeholder-agent.agent.md
├── proposal-pitch.agent.md
├── game-developer.agent.md
└── creative-app-developer.agent.md
copilot-instructions.md        # Global Copilot config
skills/
├── python-patterns/SKILL.md   # Python best practices
├── golang-patterns/SKILL.md   # Go best practices
├── flutter-patterns/SKILL.md  # Flutter/Dart/iOS best practices
├── frontend-patterns/SKILL.md # Vue, Angular, TS patterns
├── gcp-patterns/SKILL.md      # GCP architecture patterns
├── iot-embedded-patterns/SKILL.md # IoT, MQTT, PLCs, edge computing
├── testing/SKILL.md           # Testing strategies
├── marp-presentations/SKILL.md# Presentation skills
├── anti-patterns/SKILL.md     # What to avoid
├── software-engineering/      # Core SE skills
├── architecture/              # Architecture skills
├── project-management/        # PM skills
├── team-collaboration/        # Collaboration skills
├── general/                   # Cross-cutting skills
├── system-design/             # System design skills
├── game-development/          # Game design, mechanics, architecture
└── creative-apps/             # Creative app patterns
marp-templates/                # Marp slide templates
├── client-pitch.md
├── technical-deepdive.md
└── project-review.md
reference-repos/               # Golden architecture examples
├── python-golden/
└── event-driven-python/
assets/mkdocs/                 # MkDocs source files
docs/                          # Built documentation site
assets/                        # Documentation assets
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding agents, skills, and templates.

## License

MIT License — See [LICENSE](LICENSE) for details.

---

**Built for productivity, quality, and collaboration.**
