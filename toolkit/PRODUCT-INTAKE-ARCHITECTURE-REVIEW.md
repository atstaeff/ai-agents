# Product Intake as a multi-team capability: architecture review

**Status:** Design review of the offline pilot; **not a claim of production readiness**. The current GitHub Project adapter, asynchronous worker, approval verifier and live OpenCode/Herdr calls do not exist yet.

## Decision

Deliver one **versioned Product Intake capability** with a stable configuration contract and pluggable technology adapters. Teams declare project-specific facts; they do not fork process code or agent definitions for routine customization.

Product AI refines product requests; it never codes. The GitHub Project is the human-visible state. A separate deterministic controller is the only authority allowed to apply workflow transitions. The future Engineering AI begins only through an independently authorized handoff.

## Layers and swap boundaries

| Layer | Owner | Stable input/output | Replaceable implementation |
| --- | --- | --- | --- |
| Team policy | Project team | Schema-v1 team configuration + governing policy revision | Per-repository file or approved policy registry |
| Core | Capability maintainers | Issue snapshot, evidence, verdict, transition command | Python pure application/domain |
| Tracker | Connector maintainers | Issues, project item IDs, status options, assignments, comments | GitHub Projects V2 first; Jira later |
| Knowledge | Project team | Pinned AGENTS.md, accepted ADRs, ownership, citations, revision fingerprints | Local git/approved wiki adapter |
| AI analysis | Model/runtime maintainers | Bounded evidence packet -> validated review result | OpenCode now; other model runtimes later |
| Session manager | Operator | Optional execution and observation, not approval | Herdr or direct headless execution |
| Approval | Enterprise governance | Identity + approval scope + exact reviewed revision | Verified GitHub actor/event or separate approval service |
| State/queue | Platform operators | Claims, idempotency keys, retries, audit | SQLite single-host; PostgreSQL/distributed queue when scaled |

Do **not** build adapter APIs around raw vendor objects. Keep vendor identifiers inside adapters and canonical normalized issue/decision IDs in core results. Provider and model IDs are deployment configuration, not business-rule constants.

## Configuration inheritance

1. **Central invariant policy** (maintainers, immutable release): no engineering during intake, mandatory human approval, minimum DoR, bounded concurrency, protection from untrusted issue content.
2. **Central default profiles** (maintainers): quality checks, role-routing and economical/complex model tiers.
3. **Team project configuration** (team-owned): repository/project, status option names, issue template, approved sources, reviewer identity mappings, models from a provider allowlist, conservative quota overrides.
4. **Per-issue facts**: description, risk, citations, requested scope; never an overriding policy.

Validate the final resolved configuration **before** execution. Unknown schema versions/fields fail closed. Merge behaviour must be explicit; do not implicitly merge arrays, invent reviewers or weaken centrally required policy. Pin the central version (tag+commit SHA) per team, allow controlled upgrades and migration tests. Store a resolved-policy fingerprint with every assessment.

The included `examples/intake/team-config.json` and `tools/intake_config.py` establish a **small schema-v1 dry-run contract only**. The limits and route entries illustrate configuration, not server-side enforcement. The validator currently permits `dry_run` only, deliberately rejecting `live` to prevent misleading deployment claims. It does not check live GitHub membership/model availability or implement inheritance; those require an integration phase.

## Workflow and versioned approval

Five visible columns: `Backlog` → `AI Takes Over` → `AI Working` → `Human Review` → `Ready for Engineering`.

- The AI publishes suggested changes and blocking questions; incomplete issues stay in **Human Review**.
- Humans edit requirements or ask for another pass; only a material change (or explicit reprocess) can send work back to **AI Takes Over**.
- Reviewer assignment does not equal approval. Product approval always required; architecture/security approval conditional on governed risk classification, never on AI self-attestation alone.
- Approval binds authenticated human identity, issue revision, accepted ADR revisions, policy version and decision outcome. Changed inputs invalidate approval.
- Any external status move to `Ready for Engineering` without an authenticated approval record is a violation requiring remediation, not proof of readiness.

The controller must use compare-before-write (re-fetch version), leases/claims, durable event IDs and idempotent bot-comment updates. React to issue edits and board status changes, but prevent feedback loops from the bot's own writes.

## Execution & scale

**Stage 1 (one WSL workstation):** periodic single-run reconciler, one controller owner, SQLite with unique issue+fingerprint claims, bounded jobs, cautious retries. WSL sleep means it is not truly 24/7.

**Stage 2 (many teams):** central always-on execution service, queue partitioned by tenant/repository/project, separate horizontally scalable stateless workers, durable database, GitHub App installations with least privilege, per-tenant quotas and rate limits. Webhooks reduce latency; periodic reconciliation repairs missed events. GitHub API limits and eventual consistency require backoff, pagination and idempotency.

**Isolation:** Namespace all work by installation/organization/repository/project. Reject context or tool access outside the requested tenant. Do not pass arbitrary external URLs or project secrets to an AI model; apply organization's data handling and model-provider policy.

## Security controls to build and test

- Untrusted issue text, comments and ADR content cannot issue instructions or choose privileged tools. Bound input size and sanitize rendering; preserve direct citations.
- Use read-only, least-privilege OpenCode agents with shell/edit/deployment tools denied **at host permission layer**; tool denials must cover installed MCP plugins and nested agent calls.
- Separate credentials: AI reviewer never receives GitHub write tokens; controller holds narrowly scoped GitHub App installation credentials.
- Validate model/provider routes against an approved allowlist with measured cost ceilings. Fail if a required high-reasoning capability is unavailable; do not silently fall back to an unapproved cheaper model.
- Store minimally necessary data, encrypt secrets, mask logs, define retention and audit access; forbid copying customer content into unapproved providers.
- Restrict approval roles to authenticated humans and verify reviewer entitlement at decision time. Test forged approval markers, cross-repo issue IDs, stale approvals and injected prompt instructions.

## Maintainability and compatibility rules

- One shared codebase and releasable package; no per-team code forks. Optional thin adapter packages are fine when an integration truly varies.
- Keep domain logic as pure functions and ports/protocols; use `dataclasses` and `unittest` in this repository's Python style. Avoid plugin loading of arbitrary executable code from team configuration.
- Support versioned serialized results, policy contracts and migration plans; run contract tests for each adapter and a replay suite against sample issues.
- Every new check must declare applicability, evidence requirements, severity, dependency and fallback behavior. `unknown` is **not** `pass`.
- Roll out by team: offline fixtures → read-only shadow mode → write mode in sandbox → limited production canary → progressive rollout with kill switch.
- Observability: issue age, review cycles, accepted/rejected suggestions, false positive rate, API failures, cost by route/team, stale approvals and unauthorized transitions. Prioritize outcome quality and human review time over token counts.

## Current review findings / blockers

| Severity | Finding | Recommendation |
| --- | --- | --- |
| P0 | Live GitHub Projects integration is absent | Do not enable production automation |
| P0 | Approval is documented but not technically enforced | Build authenticated approval adapter and immutable audit |
| P0 | AI-only permissions, untrusted-input isolation and per-tenant access untested | Sandbox and threat-model before any customer issue processing |
| P1 | Demo models/routes are illustrative and not validated against actual provider account | Qualify IDs/effort/budget per runtime |
| P1 | No multi-team configuration protocol previously | Add schema-v1 dry-run contract and migration policy (included here) |
| P1 | SQLite and WSL are single-host choices | Do not claim horizontal scaling without durable queue / DB |
| P1 | No versioned results/adapters or integration contract tests | Add before multiple teams adopt |
| P2 | Product/Engineering names are still mixed in some pilot filenames | Preserve compatibility for demo; use Product Intake in new public APIs |
| P2 | Docs are spread across how-to, pilot and workflow | Keep this architecture decision as design reference; link from adoption guide |

### Exit criteria for organization-wide release

- Reproducible sandbox test demonstrating a real GitHub Project item moving through each authorized transition with human approval.
- Real agent response schema validation, read-only permission checks and tested adverse prompt content.
- Idempotent replay and crash/restart tests, API rate limit handling, and tenant-isolation tests.
- Config version compatibility, downgrade/rollback and adoption by two independent teams without code forks.
- Observed cost and latency budgets; audit trail and operational ownership signed off.

Until then, the result is a **sound architecture direction and safe learning pilot**, not a platform certified for rollout.
