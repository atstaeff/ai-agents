# Effective Communication

## Instructions for AI

When communicating technical concepts, follow these guidelines for clarity and effectiveness:

## Writing Style

### For Technical Documentation

**Be Clear and Concise**
- Use simple language when possible
- Define technical terms on first use
- Short paragraphs (3-5 sentences)
- Active voice over passive voice

**Structure Information**
- Start with overview/summary
- Logical progression of ideas
- Use headings and subheadings
- Bullet points for lists
- Code examples for clarity

**Be Precise**
- Specific over vague
- Quantify when possible (e.g., "reduces by 30%" vs "improves")
- Avoid ambiguous terms (e.g., "recently", "soon")
- Define scope and boundaries

### For Code Comments

**When to Comment**
- Why, not what
- Complex algorithms
- Business rules
- Workarounds for bugs
- TODO items with context

**When NOT to Comment**
- Self-explanatory code
- Redundant information
- Outdated information

```javascript
// ❌ Bad: States the obvious
// Increment counter by 1
counter++;

// ✅ Good: Explains why
// Skip first item as it's the header row
for (let i = 1; i < items.length; i++) {
```

## Technical Writing Principles

### Audience Awareness

**For Developers**
- Assume technical knowledge
- Include code examples
- Reference relevant documentation
- Focus on implementation details

**For Non-Technical Stakeholders**
- Avoid jargon or define it
- Use analogies and metaphors
- Focus on business impact
- Visual aids (diagrams, charts)

**For Mixed Audiences**
- Layer information (summary → details)
- Use sidebars for technical details
- Provide multiple entry points
- Clear section headings

### Documentation Types

**API Documentation**
- Endpoint description
- Request/response examples
- Authentication requirements
- Error codes
- Rate limits
- Try-it-out functionality

**Architecture Documentation**
- System overview diagram
- Component descriptions
- Data flow diagrams
- Technology stack
- Key decisions (ADRs)
- Trade-offs considered

**User Documentation**
- Step-by-step instructions
- Screenshots where helpful
- Common problems and solutions
- Prerequisites clearly stated

**README Files**
- What the project does
- How to install/setup
- Quick start guide
- How to contribute
- Where to get help

## Communication in Code Reviews

### Constructive Feedback

**Structure**
1. Start with positive feedback
2. Identify specific issues
3. Suggest concrete improvements
4. Explain the reasoning

**Tone**
- Use "we" not "you"
- Ask questions, don't demand
- Focus on code, not person
- Assume good intent

**Examples**
```
❌ "This is wrong. You should use a HashMap."

✅ "For this use case, a HashMap would provide O(1) lookups instead 
   of O(n), significantly improving performance when the list grows. 
   Would that work for your scenario?"
```

```
❌ "Why did you do it this way?"

✅ "I'm curious about this approach. Have you considered [alternative]? 
   It might [benefit], but I might be missing something about your 
   requirements."
```

### Levels of Feedback

**Critical** (Must fix)
- Security vulnerabilities
- Bugs that break functionality
- Breaking changes without migration

**Important** (Should fix)
- Design issues
- Maintainability concerns
- Missing tests for critical paths

**Minor** (Nice to have)
- Style inconsistencies (if not auto-fixable)
- Minor refactoring opportunities
- Additional test cases

**Praise** (Acknowledge)
- Clever solutions
- Good practices
- Improved code quality

## Architecture Decision Records (ADRs)

### Structure
```markdown
# [Number]. [Title]

Date: YYYY-MM-DD

## Status
[Proposed | Accepted | Deprecated | Superseded]

## Context
[What is the issue we're seeing that motivates this decision?]

## Decision
[What is the change we're proposing/have agreed to?]

## Consequences
[What becomes easier or harder because of this decision?]

### Positive
- [Benefit 1]
- [Benefit 2]

### Negative
- [Trade-off 1]
- [Trade-off 2]

## Alternatives Considered
[What other options did we consider?]

## References
[Links to relevant documents, discussions, etc.]
```

## Technical Presentations

### Slide Design

**Less is More**
- One idea per slide
- Large, readable fonts (minimum 24pt)
- High contrast
- Images over text
- Code snippets (short and relevant)

**Structure**
1. Title slide (what, who)
2. Agenda (what to expect)
3. Problem/Context (why we're here)
4. Solution/Proposal (what we're doing)
5. Implementation (how it works)
6. Results/Benefits (impact)
7. Next Steps (what's next)
8. Q&A

### Delivery Tips

**Before Presenting**
- Know your audience
- Rehearse key points
- Test equipment
- Have backup plan

**During Presentation**
- Make eye contact
- Speak clearly and pace yourself
- Use examples and stories
- Invite questions
- Handle interruptions gracefully

## Email Communication

### Subject Lines
```
❌ "Update"
❌ "Question"

✅ "[Action Required] Deploy approval needed by Friday"
✅ "[FYI] Q1 metrics report attached"
```

### Email Structure

**For Requests**
1. Brief context (1-2 sentences)
2. Specific ask
3. Why it matters
4. Deadline if applicable
5. Thank you

**For Updates**
1. Summary (TL;DR)
2. Detailed information
3. Action items
4. Next steps

**For Technical Issues**
1. What's happening
2. Impact and urgency
3. What you've tried
4. What you need
5. Timeline

## Meeting Communication

### Running Effective Meetings

**Before**
- Clear agenda shared in advance
- Required vs optional attendees
- Pre-read materials if needed
- Time limit stated

**During**
- Start and end on time
- Follow agenda
- Assign note-taker
- Capture action items
- Parking lot for off-topic items

**After**
- Share notes promptly
- Clear action items with owners
- Follow up on commitments

### Types of Meetings

**Standup**
- Quick (15 min)
- What did you do, what will you do, any blockers
- No problem-solving (take offline)

**Design Review**
- Present proposal
- Gather feedback
- Document decisions
- Agree on next steps

**Retrospective**
- Safe environment
- What went well, what didn't
- Action items for improvement
- Blameless

## Diagrams and Visuals

### When to Use Diagrams

- System architecture
- Data flow
- Sequence of operations
- Component relationships
- Process workflows

### Diagram Types

**Architecture Diagrams**
- C4 Model (Context, Container, Component, Code)
- Deployment diagrams
- Network topology

**Flow Diagrams**
- Flowcharts for processes
- Sequence diagrams for interactions
- Data flow diagrams

**Tools**
- draw.io (diagrams.net)
- PlantUML (text-based)
- Mermaid (markdown-based)
- Lucidchart
- Microsoft Visio

### Diagram Best Practices

- Clear labels
- Consistent notation
- Legend when needed
- Not too detailed
- Keep up-to-date

## Cross-Cultural Communication

### Be Aware Of

- Time zones (use UTC or specify timezone)
- Holidays and working hours
- Language barriers (simple English)
- Direct vs indirect communication styles
- Formality expectations

### Best Practices

- Be patient and clear
- Confirm understanding
- Avoid idioms and slang
- Written follow-up for important points
- Respectful of differences

## Example Prompts

"Write API documentation for this endpoint"

"Review this technical proposal for clarity"

"Create an ADR for this architecture decision"

"Rewrite this technical explanation for a non-technical audience"

"Improve the communication in this code review comment"

"Draft release notes for this version"

## Related Skills & Agents

- [Stakeholder Agent](../../agents/stakeholder-agent.agent.md)
- [Presentation Agent](../../agents/presentation-agent.agent.md)
- [PR Crafting](../team-collaboration/pr-crafting.md)
- [Progress Sync](../team-collaboration/progress-sync.md)
- [Principal Engineer Decisions](../general/principal-engineer-decisions.md)
