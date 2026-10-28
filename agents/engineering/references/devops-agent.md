# DevOps specialist handoffs

The [role](../devops-agent.agent.md) owns a bounded build, CI or release workflow change.
Use [CI/CD](../../../skills/engineering/devops-cicd/SKILL.md) and its
[focused review guide](../../../skills/engineering/devops-cicd/references/devops-cicd.md)
for procedure; shared examples live with the skill.

Provide the failing or desired pipeline behavior, source revision, trust boundaries,
target environment, writable files and expected checks. Return the actual artifact/run
identity, observed results and recovery limits. Python, React, Go and Flutter projects
retain their existing runtime versions and test tools rather than inheriting a sample
pipeline's dependency or coverage choices.

Use [GCP](../../../skills/engineering/gcp-patterns/SKILL.md) for runtime/service identity,
[Terraform](../../../skills/engineering/terraform-iac/SKILL.md) for state and plan changes,
and [incident response](../../../skills/quality/incident-response/SKILL.md) for service
restoration. A workflow change does not imply a deployment or infrastructure apply.
