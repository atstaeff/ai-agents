# Frequently asked questions

## What do I need to adopt?

Try the [disposable first task](getting-started/quick-start.md) before adopting anything:
export a small catalog locally, then use your host for a supplied documentation exercise.

Start with root `AGENTS.md`, `PROJECT.md` and `CONTRIBUTING.md`, or link their existing
equivalents. Name the project's actual work, review, knowledge and decision sources.
Merge the [project starter](getting-started/lean-project.md) into existing instructions;
no YAML file or `workspace/` directory is required.

## Where do plans and delivery evidence belong?

The designated issue or ticket owns shared scope, acceptance and evidence links. A linked
PR holds implementation, review and check details. Personal execution plans stay in the
privately configured Second Brain, subject to project policy. If it is unavailable, keep
an explicitly unsaved session plan and continue authorized work. Small changes need no
plan file. See the [working contract](getting-started/workflow.md).

## Must we use GitHub or keep knowledge in the repository?

Use the project's existing systems. A Jira ticket can link a GitHub PR; knowledge can
live in an authorized wiki or local Markdown. `AGENTS.md` identifies each authoritative
source. Missing access means a clearly marked proposed update, not a replacement tracker
or a claim that synchronization occurred.

## Which hosts can use the catalog?

Adapters generate layouts for Herd, OpenCode, VS Code/Copilot and Claude Code. The portable
export provides Agent Skills and generic profiles. Herd has a commander package and
v2 import bundles; follow [runtime setup](getting-started/installation.md) for the actual
formats and commands. Discovery, model/effort, tools and permissions still need a check in
your installed version. Use the [runtime and capacity record](templates/delivery/runtime-check.md)
for observed evidence and limits; no exported layout alone qualifies a host.

## Does linking the catalog adopt its process?

No. The starter's local contribution guide owns binding process. Its live catalog links
are evolving techniques and references. To adopt external policy, record the immutable
source URL and an explicit adopted SHA/version in the project process, read the body and
state any approved fallback. See the [starter policy fields](lean-project/contributing.md#policy-adoption).

## Does the toolkit run a team of agents?

The host runs sessions and delegation. The toolkit exports guidance and adapters; its
local dashboard manages files. A product, architecture or delivery leader can coordinate
bounded specialists when the host supports it and the assignment authorizes delegation.
See [orchestration](getting-started/orchestration.md).

## Where are specialist models configured?

In the host. Choose economical models for bounded work only after checking their results
on representative tasks. Use more capable models where observed failures or difficult
decisions justify them. Herd packages contain no model-routing keys. See
[model selection](references/llm-model-guide.md) and the host's current documentation.

## Can Plan and Build use different permissions or models?

Yes, where the host supports it. Permission fields and approval interfaces differ across
adapters. OpenCode has optional phase settings and
[Plannotator review](getting-started/plan-review.md). Review the effective host configuration
and verify an actual handoff before relying on either restrictions or model selection.

## Do Graphify and Ponytail run automatically?

No. They are optional integrations. Choose an authorized local source set and inspect
the proposed operation before running it. The toolkit does not install them or start
remote scans automatically. See [integrations](getting-started/integrations.md).

## What is maintained in this website?

Website-specific introductions live in `website/content/`. Catalog profiles, templates
and process guides are published from their canonical Markdown sources. Root `docs/`
is compiled website output. Edit the source linked by the page; see the
[ownership map](architecture.md).

## Does an accepted decision record prove delivery?

It records an authorized choice. Implementation, verification, required review,
integration, deployment and observed impact each need their own evidence. Preserve
significant reasons when they arise; update current knowledge against actual behavior.

## Does this upload private notes or synchronize our tracker?

The local toolkit has no remote vault or tracker synchronization service. A host can
use explicitly accessible tools under its own permissions and provider settings. Keep
private notes, credentials and vault paths outside public sources. The optional
[runner page](customer-workspace/runner.md) is a design contract, not an implemented worker.

## How do I update exported profiles?

Update canonical sources and re-export to the same dedicated destination. The manifest
protects edited and unmanaged files; resolve conflicts deliberately. Keep the exported
reference catalog with the profiles and repeat the relevant host check after changes.

## Should an available Herdr installation be used?

Yes, when its selected server and tools are usable within current permissions. Follow
[Herdr execution](getting-started/herdr.md): reuse sessions, select strong/high reasoning
for complex judgment and economical models for bounded work, keep labelled tabs and
fill free slots with independent ready tasks only while measured resource, provider, budget and review limits permit. Native commands handle routine
coordination. Report the exact availability/access gap before using a fallback.
