# Catalog efficiency audit — 2026-10-23

## Scope and measurements

Compared with main source revision 46fd41f5244a8d873632bc6159b7e45abacd14e3. Retired entries were shallow
routing layers or roles owned by surviving procedures; specialized engineering knowledge
remains available. See [selection and migration](../CATALOG-GUIDE.md) for every replacement.

| Measure | Before | After |
| --- | --- | --- |
| Active agents | 23 | 20 |
| Active skills | 49 | 39 |
| Sum of active profile/skill body words | 8206 | 7221 |
| Automatically referenced shared startup document words | 475 | 241 |
| Root AGENTS.md words | 584 | 360 |
| All registered name/description characters | 8660 | 7344 |
| Engineering preset name/description characters | Previously all: 8660 | 3272 (8 agents, 16 skills) |

Bodies use whitespace-delimited words; discovery metadata uses Unicode characters in
names plus descriptions. These are reproducible source-size measures, not tokenizer
counts, host-injected context or measured latency. The default export remains all active
entries; --preset engineering is the recommended bounded selection. Canonical reference
files stay in the bundle for on-demand reading; native registrations and index.json are
selected. Presets do not provide a security boundary or guarantee host discovery behavior.

## Structural changes

- Consolidate three agents and ten skills; preserve public profile URLs as migration pages.
- Remove repeated generic completion/operating text and duplicate/self routes. Keep role
  boundaries, actual checks, acceptance, feedback and handoff requirements at their owners.
- Give software-engineering a direct cross-module implementation procedure rather than
  another router. Preserve focused examples under their surviving skill's references.
- Move archive/move/Windows-link mechanics out of the common Obsidian capture body and
  require their reading for those operations. No private content was added.
- Inject compact SESSION-RULES.md through runtime adapters; detailed workflow stays on demand.
- Support preset/additive selection in all four exporters with existing permission,
  stale-write, dry-run, owned-file cleanup and edited-file protections intact.

## Bounded model observations

Fresh threads received a profile/skill path and a task, without the expected answer or
this assessment. All projects and the vault were disposable local fixtures. They could
not edit the catalog or publish. Six trials included two unsuccessful small-edit attempts:

| Case | Observation |
| --- | --- |
| Record-selection feature | Correct accepted contract, original identities/order and human note; four tests passed |
| Read-only review | Concrete cross-account disclosure with source evidence; no edit or test execution claims |
| Vault archival | Loaded the moved reference, stopped on occupied destination, preserved notes and links |
| Initial wording correction | Correct content but unnecessary unittest attempt on a project without tests |
| First clarification, fresh wording task | Same unnecessary test attempt; the clarification did not generalize |
| Final clarification, fresh wording task | Exact content/diff checks, preserved human note, no application tests |

The trial instruction distinguishes a listed available check command from an explicit
requirement for every kind of change. The two failed efficiency attempts are retained,
not counted as successful bypasses. A single final success does not establish reliable
small-task behavior in every host/model. Earlier feature/review/vault trials predate the
final wording clarification; they are not presented as fresh runs of every final source.

[Raw fixture/diff snapshots, observations and integrated source hashes](../../tests/fixtures/catalog-efficiency-20261023.json)
retain provenance. No hidden reasoning or real customer/vault data is included.

## Integration with current main

The trials preceded integration of main revision 46fd41f, which introduced private
Second Brain planning and the decision graph demo. Those changes remain intact. The
measurements above use that newer main as their baseline; trials describe the earlier
instruction iterations, not a fresh behavior evaluation of the integrated revision.
Root docs/ remains compiled Pages output; website/ owns Docusaurus source. Repository
and toolkit navigation now explain project knowledge, reusable guidance and executable tools.

## Limits and next evaluation

Mechanical checks exercise selected native layouts, resolved links, unchanged read-only
permissions, additive choices, invalid-name rejection before writes, phase-option guards,
owned-profile removal and edited-profile preservation. Docusaurus checks public routes
and links; these checks do not prove an installed host, model behavior or user value.

No controlled before/after latency, token-cost or product-throughput experiment was run.
Verify an actual selected bundle in the user's installed host, compare complete tasks
with the same model/environment, and observe correct selection, review/reconstruction
effort, rework and time to accepted result before claiming a performance improvement.
