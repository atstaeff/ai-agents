---
id: efficiency-pass
title: "Make repeated work faster and simpler"
kind: software
status: archived
---

# Make repeated work faster and simpler

## Goal and constraints

Optimize the merged toolkit for low overhead, simplicity and repeatable local work.
Preserve the standard-library runtime, native adapter layouts, human edits, privacy
and the existing GitHub Pages output. Baseline: main at `26381d77673a57046c22df71534059686faab313`.

## Acceptance criteria

- Unchanged exports write nothing; changed, missing and obsolete files behave correctly.
- All three runtime layouts retain edit protection, references and permissions.
- Each documentation build scans the catalog once and refreshes on subsequent builds.
- Shorter agent guidance keeps domain workflows, feedback protection and host boundaries.
- Catalog checks, unit tests, JavaScript syntax and strict documentation build pass.

## Plan

1. Measure repeated work and inspect shared instructions.
2. Remove unnecessary writes, scans and coordination overhead.
3. Verify behavior and publish a reviewable change.

## Tasks

| ID | Task | Status | Evidence |
| --- | --- | --- | --- |
| T1 | Inspect and measure current main | done | All 250 local source blobs matched remote main; baseline counters below |
| T2 | Make exports incremental | done | All runtime no-write tests; source updates, obsolete edited paths, dry-run and missing files tested |
| T3 | Load documentation metadata once per build | done | Full-page scan count, fresh-build metadata and canonical-link tests |
| T4 | Reduce instruction and process overhead | done | 23 domain workflows retained; agent words reduced from 5732 to 3690 |
| T5 | Verify the complete change | done | 35 tests, catalog, node syntax, strict locked MkDocs build and whitespace checks passed |

## Feedback

### F1

> Habe gemerged kannst du das repo nochmal analysieren und prüfen und optimieren. Effizienz ist mega wichtig. Auch Einfachheit Schnelligkeit

Disposition: addressed through measured I/O reductions and shorter shared guidance.

## Decisions

- Keep the existing local dashboard/API and zero runtime dependencies. The API already
  loads catalog metadata once at startup; the frontend does not poll automatically.
- Keep edit detection: hashing destination files remains necessary even when writes
  are skipped. Report payload counts separately from the manifest.
- Refresh the website cache per build rather than persist it across live rebuilds.
- Put common rules in the exported shared workflow. Handle clear small tasks directly;
  keep one record for larger outcomes and delegate only when useful and authorized.

## Evidence

| Measurement | Before | After |
| --- | --- | --- |
| Atomic writes for an unchanged 213-file OpenCode bundle | 214 | 0 |
| Full catalog scans for 93 documentation pages | 93 | 1 |
| Words across 23 canonical agent profiles | 5732 | 3690 |
| Documentation hook-only time, local sample | 0.632 s | 0.060 s |
| Unchanged export median, three local samples | 0.086 s | 0.073 s |

Counters are deterministic regression targets. Timings are samples on this Linux
filesystem, not a prediction for WSL/OneDrive or model latency. Word counts include
frontmatter and headings and are not token counts.

Checks run: `python3 tools/ai_toolkit.py check`; `python3 -m unittest discover -s tests -v`
(35 passed); `node --check tools/web/app.js`; locked strict MkDocs build (1.13 s);
`git diff --check`. Build output was outside tracked `docs/`.

Live OpenCode/Copilot model behavior and browser interaction were not tested here.
No frontend behavior or host permission configuration changed in this pass.
