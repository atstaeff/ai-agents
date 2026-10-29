# Herdr execution policy

Use Herdr as the preferred execution surface whenever its executable is available and
its selected server is usable within the current host/project permissions. Apply this
policy to the current session as well as delegated work. Reuse an existing matching
session before creating another one. Herdr organizes execution; the assignment and
project knowledge remain authoritative.

## Default behavior

For a substantial assignment, the lead delegates useful independent ready slices through
Herdr as the normal execution path. Keep the lead focused on unresolved judgment, contracts,
blockers and integration while economical specialists deliver bounded results. Dispatch
ready work together within the observed limits; do not serialize it merely because one
coordinator submits the tasks. Keep dependent or overlapping work queued. A small correction
stays in the current pane. Delegate when expected delivery/review benefit covers setup and
integration effort; reduce the team when that benefit disappears.

The authorized assignment is standing authorization for routine internal coordination
within host/project limits. The lead chooses expertise, qualified routes, layout and
dispatch without another "use Herdr" or "start subagents" instruction. Use the
[autonomous team startup](SESSION-RULES.md#autonomous-team-default) and
[one-time host setup](RUNTIMES.md#configure-the-autonomous-team-once). The receiving lead
keeps ownership through the stages required by the requested scope, including review,
correction and combined evidence. A real user decision or exhausted authorized capacity
can block work; routine coordination should not be returned to the user as a task list.

## Discover, connect and use

At session start, reuse a known matching Herdr context and its recent readiness evidence.
Otherwise check executable discovery through normal PATH lookup or an explicitly configured
path. Resolve the intended machine and session from project/local instructions before
calling the API. The examples below target the local session; a selected remote target
requires the same explicit `--machine MACHINE_ID` prefix on every supported API command.
Selecting a machine in the UI does not retarget existing shell commands. Never reuse
local IDs for a remote server or fall back to Local after a failed remote operation.

Inside a Herdr pane, use the release-matched native skill printed by `herdr --skill`
when supported; reuse an already loaded matching copy. Follow its operating guard:
`HERDR_ENV=1` identifies a managed caller, and `HERDR_PANE_ID` supplies its pane context.
An installed executable alone does not identify a session the caller owns. Outside a
managed pane, discover availability without assuming `--current`; control a session only
through explicitly selected, authorized external automation. Otherwise report the missing
attachment/target and continue independent work in the authorized host. Do not fabricate
Herdr environment variables. The [official skill guide](https://herdr.dev/docs/agent-skill/)
explains installation/discovery; this repository does not maintain a copied fork.

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

Reuse a qualified route for its task class. Do not buy a strong-model turn to rename a
pane, poll state or relay unchanged output. When a specialist exposes a new complex
decision, return that decision and its evidence to the lead; resume bounded implementation
on the economical route after the contract is resolved. Change model/session only after
saving the small handoff needed to continue without replaying the full conversation.

Verify effective model and effort in the harness's session settings or launch output.
Record unavailable verification explicitly. A declared model alias alone proves neither
its capability nor the active effort. If the required strong/high route is unavailable or cannot be verified,
report the configuration gap and continue only work that does not depend on it; do not
silently downgrade a complex decision. Escalate a struggling specialist with its concrete
failure, relevant sources and attempted checks; avoid repeated blind retries.

## Keep the project visible

Use one primary workspace for the project and group its writer worktree workspaces under
it. A tab is a view inside one workspace; a pane (sometimes called a panel) is one terminal.
Separate writer worktrees are workspaces, not extra tabs sharing the primary checkout.
This is a UI convention, not a required `workspace/` repository directory. Reuse the
initial tab/root pane for Control and create only the lead viewpoints needed by the outcome.

| Location | Suggested label | Contents |
| --- | --- | --- |
| Primary workspace, first tab | `00 Control` | Integration lead; assignment, ready queue and remaining capacity |
| Optional primary tabs | `10 Product`, `20 Engineering`, `30 Delivery` | Only unresolved lead viewpoints requiring a separate session |
| Grouped writer workspaces | `ISSUE-ID / api`, `ISSUE-ID / web`, `ISSUE-ID / infra` | One owned checkout/branch per concurrent writer |
| Writer workspace, work tab | `10 Work` | `api-agent` pane plus a `checks` pane when it helps |
| Workspace running the relevant service | `20 Runtime` | Labelled `server` and `logs` panes, only while needed |
| Review workspace/tab | `40 Review` | Independent reviewer at the specified combined revision; no implementation edits |

Use a pane for a tightly related test/log process and a tab for a different view; grow
the layout only while it stays readable on the actual screen. Prefer another tab or zoom
to a grid of tiny panes. Reuse and rename existing locations. Create background layout
with `--no-focus` and keep the user's focus unless a requested interaction needs it.
Use the sidebar's rolled-up agent state to attend to blockers and returned work instead
of opening every transcript. State is an attention signal, not approval or acceptance.

Every concurrent writer owns an isolated Git worktree/branch, and its terminal starts in
that checkout. Multiple tabs/panes pointing at one checkout do not isolate file writes.
Read-only leads may share sources; shared contracts still need one owner. A checks pane
can run concurrently only if it does not rewrite the writer's files; serialize formatters,
autofixes and generators or give them their own isolated scope. Prevent service/port clashes.

Native creation examples use placeholders; replace paths, revisions and IDs with verified
values. Capture returned IDs instead of predicting them:

```sh
herdr workspace create --cwd /absolute/project --label project-name --no-focus
herdr tab create --workspace WORKSPACE_ID --cwd /absolute/project --label "20 Engineering" --no-focus
herdr worktree create --workspace WORKSPACE_ID --branch work/ISSUE-ID-api --base SOURCE_REVISION --label "ISSUE-ID / api" --no-focus
```

Workspace and tab creation return a root pane under `.result.root_pane.pane_id`.
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

Use short stable live names such as `shop42-api-01`, `shop42-web-01` and `shop42-review-01`;
follow the installed name rules (currently lowercase first letter, letters/digits/underscore/
hyphen, at most 32 characters) and resolve collisions before launch. Label panes for their
role and keep their actual IDs/checkouts in the control mapping. Before each new harness
starts, establish its catalog, local model-route configuration and bounded tool access;
the lead's launch-only environment is not evidence that another pane inherited them.

For an extra checks pane in the already verified writer checkout:

```sh
herdr pane split WRITER_PANE_ID --direction down --cwd /absolute/writer-checkout --no-focus
herdr pane rename RETURNED_PANE_ID checks
```

Capture the new ID from `.result.pane.pane_id`. Use `pane run` / `pane wait-output` for
ordinary processes and `agent start` / `agent prompt` / `agent wait` for recognized agents;
creating a pane does not start an agent or select its model. Shell commands still need
correct quoting and the project's verified runbook.

## Fill available capacity without overload

The lead keeps a small ready queue at the existing assignment. Only dispatch tasks whose
inputs/contracts are ready and whose write scopes do not conflict. Effective concurrency
is the smallest relevant limit: approved worker cap, provider request/token limits, cost
budget, measured machine headroom, independent ready work and integration/review capacity.
Count active leads, workers and expensive build/test processes against the resources they use.

Use one dispatcher per assignment. Product/engineering leads can request specialists;
the dispatcher allocates them from the same remaining allowance. A worker must request
extra capacity before starting children. Nested agents do not get a fresh budget or
worker cap. Track agent/task, scope, checkout, model/effort, status and next return in the
existing assignment/host control surface; do not build another scheduler or mirror tracker.

If no measured capacity exists, start with one bounded worker and increase in small waves as work completes
without pressure. Fill newly free slots only while measured resource, provider, budget
and review limits still permit it. Reduce new dispatch when RAM/CPU or local model memory is under pressure, rate limits occur, spend approaches
the cap or review waits grow. Provider-hosted inference and local inference have different
resource costs; CPU count alone is not a universal worker limit. Queue dependent tasks;
keep the native scheduler/control surface rather than adding a polling daemon.

Dispatch ready siblings before waiting on one. While workers run, resolve blockers, review
returns and prepare integration; refill free capacity when another useful task becomes ready.
Observe lifecycle through native state, bounded reads/waits and supported notifications or
events. Wait in short intervals so the coordinator can update the user and inspect other work;
avoid repeated model calls and full transcript dumps just to poll state.

Send a new task to a ready agent after capturing its prior result. `agent prompt` success
acknowledges input delivery; `--wait` on an already working agent can settle on its previous
turn. A standalone wait can return immediately on an existing idle/done state. Match the
returned artifact, source revision and checks to the delegated task before treating it as
finished. Inspect live state/output after a timeout or uncertain delivery before retrying.
A blocked agent needs the actual requested input under existing action permissions; never
auto-approve a dialog or infer completion/permission from idle, done or unknown state.

Exchange compact internal handoffs: task/source revision, contract or blocker, requested
action and return evidence. A specialist reports a contract change to its owner before
dependent work proceeds; a reviewer sends findings on the named revision back through the
integrator to the writer. Peers can exchange permitted source facts using verified live
targets, but one owner updates each shared contract/queue. Reuse the assignment and native
agent channels; avoid duplicate chat histories, trackers and full-conversation broadcasts.
The lead handles bounded corrections and rechecks affected evidence before reporting completion.

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

## Basis and limits

Native behavior was checked against Herdr's [concepts](https://herdr.dev/docs/concepts/),
[agent automation](https://herdr.dev/docs/agent-automation/),
[agent state](https://herdr.dev/docs/agents/) and
[CLI reference](https://herdr.dev/docs/cli-reference/) on 2026-10-29. Use the installed
release's skill/schema for exact support. The numbered layout, model routes and shared
budget are this repository's engineering conventions built on those primitives; Herdr
does not automatically enforce the chosen model, file isolation, quality or spend.
