# Run the workflow in this repository

Start at the actual [project map](../PROJECT.md) and
[configuration](../project.yaml). New work uses `workspace/`, not a `.ai/`
working directory. These commands require a checkout containing the workspace changes;
an unmerged PR does not update `main` or an older local checkout automatically.

## Prepare and migrate

From the repository root:

```sh
python3 tools/ai_toolkit.py check
uv sync --locked --group validation
uv run --locked --group validation python tools/project_config.py --config project.yaml
```

Python 3.11+ runs the local CLI, dashboard, exports and pilot. The locked environment
supplies optional schema and website dependencies. For existing old-layout records,
stop writers, back up the project and use the new toolkit revision's migration:

```sh
python3 tools/ai_toolkit.py work --workspace . migrate --dry-run
python3 tools/ai_toolkit.py work --workspace . migrate
```

Record bytes are preserved. The empty old parent is removed; `legacy_directory_remaining:
true` means content still requires deliberate review. Unknown files and conflicting
destinations are not silently removed or merged. Historical migration references and
the export ownership manifest filename remain compatibility details.

## Generate and select the OpenCode bundle

```sh
python3 tools/ai_toolkit.py export --runtime opencode --output workspace/exports/opencode
```

The ignored bundle selects Jörg and includes Plan/Build and the specialist catalog.
Re-export after updating canonical profiles. Unchanged output is skipped; the ownership
manifest protects human edits. With OpenCode 1 and a provider/model already configured
on your machine, start from this repository root:

```sh
OPENCODE_CONFIG_DIR="$PWD/workspace/exports/opencode" \
OPENCODE_CONFIG="$PWD/workspace/exports/opencode/opencode.json" \
opencode web
```

This selects the generated bundle; it does not install OpenCode or configure a model
account. Perform the [installed-host check](PORTABILITY.md#verify-a-new-host-once).
Optional Plannotator and separate Plan/Build models follow the [plan-review guide](PLAN-REVIEW.md).

## Use the actual assignment

Tracked work keeps the plan and acceptance in its assigned GitHub issue and links the PR.
A direct maintenance request already represented by an open PR keeps its bounded plan
and handoff there. Do not create a second issue or local plan for the same assignment.
No GitHub Project board or field mapping is currently adopted here.

For a separate larger local outcome without a tracked assignment:

```sh
python3 tools/ai_toolkit.py work --workspace . new local-outcome \
  --title "Describe the concrete local outcome" --kind software
python3 tools/ai_toolkit.py serve --workspace .
```

The dashboard at `http://127.0.0.1:4097` manages local Markdown plans, comments and evidence.
It does not update GitHub or invoke models. Use the host's available authorized tools
for remote writes. A first request in OpenCode can be:

> Read AGENTS.md, PROJECT.md, CONTRIBUTING.md and project.yaml. Continue the assigned
> issue or current PR from its latest plan and handoff. Inspect affected decisions and
> code, implement one bounded increment and run its quality gates. Preserve my comments,
> report actual evidence and follow the agreed merge/deployment authorization.

## Replay the process locally

```sh
python3 tools/workspace_smoke.py
```

The command performs real local operations in a fresh generated fixture:

1. Create a CLI work record with a bounded plan and three tasks.
2. Serve the actual dashboard and API over loopback HTTP.
3. Save marked fixture feedback and reject stale/unversioned writes.
4. Export the actual OpenCode catalog; verify default Jörg, repeat-export behavior
   and protection of an edited profile.
5. Save evidence and handoff, recover them with a fresh store and archive completed work.
6. Migrate an old-layout fixture without changing bytes or leaving `.ai/`.

Each run prints its generated directory and saves `report.json` there. The archived
fixture is under the run's `project/workspace/archive/`. A fresh directory per run avoids
overwriting existing work. Reports and bundles stay ignored and outside the knowledge
website. This local fixture is not another plan for a tracked task.

Fixture comments are simulated input, not human approval. A fresh store proves file
recovery, not LLM reasoning. See the [pilot observation](evaluations/workspace-pilot-20261022.md)
for actual results and unverified boundaries.

## Verify and hand off

Run the gates in `project.yaml`; CI also replays the pilot. Keep current
revision, evidence, unresolved questions and the next action in the existing assignment.
Review, acceptance, integration and deployment are distinct states.
