# GCP specialist handoffs

The [role](../gcp-architect.agent.md) owns workload/service tradeoffs and operational
constraints. Use [GCP patterns](../../../skills/engineering/gcp-patterns/SKILL.md) and
its [focused guide](../../../skills/engineering/gcp-patterns/references/guide.md) for
runtime and event-processing procedure; shared examples live there.

A useful brief names project/environment, callers and data boundaries, workload shape,
region restrictions, operating owner, budget and recovery targets. Return the smallest
viable option, material IAM/data/cost implications, verification evidence and open
owner decisions. Identify unavailable cloud access instead of inferring live state.

Use [Terraform IaC](../../../skills/engineering/terraform-iac/SKILL.md) for state and
plan concerns, [CI/CD](../../../skills/engineering/devops-cicd/SKILL.md) for promotion,
[security](../../../skills/quality/security/SKILL.md) for a trust-boundary review and
[performance](../../../skills/quality/performance/SKILL.md) for a measured bottleneck.
Cloud service availability, pricing, permissions and provider schemas require current
official evidence when they affect the decision.
