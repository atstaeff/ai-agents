# Technical Debt Assessment Skill

## Purpose
Identify, evaluate, and plan for addressing technical debt in software systems.

## Assessment Approach

### Discovery Phase
Identify areas where technical debt exists:

**Code Examination**
- Look for repeated patterns that should be abstracted
- Find modules that change frequently due to fragility
- Identify areas with low or no test coverage
- Spot outdated dependencies or deprecated APIs
- Notice performance bottlenecks

**Team Feedback**
Ask developers about:
- Which parts of the codebase slow them down
- Where bugs cluster most frequently
- What makes onboarding new team members difficult
- Which areas they avoid modifying if possible

**System Metrics**
Review data showing:
- Build and deployment times
- Test execution duration
- Frequency of production incidents
- Time to implement typical changes
- Bug discovery rates by module

### Categorization
Group technical debt by type:

**Structural Issues**
- Tight coupling between components
- Unclear separation of concerns
- Poor abstraction boundaries
- Inconsistent architectural patterns

**Code Quality Problems**
- Complex methods that are hard to understand
- Inconsistent coding conventions
- Poor naming that obscures intent
- Missing or misleading documentation

**Testing Gaps**
- Critical paths without test coverage
- Flaky tests that reduce confidence
- Slow test suites that delay feedback
- Tests that don't reflect real usage

**Infrastructure Debt**
- Manual deployment processes
- Missing monitoring or observability
- Outdated or unsupported dependencies
- Inadequate development environments

### Impact Evaluation
For each debt item, assess:

**Pain Level**
- How often does this cause problems?
- How severe are those problems?
- How many people does it affect?

**Cost to Fix**
- How much effort to address properly?
- What knowledge or skills are required?
- Are there risky changes involved?

**Cost of Waiting**
- Does this get worse over time?
- What opportunities does it block?
- How much does it slow development?

Use a simple scoring method:
```
Urgency Score = (Pain Level × Affected People) / Cost to Fix

High Score = Address soon
Medium Score = Plan for upcoming sprint
Low Score = Track but defer
```

### Planning Resolution

**Quick Wins** (1-3 days each)
Pick items that are low effort but meaningful improvement. These build momentum and demonstrate value.

**Focused Sprints** (1-2 weeks)
Dedicate specific time to larger debt items. Don't mix with feature work.

**Incremental Improvement** (ongoing)
Build debt reduction into regular work: leave code better than you found it.

**Major Refactoring** (planned projects)
Treat significant architectural changes like product features with proper planning and resourcing.

### Documentation Format
Track technical debt items:

```
Item: [Brief description]
Location: [Where in the codebase]
Type: [Structural / Quality / Testing / Infrastructure]

Impact:
- Pain: [How much it hurts, scale 1-5]
- Frequency: [How often issues arise]
- Affects: [Who or what experiences the pain]

Resolution:
- Approach: [How to address this]
- Effort: [Time estimate]
- Risk: [What could go wrong]
- Blockers: [What's preventing us from fixing this now]

Priority: [High / Medium / Low]
Status: [Identified / Planned / In Progress / Resolved]
```

## Balancing Debt and Features

**Reserve Capacity**
Dedicate a percentage of each iteration to debt reduction (typically 15-25%).

**Track Trends**
Monitor whether technical debt is growing or shrinking over time.

**Make It Visible**
Share debt status with stakeholders so they understand the tradeoffs.

**Connect to Business Value**
Explain how reducing debt enables faster feature delivery, fewer bugs, or better reliability.

## Prevention Strategies

**Definition of Done**
Include quality criteria that prevent new debt:
- Tests written and passing
- Code reviewed by peer
- Documentation updated
- Performance acceptable

**Regular Maintenance**
Schedule time for:
- Dependency updates
- Refactoring opportunities
- Test improvement
- Tool upgrades

**Share Knowledge**
Ensure multiple people understand critical systems to reduce risk and improve quality.

**Automate Standards**
Use linters, formatters, and static analysis to enforce quality automatically.
