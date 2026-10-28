# Terraform plan and migration review

Read the section needed for the affected state or resource boundary. Follow the project's
execution platform and installed Terraform/provider versions.

## Plan evidence

Record the source revision, root module, environment/backend/workspace and relevant
input identity without publishing secrets. Confirm the plan belongs to that target.
Inspect replacement reasons, deletion protection, data retention, IAM changes and
dependencies. A syntactically valid configuration can still replace a database or
revoke access. Unknown values require a consequence assessment, not an assumed no-op.

Formatting checks style; validation checks configuration/provider consistency. Neither
establishes a permitted or safe live change. A plan describes proposed effects; only
authorized apply plus relevant runtime checks establishes the deployed result. A saved
plan can contain plaintext sensitive values. Keep it in the approved protected artifact
home and share a sanitized summary through the assignment.

Consult the official [plan command](https://developer.hashicorp.com/terraform/cli/commands/plan)
and [sensitive-data guidance](https://developer.hashicorp.com/terraform/language/manage-sensitive-data)
when their exact behavior matters.

## GCP IAM ownership

For a project role, an IAM binding owns the member set for that role while an IAM member
adds a member without owning its peers. A policy resource owns the project policy.
Confirm ownership across modules, states and manual administrators before changing one;
overlapping resources can remove grants or continually fight. Check resource-level scope
where it meets the need. Verify the affected provider version against the official
[Google IAM resource documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_iam).

## Imports, moves and partial failures

For a renamed module, map old to new addresses and review a plan demonstrating the
intended move without unintended recreation. Retain necessary historical moves for
consumers that have not upgraded. For an existing unmanaged resource, verify its actual
identifier and owner before importing it once into the intended state; reconcile its
configuration before applying unrelated changes.

After a failed apply or interrupted command, inspect the run and current state/resources
before retrying; some effects may already exist. Coordinate with the active state owner.
Do not disable a lock or force-unlock another active writer. A backend migration needs
explicit source/destination identity and a verified state recovery path.

Official references: [module refactoring](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring),
[imports](https://developer.hashicorp.com/terraform/language/import),
[state locking](https://developer.hashicorp.com/terraform/language/state/locking) and
[dependency lockfile scope](https://developer.hashicorp.com/terraform/language/files/dependency-lock).
Load only the reference that resolves the current uncertainty.
