# How to adopt Product AI Intake in another GitHub repository

> **Implementation status (pilot):** The current implementation is an **offline simulation**. It does **not** watch GitHub Projects, call an LLM, create comments, assign reviewers, or change board columns. Follow **Part A** to run what exists today; **Part B** documents the target deployment and the missing integration work. Do not treat successful pilot tests as a working live automation.

This guide integrates the **Product AI / PO refinement** contract into an existing project without letting an AI implement code. Source process: [Product Intake](../../toolkit/PRODUCT-INTAKE.md). Review existing project instructions and keep authoritative project facts in their original homes.

## Part A — Runnable local pilot (no GitHub mutations)

### 1. Prerequisites

- WSL2 with Linux, Git, and Python 3.11+.
- Read access to [atstaeff/ai-agents](https://github.com/atstaeff/ai-agents).
- OpenCode and Herdr are **optional** for the offline pilot; the simulator does not start them.

Clone the **pilot branch** in your WSL home (not under `/mnt/c` for best repository performance):

```bash
mkdir -p ~/src
cd ~/src
git clone --branch feat/engineering-intake-pilot https://github.com/atstaeff/ai-agents.git
cd ai-agents
python3 tools/engineering_intake_demo.py
python3 -m unittest discover -s tests -p 'test_engineering_intake_demo.py' -v
```

Expected proposed board path: `Backlog → AI Takes Over → AI Working → Human Review`. The output explicitly includes `remote_changes: false` and `actual_ai_execution: false`.

### 2. Try blocking questions and role routing

Copy the fixture; do not edit a real GitHub issue:

```bash
cp examples/intake/fixture.json /tmp/product-intake-issue.json
python3 - <<'PY'
import json
from pathlib import Path
path = Path("/tmp/product-intake-issue.json")
fixture = json.loads(path.read_text())
fixture["issue"]["acceptance_criteria"] = []
fixture["issue"]["security_impact"] = True
path.write_text(json.dumps(fixture, indent=2))
PY
python3 tools/engineering_intake_demo.py --fixture /tmp/product-intake-issue.json
```

Expected: still `Human Review`; `review_blocked: true`, a question about acceptance criteria, and `security-owner` among the proposed review roles. Nothing is written to GitHub.

### 3. Add a minimal collaboration pointer to *your project's* AGENTS.md

Do **not** copy this catalog's entire `AGENTS.md` over your own repository instructions. Merge a concise section, using a pinned GitHub commit or locally vendored approved policy for authoritative use:

```md
## Product AI Intake
- Product AI performs issue discovery/refinement and proposes readiness findings.
- It does not modify implementation files, create implementation PRs, run deployments,
  or self-approve an issue.
- Product Owner approves value/scope/acceptance. Architecture and Security Owners
  approve their relevant consequential decisions.
- The GitHub issue and Project own the state; session transcripts are not approvals.
- Use the adopted Product Intake process at: <PINNED_POLICY_URL_OR_LOCAL_PATH>.
- Ready for Engineering is a human-approved handoff, not permission to start coding.
```

Also link from `AGENTS.md` to your real `PROJECT.md` / equivalent, active ADR index, `.github/ISSUE_TEMPLATE/`, `.github/CODEOWNERS`, architecture boundaries and named owners. A policy reference alone does **not** enable automation.

### 4. Configure model routes for *your actual installed host*

The example [model-routing.json](../../examples/intake/model-routing.json) is a **reference**, not a replacement for your existing OpenCode configuration. Keep existing agent prompts and tool permissions. Use **GPT-6.1 Sol** by default for specialists; reserve **GPT-6 Astra** and highest verified supported reasoning effort for consequential lead architecture/review. Check actual provider/model identifiers with:

```bash
opencode --version
opencode models
herdr --version
herdr status server
```

Herdr is useful for managing authorized sessions but is **not** the scheduler or GitHub Project writer. Do not put secrets in your repository or model prompts. Verify permissions in the local host, rather than relying on an instruction that says "read only".

## Part B — GitHub Project setup and planned live integration

### 5. Create/choose a GitHub Project V2 board

On GitHub: **Projects → New project → Board** (or use an existing Project). Create/select a single-select **Status** field with exactly these five options:

| Status | Responsibility |
| --- | --- |
| `Backlog` | Human captures/selects an issue |
| `AI Takes Over` | Controller has claimed the issue revision |
| `AI Working` | Product AI refines scope and checks relevant ADRs |
| `Human Review` | Questions, review decisions, human approvals |
| `Ready for Engineering` | Controller-verified human handoff |

**No "Needs Clarification" column.** Incomplete issues enter `Human Review` with blocking questions. Material review feedback can return to `AI Takes Over`. Keep the initial board **manual** until the real controller is installed.

### 6. Create an issue template for PO refinement

Example `.github/ISSUE_TEMPLATE/product-intake.md` in the customer repository:

```md
---
name: Product intake
about: Product issue for PO refinement and human review
title: "[Product] "
labels: ["product-intake"]
---

## Problem
Who is affected and what is failing or missing?

## Expected outcome
What measurable change is needed?

## Scope / non-goals
What is in and out of scope?

## Acceptance criteria
- [ ] Observable behavior 1

## Owner / stakeholder
@REPLACE_WITH_REAL_OWNER

## Dependencies and architecture context
Relevant ADR links, API dependencies, data/privacy boundaries and constraints.

## Open questions
What must a human decide?
```

Assign owners based on repository/team policy. GitHub CODEOWNERS can inform **code-related** review ownership, but issue assignment is not formal approval.

### 7. Live adapter work **not yet implemented**

A future GitHub Project V2 **read/write** adapter will need to:
1. Resolve the specific project, Status field and option IDs via GraphQL, including issues that belong to more than one Project.
2. Poll only selected statuses and use a persistent per-issue+revision claim, timeouts and idempotency.
3. Read issue content, local project `AGENTS.md`, accepted/active ADR revisions, templates and relevant code context.
4. Invoke read-only Product AI analysis; separately invoke read-only architecture review **only when justified**.
5. Validate structured results; publish or update one bot-owned review comment with blocking questions and source links.
6. Resolve authorized real reviewer accounts/teams; associate each approval with the exact fingerprint and authenticated identity.
7. Re-fetch and verify before every status write; never let AI move its own issue to `Ready for Engineering`.
8. Record audit logs, rate limits, budgets, retries, stop/rollback controls and least-privilege GitHub credentials.

The future command line (`intake scan`, `intake run --once`, `intake status`) is **design only**. The current runnable command is `python3 tools/engineering_intake_demo.py`.

### 8. Deploy and test when the live adapter exists

Prefer a WSL `systemd` timer invoking a **single-run CLI**, with credentials from a protected local store. Understand that suspended Windows/WSL does not run the timer; reconciliation must resume missed work. Start on a disposable GitHub Project and test incomplete requirements, duplicate events, denied review, changed ADRs, network errors, prompt injection and model budget exhaustion. Only enable GitHub writes after verifying identity-based approval and safe retries.

## Adoption checklist

- [ ] Offline simulator and its unit tests pass in WSL.
- [ ] Project `AGENTS.md` references the pinned Product Intake policy and owner/ADR sources.
- [ ] Five GitHub Project statuses configured (currently **manually maintained**).
- [ ] Product issue template and authorized reviewers documented.
- [ ] Specialist and architecture model routes verified locally; secrets excluded.
- [ ] Live GitHub/agent integration remains **disabled until implemented and tested**.

**Boundary:** This project setup is **Product AI**. An eventual Engineering AI gets its own workflow and can only start following a separately authorized engineering assignment.

## Multi-team configuration and platform readiness

Before adopting this across teams, read the [multi-team architecture review](PRODUCT-INTAKE-ARCHITECTURE-REVIEW.md). A team may start with the [sample schema-v1 config](../examples/intake/team-config.json) and run:

```bash
python3 tools/intake_config.py examples/intake/team-config.json
python3 -m unittest discover -s tests -p 'test_intake_config.py' -v
```

The schema-v1 validator is offline-only. Team configuration does **not** install a GitHub connector, authorize live mode, or enforce a GitHub approval. In a target repository, keep a reviewed copy of the config under a project-chosen path and point the future controller to it. Do not copy the toolkit or agent code into each team repository.
