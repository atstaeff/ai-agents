---
id: portable-outcomes
title: "Portable guidance and verified product outcomes"
kind: software
status: active
---

# Portable guidance and verified product outcomes

## Goal and constraints

Keep reusable guidance independent of the model and host, improve product delivery
with proportionate verification, and preserve customer-owned planning and knowledge.
Base: main 1380f03133055dee014582cff029a69de930679d. Source blobs match the local checkout;
generated docs remain owned by the existing main workflow. No merge or deployment.

## Acceptance criteria

- OpenCode, Copilot, Claude Code and portable exports reuse canonical profiles with valid links.
- Claude Plan/reviewers have a read/search allowlist; exports preserve human edits and no-op updates.
- The project defines tracker, plan, review and knowledge homes; missing access creates no mirror records.
- Skills consistently follow that mapping; small tasks need no added record.
- Product discovery separates assumptions, acceptance and measured outcomes; tests use independent requirements.
- Shared concept, website and customer starter explain source ownership and host-specific discovery.
- Required catalog, unit and strict site checks pass; installed-host checks are explicitly distinguished.

## Plan

1. Compare main, inspect guidance and verify official host formats.
2. Improve shared process, selected skills/agents, adapter and website entry points.
3. Check exports, run realistic skill scenarios and required verification; publish a focused PR.

## Tasks

| ID | Task | Status | Evidence |
| --- | --- | --- | --- |
| T1 | Inspect baseline and host formats | done | Main/source blob comparison; official host documentation |
| T2 | Update portable guidance and delivery skills | done | Shared config contract, YAML examples, host adapter and canonical profiles |
| T3 | Verify and prepare reviewable changes | done | 67 unit tests, catalog/link checks, both YAML examples, JavaScript syntax and strict site build |

## Feedback

User requested tool/model independence and professional, efficient product delivery.
User clarified that each project chooses its own tracker and tools (e.g. Jira or GitHub).
User suggested a YAML configuration.
Disposition: project.yaml becomes the canonical tooling map, with GitHub/Jira examples
and an optional local validator; Markdown links to it rather than duplicating locations.

## Decisions

- Keep the existing 23 agents and 48 skills; improve selection and behavior before adding roles.
- Add a native Claude adapter, not a second manually maintained catalog.
- Remove repeated agent Role sections while retaining their descriptions and focused workflows.

## Evidence

- `python3 tools/ai_toolkit.py check`: 23 agents, 48 skills, local links resolve.
- `python3 -m unittest discover -s tests -v`: 67 tests passed.
- `uv run --locked --group docs python -m unittest discover -s tests -v`: 67 tests passed, including optional YAML/graph validation.
- Both project YAML examples pass the optional local validator.
- `node --check` passed for dashboard JS and Docusaurus options.
- Strict MkDocs build passed with an absolute site directory; `index.html` exists at the workflow upload path.
- Native layout/link, read-only Claude profile, no-op update, human-edit protection and CLI dry-run tests pass.
- Independent skill scenario: supplied Jira snapshot, no tracker/wiki access and no application execution. Output retained Jira ownership, gave an unsent update, kept verification open and claimed no writes.
- Independent skill scenario: unproven chatbot benefit, no baseline, existing help center. Output proposed an evidence-gathering increment, labeled targets and kept Jira/Confluence ownership; it claimed no customer validation.
- These two instruction-level scenarios do not establish installed-host/model performance.
- Installed OpenCode/Claude discovery, effective permissions, model behavior and browser interaction remain local smoke checks. No application deployment or customer-system synchronization was performed.
