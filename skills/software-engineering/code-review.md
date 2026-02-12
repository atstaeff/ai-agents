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

## Review Workflow

### Phase 1: Discovery
Start by gathering information about the changes:
- What triggered this modification?
- Which files contain the alterations?
- Are there connections to specific tasks or bugs?

### Phase 2: Technical Examination
Examine the technical aspects:
- Does the implementation achieve its intended goal?
- Are there scenarios that might cause unexpected behavior?
- Is the control flow clear and logical?
- Can someone unfamiliar with this code understand it quickly?
- Are variable and function names self-explanatory?

### Phase 3: Constructive Feedback
Structure your observations:

**Celebrate Wins** — Point out clever solutions and good practices.

**Flag Concerns** — Group feedback by urgency:
- Urgent: Blocks merging, needs immediate attention
- Important: Should be addressed soon
- Optional: Suggestions for future improvement

**Offer Guidance** — For each concern, provide:
- Why it matters
- A concrete example or alternative approach
- Resources if helpful

### Phase 4: Decision Point
Conclude with your recommendation:
- Ready to integrate
- Needs minor adjustments (specify which ones)
- Requires significant changes (explain why)

## Review Tips
- Balance critique with recognition
- Focus on substance over style preferences
- Ask questions when uncertain rather than making assumptions
- Consider the project's maturity and constraints
- Remember you're reviewing code, not judging the author

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
