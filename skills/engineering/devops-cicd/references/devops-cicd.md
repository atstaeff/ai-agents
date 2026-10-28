# Pipeline and recovery review

Use the section relevant to the current change. The established CI provider, deployment
target and authorization govern; this reference supplies no executable release template.

## Trust and artifact flow

Trace a change from source revision through dependency installation, tests, artifact
creation, registry/storage and promotion. Identify which inputs are controlled by an
untrusted contributor and which steps can access credentials or execute deployment.
Do not run untrusted pull-request code in a privileged release context.

Use the project's supported runtime and lockfiles. Keep build outputs identifiable by
revision and digest where supported. Check cache keys/permissions so an untrusted build
cannot supply trusted release inputs. Promote the artifact that passed the relevant
checks; rebuilding later can change dependencies and invalidate that evidence.

For a Python API plus React frontend, test the API contract and actual interaction at
the affected boundary as well as each package's build. A successful Python unit suite
and frontend compilation alone do not prove a compatible end-to-end feature. Use the
existing test runners; introduce no universal coverage or timing threshold.

## Release and recovery

State the target, rollout signals, stop conditions, owner and recovery action. Compare
application and data/schema compatibility before calling a previous artifact a rollback.
For a destructive migration, define data restoration or repair and how it will be
verified; reverting a Git change cannot recover deleted records.

Exercise the relevant failure path in the permitted environment. Record the source and
artifact, commands/checks, observed result and limits. Keep a proposed runbook distinct
from an executed recovery exercise. Production release, infrastructure apply and external
notifications follow existing authorization rather than being implied by pipeline edits.

## Select the affected specialty

- [Terraform IaC](../../terraform-iac/SKILL.md): root modules, state, plans, drift or moves.
- [GCP patterns](../../gcp-patterns/SKILL.md): service identities and cloud runtime behavior.
- [Testing](../../../quality/testing/SKILL.md): consumer contracts and regression evidence.
- [Incident response](../../../quality/incident-response/SKILL.md): an active outage or regression.
