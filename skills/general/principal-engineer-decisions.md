# Principal Engineer Decision Making

## Instructions for AI

Guide technical decisions at the principal/lead engineer level, balancing multiple competing concerns.

## Decision Framework

### The Three Pillars Analysis

When evaluating technical options:

**Business Alignment**
- Revenue impact timeline
- Market positioning advantage
- Competitive response capability
- Customer satisfaction metrics

**Technical Excellence**
- Long-term maintainability horizon
- Team capability match
- Technology risk assessment
- Scaling characteristics

**Organizational Impact**
- Team velocity implications
- Knowledge distribution
- Hiring market considerations
- Cross-team dependencies

## Decision Documentation

### Lightweight Decision Log Format

```markdown
## Decision: [Brief Title]
Date: [YYYY-MM-DD] | Participants: [Names] | Reversible: [Yes/No]

Context (2-3 sentences):
The specific situation requiring a decision.

Options Evaluated:
A. [Option] - Pros: [...] Cons: [...]
B. [Option] - Pros: [...] Cons: [...]

Chosen Path: [Letter]
Rationale: [2-3 key deciding factors]

Success Metrics: [How we'll know this worked]
Review Date: [When to reassess]
```

## Handling Ambiguity

### The 70% Rule

Make decisions when you have 70% of the information you wish you had:
- Waiting for 100% means delayed action
- Acting at 50% means excessive risk
- 70% balances speed with informed choice

### Reversibility Assessment

**Type 1 Decisions** (One-way doors)
- Database technology choice
- Primary programming language
- Core architecture patterns
Take more time, involve more people

**Type 2 Decisions** (Two-way doors)
- Library selections
- UI framework choices  
- Deployment tooling
Decide faster, iterate based on feedback

## Communication Patterns

### Upward Communication (To Leadership)

Focus on business outcomes:
"Moving to event-driven architecture enables 3x faster feature deployment by eliminating database coupling between teams."

Not technical details:
"We need Kafka because microservices should use async messaging."

### Peer Communication (To Other Leads)

Emphasize collaboration:
"Here's what I'm considering [X, Y, Z]. What constraints am I missing from your domain?"

### Downward Communication (To Team)

Provide context and autonomy:
"We're prioritizing API stability over new features this quarter because [business reason]. Within that constraint, you have full autonomy on implementation approach."

## Managing Technical Strategy

### Strategy vs Tactics

**Strategic** (Changes every 2-3 years):
- Core technology stack
- Architectural patterns
- Data storage approaches
- Security model

**Tactical** (Changes every 3-6 months):
- Specific tools and libraries
- Development workflows
- Testing approaches
- Deployment processes

Don't confuse the two - tactics should adapt quickly to new information.

## Building Consensus

### The Disagreement Ladder

When facing opposition:

1. **Silent Disagreement** - They don't speak up
   Response: Create psychological safety

2. **Stated Concerns** - They voice worries
   Response: Address each concern explicitly

3. **Alternative Proposals** - They suggest different approaches
   Response: Compare objectively using framework

4. **Fundamental Opposition** - Deep disagreement on principles
   Response: Escalate or commit to disagree-and-commit

### Disagree and Commit

When consensus isn't possible:
"I hear your concerns about [X]. I've decided we're going with [Y] because [reasons]. I need your full commitment to make this successful, even though you disagree. Can I count on that?"

## Balancing Innovation vs Stability

### The Innovation Budget

Allocate risk across the portfolio:
- 70% proven, stable technologies
- 20% recently proven (1-2 years in production elsewhere)
- 10% experimental or cutting edge

Don't exceed 10% experimental simultaneously.

## Mentoring Through Decisions

### Teaching Decision-Making

Instead of: "Use PostgreSQL for this."

Try: "What factors are you considering? [Listen] Those are good points. Have you also thought about [X]? Here's how I'd weight these factors: [framework]. What would you decide given that?"

## Example Prompts

"Help me decide between technology options using principal engineer perspective"

"Document this architecture decision for leadership review"

"Evaluate whether this is a Type 1 or Type 2 decision"

"Frame this technical concern in business impact terms"

"Create a lightweight decision record for this choice"
