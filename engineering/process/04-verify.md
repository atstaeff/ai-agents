# 04 — Verify

Use to assess whether a change meets acceptance. Inspect the current diff, acceptance
references and the project's actual commands and review requirements.

1. Verify the affected boundary, including important failure/recovery cases. For wording-only
   edits, inspect content and diff; run applications/tests for affected behavior or an explicit
   project requirement. This repository's [runbook](../../toolkit/REPOSITORY-WORKFLOW.md)
   and [CI](https://github.com/atstaeff/ai-agents/blob/main/.github/workflows/checks.yml) own its commands and required gates.
2. Use [testing](../../skills/quality/testing/SKILL.md) or
   [code review](../../skills/quality/code-review/SKILL.md) where relevant. Obtain independent
   review for consequential changes or when required; AI review does not imply human approval.
   For substantial narrative/procedure changes, use authoring and independent editing.
3. Check the combined revision and correct material findings. Repeat checks for relevant
   changes, failures or unresolved concerns. Report actual results, tested revision, unrun
   checks and limits at the PR/current assignment. Do not infer performance gains from
   shorter instructions or more workers; follow the [evaluation protocol](../../toolkit/QUALITY-STANDARD.md#evaluate-context-changes).

Result: acceptance evidence or concrete gaps. Return defects to [build](03-build.md);
proceed to [integrate and retain](05-integrate-retain.md) when ready under the actual agreement.
