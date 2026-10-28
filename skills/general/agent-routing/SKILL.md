---
name: "agent-routing"
description: "Select the next skill or bounded specialist for a concrete uncertainty. Handle clear small tasks directly; delegate only when authorized capabilities and expected benefit justify coordination."
---

# Agent Routing

1. Use the current request and available metadata. A clear small task stays in this
   session. Select one skill for the next unresolved activity; load another only when
   that skill or the task exposes a different uncertainty. Do not traverse the catalog.
2. Use a separate specialist only for useful independent review or a bounded deliverable.
   Confirm supported tools and authorization; otherwise apply the guidance directly.
   Match lead/reviewer reasoning to consequence; use lower-cost specialists for bounded
   tasks when observed quality supports it. Set time/retry limits; no universal maximum.
3. Give the specialist outcome, relevant source revisions/pointers, write scope, acceptance,
   constraints/required approvals, expected artifact/checks and escalation triggers. Coordinate overlapping work, use isolated
   working directories for writers and name the integrator. Do not invent sessions.
4. Inspect artifacts and evidence, then verify the combined behavior. Give a reviewer
   requirements and the diff; seek counterexamples. A second model is not automatic
   independent approval. Read-only reviewers return findings, not claimed execution.
5. Preserve shared feedback/handoff at the assignment; keep personal plans private. Never create a mirror
   tracker or treat an available connector as the information owner.
6. Stop repeated ineffective retries at the agreed limit; revise scope/context or escalate
   with evidence. Track available cost/time, review effort, rework and accepted outcome
   before claiming improvement; mark unavailable host measurements explicitly.

| Uncertainty | First skill | Specialist only when useful |
| --- | --- | --- |
| User value or acceptance | product-discovery | product-manager |
| System boundary or compatibility | architecture-planning | lead-architect |
| Python implementation | python-patterns | python-expert |
| React/JavaScript interaction | frontend-patterns | frontend-expert |
| Google Cloud service behavior | gcp-patterns | gcp-architect |
| Terraform state or plan | terraform-iac | terraform-engineer |
| Guide/runbook authoring or editing | technical-writing | documentation-editor |
| Review of a concrete diff | code-review | code-reviewer |
| Private vault operation | obsidian-para | second-brain |
