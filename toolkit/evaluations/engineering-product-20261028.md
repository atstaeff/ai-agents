# Engineering product review — 2026-10-28

## Scope and outcome

Reviewed the repository entry, catalog selection, primary stack guidance, templates,
operating model, runtime exports and Docusaurus narrative. Implemented focused changes
and independent process, code and editorial review. This is a bounded engineering review,
not certification of every peripheral reference or a live customer installation.

| Finding | Result |
| --- | --- |
| Starter process contradicted private personal planning | Aligned starter, variants, worked examples and optional shared record guidance |
| Assignment lacked explicit coordination owners | Added accountable owner, writer scope, dependency and integrator fields |
| Broad references duplicated stack guidance | Short entry procedures plus focused Python/FastAPI, React/JavaScript and GCP references |
| Terraform and technical writing lacked focused procedures | Added two skills and two specialist roles; opt-in platform/documentation presets |
| Leadership and model choices were scattered | One value stream, product/engineering/delivery viewpoints and bounded specialist packets |
| No native fleet import | Native NickGuAI/Herd package-v1 and portable bundle-v2 exports with pinned upstream contract |
| Export failures could leave inconsistent updates | Validated paths/hashes, cooperative writer lock, replacement checks and recoverable journal |
| Copied catalog lost nested source links | Kept included links local; verified omitted public sources point to the source repository |
| Source directory symlinks could import unintended files | Reject source-directory and interface symlinks before export |
| Export omitted redistribution notice | Include source LICENSE in reference snapshots and Herd imports |
| Primary docs contained stale YAML/workspace and PR assumptions | Rewrote authored pages, clarified non-code outcomes and updated navigation |

## Catalog evidence

The active catalog has 22 agents and 41 skills. Minimal remains 3/4; engineering is 9/16;
product 4/7; platform 6/10; documentation 2/5; knowledge 3/5. These are native selections,
not required team sizes. The changed catalog sources are approximately 60 KB smaller,
including additions. Source-size reduction does not establish token, latency or cost savings.

## Independent observations

- A separate process reviewer identified contradictory copyable instructions and missing
  ownership fields; these were corrected in the templates and model.
- A separate code reviewer reproduced an unchanged-manifest recovery defect during a
  forced repair. Explicit transaction phases corrected it; the regression check passed.
- The editorial reviewer identified a universal review gate, a missing non-code outcome
  path, an inaccessible-update fallback and ambiguous integration ownership. The final
  narrative makes these responsibilities explicit.

Three fresh bounded model trials exercised the changed expertise:

| Trial | Observed result | Limit |
| --- | --- | --- |
| Small spelling correction through agent-routing | Changed one word, inspected the diff and avoided unnecessary tests/delegation | One text-only task |
| Python/FastAPI invoice access proposal | Used bound parameters, tenant filtering, output schema, sync I/O boundary and explicit unavailable checks | Proposal only; added ID-domain assumptions require repository confirmation |
| Terraform address/IAM migration without tools | Preserved resource/state identity, identified competing IAM ownership and marked missing plan/apply evidence | No live Terraform or cloud execution |

These trials demonstrate specific observed behavior; they are not comparative model
benchmarks or evidence that future agents always follow instructions.

## Executed checks

- Catalog metadata, generated indexes and local links: valid 22 agents/41 skills.
- Locked Python validation suite: 124 tests passed, including 15 focused Herd/export checks.
- Graph/privacy/scale suite: 9 tests passed; fixtures include 50,000 records and a 30,000-record chain.
- Local HTTP/storage/export replay: passed, including persisted comments and stale writes.
- Python compilation, JavaScript/options syntax and diff whitespace: passed.
- Strict Docusaurus production build: passed; 193 generated documents from canonical sources.
- Local browser smoke: blocked by unavailable Chromium executable. The PR CI installs
  Chromium and runs the browser journey and mobile checks; its result is recorded in CI.

## Remaining verification boundaries

No live Herd installation, provider/model call, remote-worker filesystem transfer,
customer tracker synchronization, Terraform apply, cloud deployment or release was run.
Herd import shape and reference paths were cross-checked against the pinned upstream
parser; effective tools, models and recovery across real machines require the documented
installed-host exercise. The exporter coordinates its own writers; arbitrary editors
and distributed hosts still require ownership coordination. Power-loss durability was
not tested.

The knowledge map uses bounded static views. Million-record operation still needs an
incremental authorized metadata/search backend. Graphify and Ponytail have documented
native adoption paths; they are not installed or run by the exporter.

Reviewable work remains in the current PR. Merge, publication and observed customer
outcomes are separate from these source-level checks.
