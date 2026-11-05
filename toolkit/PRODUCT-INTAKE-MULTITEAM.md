# Multi-team Product AI Intake: configurable starter

**Current delivery stage: executable offline project scaffolding and workflow simulation.**
This is NOT a running GitHub Project automation, multi-tenant cloud service, OpenCode worker or approval system. The schema-v2 engine does not yet read issue bodies or run LLMs. It validates arbitrary team-defined board graphs and plans authorized transitions.

## Quick start in WSL

```bash
git clone --branch feat/engineering-intake-pilot https://github.com/atstaeff/ai-agents.git ~/src/ai-agents
cd ~/src/ai-agents
python3 tools/intake_workflow.py examples/intake/profiles/team-3.json
python3 tools/intake_workflow.py examples/intake/profiles/team-10.json --from-stage working --to-stage review
python3 tools/intake_workflow.py examples/intake/profiles/team-20.json --from-stage review --to-stage ready
python3 -m unittest discover -s tests -p 'test_intake_*.py' -v
```

The last example should return `blocked_pending_external_approval_verifier` even if a caller claims that approval was obtained: no verified human identity or GitHub API integration exists yet.

## Install the starter in a customer repository

```bash
mkdir -p ~/src/my-service
python3 ~/src/ai-agents/tools/intake_scaffold.py --target ~/src/my-service --team-size 10
python3 ~/src/ai-agents/tools/intake_workflow.py ~/src/my-service/.product-intake/config.json
```

The tool creates only:
- `.product-intake/config.json`: team-owned process graph, roles, reviewer placeholders, model routes, and resource limits.
- `.product-intake/prompts/*.md`: initial read-only Product/Architecture/Security brief templates, edited and reviewed by the team.
- `.product-intake/AGENTS.snippet.md`: instructions to **merge** manually into existing `AGENTS.md`, never overwrite it.

Project teams must fill in their actual organization/repository, GitHub Project number, named reviewers, approved model IDs and prompts. These are examples, not authorized identities. Skills in the examples (`product-refinement`, `architecture-review`, `security-review`) are **logical identifiers**; map them to actual approved central skills and versions before the future runtime executes them.

The scaffold is intentionally safe: refuses to overwrite an existing product-intake configuration. If you change profiles, use a reviewed diff and migration rather than re-running the scaffold.

## Profiles and scope

| Reference | Team | Configurable workflow |
| --- | --- | --- |
| `profiles/team-3.json` | Small, 3 | Standard Backlog → AI → Human Review → Engineering handoff |
| `profiles/team-10.json` | Medium, 10 | Adds Product Triage and architecture review role |
| `profiles/team-20.json` | Larger, 20 | Adds Product Triage, Domain Review and security role |

These are examples, not staffing rules: all profiles use the same code. Teams can add up to 30 stages and 100 transition edges, rename visible columns, customize role names, reviewer lists, model aliases, skills, and prompt references. The schema-v2 engine rejects duplicate edges, unreachable review, unknown assets, unapproved exit paths and unauthorized final handoffs.

`process.entry`, `process.review` and `process.handoff` are stable semantic anchors. Human Review is always required before Engineering; other stages may vary.

## Configuration ownership and inheritance

- **Platform owners** maintain the versioned runtime, security invariants and approved adapter contracts. Global hard gates cannot be overridden.
- **Team owners** keep the schema-v2 config and prompt text in their repository, reviewed by humans via PRs. Project-specific prompts are treated as untrusted content by the execution host and cannot grant tools or permissions.
- **Project owners** choose the repository, board project, ADRs, templates and accountable reviewers. The project `AGENTS.md` links to these canonical sources.
- **The issue author** supplies feature requirements; issue text cannot modify model routes, permissions, or security gates.

Current schema-v2 validation is a **single-file, already-resolved profile**; automatic hierarchical inheritance, organization policy registry, live reviewer membership validation and dynamic skill resolution are future work. For rollout, add a deterministic release-pinned overlay resolver with explicit precedence and migration reports; avoid hidden defaults and arbitrary executable plugins.

## Model routing and skill ownership

The sample profiles use GPT-6.1 Sol for product/specialist work and GPT-6 Astra for consequential architecture consultation, but teams can replace model routes with *approved* alternatives. The JSON declares a route; it neither establishes model availability nor applies `xhigh` to an actual provider. A production adapter must verify installed model capabilities, per-route spending ceilings and the actual prompt/skill version before dispatch.

Prompts are referenced by local relative paths; no runtime evaluation is performed by the validator. Do not embed credentials, private URLs or personal vault paths in team configurations.

## Host execution architecture for later live delivery

```text
GitHub Projects / other tracker
          |
    Webhook + reconcile
          |
    Queue / claim store  -- per-tenant fair scheduling and quotas
          |
    Deterministic workflow controller (schema-v2 resolved policy)
          |
    Context adapter (AGENTS.md, accepted ADRs, issue snapshot)
          |
    Read-only Product AI runtime (OpenCode + optional Herdr session surface)
          |
    Validated findings + reviewer mapping + human approval verifier
          |
    GitHub Project adapter (only privileged writer)
```

Define stable protocols for Tracker, Context, AgentRunner, Approval and StateStore. Keep GitHub API identifiers inside the tracker adapter; prohibit arbitrary Python/JS code in JSON profiles. Separate project/organization credentials, no shared writable worktrees, rate-limited and idempotent writes, revision-pinned approvals and append-only audit evidence.

**Important:** The offline engine only plans transitions. In particular, it never interprets `approved=True` as verified human approval. The production controller must verify a signed/authenticated external approval against the exact issue+policy+ADR fingerprint before any final status mutation.

## Release and observability

Roll out: fixture tests → shadow read mode → GitHub sandbox with controlled writes → limited canary across two independent teams → production scale. Instrument time-to-review, acceptance/rework rate, API errors, cost per team/model, delayed jobs, duplicate events and security policy violations. Reconcile on startup after WSL sleep. A permanently running multi-team service needs durable queue/database and workers independent of desktop WSL.

For architecture risks and acceptance gates see [Product Intake platform review](PRODUCT-INTAKE-ARCHITECTURE-REVIEW.md). For the original offline issue example see [pilot](ENGINEERING-INTAKE-PILOT.md).
