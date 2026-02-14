# Copilot Expert Hub — Documentation

## Overview

The **Copilot Expert Hub** is a centralized repository for AI agents, skills, templates, and reference architectures. It provides a complete, modular, and scalable toolkit for AI-assisted software development.

## Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│                       Copilot Expert Hub                             │
├──────────────┬──────────────┬──────────┬───────────┬────────────────┤
│   Agents     │   Skills     │Templates │ Reference │     Docs       │
│   (18)       │   (17)       │          │   Repos   │                │
├──────────────┼──────────────┼──────────┼───────────┼────────────────┤
│ Lead         │ Python       │ Client   │ Python    │ README         │
│ Architect    │ Patterns     │ Pitch    │ Golden    │                │
│              │              │          │           │ CONTRIBUTING   │
│ Python       │ Golang       │ Tech     │ Event-    │                │
│ Expert       │ Patterns     │ Deep-Dive│ Driven    │ GUIDELINES     │
│              │              │          │           │                │
│ Golang       │ Flutter      │ Project  │           │ MkDocs Site    │
│ Expert       │ Patterns     │ Review   │           │                │
│              │              │          │           │                │
│ Flutter &    │ Frontend     │          │           │                │
│ iOS Expert   │ Patterns     │          │           │                │
│              │              │          │           │                │
│ Frontend     │ GCP          │          │           │                │
│ Expert       │ Patterns     │          │           │                │
│              │              │          │           │                │
│ GCP          │ IoT &        │          │           │                │
│ Architect    │ Embedded     │          │           │                │
│              │              │          │           │                │
│ IoT &        │ Testing      │          │           │                │
│ Embedded     │ Strategies   │          │           │                │
│ Expert       │              │          │           │                │
│              │ Clean Code   │          │           │                │
│ Test         │ SOLID        │          │           │                │
│ Strategist   │ Design Pat.  │          │           │                │
│              │              │          │           │                │
│ DevOps       │ Microservices│          │           │                │
│ Agent        │ DDD          │          │           │                │
│              │ Cloud-Native │          │           │                │
│ Arch.        │ API Design   │          │           │                │
│ Reviewer     │ Security     │          │           │                │
│              │ Performance  │          │           │                │
│ Code         │              │          │           │                │
│ Reviewer     │ Game Dev     │          │           │                │
│              │ Creative     │          │           │                │
│ Task         │ Marp         │          │           │                │
│ Orchestrator │ Anti-Pattern │          │           │                │
│              │              │          │           │                │
│ Context      │ Agile        │          │           │                │
│ Manager      │ Tech Debt    │          │           │                │
│              │ DevOps/CICD  │          │           │                │
│ Presentation │ PR Crafting  │          │           │                │
│ Agent        │ Progress     │          │           │                │
│              │              │          │           │                │
│ Stakeholder  │ Communication│          │           │                │
│ Agent        │ Architecture │          │           │                │
│              │ Planning     │          │           │                │
│ Proposal/    │              │          │           │                │
│ Pitch        │              │          │           │                │
│              │              │          │           │                │
│ Game         │              │          │           │                │
│ Developer    │              │          │           │                │
│              │              │          │           │                │
│ Creative App │              │          │           │                │
│ Developer    │              │          │           │                │
└──────────────┴──────────────┴──────────┴───────────┴────────────────┘
```

## Agent Chain

The agents form a complete delivery chain:

```
Architecture → Implementation → Quality → Deployment → IoT/Embedded → Creative → Communication
     │              │              │          │              │             │            │
Lead Architect  Python Expert  Test       DevOps     IoT &        Game      Presentation
GCP Architect   Golang Expert  Strategist  Agent     Embedded     Developer    Agent
Task            Flutter Expert Code                  Expert       Creative  Stakeholder
Orchestrator    Frontend Expert Reviewer                          App Dev     Agent
                               Arch.                                       Proposal
                               Reviewer                                     Agent
                                                                          Context Mgr
```

## Quick Start

1. Clone this repository
2. Open in VS Code with GitHub Copilot
3. Reference agents and skills in your conversations
4. Use templates for presentations and proposals

See the [main README](../README.md) for detailed usage instructions.

## Index

### Agents
| Agent | Purpose | File |
|-------|---------|------|
| Lead Architect | Architecture design, ADRs, DDD | `agents/lead-architect.agent.md` |
| Python Expert | Idiomatic Python, patterns | `agents/python-expert.agent.md` |
| Golang Expert | Idiomatic Go, concurrency | `agents/golang-expert.agent.md` |
| Flutter & iOS Expert | Dart/Flutter, BLoC, mobile | `agents/flutter-ios-expert.agent.md` |
| Frontend Expert | TypeScript, Vue, Angular | `agents/frontend-expert.agent.md` |
| GCP Architect | Cloud infrastructure, Terraform | `agents/gcp-architect.agent.md` |
| IoT & Embedded Expert | MQTT, sensors, PLCs, edge computing | `agents/iot-embedded-expert.agent.md` |
| Test Strategist | Test strategies, quality gates | `agents/test-strategist.agent.md` |
| DevOps Agent | CI/CD, deployments | `agents/devops-agent.agent.md` |
| Architecture Reviewer | Architecture quality review | `agents/architecture-reviewer.agent.md` |
| Code Reviewer | Code quality, security, style | `agents/code-reviewer.agent.md` |
| Task Orchestrator | Task planning, coordination | `agents/task-orchestrator.agent.md` |
| Context Manager | Project memory, ADR tracking | `agents/context-manager.agent.md` |
| Presentation Agent | Marp slides, storytelling | `agents/presentation-agent.agent.md` |
| Stakeholder Agent | Business communication | `agents/stakeholder-agent.agent.md` |
| Proposal/Pitch Agent | Proposals, roadmaps, pitches | `agents/proposal-pitch.agent.md` |
| Game Developer | Game design, mechanics, Godot/Phaser | `agents/game-developer.agent.md` |
| Creative App Developer | Generative art, gamification | `agents/creative-app-developer.agent.md` |

### Skills
| Skill | Purpose | File |
|-------|---------|------|
| Python Patterns | Idiomatic Python best practices | `skills/python-patterns/SKILL.md` |
| Golang Patterns | Idiomatic Go best practices | `skills/golang-patterns/SKILL.md` |
| Flutter Patterns | Dart/Flutter architecture | `skills/flutter-patterns/SKILL.md` |
| Frontend Patterns | TypeScript, Vue, Angular | `skills/frontend-patterns/SKILL.md` |
| GCP Patterns | GCP architecture patterns | `skills/gcp-patterns/SKILL.md` |
| IoT & Embedded Patterns | MQTT, sensors, PLCs, edge | `skills/iot-embedded-patterns/SKILL.md` |
| Testing | Test strategies & patterns | `skills/testing/SKILL.md` |
| Clean Code | Naming, functions, DRY | `skills/software-engineering/` |
| SOLID Principles | SRP, OCP, LSP, ISP, DIP | `skills/software-engineering/` |
| Design Patterns | Strategy, Observer, Factory | `skills/software-engineering/` |
| Microservices | Service boundaries, resilience | `skills/architecture/` |
| Domain-Driven Design | Bounded Contexts, Aggregates | `skills/architecture/` |
| Game Development | Game design, mechanics, architecture | `skills/game-development/` |
| Creative Apps | Generative design, gamification | `skills/creative-apps/` |
| Marp Presentations | Slide deck creation | `skills/marp-presentations/SKILL.md` |
| Anti-Patterns | What to avoid | `skills/anti-patterns/SKILL.md` |
| Project Management | Agile, tech debt, DevOps/CI-CD | `skills/project-management/` |

### Templates
| Template | Audience | File |
|----------|----------|------|
| Client Pitch | Business stakeholders | `marp-templates/client-pitch.md` |
| Technical Deep-Dive | Engineers | `marp-templates/technical-deepdive.md` |
| Project Review | Mixed audience | `marp-templates/project-review.md` |
