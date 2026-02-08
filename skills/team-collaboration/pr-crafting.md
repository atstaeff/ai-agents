# PR Crafting Skill

## Goal
Compose pull requests that communicate changes clearly and speed up the review process.

## Crafting Your PR

### The Header
Create a title that tells the story in one line:
- Use action verbs: "Implement", "Resolve", "Optimize", "Remove"
- Be specific: "Fix memory leak in image processor" beats "Fix bug"
- Keep it under 72 characters when possible

### The Body

**Opening Statement**
Begin with 2-3 sentences answering:
- What changed?
- Why was this necessary?

**The Details Section**
Break down your explanation:

*Implementation Notes*
- Key technical decisions you made
- Why you chose this approach over alternatives
- Any interesting challenges you solved

*Connection Points*
- Reference relevant issue numbers
- Link to design docs or discussions
- Mention dependent or related PRs

*Validation Approach*
- How you confirmed it works
- Test scenarios you covered
- Edge cases you considered

**Visual Context**
Include when relevant:
- Screenshots showing UI modifications
- Terminal output demonstrating functionality
- Diagrams explaining complex changes

### The Checklist
Track what you've verified:
- Passes all existing tests
- New tests cover the changes
- Documentation reflects the updates
- No unintended side effects observed
- Follows the codebase conventions

### Request Reviews Thoughtfully
- Tag people familiar with affected areas
- Add context if reviewers aren't domain experts
- Use labels to categorize the change type

## Composition Strategies

**Keep It Focused**
One PR should address one thing. Multiple unrelated changes? Split them up.

**Size Matters**
Large PRs take longer to review. If yours exceeds 400 lines of substantive changes, consider breaking it into logical chunks.

**Update as You Go**
Made changes based on feedback? Update your description to reflect the current state.

**Write for Your Audience**
Consider what information your reviewers need to evaluate this effectively.
