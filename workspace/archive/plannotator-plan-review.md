---
id: plannotator-plan-review
title: "Add local plan review and independent Plan/Build model settings"
kind: software
status: archived
---

# Add local plan review and independent Plan/Build model settings

## Goal and constraints

Support local Plannotator comments, revision and actual approval before Build when
required. Allow independent OpenCode 1 phase models and supported thinking variants.
Preserve scoped Plan permissions, customer-owned knowledge, default exports and stdlib runtime.

## Acceptance criteria

- Optional OpenCode export enables the external review plugin without broadening Plan edits.
- Phase model/variant options validate before writing and protect hand-edited exports.
- Canonical guidance, customer examples and website distinguish plan approval from later decisions.
- Repository checks pass; actual WSL/plugin/provider behavior is explicitly left for local verification.

## Plan

1. Check primary OpenCode 1 and Plannotator documentation and source.
2. Add optional export settings, review workflow and customer example.
3. Verify profiles, failure cases and strict documentation output; prepare the PR update.

## Tasks

| ID | Task | Status | Evidence |
| --- | --- | --- | --- |
| T1 | Configure optional review and independent phase models | done | Four added regression cases; 59 total unit tests pass; default exports remain plugin-free. |
| T2 | Clarify plan revision, feedback, approval and knowledge ownership | done | Canonical workflow and profiles plus a fictional unapproved customer walkthrough; catalog and local links pass. |
| T3 | Verify documentation and portable preview | done | Strict MkDocs build; 113 HTML pages and 14,419 local references with no broken targets or cross-page anchors in each build. |

## Feedback

User requested Plannotator to verify, comment on and approve plans before Build, with
an optional different model and thinking mode. Addressed through opt-in export settings
and a shared review contract; no installation on the user's WSL is claimed.

## Decisions

- Use the external plugin's user-managed workflow to preserve existing scoped Plan permissions.
- Keep one canonical plan and a short approval receipt in the customer issue or local record.
- Reject variant-only settings because the OpenCode 1 variant applies to the configured agent model.
- Avoid provider/model recommendations or forced thinking levels; validate the selected host setup locally.

## Evidence

Catalog: 23 agents and 48 skills, all local links resolve. Standard unittest discovery:
59 cases pass. Optional knowledge graph suite also passes in the locked docs environment.
Dashboard and Docusaurus fragment JavaScript syntax checks pass. Strict documentation
build passes without modifying tracked docs/ output. Portable preview includes the new
setup and worked review pages, with search/instant navigation disabled for file use.

Primary sources: Plannotator OpenCode README, workflow and submit-plan source; OpenCode
agents documentation and the 1.18.32 agent schema. Review gate integration, browser opening,
agent/model switching and provider reasoning were not run in the user's installed host.
The local runner remains a design contract. Repository changes are prepared for the
existing authorized PR; no merge or deployment is part of this change.
