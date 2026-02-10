# Copilot Expert Hub

A complete, modular, and scalable repository of **AI Agents, Skills, Templates, and Reference Architectures** for GitHub Copilot and AI-assisted software development.

## Overview

The Copilot Expert Hub provides a full agent chain covering the entire software delivery lifecycle:

```
Architecture → Implementation → Testing → Review → Deployment → Presentation → Client Communication
```

### What's Inside

| Category | Count | Description |
|----------|-------|-------------|
| **Agents** | 13 | Specialized AI agents for every role |
| **Skills** | 10+ | Technical knowledge bases |
| **Marp Templates** | 3 | Presentation templates |
| **Reference Repos** | 2 | Golden architecture examples |
| **Workflows** | 2 | CI/CD validation |

## Agents

### Core Engineering Agents

| Agent | Role | File |
|-------|------|------|
| **Lead Architect** | Architecture design, ADRs, DDD, Event Sourcing | [agents/lead-architect.agent.md](.github/agents/lead-architect.agent.md) |
| **Python Expert** | Idiomatic Python, Pydantic, async, testing | [agents/python-expert.agent.md](.github/agents/python-expert.agent.md) |
| **Frontend Expert** | Vue, Angular, TypeScript/JS, component architecture | [agents/frontend-expert.agent.md](.github/agents/frontend-expert.agent.md) |
| **GCP Architect** | Cloud Run, Pub/Sub, BigQuery, Terraform, IAM | [agents/gcp-architect.agent.md](.github/agents/gcp-architect.agent.md) |
| **Test Strategist** | Test pyramid, quality gates, coverage, CI/CD | [agents/test-strategist.agent.md](.github/agents/test-strategist.agent.md) |
| **DevOps Agent** | CI/CD pipelines, deployments, Docker | [agents/devops-agent.agent.md](.github/agents/devops-agent.agent.md) |

### Quality & Review Agents

| Agent | Role | File |
|-------|------|------|
| **Architecture Reviewer** | Review designs, identify risks & anti-patterns | [agents/architecture-reviewer.agent.md](.github/agents/architecture-reviewer.agent.md) |
| **Code Reviewer** | Code quality, security, style, tests | [agents/code-reviewer.agent.md](.github/agents/code-reviewer.agent.md) |

### Productivity Agents

| Agent | Role | File |
|-------|------|------|
| **Task Orchestrator** | Coordinate agents, plan tasks, track progress | [agents/task-orchestrator.agent.md](.github/agents/task-orchestrator.agent.md) |
| **Context Manager** | Maintain project memory, track decisions | [agents/context-manager.agent.md](.github/agents/context-manager.agent.md) |

### Customer-Facing Agents

| Agent | Role | File |
|-------|------|------|
| **Presentation Agent** | Create Marp slide decks for any audience | [agents/presentation-agent.agent.md](.github/agents/presentation-agent.agent.md) |
| **Stakeholder Agent** | Translate technical → business language | [agents/stakeholder-agent.agent.md](.github/agents/stakeholder-agent.agent.md) |
| **Proposal/Pitch Agent** | Roadmaps, milestones, proposals | [agents/proposal-pitch.agent.md](.github/agents/proposal-pitch.agent.md) |

## Skills

### New Skills

| Skill | Description | File |
|-------|-------------|------|
| **Python Patterns** | Repository pattern, DI, domain events, Result type | [skills/python-patterns/SKILL.md](skills/python-patterns/SKILL.md) |
| **GCP Patterns** | Cloud Run, Pub/Sub, BigQuery, Terraform modules | [skills/gcp-patterns/SKILL.md](skills/gcp-patterns/SKILL.md) |
| **Testing** | Test pyramid, fakes, factories, quality gates | [skills/testing/SKILL.md](skills/testing/SKILL.md) |
| **Marp Presentations** | Slide design, Marp syntax, templates | [skills/marp-presentations/SKILL.md](skills/marp-presentations/SKILL.md) |
| **Anti-Patterns** | Code, architecture, and event-driven anti-patterns | [skills/anti-patterns/SKILL.md](skills/anti-patterns/SKILL.md) |
| **Frontend Patterns** | Vue/Angular patterns, composables, signals, testing | [skills/frontend-patterns/SKILL.md](skills/frontend-patterns/SKILL.md) |

### Existing Skills

| Category | Skills |
|----------|--------|
| **Software Engineering** | [Clean Code](skills/software-engineering/clean-code.md), [SOLID](skills/software-engineering/solid-principles.md), [Design Patterns](skills/software-engineering/design-patterns.md), [Code Review](skills/software-engineering/code-review.md), [Testing Strategies](skills/software-engineering/testing-strategies.md), [Practical Refactoring](skills/software-engineering/practical-refactoring.md) |
| **Architecture** | [Microservices](skills/architecture/microservices.md), [DDD](skills/architecture/domain-driven-design.md), [Cloud-Native](skills/architecture/cloud-native.md), [API Design](skills/architecture/api-design.md), [Security](skills/architecture/security.md), [Performance](skills/architecture/performance.md) |
| **Project Management** | [Agile](skills/project-management/agile-methodologies.md), [Technical Debt](skills/project-management/technical-debt.md), [DevOps/CI-CD](skills/project-management/devops-cicd.md) |
| **Code Quality** | [Review Assistant](skills/code-quality/review-assistant.md), [Tech Debt Assessment](skills/code-quality/technical-debt-assessment.md) |
| **Team Collaboration** | [PR Crafting](skills/team-collaboration/pr-crafting.md), [Progress Sync](skills/team-collaboration/progress-sync.md), [Feature Discovery](skills/team-collaboration/feature-discovery-session.md), [Incident Response](skills/team-collaboration/incident-response.md) |

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
   git clone https://github.com/atstaeff/ai-skills.git
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
 4. Python Expert        → Implement backend solution
 5. Frontend Expert      → Implement frontend/UI
 6. Test Strategist      → Design & implement tests
 7. Code Reviewer        → Review code quality
 8. DevOps Agent         → Set up CI/CD & deploy
 9. Context Manager      → Document decisions
10. Presentation Agent   → Create client presentation
11. Stakeholder Agent    → Prepare status reports
12. Proposal/Pitch Agent → Create project proposals
```

## Repository Structure

```
.github/
├── agents/                    # 13 specialized AI agents
│   ├── lead-architect.agent.md
│   ├── python-expert.agent.md
│   ├── frontend-expert.agent.md
│   ├── gcp-architect.agent.md
│   ├── test-strategist.agent.md
│   ├── devops-agent.agent.md
│   ├── presentation-agent.agent.md
│   ├── architecture-reviewer.agent.md
│   ├── code-reviewer.agent.md
│   ├── task-orchestrator.agent.md
│   ├── context-manager.agent.md
│   ├── stakeholder-agent.agent.md
│   └── proposal-pitch.agent.md
├── workflows/                 # CI/CD validation
│   ├── validate-agents.yml
│   └── ci-cd-check.yml
└── copilot-instructions.md    # Global Copilot config
skills/
├── python-patterns/SKILL.md   # Python best practices
├── gcp-patterns/SKILL.md      # GCP architecture patterns
├── testing/SKILL.md           # Testing strategies
├── marp-presentations/SKILL.md# Presentation skills
├── anti-patterns/SKILL.md     # What to avoid
├── frontend-patterns/SKILL.md # Vue, Angular, TS patterns
├── software-engineering/      # Core SE skills
├── architecture/              # Architecture skills
├── project-management/        # PM skills
├── code-quality/              # Quality skills
├── team-collaboration/        # Collaboration skills
├── general/                   # Cross-cutting skills
└── system-design/             # System design skills
marp-templates/                # Marp slide templates
├── client-pitch.md
├── technical-deepdive.md
└── project-review.md
reference-repos/               # Golden architecture examples
├── python-golden/
└── event-driven-python/
docs/                          # Documentation
├── README.md
├── CONTRIBUTING.md
└── GUIDELINES.md
```

## Contributing

See [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines on adding agents, skills, and templates.

## License

MIT License — See [LICENSE](LICENSE) for details.

---

**Built for productivity, quality, and collaboration.**
