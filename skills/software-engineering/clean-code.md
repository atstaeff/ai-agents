# Clean Code Principles

## Instructions for AI

When writing or reviewing code, apply these clean code principles:

### Naming Conventions
- Use descriptive, intention-revealing names
- Avoid abbreviations unless universally understood
- Use pronounceable and searchable names
- Class names should be nouns, method names should be verbs
- Use consistent naming patterns across the codebase

### Functions
- Keep functions small (ideally < 20 lines)
- Functions should do one thing and do it well
- Use descriptive function names that explain what they do
- Minimize function parameters (ideally ≤ 3)
- Avoid flag arguments - split into separate functions
- Extract complex logic into well-named helper functions

### Code Structure
- Follow the Single Responsibility Principle
- Organize code by feature/domain, not by technical layer
- Keep related code close together
- Use consistent indentation and formatting
- Remove dead code and commented-out code

### Comments
- Code should be self-explanatory; minimize comments
- Use comments to explain "why", not "what"
- Keep comments up-to-date with code changes
- Document complex algorithms and business rules
- Use TODO comments sparingly and track them

### Error Handling
- Use exceptions for exceptional cases
- Provide meaningful error messages
- Don't return null; use Optional or null object pattern
- Clean up resources using try-with-resources or similar
- Log errors with appropriate context

### Testing
- Write tests first (TDD) when appropriate
- One assertion per test when possible
- Use descriptive test names that explain the scenario
- Follow AAA pattern: Arrange, Act, Assert
- Test edge cases and error conditions

## Example Prompts

"Review this code for clean code violations and suggest improvements"

"Refactor this function following clean code principles"

"Write this feature using TDD approach with clean code practices"
