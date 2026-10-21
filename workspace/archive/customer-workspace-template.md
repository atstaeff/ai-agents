---
id: customer-workspace-template
title: Customer-owned workspace starter
kind: engineering
status: archived
---

# Customer-owned workspace starter

## Goal and constraints

Add a reusable English customer workspace under templates and expose its canonical
guide through the existing MkDocs site. Preserve existing efficiency changes and the
generated Pages output. Prepare a reviewable increment for the existing pull request branch.

## Acceptance criteria

- GitHub Project, issue, PR and durable knowledge each have one canonical role.
- Fictional examples cover stakeholders, ADRs, iteration closeout and local graphs.
- Docusaurus integration preserves existing source and output arrangements.
- Catalog, unit tests, template generation and strict documentation checks pass.
- No real customer data, private vault content or generated site output is committed.

## Plan

1. Verify the current pull request source and preserve its tree.
2. Integrate the template, canonical guide and relevant verification.
3. Verify the complete increment for publication to the existing pull request.

## Tasks

| ID | Task | Status | Evidence |
| --- | --- | --- | --- |
| T1 | Verify the existing pull request and source | done | All 252 local source blobs match the pull request head |
| T2 | Integrate the template and guide | done | 20 reusable starter files and the canonical MkDocs guide |
| T3 | Verify the complete increment | done | 50 tests, catalog/links, local generation, node syntax and strict locked docs build |

## Feedback

Use a templates/workspace folder and the existing pull request. Prioritize simplicity,
speed and customer ownership of knowledge. Keep docs/ available for compiled output.

## Decisions

Use templates/customer-workspace/ to make its copyable customer purpose clear. The
existing catalog site stays MkDocs; Docusaurus integration belongs to the customer's
existing website. Keep the optional YAML parser out of the toolkit runtime.

## Evidence

Checks actually run:

- `python3 tools/ai_toolkit.py check`: 23 agents, 48 skills; local links resolve.
- `python3 -m unittest discover -s tests -v`: 50 tests passed with the optional parser available.
- Local graph generation: 4 records, 6 typed relations; output matches the checked-in views.
- Parser-free discovery of the optional test module: 14 tests skipped as designed.
  CI runs those tests after installing the locked documentation group, which includes PyYAML.
- `node --check` for the existing dashboard and the Docusaurus options fragment: passed.
- Locked, strict MkDocs build: passed; output is outside tracked docs/.
- `git diff --check`: passed.

The existing efficiency change stays intact. Runtime dependencies remain unchanged.
The template graph requires the optional parser; its script declaration supports uv.
Official Docusaurus docs were checked for content paths, automatic sidebars, Mermaid
configuration and build/serve output options. No customer Docusaurus site was built,
no interactive Cytoscape component was implemented and no background runner was started.

Prepared for existing PR #2. Its branch history and CI are the publication evidence.
