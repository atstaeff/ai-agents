# Architecture Planning Skill

## Purpose
Design software systems that solve real problems while remaining flexible for future needs.

## Planning Process

### Step 1: Understand the Landscape
Before designing anything, investigate:
- What problems are users actually experiencing?
- What are the hard constraints (budget, timeline, technical)?
- What existing systems must this integrate with?
- What volumes and loads will it handle?

### Step 2: Define Success Criteria
Be explicit about what matters most:
- Speed targets (response times, throughput)
- Reliability expectations (uptime, error rates)
- Scale requirements (users, data volume, growth rate)
- Security boundaries (data protection, access control)
- Cost limitations (infrastructure, maintenance)

### Step 3: Explore Approaches
Consider different structural patterns:

**Organizational Patterns**
- Single unified application
- Multiple independent services
- Event-driven reactive system
- Hybrid combinations

For each approach, document:
- What it enables
- What it complicates
- Where it fits best
- What it costs

### Step 4: Component Mapping
Sketch out the major pieces:
- What responsibilities does each piece have?
- How do they communicate?
- Where does data live?
- What fails if a piece goes down?

### Step 5: Technology Matching
Select tools and frameworks based on:
- Team familiarity and expertise
- Community support and documentation
- Performance characteristics
- Operational complexity
- Long-term viability

### Step 6: Document Decisions
For significant choices, record:
- The situation that prompted this decision
- Options you evaluated
- Why you picked this option
- Trade-offs you're accepting
- Date and decision makers

Use this format:
```
Decision: [Short descriptive title]
Date: [When decided]
Context: [What situation led to this choice]
Options: [What alternatives did you consider]
Choice: [What you decided]
Reasoning: [Why this made sense]
Consequences: [What this enables and what it costs]
```

### Step 7: Visual Documentation
Create diagrams showing:
- How users interact with the system
- How components connect and communicate
- How data flows through the system
- Where external dependencies exist

Keep diagrams simple and focused on specific aspects.

### Step 8: Validation
Test your design before implementing:
- Build small prototypes of risky components
- Simulate load patterns
- Verify integration assumptions
- Review with experienced engineers

## Design Principles

**Start Simple**
Begin with the simplest thing that works. Add complexity only when simpler approaches fail.

**Plan for Change**
Assume requirements will evolve. Make boundaries between components clear.

**Consider Operations**
Think about deployment, monitoring, debugging, and scaling from the start.

**Document Reasoning**
Future you (or others) will need to understand why choices were made.

**Embrace Trade-offs**
Every decision sacrifices something. Be intentional about what you're trading.

## Common Pitfalls
- Over-engineering for hypothetical future requirements
- Choosing unfamiliar technology without good reason
- Ignoring operational complexity
- Not validating assumptions early
- Forgetting about data migration paths
- Skipping documentation of key decisions
