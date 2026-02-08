# How to Contribute a New Skill

Thank you for contributing to the AI Skills repository! Follow these guidelines to add a new skill.

## Before You Start

1. Check if the skill already exists
2. Ensure it fits one of the categories: Software Engineering, Architecture, Project Management, or General
3. Consider if it's broadly applicable to AI-assisted development

## Steps to Add a Skill

### 1. Choose the Right Category

Place your skill file in the appropriate directory:
- `/skills/software-engineering/` - Coding practices, testing, code quality
- `/skills/architecture/` - System design, patterns, architectural styles
- `/skills/project-management/` - Process, methodology, team practices
- `/skills/general/` - Cross-cutting concerns or other topics

### 2. Create Your Skill File

- Use lowercase with hyphens for filename: `your-skill-name.md`
- Copy the template from `/templates/skill-template.md`
- Follow the structure in the template

### 3. Write Clear Instructions

The "Instructions for AI" section is crucial:
- Be specific and actionable
- Focus on "how" not just "what"
- Include concrete examples
- Consider edge cases

### 4. Provide Examples

Include code examples showing:
- ✅ Good practices
- ❌ Bad practices (anti-patterns)
- Before/after refactoring
- Different scenarios

### 5. Add Example Prompts

Help users know how to invoke this skill:
```markdown
## Example Prompts

"Review this code for [specific issue]"
"Implement [feature] using [pattern/practice]"
"Refactor this to follow [principle]"
```

### 6. Quality Checklist

Before submitting:
- [ ] File follows template structure
- [ ] Instructions are clear and actionable
- [ ] Includes concrete code examples
- [ ] Has 3+ example prompts
- [ ] Free of typos and grammatical errors
- [ ] Properly formatted markdown
- [ ] Tested with an AI assistant (if possible)

### 7. Update Documentation

If adding a new category or major skill:
- Update main README.md
- Add to table of contents
- Link from related skills

## Skill Quality Guidelines

### Good Instructions
```markdown
When reviewing code for SOLID violations:
1. Check each class for single responsibility
2. Identify dependencies on concrete classes
3. Suggest abstractions for dependencies
4. Provide specific refactoring steps
```

### Poor Instructions
```markdown
Review the code and make it better following SOLID principles.
```

### Good Examples
```python
# ❌ Violates Single Responsibility
class UserManager:
    def save_user(self, user):
        # Database logic
        pass
    
    def send_welcome_email(self, user):
        # Email logic
        pass

# ✅ Follows Single Responsibility
class UserRepository:
    def save(self, user):
        # Database logic only
        pass

class EmailService:
    def send_welcome_email(self, user):
        # Email logic only
        pass
```

## Markdown Formatting

### Headers
```markdown
# Main Title (h1) - Only for document title
## Major Section (h2)
### Subsection (h3)
#### Minor Point (h4)
```

### Code Blocks
```markdown
​```python
def example():
    return "Use language-specific highlighting"
​```
```

### Lists
```markdown
- Unordered list item
- Another item
  - Nested item

1. Ordered list item
2. Another item
```

### Emphasis
```markdown
**Bold** for important terms
*Italic* for emphasis
`code` for inline code or commands
```

### Links
```markdown
[Link text](url)
[Related Skill](../architecture/microservices.md)
```

## Testing Your Skill

1. Try using it with an AI assistant (GitHub Copilot, ChatGPT, etc.)
2. Test the example prompts
3. Verify the AI understands and applies the guidance
4. Refine based on results

## Submitting Your Contribution

1. Fork the repository
2. Create a branch: `git checkout -b add-skill-name`
3. Add your skill file
4. Update relevant documentation
5. Commit with clear message: `git commit -m "Add skill: Your Skill Name"`
6. Push and create a Pull Request
7. Describe what the skill covers and why it's useful

## Review Process

Maintainers will review for:
- Accuracy of technical content
- Clarity of instructions
- Quality of examples
- Proper formatting
- Fit with repository goals

## Questions?

Open an issue for:
- Clarification on guidelines
- Suggestions for new categories
- Discussion of potential skills
- General feedback

Thank you for contributing! 🎉
