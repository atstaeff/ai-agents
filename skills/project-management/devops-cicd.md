---
name: "devops-cicd"
description: "Build or repair CI, deployment, release, rollback or reproducible development workflows."
---

# Devops Cicd

## Workflow

1. Inspect the current build, deployment permissions and release target before editing workflows.
2. Make dependency versions and commands reproducible; run relevant checks on pull requests.
3. Keep credentials scoped and avoid exposing secrets in commands or logs. Build once and reuse artifacts when appropriate.
4. Define rollback and recovery, test failure handling and preserve the existing deployment contract unless a migration is requested.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/devops-cicd.md): load only the section relevant to the task.
