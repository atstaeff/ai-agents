---
id: concept-website
title: Explain the operating model and clarify the website
kind: software
status: archived
---

# Explain the operating model and clarify the website

## Goal and constraints

Present customer-owned AI delivery clearly, align entry pages, make examples navigable
and provide a local preview. Preserve MkDocs, canonical sources and generated Pages output.

## Acceptance criteria

- Explain outcomes, ownership, live work, durable knowledge and generated views.
- Show when an issue replaces a local work record.
- Distinguish this MkDocs site from a customer's Docusaurus integration.
- Provide a complete example and locally rendered linked knowledge graph.
- Verify affected behavior, strict docs build and generated local links.
- Prepare PR #2 and a user-openable local preview.

## Plan

1. Check current sources and contradictory onboarding messages.
2. Revise canonical concept, navigation, pages and example views.
3. Verify the complete increment and prepare publication and local preview.

## Tasks

| ID | Task | Status | Evidence |
| --- | --- | --- | --- |
| T1 | Verify current PR and website sources | done | All 275 source blobs match PR #2 |
| T2 | Revise concept, onboarding and knowledge views | done | Canonical operating model, six navigation areas and canonical example views |
| T3 | Verify the complete result and preview | done | 55 tests, strict docs build, both graph URL layouts and 14057 local references per build |

## Feedback

Introduce the new concept clearly, revise the documentation site and show it locally.

## Decisions

Keep MkDocs; Docusaurus is the customer's integration. Reuse canonical template sources.
Preserve page paths and simplify top-level navigation. Use linked SVG and an accessible table.

## Evidence

The cloud browser cannot reach the local server and blocks file URLs. No workaround
is used. Provide a static preview the user can open on their own device.

Checks actually completed:

- Catalog and source links: 23 agents, 48 skills; local links resolve.
- Unit suite: 55 tests passed with the optional graph parser available.
- Dashboard and customer Docusaurus fragment: JavaScript syntax passed.
- Locked strict MkDocs build: passed outside tracked docs/.
- Served and portable HTML builds: each has 111 HTML files and 14057 verified local
  links/assets, including the existing production base path on the generated error page.
- SVG example: four keyboard-accessible record links and six typed relations. HTML
  metadata escaping, table preservation and both URL layouts are tested.
- Portable preview: 158 files; ZIP CRC and critical HTML bytes verified. Search and
  instant navigation are disabled only for the exported local preview.
- Existing catalog indexes and the compatibility page now use thin placeholders;
  rendered profiles continue to come from canonical sources.
- Whitespace checks passed. Canonical agents, skills, runtime dependencies and
  generated Pages output remain unchanged in this increment.

Visual browser review was unavailable; actual rendering and interaction in the user's
browser are not established by these checks. The customer Docusaurus site and recurring
runner were not built. Prepared for the existing PR; its history and CI show publication.
