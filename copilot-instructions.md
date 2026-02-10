# GitHub Copilot Instructions — Copilot Expert Hub

This repository is the **Copilot Expert Hub** — a comprehensive collection of AI agents, skills, templates, and reference architectures for professional software engineering.

## Repository Structure

- **`.github/agents/`** — 12 specialized AI agents covering the full delivery lifecycle
- **`skills/`** — Technical knowledge bases (Python, GCP, Testing, Architecture, etc.)
- **`marp-templates/`** — Presentation templates (Client Pitch, Tech Deep-Dive, Project Review)
- **`reference-repos/`** — Golden architecture examples
- **`docs/`** — Documentation and contribution guidelines

## Available Agents

Use these agents by referencing them in conversations:

| Agent | Use When |
|-------|----------|
| **Lead Architect** | Designing systems, creating ADRs, DDD bounded contexts |
| **Python Expert** | Writing/reviewing Python, Pydantic, FastAPI, async patterns |
| **Frontend Expert** | Vue, Angular, TypeScript/JavaScript, component architecture |
| **GCP Architect** | Cloud architecture, Terraform, Pub/Sub, BigQuery, IAM |
| **Test Strategist** | Designing test strategies, quality gates, fixtures |
| **DevOps Agent** | CI/CD pipelines, Docker, deployments, GitHub Actions |
| **Presentation Agent** | Creating Marp slide decks for any audience |
| **Architecture Reviewer** | Reviewing designs for risks and anti-patterns |
| **Code Reviewer** | Reviewing code for quality, security, performance |
| **Task Orchestrator** | Breaking down projects, planning task sequences |
| **Context Manager** | Maintaining project context, tracking decisions |
| **Stakeholder Agent** | Translating technical content for business audiences |
| **Proposal/Pitch Agent** | Creating proposals, roadmaps, cost estimates |

## General Guidelines

- Follow clean code principles and SOLID design patterns
- Apply enterprise-grade software engineering practices
- Consider scalability, maintainability, and security in all solutions
- Use industry-standard architectural patterns and best practices
- Apply systematic project management methodologies

## Code Quality Standards

- Write self-documenting code with clear naming conventions
- Use modern Python (3.12+): type hints, Pydantic v2, dataclasses
- Include comprehensive error handling and structured logging
- Follow PEP standards and use `ruff` for linting/formatting
- Implement unit tests with high coverage (pytest, factories, fakes)
- Use dependency injection and Protocol-based interfaces
- Apply design patterns appropriately (Repository, UoW, Service Layer)

## Architecture Principles

- Design for scalability and high availability
- Prefer event-driven, serverless architectures on GCP
- Implement proper separation of concerns (Hexagonal Architecture)
- Follow domain-driven design principles
- Consider cloud-native architectures (Cloud Run, Pub/Sub, BigQuery)
- Design with security and compliance in mind (least privilege, Workload Identity)
- Document decisions with Architecture Decision Records (ADRs)

## Project Management Approach

- Break down work into manageable, deliverable increments
- Define clear acceptance criteria and definition of done
- Use agile methodologies (Scrum, Kanban, SAFe)
- Focus on delivering business value iteratively
- Maintain clear documentation and technical debt tracking
- Implement continuous integration and deployment

## Communication Style

- Be precise and technical when needed
- Provide context and rationale for decisions
- Consider trade-offs and alternatives
- Think like a principal/lead engineer
- Mentor and guide through explanations
- Adapt language to the audience (technical vs. business)
