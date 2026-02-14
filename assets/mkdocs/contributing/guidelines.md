# Guidelines

> Quality standards and conventions for contributions to the Copilot Expert Hub.

---

## General Conventions

### File Naming

- Lowercase with hyphens: `my-skill-name.md`
- Agents: `{name}.agent.md`
- Skills: `{name}.md` or `SKILL.md` in a subdirectory

### Markdown Standards

- Headings: `#` for title, `##` for sections, `###` for subsections
- Code blocks with language identifier: ` ```python `
- Consistent lists (either `-` or `*`)
- Tables for structured information

### Language

- Agent and skill source files: **English**
- Documentation pages (MkDocs): **English**
- Code examples and comments: **English**

## Content Standards

### Agents

| Requirement | Required |
|-------------|----------|
| Identity section | ✅ |
| Core Responsibilities (5-8) | ✅ |
| Numbered Instructions | ✅ |
| Code examples | ✅ |
| Before/after demos | Recommended |
| Cross-references | ✅ |

### Skills

| Requirement | Required |
|-------------|----------|
| "Instructions for AI" section | ✅ |
| Best Practices (✅) | ✅ |
| Anti-Patterns (❌) | ✅ |
| Code examples | ✅ |
| Example Prompts | Recommended |
| Related Skills | ✅ |

## Code Examples

### Languages

- **Python** — Primary language, used for most examples
- **Go** — For concurrency, microservices, CLIs
- **TypeScript** — For frontend examples
- **Dart** — For Flutter/mobile examples
- **Terraform** — For infrastructure-as-code

### Format

```python
# ❌ Before: Problematic code with explanation
def bad_example():
    pass

# ✅ After: Improved code with explanation
def good_example():
    pass
```

## Pull Request Process

1. Create a fork and branch
2. Implement changes and test locally
3. Create a PR with a clear description
4. Wait for review and incorporate feedback
5. Merged after approval

---

*Source files: [`CONTRIBUTING.md`](https://github.com/atstaeff/ai-agents/blob/main/CONTRIBUTING.md) · [`docs/GUIDELINES.md`](https://github.com/atstaeff/ai-agents/blob/main/docs/GUIDELINES.md)*
