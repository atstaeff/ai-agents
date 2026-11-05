# Engineering Intake board pilot (offline)

A **runnable read-only simulation**, not a deployed GitHub automation. It makes no API calls or GitHub writes, starts no OpenCode/Herdr sessions and incurs no model costs. Issue #142 and ADRs in the fixture are synthetic.

## Test

```bash
python3 tools/engineering_intake_demo.py
python3 -m unittest discover -s tests -p 'test_engineering_intake_demo.py' -v
```

Change `examples/intake/fixture.json`: remove acceptance criteria to create **blocking questions in Human Review**, or add security impact to propose a security reviewer. Re-run the demo.

## Board contract

`Backlog` → `AI Takes Over` → `AI Working` → `Human Review` → `Ready for Engineering`. Incomplete work also routes to `Human Review` with blocking questions, not a separate clarification column; review feedback routes to `Changes Requested`, which can go back to `AI Takes Over` after material edits. These are proposed GitHub Project V2 status option names; create and validate them manually before real integration.

The agent **cannot** approve its own work. An authorized reviewer must approve an exact issue+ADR+policy revision. Any material change invalidates approvals. An architecture-change with no accepted ADR evidence needs architecture review even if basic fields are complete. Missing requirements remain visible as blocking questions within Human Review, and must be resolved before approval.

## Model routing (OpenCode Console)

`examples/intake/model-routing.json` is an **example merge fragment**: preserve the existing `opencode.json` agent prompts and permissions. Use:
- `opencode/gpt-6.1-sol` (GPT-6.1 **Sol**, not Luna) for routine work and specialists.
- `opencode/gpt-6-astra` for consequential architecture and independent architecture review; request the highest supported reasoning effort only after checking the installed runtime.
- The OpenCode provider prefix may differ if using direct OpenAI or a custom proxy. Check `opencode models` locally.
- Apply model options with the installed OpenCode version's supported schema. High-cost escalation must be explicit, budgeted and logged.

## Scope of this pilot

The fixture checks field completeness and ADR *status*, not technical correctness or actual architecture conformance. Reviewer identities are role placeholders, not verified GitHub assignees. These limitations are deliberate.

Next: add a GitHub Project V2 read adapter; scope context from `AGENTS.md`; add evidence-backed OpenCode JSON reviews and Herdr dispatch; implement idempotent writes, identity-based human approval and WSL systemd scheduling only after sandbox tests.
