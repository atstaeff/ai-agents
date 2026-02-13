# Agent Catalog

The Copilot Expert Hub includes **15 specialized AI agents**, organized by the phases of the Software Delivery Lifecycle.

---

## The Agent Lifecycle

```mermaid
graph LR
    A["🎯 Planning"] --> B["💻 Implementation"]
    B --> C["🧪 Quality"]
    C --> D["🚀 Deployment"]
    D --> E["📊 Communication"]

    style A fill:#e8eaf6,stroke:#3949ab
    style B fill:#e3f2fd,stroke:#1565c0
    style C fill:#e8f5e9,stroke:#2e7d32
    style D fill:#f3e5f5,stroke:#6a1b9a
    style E fill:#fce4ec,stroke:#c62828
```

---

## :material-target: Phase 1 — Planning & Architecture

<div class="grid" markdown>

<div class="card" markdown>
### :material-floor-plan: Lead Architect
<span class="agent-badge badge-phase-plan">Planning</span>

System architecture, ADRs, DDD, Event Sourcing, C4 diagrams. Designs scalable and maintainable systems.

[:material-arrow-right: Details](lead-architect.md)
</div>

<div class="card" markdown>
### :material-clipboard-list: Task Orchestrator
<span class="agent-badge badge-phase-plan">Planning</span>

Breaks projects into epics and tasks, coordinates agent workflows, and tracks progress.

[:material-arrow-right: Details](task-orchestrator.md)
</div>

<div class="card" markdown>
### :material-cloud: GCP Architect
<span class="agent-badge badge-phase-plan">Planning</span>

Google Cloud Platform solutions: Cloud Run, Pub/Sub, BigQuery, Terraform, IAM.

[:material-arrow-right: Details](gcp-architect.md)
</div>

</div>

---

## :material-code-braces: Phase 2 — Implementation

<div class="grid" markdown>

<div class="card" markdown>
### :material-language-python: Python Expert
<span class="agent-badge badge-phase-build">Code</span>

Idiomatic Python 3.12+, Pydantic, async/await, Repository Pattern, SOLID.

[:material-arrow-right: Details](python-expert.md)
</div>

<div class="card" markdown>
### :material-language-go: Golang Expert
<span class="agent-badge badge-phase-build">Code</span>

Production-grade Go: Interfaces, Concurrency, Error Handling, Clean Architecture.

[:material-arrow-right: Details](golang-expert.md)
</div>

<div class="card" markdown>
### :material-cellphone: Flutter & iOS Expert
<span class="agent-badge badge-phase-build">Code</span>

Dart/Flutter, BLoC, Riverpod, Clean Architecture, iOS Human Interface Guidelines.

[:material-arrow-right: Details](flutter-ios-expert.md)
</div>

<div class="card" markdown>
### :material-language-typescript: Frontend Expert
<span class="agent-badge badge-phase-build">Code</span>

TypeScript, Vue.js, Angular, Component Patterns, State Management, Testing.

[:material-arrow-right: Details](frontend-expert.md)
</div>

</div>

---

## :material-test-tube: Phase 3 — Quality & Review

<div class="grid" markdown>

<div class="card" markdown>
### :material-beaker-check: Test Strategist
<span class="agent-badge badge-phase-quality">Quality</span>

Test Pyramid, TDD, Quality Gates, Coverage strategies, CI integration.

[:material-arrow-right: Details](test-strategist.md)
</div>

<div class="card" markdown>
### :material-city-variant: Architecture Reviewer
<span class="agent-badge badge-phase-quality">Quality</span>

Architecture assessment, risk analysis, anti-pattern detection, trade-off analysis.

[:material-arrow-right: Details](architecture-reviewer.md)
</div>

<div class="card" markdown>
### :material-code-tags-check: Code Reviewer
<span class="agent-badge badge-phase-quality">Quality</span>

Code quality, security checks, style enforcement, constructive feedback.

[:material-arrow-right: Details](code-reviewer.md)
</div>

</div>

---

## :material-rocket-launch: Phase 4 — Deployment

<div class="grid" markdown>

<div class="card" markdown>
### :material-pipe: DevOps Agent
<span class="agent-badge badge-phase-deploy">Deploy</span>

CI/CD Pipelines, Docker, GitHub Actions, GitOps, Deployment Strategies, Monitoring.

[:material-arrow-right: Details](devops-agent.md)
</div>

</div>

---

## :material-account-voice: Phase 5 — Communication

<div class="grid" markdown>

<div class="card" markdown>
### :material-brain: Context Manager
<span class="agent-badge badge-phase-communicate">Communication</span>

Project memory, ADR tracking, decision documentation, knowledge management.

[:material-arrow-right: Details](context-manager.md)
</div>

<div class="card" markdown>
### :material-presentation-play: Presentation Agent
<span class="agent-badge badge-phase-communicate">Communication</span>

Professional Marp slide decks for client pitches, tech talks, and reviews.

[:material-arrow-right: Details](presentation-agent.md)
</div>

<div class="card" markdown>
### :material-chart-line: Stakeholder Agent
<span class="agent-badge badge-phase-communicate">Communication</span>

Translates technical details into business language — status reports, summaries, KPIs.

[:material-arrow-right: Details](stakeholder-agent.md)
</div>

<div class="card" markdown>
### :material-file-document-edit: Proposal/Pitch Agent
<span class="agent-badge badge-phase-communicate">Communication</span>

Project proposals, roadmaps, milestones, effort estimates.

[:material-arrow-right: Details](proposal-pitch.md)
</div>

</div>

---

## Quick Reference

| Agent | Category | Core Competency | Typical Use Case |
|-------|----------|-----------------|------------------|
| Lead Architect | Engineering | System Design, DDD, ADRs | Designing new system architectures |
| Python Expert | Engineering | Python 3.12+, SOLID, Patterns | Backend services, refactoring |
| Golang Expert | Engineering | Go 1.22+, Concurrency | Microservices, CLIs |
| Flutter & iOS Expert | Engineering | Dart/Flutter, BLoC, Clean Arch | Mobile apps |
| Frontend Expert | Engineering | TypeScript, Vue, Angular | Web frontends, SPAs |
| GCP Architect | Engineering | Serverless, Terraform, Pub/Sub | Cloud infrastructure |
| Test Strategist | Engineering | Test Pyramid, TDD | Test strategies, quality gates |
| DevOps Agent | Engineering | GitHub Actions, GitOps | CI/CD pipelines |
| Architecture Reviewer | Review | Architecture Assessment | Risk analysis, anti-patterns |
| Code Reviewer | Review | Code Quality | PR reviews, bug detection |
| Task Orchestrator | Productivity | Task Decomposition | Project planning |
| Context Manager | Productivity | Knowledge Management | Documentation, ADR tracking |
| Presentation Agent | Communication | Marp Slides | Client pitches, tech talks |
| Stakeholder Agent | Communication | Business Language | Status reports, summaries |
| Proposal/Pitch Agent | Communication | Proposals, Roadmaps | Proposal creation |

---

## Choosing an Agent

```mermaid
graph TD
    A[What do you want to do?] --> B{Write code?}
    B -->|Python| C[Python Expert]
    B -->|Go| D[Golang Expert]
    B -->|Flutter| E["Flutter & iOS Expert"]
    B -->|Frontend| F[Frontend Expert]
    A --> G{Architecture?}
    G -->|Design| H[Lead Architect]
    G -->|Review| I[Architecture Reviewer]
    G -->|Cloud| J[GCP Architect]
    A --> K{Organization?}
    K -->|Plan| L[Task Orchestrator]
    K -->|Document| M[Context Manager]
    A --> N{Communication?}
    N -->|Presentation| O[Presentation Agent]
    N -->|Report| P[Stakeholder Agent]
    N -->|Proposal| Q["Proposal/Pitch Agent"]
```
