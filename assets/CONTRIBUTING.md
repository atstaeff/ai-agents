# Contributing to Copilot Expert Hub

Thank you for your interest in contributing! This guide will help you add new agents, skills, and templates.

## How to Contribute

### Adding a New Agent

1. Create a file in `agents/` following the naming convention: `{name}.agent.md`
2. Use the required structure:

```markdown
# {Agent Name} Agent

## Identity
Who is this agent? What expertise do they have?

## Core Responsibilities
What does this agent do? (5-7 bullet points)

## Instructions
Step-by-step guidance for the agent's behavior.

## {Domain-Specific Sections}
Templates, patterns, checklists relevant to this agent.

## Best Practices
✅ What to do

## Anti-Patterns
❌ What to avoid

## Example Prompts
How to invoke this agent effectively.

## Related Skills
Links to relevant skills and other agents.
```

3. Run the validation workflow to ensure compliance
4. Submit a PR with a clear description

### Adding a New Skill

1. Create a directory in `skills/` with a descriptive name
2. Add a `SKILL.md` file with the required structure:

```markdown
# {Skill Name} Skill

## Instructions for AI
Clear guidance on how to apply this skill.

## Core Patterns / Concepts
The main content of the skill with code examples.

## Best Practices
✅ Recommended approaches

## Anti-Patterns
❌ Common mistakes

## Example Prompts
How to use this skill.

## Related Skills
Links to related content.
```

### Adding a Marp Template

1. Create a `.md` file in `marp-templates/`
2. Include Marp frontmatter:

```yaml
---
marp: true
theme: default
paginate: true
---
```

3. Follow the slide design principles from the [Marp Presentations Skill](../skills/marp-presentations/SKILL.md)

### Adding a Reference Repository

1. Create a directory in `reference-repos/`
2. Add a `README.md` explaining the reference architecture
3. Include structure diagrams, key principles, and getting started instructions

## Quality Standards

### All Content Must:

- Be accurate and up-to-date
- Include practical, real-world examples
- Follow consistent formatting
- Cross-reference related content
- Be tested (agents via prompts, templates via rendering)

### Code Examples Must:

- Use modern language features (Python 3.12+, Go 1.22+, Dart 3.x)
- Include type hints
- Follow language-specific style guides
- Be syntactically correct and runnable

### Writing Style:

- Be concise and actionable
- Use consistent terminology
- Include both "what to do" and "what to avoid"
- Provide context for recommendations

## Pull Request Process

1. **Branch** — Create a feature branch from `main`
2. **Implement** — Add or modify content following the guidelines
3. **Validate** — Ensure the CI checks pass
4. **PR** — Submit with a clear title and description
5. **Review** — Address feedback promptly
6. **Merge** — Squash merge into `main`

### PR Title Convention

```
feat(agents): add terraform-expert agent
fix(skills): update Python patterns for Pydantic v2
docs: improve contributing guidelines
feat(templates): add sprint retrospective Marp template
```

## Development Setup

```bash
# Clone the repository
git clone https://github.com/atstaeff/ai-agents.git
cd ai-agents

# Create a branch
git checkout -b feat/new-agent

# Make changes, then validate locally
# Check agent structure
for f in agents/*.agent.md; do
  echo "Checking $f..."
  grep -q "## Identity" "$f" && echo "  ✅ Identity" || echo "  ❌ Identity"
  grep -q "## Instructions" "$f" && echo "  ✅ Instructions" || echo "  ❌ Instructions"
done

# Commit and push
git add .
git commit -m "feat(agents): add new-agent"
git push origin feat/new-agent
```

## Questions?

Open an issue on GitHub or start a discussion.
