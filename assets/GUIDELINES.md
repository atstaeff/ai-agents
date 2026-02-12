# Copilot Expert Hub — Guidelines

## Agent Design Guidelines

### 1. Single Responsibility
Each agent should have a clear, focused role. If an agent does too many things, split it.

### 2. Consistent Structure
Every agent file must follow the standard template:
- Identity → Core Responsibilities → Instructions → Domain Content → Best Practices → Anti-Patterns → Example Prompts → Related Skills

### 3. Actionable Instructions
Instructions should be specific enough that the agent behavior is predictable and useful. Avoid vague guidance like "be helpful" — instead, define concrete behaviors.

### 4. Cross-Referencing
Agents should reference related skills and other agents. This creates a navigable knowledge graph.

### 5. Example-Driven
Include code examples, templates, and real-world scenarios. Abstract advice is less useful than concrete patterns.

## Skill Design Guidelines

### 1. AI-First
Skills are primarily consumed by AI assistants. Write them so an AI can parse and apply the guidance effectively.

### 2. Pattern-Based
Organize skills around reusable patterns with:
- Problem description
- Solution with code example
- When to use / when not to use

### 3. Language & Framework Specificity
Be specific about versions (Python 3.12+, Pydantic v2, FastAPI) to avoid ambiguity.

### 4. Progressive Detail
Start with the most common/important patterns, then add advanced topics. This helps both AI and human readers.

## Template Guidelines

### Marp Templates
- Must include `marp: true` in frontmatter
- Use consistent theme/styling within a template
- Include placeholders clearly marked with `{variable_name}`
- Add speaker notes for content slides
- Follow the Rule of Three (max 3 points per slide)

### Proposal Templates
- Include all standard sections (summary, scope, timeline, budget)
- Use tables for structured data
- Clearly mark out-of-scope items
- Include assumptions and risks

## Content Quality

### Writing
- Use clear, concise language
- Prefer active voice
- Include both positive (✅) and negative (❌) examples
- Use consistent formatting and terminology

### Code Examples
- Must be syntactically correct
- Use modern language features
- Include type hints (Python)
- Follow the project's style guidelines (ruff, PEP 8)
- Keep examples focused — show one concept at a time

### Diagrams
- Use Mermaid.js for diagrams (supported in GitHub Markdown)
- Keep diagrams simple and readable
- Include text descriptions alongside diagrams for accessibility

## Versioning

### When to Update
- Language/framework version changes (e.g., Python 3.11 → 3.12)
- New best practices emerge
- Anti-patterns are discovered
- Community feedback suggests improvements

### Deprecation
Mark deprecated content clearly:
```markdown
> ⚠️ **Deprecated:** This pattern is deprecated in favor of [New Pattern](link).
> Reason: {why it was deprecated}
> Migration: {how to update}
```

## Security

- Never include real credentials, API keys, or secrets in examples
- Use placeholder values clearly marked as such
- Follow security best practices in all code examples
- Reference the [Security Skill](../skills/architecture/security.md) for security-related content

## Naming Conventions

| Item | Convention | Example |
|------|-----------|---------|
| Agent files | `{name}.agent.md` | `lead-architect.agent.md` |
| Skill directories | `kebab-case/` | `python-patterns/` |
| Skill files | `SKILL.md` | `skills/testing/SKILL.md` |
| Template files | `kebab-case.md` | `client-pitch.md` |
| Workflow files | `kebab-case.yml` | `validate-agents.yml` |
