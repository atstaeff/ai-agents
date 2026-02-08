# Technical Debt Management

## Instructions for AI

Manage technical debt systematically to maintain code quality and team velocity:

## Understanding Technical Debt

### Definition
Technical debt is the implied cost of rework caused by choosing an easy (limited) solution now instead of a better approach that would take longer.

### Types of Technical Debt

**Deliberate & Prudent**
- Conscious decision to ship faster
- Plan to pay back later
- Example: "We know this is not optimal, but we need to meet deadline"

**Deliberate & Reckless**
- Knowing the right way but not caring
- No plan to improve
- Example: "We don't have time for design"

**Inadvertent & Prudent**
- Learn better approach after implementation
- Example: "Now we know how we should have done it"

**Inadvertent & Reckless**
- Lack of skill or knowledge
- Example: "What's layering?"

## Sources of Technical Debt

- **Code Quality**: Poor design, code smells, lack of tests
- **Architecture**: Outdated patterns, tight coupling, no separation of concerns
- **Documentation**: Missing or outdated documentation
- **Infrastructure**: Legacy systems, outdated dependencies
- **Testing**: Insufficient test coverage, manual testing
- **Process**: No code reviews, poor CI/CD
- **Knowledge**: Only one person knows critical system

## Measuring Technical Debt

### Metrics

**Code Quality Metrics:**
- Code coverage percentage
- Cyclomatic complexity
- Code duplication
- Code smells (SonarQube)
- Technical debt ratio

**Team Impact Metrics:**
- Velocity trend (declining indicates debt)
- Bug rate and severity
- Time to add features (increasing)
- Deployment frequency (decreasing)
- Mean time to recover

**Business Impact:**
- Cost of maintenance
- Time to market for new features
- Customer satisfaction
- System downtime/reliability

### Tools
- SonarQube: Code quality and security
- CodeClimate: Maintainability analysis
- NDepend: .NET code analysis
- ESLint/TSLint: JavaScript/TypeScript
- ReSharper: C# code analysis

## Technical Debt Quadrant

```
         Prudent
            |
Deliberate  |  Inadvertent
------------|------------
 Reckless   |
            |
```

**Goal:** Move toward Deliberate & Prudent quadrant
- Accept some debt strategically
- Document and plan repayment
- Avoid reckless debt

## Managing Technical Debt

### Tracking

**Technical Debt Backlog**
- Maintain separate backlog or tagged items
- Describe impact and effort
- Prioritize by ROI
- Review regularly

**Debt Item Template:**
```markdown
## Description
[What is the technical debt?]

## Impact
- Development speed
- Code maintainability
- System reliability
- Team morale

## Effort to Fix
[Estimated time/story points]

## Priority
[High/Medium/Low based on impact/effort]

## Notes
[Additional context, dependencies]
```

### Prioritization

**Impact vs Effort Matrix:**
```
High Impact, Low Effort   →  Fix immediately
High Impact, High Effort  →  Plan for dedicated time
Low Impact, Low Effort    →  Fix when in area
Low Impact, High Effort   →  Defer or accept
```

**Consider:**
- Business risk
- Development velocity impact
- Security vulnerabilities
- Onboarding difficulty
- Team morale

### Strategies for Paying Down Debt

**Boy Scout Rule**
- Leave code better than you found it
- Small improvements with each change
- Gradual improvement over time

**Dedicated Debt Sprints**
- Allocate entire sprint to debt
- Schedule regularly (quarterly)
- Focus on high-impact items
- Measure improvement

**20% Time**
- Reserve 20% of each sprint for debt
- Balance features with improvements
- Sustainable pace
- Prevents accumulation

**Strangler Fig Pattern**
- Gradually replace problematic areas
- Implement new system alongside old
- Route new features to new system
- Eventually retire old system

**Refactoring**
- Continuous improvement
- Part of normal development
- Improve structure without changing behavior
- Supported by tests

### Prevention

**Code Reviews**
- Catch debt before it's merged
- Knowledge sharing
- Maintain standards

**Definition of Done**
- Include quality requirements
- Tests written and passing
- Documentation updated
- No critical code smells

**Automated Quality Gates**
- Fail build on quality threshold
- Code coverage requirements
- No critical vulnerabilities
- Complexity limits

**Architecture Decision Records (ADRs)**
- Document significant decisions
- Explain trade-offs
- Prevent inadvertent debt
- Help future teams understand context

**Regular Refactoring**
- Part of normal workflow
- Improve code structure
- Keep codebase healthy
- Don't wait for dedicated time

## Communication

### With Stakeholders

**Translate to Business Impact:**
- ❌ "We have high cyclomatic complexity"
- ✅ "Adding new features takes 50% longer due to code complexity"

**Use Analogies:**
- "Like not changing oil in a car - works fine initially but eventually breaks down"
- "Like taking a shortcut through mud - faster now, but tracking mud everywhere later"

**Quantify Impact:**
- "Reduces development velocity by 30%"
- "Increases bug rate by 2x"
- "Costs $X in maintenance per month"

### With Team

**Make Debt Visible:**
- Track in backlog
- Discuss in retrospectives
- Include in sprint planning
- Dashboard/metrics

**Celebrate Improvements:**
- Acknowledge debt reduction
- Share metrics improvements
- Recognize good practices
- Motivate continued effort

## Technical Debt Policy

### Example Policy

**Prevention:**
- All code requires review
- Tests required for all features
- Automated quality gates in CI/CD
- Regular architecture reviews

**Measurement:**
- Weekly code quality metrics review
- Monthly technical debt backlog review
- Track velocity and quality trends

**Resolution:**
- 20% of sprint capacity for debt
- Quarterly debt reduction sprint
- Boy Scout Rule enforced
- High-priority debt addressed immediately

**Governance:**
- Architecture review board
- Technical debt champions
- Regular debt audits
- Executive sponsorship

## Anti-Patterns

❌ Ignoring technical debt
❌ "We'll fix it later" (never happens)
❌ Accumulating without tracking
❌ No time allocated for paydown
❌ Only addressing when crisis hits
❌ Blaming individuals
❌ Perfect code paralysis (opposite extreme)

## Example Prompts

"Analyze this codebase for technical debt"

"Create a technical debt item for this design issue"

"Prioritize these technical debt items by impact and effort"

"Propose a refactoring plan for this legacy system"

"Write a technical debt report for stakeholders"

"Design a process for preventing technical debt accumulation"
