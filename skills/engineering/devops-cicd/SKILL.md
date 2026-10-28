---
name: "devops-cicd"
description: "Build or repair CI, deployment, release, rollback or reproducible development workflows."
---

# DevOps and CI/CD

## Workflow

1. Inspect the current build/release contract, lockfiles, workflow triggers, environment targets and actual permissions. Identify untrusted pull-request inputs and keep them outside credential-bearing execution.
2. Use reproducible commands and the project's version/update policy. Run affected checks before promotion; identify the source revision and immutable artifact or image digest that passes them.
3. Scope short-lived credentials and keep secrets out of commands, logs and artifacts. Promote the tested artifact through the established environments rather than rebuilding an untracked variant.
4. Define health signals, rollout/stop conditions, owner and recovery action. Check database/schema compatibility; reverting an application image does not undo an incompatible data migration.
5. Exercise the affected build and failure/recovery path within available permissions. Report build, integration and deployed evidence separately. Preserve the release contract unless a migration is in scope.

## Focused references

- [Detailed examples](references/devops-cicd.md): load only the section relevant to the task.
- [Terraform IaC](../terraform-iac/SKILL.md): infrastructure plans, state and drift.
