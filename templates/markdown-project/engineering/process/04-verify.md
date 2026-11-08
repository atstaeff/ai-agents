# 04 — Verify

Use to establish whether the changed boundary satisfies acceptance. Read the diff,
acceptance references and relevant project check/review requirements.

- Run checks proportionate to the affected behavior, including important failure cases.
  Use actual commands from [CONTRIBUTING.md](../../CONTRIBUTING.md); report missing evidence.
- Review the combined revision, not just individual worker results. Use an independent
  reviewer where warranted or required; AI review does not imply human approval.
- Report tested revision, actual results, unrun checks and material limitations at the PR
  or existing assignment. Repeat after a relevant change or unresolved failure.

Result: evidence supporting acceptance, or concrete defects/gaps. Return defects to
[build](03-build.md); proceed to [integrate and retain](05-integrate-retain.md) when ready.
