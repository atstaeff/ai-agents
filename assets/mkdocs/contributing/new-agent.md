# Create a New Agent

Guide for creating a new specialized AI agent.

---

## Prerequisites

- The agent covers a clearly defined role or technology
- No existing agent has the same focus
- The agent is broadly applicable (not too specific to one project)

## Step by Step

### 1. Create the File

Create a file under `agents/` following the naming convention:

```
agents/{name}.agent.md
```

Example: `agents/rust-expert.agent.md`

### 2. Follow the Structure

Every agent needs the following sections:

```markdown
# {Name} Agent

## Identity
Who is the agent? Role, experience level, specialization.

## Core Responsibilities
What can the agent do? 5-8 core competencies.

## Instructions
How does the agent work? Numbered instructions.

## [Patterns / Templates / Checklists]
Concrete artifacts the agent uses.

## Example Output
Example of typical agent outputs.

## Cross-References
Related agents and skills.
```

### 3. Write the Identity

!!! tip "Best Practice"
    Write the identity in the second person:
    "You are a **{Name} Agent** — a {experience} specializing in {area}."

### 4. Define Instructions

- Numbered, prioritized instructions
- Start each instruction with a **bold label**
- Use concrete, action-oriented wording

### 5. Add Examples

- Before/after code examples
- Templates for typical outputs
- Checklists for recurring tasks

### 6. Set Cross-References

Link to:
- Related agents (e.g., Test Strategist for every language expert)
- Relevant skills (e.g., Clean Code, SOLID, Design Patterns)

## Checklist

- [ ] `.agent.md` file naming convention followed
- [ ] Identity, Responsibilities, Instructions present
- [ ] At least 3 practical examples
- [ ] Cross-references to agents and skills
- [ ] No copyrighted content
- [ ] PR created with description
