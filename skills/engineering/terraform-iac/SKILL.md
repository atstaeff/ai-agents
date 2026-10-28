---
name: "terraform-iac"
description: "Create, review or refactor Terraform infrastructure with explicit state ownership, provider/module compatibility, IAM scope and plan evidence. Select for drift, imports, moves or replacement risk."
---

# Terraform IaC

## Workflow

1. Identify the root module, environment, backend/workspace, state owner, credentials and intended resources. Inspect declared Terraform/provider versions, lockfile and module sources. Keep dependency upgrades separate unless required by the change.
2. Define a small infrastructure increment and its blast radius. Use typed inputs and useful outputs; introduce modules for a cohesive owned boundary or demonstrated reuse. Pin remote module sources to reviewed versions/revisions; the provider lockfile does not lock module versions.
3. Preserve one writer per state and backend locking where supported. Protect state, saved plans and JSON output as potentially sensitive; redacted CLI values may still persist. Do not place credentials in source or backend arguments that leak into artifacts.
4. Review IAM ownership and environment isolation. In GCP, distinguish policy, binding and member semantics; avoid competing authoritative/additive resources for the same scope/role. Scope privileges to the actual operation.
5. Run formatting and validation with the established toolchain. Where access permits, produce and inspect a plan for the exact revision, variables and target environment. Review every create/update/delete/replacement, unknown value and drift effect; explain unexpected changes before proceeding.
6. For imports, address moves or backend changes, retain the resource-to-state mapping and a tested recovery approach. Prefer declarative import/moved mechanisms supported by the installed version. Do not bypass locking or edit state casually to obtain a clean plan.
7. Apply only within existing authorization and review requirements, using the reviewed plan or the platform's equivalent controlled run. Replan after material source/input/state changes. Verify actual access, service behavior and remaining drift after an authorized apply; reverting configuration is not automatic recovery of deleted data.

## Result

Return the configuration diff, target/state identity, plan effects, executed checks and
recovery limits. Without tooling or credentials, deliver a reviewable change and mark
validation/plan/apply evidence unavailable; do not infer a no-op or successful deployment.

## Focused reference

- [Plan and migration review](references/plan-review.md): for IAM, imports/moves, sensitive artifacts or a failed operation.
- [GCP patterns](../gcp-patterns/SKILL.md): cloud service selection and runtime behavior.
