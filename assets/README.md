# Copilot Expert Hub — Documentation

## Overview

The **Copilot Expert Hub** is a centralized repository for AI agents, skills, templates, and reference architectures. It provides a complete, modular, and scalable toolkit for AI-assisted software development.

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                   Copilot Expert Hub                  │
├──────────┬──────────┬──────────┬───────────┬────────┤
│  Agents  │  Skills  │Templates │ Reference │  Docs  │
│          │          │          │   Repos   │        │
├──────────┼──────────┼──────────┼───────────┼────────┤
│ Lead     │ Python   │ Client   │ Python    │ README │
│ Architect│ Patterns │ Pitch    │ Golden    │        │
│          │          │          │           │        │
│ Python   │ GCP      │ Tech     │ Event-    │ CONTR- │
│ Expert   │ Patterns │ Deep-Dive│ Driven    │ IBUTING│
│          │          │          │           │        │
│ GCP      │ Testing  │ Project  │           │ GUIDE- │
│ Architect│          │ Review   │           │ LINES  │
│          │ Marp     │          │           │        │
│ Test     │ Present. │          │           │        │
│ Strategst│          │          │           │        │
│          │ Anti-    │          │           │        │
│ DevOps   │ Patterns │          │           │        │
│          │          │          │           │        │
│ Present. │          │          │           │        │
│ Agent    │          │          │           │        │
│          │          │          │           │        │
│ Arch.    │          │          │           │        │
│ Reviewer │          │          │           │        │
│          │          │          │           │        │
│ Code     │          │          │           │        │
│ Reviewer │          │          │           │        │
│          │          │          │           │        │
│ Task     │          │          │           │        │
│ Orchestr.│          │          │           │        │
│          │          │          │           │        │
│ Context  │          │          │           │        │
│ Manager  │          │          │           │        │
│          │          │          │           │        │
│ Stake-   │          │          │           │        │
│ holder   │          │          │           │        │
│          │          │          │           │        │
│ Proposal │          │          │           │        │
│ Pitch    │          │          │           │        │
└──────────┴──────────┴──────────┴───────────┴────────┘
```

## Agent Chain

The agents form a complete delivery chain:

```
Architecture → Implementation → Testing → Review → Deployment → Presentation → Client Communication
     │              │              │          │          │              │                │
Lead Architect  Python Expert  Test       Code      DevOps    Presentation    Stakeholder
GCP Architect                 Strategist  Reviewer   Agent       Agent           Agent
                                         Arch.                                 Proposal
                                         Reviewer                               Agent
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
| Lead Architect | Architecture design, ADRs, DDD | `.github/agents/lead-architect.agent.md` |
| Python Expert | Idiomatic Python, patterns | `.github/agents/python-expert.agent.md` |
| GCP Architect | Cloud infrastructure, Terraform | `.github/agents/gcp-architect.agent.md` |
| Test Strategist | Test strategies, quality gates | `.github/agents/test-strategist.agent.md` |
| DevOps Agent | CI/CD, deployments | `.github/agents/devops-agent.agent.md` |
| Presentation Agent | Marp slides, storytelling | `.github/agents/presentation-agent.agent.md` |
| Architecture Reviewer | Architecture quality review | `.github/agents/architecture-reviewer.agent.md` |
| Code Reviewer | Code quality, security, style | `.github/agents/code-reviewer.agent.md` |
| Task Orchestrator | Task planning, coordination | `.github/agents/task-orchestrator.agent.md` |
| Context Manager | Project memory, ADR tracking | `.github/agents/context-manager.agent.md` |
| Stakeholder Agent | Business communication | `.github/agents/stakeholder-agent.agent.md` |
| Proposal/Pitch Agent | Proposals, roadmaps, pitches | `.github/agents/proposal-pitch.agent.md` |

### Skills
| Skill | Purpose | File |
|-------|---------|------|
| Python Patterns | Idiomatic Python best practices | `skills/python-patterns/SKILL.md` |
| GCP Patterns | GCP architecture patterns | `skills/gcp-patterns/SKILL.md` |
| Testing | Test strategies & patterns | `skills/testing/SKILL.md` |
| Marp Presentations | Slide deck creation | `skills/marp-presentations/SKILL.md` |
| Anti-Patterns | What to avoid | `skills/anti-patterns/SKILL.md` |

### Templates
| Template | Audience | File |
|----------|----------|------|
| Client Pitch | Business stakeholders | `marp-templates/client-pitch.md` |
| Technical Deep-Dive | Engineers | `marp-templates/technical-deepdive.md` |
| Project Review | Mixed audience | `marp-templates/project-review.md` |
