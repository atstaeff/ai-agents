# Code Review Guidelines

## Instructions for AI

When conducting code reviews, evaluate code across multiple dimensions:

## Functional Correctness
- Does the code do what it's supposed to do?
- Are edge cases handled properly?
- Is error handling comprehensive?
- Are there potential bugs or logical errors?
- Does it meet the acceptance criteria?

## Code Quality
- Is the code readable and maintainable?
- Are naming conventions followed?
- Is the code properly structured and organized?
- Are there code smells (duplications, long methods, etc.)?
- Does it follow language idioms and best practices?

## Design & Architecture
- Does it follow SOLID principles?
- Are appropriate design patterns used?
- Is there proper separation of concerns?
- Is the abstraction level appropriate?
- Does it fit well with existing architecture?

## Performance
- Are there obvious performance issues?
- Is resource usage optimal (memory, CPU, I/O)?
- Are database queries efficient?
- Are there N+1 query problems?
- Is caching used appropriately?

## Security
- Are there SQL injection vulnerabilities?
- Is input properly validated and sanitized?
- Are authentication and authorization correct?
- Are secrets properly managed?
- Is sensitive data encrypted/protected?

## Testing
- Are unit tests present and meaningful?
- Is test coverage adequate?
- Are edge cases tested?
- Are tests readable and maintainable?
- Do tests follow AAA pattern?

## Documentation
- Are complex algorithms documented?
- Is the public API documented?
- Are assumptions and limitations noted?
- Is the README updated if needed?
- Are breaking changes clearly communicated?

## Dependencies
- Are new dependencies necessary and appropriate?
- Are dependency versions specified and up-to-date?
- Are security vulnerabilities checked?
- Is the dependency well-maintained?

## Review Process
1. Understand the context and requirements
2. Review high-level design before details
3. Look for patterns, not just individual issues
4. Be constructive and specific in feedback
5. Distinguish between must-fix and suggestions
6. Acknowledge good practices

## Review Comment Levels
- **Critical**: Must be fixed (bugs, security issues)
- **Important**: Should be fixed (design flaws, maintainability)
- **Minor**: Consider fixing (style, minor improvements)
- **Suggestion**: Optional (alternative approaches)
- **Praise**: Recognize good work

## Example Prompts

"Review this pull request for code quality and best practices"

"Check this code for potential security vulnerabilities"

"Evaluate this implementation for performance issues"

"Review these unit tests for completeness and quality"
