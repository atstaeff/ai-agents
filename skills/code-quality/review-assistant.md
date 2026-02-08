# Review Assistant Skill

## Objective
Help teams examine code changes effectively through structured analysis and collaborative feedback.

## Workflow

### Phase One: Discovery
Start by gathering information about the changes:
- What triggered this modification?
- Which files contain the alterations?
- Are there connections to specific tasks or bugs?

### Phase Two: Technical Examination
Examine the technical aspects using these lenses:

**Logic Verification**
- Does the implementation achieve its intended goal?
- Are there scenarios that might cause unexpected behavior?
- Is the control flow clear and logical?

**Code Craftsmanship**
- Can someone unfamiliar with this code understand it quickly?
- Are variable and function names self-explanatory?
- Is there unnecessary complexity that could be simplified?

**Safety Considerations**
- Where are the entry points for external data?
- How is sensitive information handled?
- Are there protections against common attack vectors?

**Resource Efficiency**
- Will this perform well under load?
- Are there opportunities to reduce computational overhead?
- Does it use appropriate data structures?

### Phase Three: Constructive Feedback
Structure your observations as:

**Celebrate Wins**
Point out clever solutions and good practices you notice.

**Flag Concerns**
Group feedback by urgency:
- Urgent: Blocks merging, needs immediate attention
- Important: Should be addressed soon
- Optional: Suggestions for future improvement

**Offer Guidance**
For each concern, provide:
- Why it matters
- A concrete example or alternative approach
- Resources if helpful

### Phase Four: Decision Point
Conclude with your recommendation:
- Ready to integrate
- Needs minor adjustments (specify which ones)
- Requires significant changes (explain why)

## Tips for Effective Reviews
- Balance critique with recognition
- Focus on substance over style preferences
- Ask questions when uncertain rather than making assumptions
- Consider the project's maturity and constraints
- Remember you're reviewing code, not judging the author
