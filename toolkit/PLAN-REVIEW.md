# Review the plan before Build

Use a local Plannotator review when the user or project requires approval before
implementation. Plan proposes the change; a person verifies assumptions, comments and
approves the current revision; Build implements it and supplies evidence. Small direct
tasks keep their shorter path unless approval is required for them too.

| Phase | Responsible action | Exit condition |
| --- | --- | --- |
| Plan | Inspect context; define scope, acceptance and checks | A concrete, reviewable plan |
| Comment and revise | Verify assumptions; incorporate requested changes | Feedback addressed in a revised plan |
| Approve | Authorized reviewer approves that revision and any attached notes | Actual approval evidence |
| Build | Implement the approved scope with the selected model | Reviewable change and relevant checks |

## One plan, one approval receipt

Keep the live plan in the assigned customer issue, or the existing local work record.
Plannotator is its review interface; its local history is supporting material. It does
not synchronize an issue or enforce the customer's decision rights. The authorized host
must preserve comments and update the planning home after review.

Record a short receipt with the plan revision, actual reviewer or known user, decision,
attached notes and available review/message reference. Do not invent identities or
approval links. Build reads the approved plan, acceptance criteria, relevant context
links and receipt. When using another session, pass those pointers and the approval
evidence rather than copying the entire conversation.

Request changes, answered questions, cancellation, timeout and tool failure do not
approve a plan. Revise and resubmit after requested changes. Reopen review when scope,
acceptance or a consequential design choice changes; routine implementation details
within the approved scope do not need another approval. An approved plan permits the
agreed implementation only. ADR acceptance, code review, merge and deployment have
their own decision rights. A tool response does not expand host permissions.

See the [customer review example](../templates/customer-workspace/examples/plan-review.md).

## Enable it in OpenCode 1 Web on WSL

From the AI Agents checkout, export an isolated configuration:

```sh
python3 tools/ai_toolkit.py export --runtime opencode --plannotator \
  --output "$HOME/.config/ai-agents/opencode"
cd /path/to/project
PLANNOTATOR_REMOTE=0 PLANNOTATOR_PORT=19432 \
OPENCODE_CONFIG_DIR="$HOME/.config/ai-agents/opencode" \
OPENCODE_CONFIG="$HOME/.config/ai-agents/opencode/opencode.json" opencode web
```

OpenCode installs the configured npm plugin at startup; `npx` is unnecessary for this
setup. Restart OpenCode after changing plugins. Use `/work-plan` in the main session and
ask it to review the plan with Plannotator before implementation. Jörg remains the
default profile and can coordinate the assignment; Plan owns the gated planning phase.
Use one active plan review per project, rather than concurrent reviewers editing the
same plan.

The export uses OpenCode 1's singular `plugin` key and Plannotator's `user-managed`
workflow. Our Plan profile owns the prompt and scoped edit permissions: it can call
`submit_plan`, cannot call `plan_exit`, and still denies shell/task tools. Other profiles
inherit a denial for `submit_plan`. Sharing is disabled. The installed tool defines its
arguments; do not hardcode a schema from another plugin release. This is a workflow
guardrail; installed tools and the final merged host configuration still determine access.

Plannotator opens a separate local browser page when Plan calls `submit_plan`. If WSL
does not open Windows' browser, try `http://localhost:19432` while the review is active;
use the plugin's actual local URL if it reports a different one. The review server exists
only while a review is active.
OpenCode Web and Plannotator have separate URLs.

Select text to comment, then request changes or approve. Choose `build` as the target
agent in the review UI when available. If your Web release does not switch agent/model,
select Build explicitly or use `/work-build` after approval. Verify the selected model
and variant before implementation. Reopening a review with `/plannotator-last` is useful
for comments; it does not replace the planned `submit_plan` gate.

## Select models and thinking per phase

Run `opencode models` and use IDs available in your configured host. Supply supported
variant names for those models; `high` and `medium` below are examples, not universal
levels. Replace the two model placeholders before running:

```sh
python3 tools/ai_toolkit.py export --runtime opencode --plannotator \
  --plan-model 'PROVIDER/PLAN_MODEL' --plan-variant high \
  --build-model 'PROVIDER/BUILD_MODEL' --build-variant medium \
  --output "$HOME/.config/ai-agents/opencode"
```

These options emit `agent.plan.model`, `agent.plan.variant`, `agent.build.model` and
`agent.build.variant`. They can also be used without Plannotator. Omit either variant
to use the model's default; a variant requires an explicit model. More thinking is
appropriate when ambiguity warrants its time and cost, not as a universal default.
Verification still comes from affected behavior and checks.

OpenCode 1 supports separate agent model fields and, in current releases, an agent
`variant`. The latter applies to the agent's configured model; older 1.x versions can
behave differently. This recipe was checked against the 1.18.32 source schema. Provider
options such as `reasoningEffort` or a thinking budget are model-specific alternatives
in local configuration. OpenCode 2 uses a different plugin configuration; do not copy it
into OpenCode 1.

Re-export with the same options to retain this setup. The exporter does not merge
hand-edited configuration; it protects those edits. Keep additional provider settings
in a separate local configuration and inspect the merged result. The optional plugin
tracks `@latest`; to pin a vetted version, deliberately maintain that package entry in
local configuration and retain the export's edit protection.

## Local operation and verification limits

The plugin and review UI run on your computer. Leave sharing, hosted Workspaces, remote
URL/PR review and Plannotator's optional AI features unused for local plan review. Its
current UI still checks GitHub for updates on load; the upstream documentation provides
no opt-out. Local operation therefore does not promise zero network requests. OpenCode's
model provider independently determines where inference runs.

Leave Obsidian auto-save off for customer work: customer issues and repositories own
that knowledge. Enable it only for authorized personal material in the private PARA vault.
The core plan gate needs no separate CLI in a Bun-hosted OpenCode; wrapped/Node hosts can
need the Plannotator CLI fallback. Optional slash commands may require the upstream
installer. The toolkit neither installs that CLI nor launches a review itself.

Repository tests verify configuration, permissions, update protection and documentation.
They do not prove browser opening, agent switching or provider reasoning in your WSL
installation. Before relying on the setup, review a harmless plan: request one change,
confirm it is incorporated, approve the revision, and verify Build's selected model.

Sources: [Plannotator OpenCode setup](https://github.com/backnotprop/plannotator/blob/main/apps/opencode-plugin/README.md),
[workflow configuration](https://github.com/backnotprop/plannotator/blob/main/apps/opencode-plugin/workflow.ts),
[OpenCode agent configuration](https://opencode.ai/docs/agents/) and
[OpenCode 1.18.32 agent schema](https://github.com/anomalyco/opencode/blob/v1.18.32/packages/core/src/v1/config/agent.ts).
