# Create a New Skill

Guide for creating a new technical knowledge base (skill).

---

## Prerequisites

- The skill fits into an existing category or justifies a new one
- No skill with the same focus exists
- The skill is broadly applicable for AI-assisted development

## Step by Step

### 1. Choose a Category

| Category | Directory | Examples |
|----------|-----------|----------|
| Language Patterns | `skills/{language}-patterns/` | Python, Golang, Flutter |
| Software Engineering | `skills/software-engineering/` | Clean Code, SOLID |
| Architecture | `skills/architecture/` | Microservices, DDD |
| Project & Team | `skills/team-collaboration/` | PR Crafting, Incident Response |
| Other | `skills/{topic}/` | Anti-Patterns |

### 2. Create the File

```
skills/{category}/{skill-name}.md
# or
skills/{skill-name}/SKILL.md
```

### 3. Use the Template

Copy the template from `templates/skill-template.md`:

```markdown
# {Skill Name}

## Instructions for AI
Clear instructions for the AI agent.

## [Main Topic 1]
Detailed explanation with examples.

## Best Practices
✅ Good Practice 1
✅ Good Practice 2

## Anti-Patterns
❌ Bad Practice 1
❌ Bad Practice 2

## Example Prompts
"Example prompt 1"

## Related Skills
- [Related Skill 1]
```

### 4. Write "Instructions for AI"

This section is **the most important** — it controls how the agent applies the skill.

!!! tip "Best Practice"
    - Be specific and action-oriented
    - Describe "how", not just "what"
    - Include concrete examples
    - Consider edge cases

### 5. Provide Examples

- ✅ / ❌ Before/after comparisons
- Code in Python, Go, or TypeScript
- Real-world scenarios

## Checklist

- [ ] Correct category and directory chosen
- [ ] Template structure followed
- [ ] "Instructions for AI" clearly formulated
- [ ] At least 2 code examples (good/bad)
- [ ] Related skills linked
- [ ] PR created with description
