# Incident Response Coordination Skill

## Instructions for AI
Manage production incidents efficiently to restore service and learn from failures.

## Response Framework

### Detection and Initial Response (0-5 minutes)

**Recognize the Incident**
Determine if this requires immediate action:
- Is service degraded or unavailable?
- Are users impacted?
- Is data at risk?
- Does this violate SLAs?

**Declare Severity**
Rate the incident urgency:
- Critical: Major functionality down, many users affected, data loss risk
- High: Significant degradation, subset of users affected
- Medium: Minor issues, workarounds available
- Low: Cosmetic problems, isolated cases

**Assemble Response Team**
Based on severity, bring in:
- Incident commander (coordinates response)
- Technical leads (systems experts)
- Communication lead (updates stakeholders)
- Customer support liaison (handles user questions)

### Investigation Phase (5-30 minutes)

**Gather Information**
- What symptoms are users experiencing?
- When did this start occurring?
- What changed recently (deployments, config, traffic)?
- What does monitoring show?

**Form Hypotheses**
Create theories about root causes:
- Most likely culprits based on symptoms
- Recent changes that correlate with timing
- Known weak points in the system

**Test Hypotheses**
Check each theory:
- Review relevant logs
- Check system metrics
- Verify recent changes
- Test specific scenarios

**Communicate Status**
Update stakeholders every 15-30 minutes:
- What you know so far
- What you're investigating
- Estimated time to resolution (if possible)
- Workarounds users can try

### Mitigation Phase (varies)

**Immediate Actions**
Take steps to reduce impact:
- Roll back recent changes if suspected
- Scale up resources if capacity-related
- Enable backup systems if available
- Disable problematic features if necessary

**Track Actions**
Document everything tried:
- What action was taken
- Who authorized it
- What resulted
- Timestamp of change

**Validate Effectiveness**
After each mitigation attempt:
- Check if symptoms improved
- Verify no new problems introduced
- Confirm with monitoring data

### Resolution Phase

**Verify Normal Operation**
Confirm the incident is truly resolved:
- Key metrics returned to normal
- Users can complete critical workflows
- No errors in monitoring systems
- Customer support confirms improvement

**Communicate Resolution**
Notify stakeholders:
- What was the issue
- What fixed it
- Any ongoing concerns
- Actions users should take if needed

**Maintain Vigilance**
Continue monitoring closely for:
- Recurrence of the issue
- Related problems emerging
- Unusual patterns

### Post-Incident Phase (24-72 hours later)

**Document Timeline**
Create incident record with:
- Detection time
- Key investigation milestones
- Mitigation attempts
- Resolution time
- Total impact duration

**Conduct Review**
Meet with response team to discuss:

*What Happened*
Establish factual timeline without blame.

*Why It Happened*
Identify root causes, not just symptoms.

*How We Responded*
Evaluate response effectiveness.

*What We'll Change*
Create specific action items to prevent recurrence and improve response.

**Share Learnings**
Write an incident report covering:
- Summary of the incident
- User impact assessment
- Root cause analysis
- Response evaluation
- Prevention measures planned
- Response improvements planned

Share with broader team and relevant stakeholders.

## Commander Responsibilities

**During the Incident**
- Make final decisions on actions
- Coordinate team members
- Ensure communication happens
- Keep focus on restoration
- Call in additional help if needed

**Avoid Common Traps**
- Don't jump to conclusions without evidence
- Don't blame individuals during active incident
- Don't hide bad news from stakeholders
- Don't forget to document decisions

## Communication Templates

**Initial Notification**
```
Status: Investigating Incident
Severity: [Critical/High/Medium]
Impact: [What users are experiencing]
Detection: [When we noticed]
Current Actions: [What we're doing]
Next Update: [When you'll hear from us next]
```

**Progress Update**
```
Status: In Progress
Investigation: [What we've learned]
Mitigation: [What we're trying]
Current Status: [Latest on user impact]
Next Update: [When you'll hear from us next]
```

**Resolution Notice**
```
Status: Resolved
Issue: [What happened]
Resolution: [What fixed it]
Duration: [How long users were impacted]
Next Steps: [Any actions users need to take]
Post-Mortem: [When detailed analysis will be available]
```

## Preparation Checklist

**Before Incidents Happen**
- Document response procedures
- Identify on-call rotations
- Set up communication channels
- Create monitoring and alerts
- Test backup systems
- Run incident drills
- Maintain runbooks for common issues
- Ensure access credentials are available

## Metrics to Track

**Response Metrics**
- Time to detection
- Time to acknowledgment
- Time to mitigation
- Time to resolution
- Number of people involved

**Impact Metrics**
- Users affected
- Revenue impact
- SLA breach duration
- Support ticket volume

Use these to improve response over time.

## Related Skills & Agents

- [DevOps Agent](../../agents/devops-agent.agent.md)
- [GCP Architect Agent](../../agents/gcp-architect.agent.md)
- [GCP Patterns](../gcp-patterns/SKILL.md)
- [DevOps & CI/CD](../project-management/devops-cicd.md)
