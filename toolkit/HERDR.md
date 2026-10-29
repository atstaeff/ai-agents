# Herdr execution policy

Use Herdr as the preferred execution surface whenever its executable is available and
its selected server is usable within the current host/project permissions. Apply this
policy to the current session as well as delegated work. Reuse an existing matching
session before creating another one. Herdr organizes execution; the assignment and
project knowledge remain authoritative.

## Discover, connect and use

At session start, reuse a known matching Herdr context and its recent readiness evidence.
Otherwise check executable discovery through normal PATH lookup or an explicitly configured
path. Resolve the intended machine and session from project/local instructions before
calling the API. The examples below target the local session; a selected remote target
requires the same explicit `--machine MACHINE_ID` prefix on every supported API command.
Selecting a machine in the UI does not retarget existing shell commands. Never reuse
local IDs for a remote server or fall back to Local after a failed remote operation.

For a new available context, the small read-only readiness check is:

```sh
herdr status server
```

Inspect `herdr --version` and the local CLI's `herdr api schema --json` when compatibility
is uncertain, and `workspace list` / `agent list` when finding or dispatching work. Use
`herdr machine list` to resolve a configured remote alias when needed. Avoid repeating a
full inventory for every prompt. Local schema output describes the CLI, not proof of a
remote server's capabilities; confirm compatibility against that selected server.

Use the installed CLI/schema and its [official reference](https://herdr.dev/docs/cli-reference/).
If the intended local server is stopped, start or attach it using the project's established
session setup; `herdr server` starts a local headless server. Recheck readiness. For a
remote target, use its established connection/setup flow; starting a local server does
not repair remote readiness. Preserve existing panes and sessions; do not replace another
server to establish the requested session.

If Herdr is unavailable, incompatible or inaccessible for the intended target, state
the concrete gap. Continue independent work only through a host already authorized
for that same target; never substitute Local for an inaccessible remote target. Do not silently ignore an available
usable Herdr installation. Do not install another orchestrator just to work around an
unavailable binary. A small task uses the current Herdr pane when applicable; it does
not require a new lead, tab or specialist.

Use the [runtime qualification record](RUNTIME-QUALIFICATION.md) to retain verified
host/route evidence and capacity. Reuse matching evidence; recheck after material changes
or failures rather than repeating setup for every prompt.

## Route work by complexity

Resolve these routes to actual installed provider/model settings before dispatch. Keep
model IDs, credentials, reasoning flags and budgets in private host configuration. Use
provider-supported effort settings; there is no universal `thinking` command or flag.

| Work class | Model capability and effort | Examples |
| --- | --- | --- |
| Complex judgment | Strong approved model with high reasoning; use a higher supported effort when the task warrants it | Ambiguous requirements, architecture, difficult debugging, decomposition and integration conflicts |
| Bounded specialist work | Proven economical model; normal or low reasoning when sufficient | Implement an agreed API slice, UI behavior, tests, a scoped refactor or a factual documentation update |
| Mechanical coordination | Native CLI first; smallest capable model only when interpretation is needed | Inspect state, name tabs, pass an agreed packet, collect check results and summarize a known result |
| Consequential independent review | Strong approved model with high reasoning | Authorization boundaries, state migrations, security and major contracts |

Complexity overrides job title: a delivery lead's routine status check is mechanical;
a specialist facing an unresolved architectural problem needs the complex route. Keep
expensive reasoning on the decisions that need it, then return bounded execution to the
economical route. Do not resend the full leader conversation to every worker.

Verify effective model and effort in the harness's session settings or launch output.
Record unavailable verification explicitly. A declared model alias alone proves neither
its capability nor the active effort. If the required strong/high route is unavailable or cannot be verified,
report the configuration gap and continue only work that does not depend on it; do not
silently downgrade a complex decision. Escalate a struggling specialist with its concrete
failure, relevant sources and attempted checks; avoid repeated blind retries.

## Keep the project visible

Use a project workspace and labelled tabs. The labels below are examples; one useful
control/lead view is sufficient when it covers the outcome. This is a UI convention;
it does not require a `workspace/` repository directory. Create only the lead viewpoints needed by the outcome.

| Tab or grouped workspace label | Purpose |
| --- | --- |
| `00 Control` | Integration owner, assignment link, active capacity and short handoff |
| `10 Product` | Product lead when user value, stakeholder alignment or acceptance is unresolved |
| `20 Engineering` | Technical lead for contracts and consequential choices |
| `30 Delivery` | Delivery lead when several work streams need sequencing |
| `40 Review` | Independent review of a named revision |
| `ISSUE-ID / api`, `ISSUE-ID / web`, `ISSUE-ID / infra` | Active specialist scope and its owned checkout |

Reuse and rename tabs rather than generating a new tab for every prompt. Separate
terminal layout from writer isolation: every concurrent writer owns an isolated Git
worktree/branch, and its terminal starts in that checkout. Use Herdr's native worktree
workspaces grouped with the project. Multiple tabs pointing at one checkout do not
isolate file writes. Read-only leads may share sources; shared contracts still need one owner.

Native creation examples use placeholders; replace paths, revisions and IDs with verified
values. Capture returned IDs instead of predicting them:

```sh
herdr workspace create --cwd /absolute/project --label project-name --no-focus
herdr tab create --workspace WORKSPACE_ID --cwd /absolute/project --label "20 Engineering" --no-focus
herdr worktree create --workspace WORKSPACE_ID --branch work/ISSUE-ID-api --base SOURCE_REVISION --label "ISSUE-ID / api" --no-focus
```

Reuse the initial tab and root pane created with the project workspace for Control;
add a separate tab only for another needed view. Workspace and tab creation return a
root pane under `.result.root_pane.pane_id`.
Inspect the installed schema for the worktree response. Start an agent only in its
available shell pane. `HOST_KIND` is a placeholder for an installed supported kind
such as `opencode`, `codex` or `claude`; pass that harness's verified launch arguments
after `--`:

```sh
herdr agent start project-api --kind HOST_KIND --pane PANE_ID -- VERIFIED_HOST_ARGUMENTS
```

The launch arguments must resolve the selected model/effort route and required profile.
Inspect returned state and effective settings before sending the task. Keep the mapping
from live agent name to task, pane, checkout and route at the existing coordination home.
Never resume work by guessing that a reused name still identifies the old session.

## Fill available capacity without overload

The lead keeps a small ready queue at the existing assignment. Only dispatch tasks whose
inputs/contracts are ready and whose write scopes do not conflict. Effective concurrency
is the smallest relevant limit: approved worker cap, provider request/token limits, cost
budget, measured machine headroom, independent ready work and integration/review capacity.
Count active leads, workers and expensive build/test processes against the resources they use.

If no measured capacity exists, start with one bounded worker and increase in small waves as work completes
without pressure. Fill newly free slots only while measured resource, provider, budget
and review limits still permit it. Reduce new dispatch when RAM/CPU or local model memory is under pressure, rate limits occur, spend approaches
the cap or review waits grow. Provider-hosted inference and local inference have different
resource costs; CPU count alone is not a universal worker limit. Queue dependent tasks;
keep the native scheduler/control surface rather than adding a polling daemon.

Observe lifecycle through `agent get`, bounded `agent read`, `agent prompt` and `agent wait`.
Use short bounded waits so the coordinator can update the user and inspect other workers.
After a timeout or uncertain prompt delivery, inspect the live agent before retrying.
A blocked prompt requires the actual requested input; idle/unknown states are not acceptance.
Avoid large repeated terminal dumps and repeated model calls just to poll state.

## Integrate, retain and release resources

Inspect each returned diff and actual check evidence, then verify the combined revision.
Retain significant decisions and current knowledge in their project homes; link them from
the assignment and Docusaurus when adopted. A pane transcript is not the project memory.
Save a short handoff before switching models or sessions. Reuse an idle worker only after
its prior result is captured. Close only finished owned tabs/panes after preserving their
useful state; keep dirty worktrees and unresolved review evidence until safe integration.

Measure time to accepted result, cost, rework and review effort. Tab count, simultaneous
agents and expensive model usage are not success measures. See [orchestration](ORCHESTRATION.md)
for bounded task packets and [quality](QUALITY-STANDARD.md) for acceptance evidence.
