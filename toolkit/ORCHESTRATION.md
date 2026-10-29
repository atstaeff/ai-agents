# Lead a team of AI specialists

Use this guide when independent slices or independent review justify multiple agents.
One session is sufficient for a routine correction. The [operating model](OPERATING-MODEL.md)
owns the delivery process; the issue or Jira ticket owns this assignment.

## Prefer available Herdr

Discover and use [Herdr](HERDR.md) when its executable and selected server are usable.
The policy owns readiness, high-reasoning complex work, economical specialists, native
mechanical coordination, labelled tabs and adaptive capacity. Reuse matching sessions;
report a concrete gap before falling back. Routine work can stay in the current pane.

Use Herdr's native agent dispatch/lifecycle as the preferred path; no Herd installation
or `herd` export is required. Load the installed release's native Herdr skill when supported.
For substantial work, delegate useful independent ready slices by default, submit siblings
before waiting and refill free capacity. One dispatcher allocates the shared worker/spend
allowance across all leads and nested specialists; no worker starts children outside it.

For each assignment, keep one owner of dispatch and integration. If another adopted
fleet tool owns worker creation, use Herdr for its terminal surface without duplicating
workers or task queues. The Herd exporter below is a separate optional integration.

## A team has one integrated outcome

Activate product, engineering and delivery leadership as needed. Give each lead a distinct
question and retain one named integration owner. Several commanders can own separate work
streams; they must not independently rewrite the same contract or prioritize the same issue.

| Work | Lead contribution | Bounded specialists |
| --- | --- | --- |
| Product scope | product-manager proposes value, stakeholder questions and acceptance | product-discovery and domain research |
| System design | lead-architect resolves boundaries, contracts and consequential alternatives | API, GCP, security and architecture review |
| Implementation | task-orchestrator sequences dependencies and integrates results | python-expert, frontend-expert, terraform-engineer, devops-agent |
| Evidence and narrative | Integrator requests independent assessment | code-reviewer, test-strategist, documentation-editor |

Use the [delegation brief](../templates/delivery/delegation.md). Each task packet includes
outcome, observable acceptance, exact source revisions, necessary contracts, permitted write
scope, dependencies, relevant skill and expected return. A specialist returns changed paths,
revision, executed checks, limitations and one next action. Pass source pointers and a short
summary rather than the entire leader conversation.

## Parallelism and model choices

1. Agree interfaces before starting dependent writers. Use isolated worktrees/branches.
2. Run independent bounded tasks concurrently within the shared capacity and cost budget,
   including nested workers. Keep one agent pane per worker, related checks/logs in labelled
   panes, isolated writer workspaces grouped with the project and the user's focus intact.
3. Use strong approved models with high reasoning for unresolved architecture, decomposition,
   integration and consequential review. Use a proven economical configuration for a clear
   specialty; native commands or the smallest capable model handle mechanical coordination.
4. Inspect failed outputs. Correct the task packet or escalate the specific uncertainty;
   stop repeated failures at the assignment's retry/budget limit.
5. Review returned work and test the combined revision. Task completion or an idle agent
   is not acceptance. A provider change does not transfer unsaved state or imply approval.

Set actual model IDs, effort, provider credentials, concurrency, timeouts and budgets in
private host configuration. No model is universally the best or cheapest. Compare evaluated
results, review effort, rework, elapsed time and actual spend for a representative workload.
Use the host's scheduling primitives rather than creating a second scheduler in prompts.

Reviewers assess a specified revision independently. The implementation author must not
approve their own result by switching personas. Run a separate authoring pass and editorial
pass when documentation changes substantially; a minor correction needs no writing team.
Host tool restrictions enforce access; profile prose supplies task boundaries.

## Native Herd commanders

This adapter targets **[Herd by NickGuAI](https://github.com/NickGuAI/Herd)**, the meta-harness
with commanders, workers and persistent mission state. Herdr, HerdOS and herd-ag/herd-core
are separate products. The [integration guide](INTEGRATIONS.md) names their different roles.

```sh
python3 tools/ai_toolkit.py export --runtime herd --preset engineering \
  --agent product-manager --agent task-orchestrator --agent frontend-expert \
  --agent terraform-engineer --agent documentation-editor \
  --skill product-discovery --skill terraform-iac --skill technical-writing \
  --output /path/to/herd-export --dry-run
```

Inspect the selection, then repeat without `--dry-run` to create the bundle. The export contains:

- `herd/imports/<lead>.bundle.json`: portable schema-v2 files for Marketplace's **Install from file**.
- `herd/commanders/<lead>/`: native package sources with `package.json`, `COMMANDER.md`,
  `skills.manifest.json`, `onboarding.md` and `memory-seed.md`.
- `catalog/`: canonical reference snapshot, selected entry index and redistribution notice.

Import the desired leads using **Install from file**. Native package directories are for
Herd's backend package registry; placing a directory in a customer repository does not
register it automatically. Importing a commander creates a distinct identity; updating
this repository or re-exporting does not upgrade an already imported commander.

The import embeds selected skill files and an on-demand catalog reference skill. It
contains reusable expertise, not customer memory, credentials or automations. Skill bindings
supply procedures; worker profiles remain reference material for a commander to use when
forming bounded assignments. They are not additional running workers.

Imported bindings live on the commander's filesystem. For remote workers, provide the
necessary authorized files or a bounded source packet in a reachable worker workspace,
with the same source revision. Verify access before dispatch; a commander-local path
does not imply a shared filesystem or automatic synchronization.

Select the actual provider/model and worker policies in the installed Herd environment.
The adapter emits no invented specialist routing or permission fields. Establish restrictive
review permissions in the underlying harness. Imported commander defaults and worker
capabilities depend on Herd's version and local configuration.

### Verify the installed host

Before customer work, use a disposable project:

1. Import one bundle and inspect its identity, skill bindings and reference links.
2. Configure a lead and an economical worker; inspect effective provider/model and tools.
3. Delegate a harmless bounded change. Verify source discovery, isolated scope and returned evidence.
4. Interrupt and resume it. Confirm shared assignment links and durable decisions survive.
5. Inspect independent review and the combined check result before accepting the change.

The repository tests package/import shape, embedded links and safe export updates. They
cannot establish a live Herd installation, provider behavior or cross-host recovery.

The adapter contract is pinned to upstream commit
[`fbda6618c7b53524faddbed070e4fbc14970e412`](https://github.com/NickGuAI/Herd/tree/fbda6618c7b53524faddbed070e4fbc14970e412),
including the [package guide](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/docs/guides/commander-packages.md)
and [bundle-v2 guide](https://github.com/NickGuAI/Herd/blob/fbda6618c7b53524faddbed070e4fbc14970e412/docs/guides/commander-bundles.md).
Verify compatibility when upgrading Herd. Herd is a separately installed third-party product;
this repository supplies original profiles and adapter output, and bundles no Herd runtime code.

## Example: a FastAPI and React feature on Google Cloud

The product lead defines who can use the feature and its observable acceptance in the
existing ticket. The engineering lead agrees the API, authorization and data ownership,
recording an ADR only for a consequential choice. The delivery lead delegates:

| Slice | Write scope | Can start after | Return evidence |
| --- | --- | --- | --- |
| API | Backend route/service and contract tests | API contract agreed | Authorized, denied and invalid request cases |
| Web | Feature components and frontend tests | API contract agreed | Loading, empty, success and error journeys; keyboard access |
| Infrastructure | Relevant Terraform module and environment config | Runtime requirements agreed | Formatting/validation and reviewed plan where authorized |
| Documentation | Affected concept/runbook/decision pages | Implemented behavior available | Source-linked instructions and explicit gaps |

Keep the integrator in `00 Control`. Group `ISSUE-ID / api`, `/ web` and `/ infra` writer
workspaces under the project, each with its own branch and `10 Work` tab. Its specialist
pane uses the qualified economical route; a separate checks pane runs only nonconflicting
commands. Product/engineering leads use the strong/high route only for complex decisions.
Add `20 Runtime` or `40 Review` views when needed; these labels are repository conventions.

The first three slices can overlap when their write scopes and capacity permit. A reviewer
assesses the integrated diff and real checks. The documentation editor checks the narrative
against the final behavior. The release owner controls deployment and observes the product
outcome; the team retains current knowledge and significant rationale in the project.
