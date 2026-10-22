---
id: ai-ready-toolkit
title: "Portable AI work toolkit, Jörg and PARA"
kind: software
status: active
---

# Portable AI work toolkit, Jörg and PARA

## Goal and constraints

Improve the catalog and workflow for software, product and general work. Provide
English portable instructions, OpenCode 1/WSL integration and a locally running
companion. Keep private Obsidian content outside this public repository and preserve
the existing GitHub Pages role of `docs/`. Deliver reviewable changes without merging.

## Acceptance criteria

- All canonical agents and skills have valid name/description frontmatter and focused English instructions.
- Every canonical skill exports to a native named SKILL.md directory; references resolve.
- Jörg, Second Brain/PARA and product/workflow guidance are available without invented host capabilities.
- Work records preserve feedback and reject normal stale API writes; completed tasks need evidence.
- The local UI/API uses loopback and local assets; relevant automated checks pass.
- MkDocs renders canonical instructions and builds strictly; main publication stays a separate action.

## Plan

1. Audit the pinned source snapshot and project instructions.
2. Curate short canonical entries and retain useful examples as focused references.
3. Implement runtime adapters, one-file records and a local UI/API.
4. Generate the website from canonical sources and add reproducible CI checks.
5. Run available validation and open a reviewable GitHub change.

## Tasks

| ID | Task | Status | Evidence |
| --- | --- | --- | --- |
| T1 | Audit source structure and existing guidance | done | Base 6fd9461: 18 agents and 27 topic skills lacked frontmatter; 91 local links failed the initial audit; root Copilot discovery guidance was incorrect. |
| T2 | Improve all agents and skills | done | Catalog check: 23 agents and 48 skills; all checked local links resolve; core entries load examples on demand. |
| T3 | Add Jörg, PARA and product/workflow guidance | done | Two isolated skill forward-tests; clarified concurrent edits, archive collisions, link fragments and unavailable verification. |
| T4 | Implement native adapters and work UI/API | done | 28 unittest checks cover native layouts, ownership protection, traversal, stale writes, comments, task evidence and real HTTP requests. |
| T5 | Improve canonical website and CI | done | Strict MkDocs 1.6.1 / Material 9.7.7 build passes; uv.lock records public package URLs; CI validates PRs. |
| T6 | Validate skill compatibility and frontend syntax | done | All 21 native source skills and all 48 exported skills pass skill-creator validation; node --check passes. |
| T8 | Publish a GitHub branch and PR | done | Draft PR [#1](https://github.com/atstaeff/ai-agents/pull/1) opened on 2026-10-07; all 236 changed files verified against local Git blobs; unrelated source files and the Pages output tree are preserved; [Validate Toolkit CI](https://github.com/atstaeff/ai-agents/actions/runs/37573557937) passed. |
| T7 | Review in installed OpenCode/VS Code and visually inspect UI | open | Host executables unavailable here; local browser binary download failed and the provided browser blocks localhost. This manual check remains explicit. |

## Feedback

### F1 · Scope extension

> Und gerne kannst du auch die ganzen Skills und Agents noch verbessern, optimieren, Englisch schreiben, Frontmatter dazu machen, für maximal Kompatibilität.

Disposition: implemented in the canonical profiles and runtime adapters.

### F2 · Personal knowledge and assistant

> Interessant wäre auch noch ein Skill und Agent für meinen Second Brain mit Obsidian, was nach der PARA-Methode aufgebaut ist: Projects, Areas, Resources und Archive. Und spannend wäre in der Tat auch noch, wenn ich einen persönlichen Assistenten hätte, namens Jörg, der sozusagen auf alle Skills und Agents zurückgreift.

Disposition: implemented as obsidian-para, second-brain and joerg, with progressive selection and explicit private-vault access requirements.

## Decisions

- Common name/description metadata plus adapters: native tool/mode/permission fields differ between hosts.
- Standard-library Python runtime: a small CLI/loopback companion needs no installed framework. Typer remains an option for a richer CLI.
- One record per larger outcome: avoid competing proposal/task/CSV sources of truth; small changes need no record.
- Keep rich examples as optional references and render website entries from canonical sources to avoid duplicated instructions.
- Keep the existing Pages branch/output contract; do not deploy during this change.

## Evidence and remaining limits

Commands: `python3 tools/ai_toolkit.py check`, `python3 -m unittest discover -s tests -v`,
`node --check tools/web/app.js`, and
`uv run --locked --group docs mkdocs build -f assets/mkdocs.yml --strict` with a scratch output.

OpenCode 1 and VS Code profiles follow their documented formats, but actual host/model
behavior and the local dashboard's visual layout are not established by structural
tests. Obsidian URI encoding is tested; OpenCode Web custom-protocol clickability is
host-dependent. OneDrive/uncoordinated filesystem editing is not a distributed transaction
system. No real private vault, deployment or merge was modified.

The record remains active for review and the manual checks above. Archive it only after
those decisions and checks are resolved; do not mark unrun checks as passed.

Published implementation: commit 4539e74b on branch codex/ai-ready-toolkit-20261006,
with parent 6fd9461 and draft PR #1. Publication is complete; host and visual review
remains open under T7.
