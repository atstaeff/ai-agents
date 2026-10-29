# Showcase hardening — 2026-10-28

## Scope

This follow-up addresses reproduced defects and adoption gaps from the critical review
of revision 8349867. It starts from the merged main branch. Source changes cover export
privacy, record integrity, graph metadata/publication, catalog quality and first-use
navigation. Independent security and editorial reviews supplemented automated checks.

## Findings and implemented results

| Finding | Result and evidence |
| --- | --- |
| Ignored local credentials could enter exports | Apply explicit supported-file and path-name inclusion before reading bytes; test portable and embedded Herd snapshots with synthetic credential/state files |
| External editor saves could be overwritten during record preparation | Recheck expected hashes after temporary-file fsync; expected-absent creation cannot overwrite a competing creator |
| Archive races and handled removal failures | Preserve active/editor and existing archive data; remove only this invocation's unchanged generated archive on handled failure so normal retry works |
| ADR template incompatible with the current graph | Add area metadata, use a portable relative slug and normalize existing absolute forms; pass the actual template through current and legacy publishers |
| Graph and site customer sources hardcoded independently | Share one trusted curated-source configuration for root, route, sidebar and publication allowlist; validate privacy markers, symlinks and routes |
| Shared-plan instructions conflict | Distinguish shared coordination, optional private notes and authorized sanitized review extracts across roles and skills |
| Generic or defective examples consume context | Condense duplicate role tutorials and correct authentication, retry, idempotency, concurrency and universal architecture/testing advice |
| First success hidden behind project setup | Visible quick-start path with disposable export, supplied notes, bounded host exercise and explicit evidence limits |
| Mutable links treated as adopted policy | Local starter rules own the contract; evolving technique links are references, and external binding policy needs an explicit immutable revision |
| Large documentation collection hard to retrieve | Local title/prose search with type filters, shareable URLs and bounded results from selected published documentation |
| Runtime/model/capacity claims lack an evidence home | Provide one reusable qualification/capacity record, route criteria and a real-host trial procedure; retain untested status honestly |

The security reviewer reproduced further plural credential-name/directory cases and
archive PermissionError recovery during iteration. Both were corrected. Independent
recheck confirmed no bytes read for the five reported credential paths in both runtimes,
retry after a handled removal failure, and preservation of intervening human archive edits.
The editorial review verified the first-task commands and adoption wording; its capacity
summary correction was applied.

## Catalog measurements

All 22 agent and 41 skill IDs and preset selections remain stable. Measurements below
exclude generated indexes and YAML metadata; they describe Markdown sources, not
runtime injection or model costs.

| Source | Before | After |
| --- | ---: | ---: |
| Agent Markdown | 153,854 bytes | 48,246 bytes |
| Skill Markdown | 345,107 bytes | 268,288 bytes |
| Combined | 498,961 bytes | 316,534 bytes |

Reduction: 182,427 bytes (36.56%) and 20,169 whitespace words (33.15%). Entry bodies grew
slightly to clarify boundaries/results; reductions concern optional references. Useful
domain/API, game and refactoring depth remains. No runtime savings were measured.

Three fresh bounded model observations checked the changed work-management procedure:

- A shared sequence for dependent API/UI writers was retained at the assignment despite
  an unavailable private vault; an authorized sanitized review extract did not expose notes.
- Missing Jira access produced an unapplied response draft with intended destination,
  without creating a mirror tracker or claiming deployment.
- A standalone typo changed only one word, with no extra planning record or delegation.

These observations establish those cases, not statistical reliability or live integration.

## Executed validation

- Catalog/index/local-link checks: 22 agents and 41 skills; portable name/description metadata checked across all 63 entries.
- Locked Python suite: 136 tests passed, including persistence/export/search publication regressions.
- Graph suite: 16 tests passed, including real template compatibility, source configuration and privacy/scale cases.
- Documentation search suite: 4 tests passed for ranking, combined terms, types, accents, empty queries and bounded results.
- Local HTTP/storage/export replay passed, including persisted comments, stale writes, archive and migration.
- Strict Docusaurus production build passed with 196 generated documents.
- Independent checks covered 320 catalog relative links, changed fence balance and diff whitespace.
- Browser coverage in CI includes first-use navigation, actual search interactions/deep links,
  graph filters/recovery/source routes and mobile layouts. Local Chromium was unavailable;
  CI records the final tested revision and browser result.

## Remaining boundaries

Filename/path policy does not scan otherwise publishable content for secrets. Review
source content. Local hash rechecks are not cross-process compare-and-swap. An abrupt
archive interruption or failed cleanup can leave both copies for explicit reconciliation.
The Go toolchain was unavailable, so its corrected illustrative middleware fragment was
not compiler-tested.

No native Herdr/Herd/provider or cloud/Terraform deployment was executed. Real host
qualification, model/effort behavior, remote-worker access and measured delivery cost need
the documented pilot. The static graph still builds its selected corpus; million-record
operation requires an incremental authorized index. Local documentation search is not a
customer-wide ADR or permission-aware service. Merge and deployment remain separate.
