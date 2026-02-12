# Agile Methodologies

## Instructions for AI

Apply agile principles and methodologies to manage software projects effectively:

## Agile Manifesto

**Values:**
- Individuals and interactions over processes and tools
- Working software over comprehensive documentation
- Customer collaboration over contract negotiation
- Responding to change over following a plan

**Principles:**
- Satisfy customer through early and continuous delivery
- Welcome changing requirements
- Deliver working software frequently
- Business and developers work together daily
- Build projects around motivated individuals
- Face-to-face conversation is most efficient
- Working software is primary measure of progress
- Sustainable development pace
- Continuous attention to technical excellence
- Simplicity - maximize work not done
- Self-organizing teams
- Regular reflection and adjustment

## Scrum Framework

### Roles

**Product Owner**
- Owns product backlog
- Prioritizes features based on business value
- Defines acceptance criteria
- Available to answer questions
- Makes go/no-go decisions

**Scrum Master**
- Facilitates scrum events
- Removes impediments
- Coaches team on agile practices
- Protects team from distractions
- Promotes continuous improvement

**Development Team**
- Self-organizing and cross-functional
- 3-9 members ideally
- Collectively responsible for deliverables
- No sub-teams or titles

### Events

**Sprint**
- Time-boxed iteration (1-4 weeks, typically 2)
- Goal: Create potentially shippable increment
- Fixed duration throughout project
- New sprint starts immediately after previous

**Sprint Planning**
- Duration: 2-8 hours
- Team selects items from product backlog
- Define sprint goal
- Break down stories into tasks
- Commit to sprint backlog

**Daily Standup**
- Duration: 15 minutes
- Same time and place daily
- Three questions:
  - What did I do yesterday?
  - What will I do today?
  - Any impediments?
- Not a status report to manager

**Sprint Review**
- Duration: 1-4 hours
- Demo completed work to stakeholders
- Gather feedback
- Update product backlog
- Celebrate achievements

**Sprint Retrospective**
- Duration: 1-3 hours
- Team reflection on process
- What went well?
- What could be improved?
- Action items for next sprint
- Continuous improvement

### Artifacts

**Product Backlog**
- Ordered list of everything needed
- Single source of requirements
- Continuously refined
- Prioritized by business value
- User stories, bugs, technical debt

**Sprint Backlog**
- Selected items for current sprint
- Tasks to complete items
- Updated daily by team
- Owned by development team

**Increment**
- Sum of completed items
- Must be potentially shippable
- Meets Definition of Done
- Usable by end users

### Definition of Done (DoD)
- Clear checklist for completion
- Code complete and reviewed
- Tests passed (unit, integration)
- Documentation updated
- Deployed to staging/production
- Accepted by Product Owner

## Kanban

### Core Practices

**Visualize Workflow**
- Kanban board with columns (To Do, In Progress, Done)
- Swim lanes for different work types
- Visual indicators (colors, labels)
- Make work and blockers visible

**Limit Work in Progress (WIP)**
- Set WIP limits per column
- Prevents multitasking
- Improves flow
- Identifies bottlenecks
- Example: Max 3 items "In Progress"

**Manage Flow**
- Optimize throughput
- Monitor cycle time and lead time
- Identify and remove bottlenecks
- Continuous delivery

**Make Policies Explicit**
- Define when items move between columns
- Acceptance criteria
- Definition of done
- Team agreements

**Feedback Loops**
- Regular standups
- Replenishment meetings
- Retrospectives
- Review metrics

**Improve Collaboratively**
- Use data to drive improvements
- Experiment with changes
- Measure impact
- Kaizen (continuous improvement)

### Kanban Metrics

**Cycle Time**: Time from start to finish
**Lead Time**: Time from request to delivery
**Throughput**: Items completed per time period
**WIP**: Current work in progress
**Flow Efficiency**: Value-add time / total time

## User Stories

### Format
```
As a [role]
I want [feature]
So that [benefit]
```

**Example:**
```
As a customer
I want to save items to a wishlist
So that I can purchase them later
```

### INVEST Criteria
- **I**ndependent: Can be developed independently
- **N**egotiable: Details can be discussed
- **V**aluable: Delivers value to users
- **E**stimable: Can estimate size/effort
- **S**mall: Completable in one sprint
- **T**estable: Clear acceptance criteria

### Acceptance Criteria
- Specific conditions for story completion
- Given-When-Then format
- Testable and unambiguous
- Agreed upon before development

**Example:**
```
Given I am logged in
When I click "Add to Wishlist"
Then the item appears in my wishlist
```

## Estimation Techniques

### Story Points
- Relative sizing (Fibonacci: 1, 2, 3, 5, 8, 13)
- Complexity, not hours
- Team-specific meaning
- Used to calculate velocity

### Planning Poker
- Team estimates together
- Each member selects card privately
- Reveal simultaneously
- Discuss differences
- Reach consensus

### T-Shirt Sizing
- XS, S, M, L, XL
- Quick, high-level estimates
- Good for backlog refinement
- Convert to story points later

## Velocity and Capacity

**Velocity**: Story points completed per sprint
- Calculate as rolling average (3-4 sprints)
- Used for release planning
- Should stabilize over time

**Capacity**: Available hours per sprint
- Account for vacations, holidays
- Include meetings and other work
- Leave buffer for unexpected work

## Release Planning

- Group stories into releases
- Define release goals
- Estimate based on velocity
- Plan for 3-6 sprints ahead
- Adjust based on progress
- Communicate timeline to stakeholders

## Scaling Agile

### SAFe (Scaled Agile Framework)
- Portfolio, Program, Team levels
- Agile Release Trains (ARTs)
- PI (Program Increment) Planning
- Suitable for large organizations

### Scrum of Scrums
- Coordination across multiple teams
- Representatives from each team meet
- Discuss dependencies and impediments
- Typically 2-3 times per week

### LeSS (Large-Scale Scrum)
- Extends Scrum to multiple teams
- One Product Owner, multiple teams
- Shared sprint and backlog refinement
- Simpler than SAFe

## Common Anti-Patterns

❌ Skipping retrospectives
❌ Product Owner not available
❌ No clear Definition of Done
❌ Stories too large
❌ Carrying over incomplete work
❌ Sprint treated as mini-waterfall
❌ Daily standup becomes status report
❌ Ignoring impediments
❌ No sprint goal

## Best Practices

✅ Keep sprint length consistent
✅ Protect sprint from changes
✅ Team estimates together
✅ Regular backlog refinement
✅ Focus on delivering value
✅ Empower the team
✅ Transparency with stakeholders
✅ Continuous improvement

## Example Prompts

"Create user stories with acceptance criteria for a login feature"

"Plan a two-week sprint for this product backlog"

"Facilitate a sprint retrospective and identify improvements"

"Estimate these user stories using Planning Poker"

"Define a Definition of Done for our team"

"Design a Kanban board for customer support tickets"

## Related Skills & Agents

- [Task Orchestrator Agent](../../agents/task-orchestrator.agent.md)
- [Context Manager Agent](../../agents/context-manager.agent.md)
- [Progress Sync](../team-collaboration/progress-sync.md)
- [Feature Discovery Session](../team-collaboration/feature-discovery-session.md)
- [Technical Debt Management](../project-management/technical-debt.md)
