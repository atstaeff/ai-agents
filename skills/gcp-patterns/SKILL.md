---
name: "gcp-patterns"
description: "Design, deploy or troubleshoot a workload on Google Cloud with clear cost and operational constraints."
---

# Gcp Patterns

## Workflow

1. Confirm existing projects, IAM, regions, data restrictions and workload needs before selecting services.
2. Prefer the least complex managed option that meets the requirements; Cloud Run may suit a containerized application, while Kubernetes requires a concrete need.
3. Use least privilege, secret management, infrastructure as code and separate environments where warranted.
4. Define metrics, budget alerts, rollback and restore; verify current service behavior in official documentation when needed.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/guide.md): load only the section relevant to the task.
