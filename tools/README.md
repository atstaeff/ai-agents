# Local executable tools

These tools are optional. Reading agents, skills and the operating model does not
require running a server or installing a model framework.

| Source | Responsibility |
| --- | --- |
| ai_toolkit.py | Catalog metadata/link checks, selected runtime exports (including native Herd imports), local work-record CLI, loopback HTTP API and Obsidian URI encoding |
| project_config.py | Validate optional existing project/workspace YAML configuration |
| workspace_smoke.py | Exercise the real local HTTP and record flow, including comments and stale-write handling |
| web/ | Browser assets for the local catalog and Markdown workbench |

The core runs on Python 3.11+ with the standard library. Optional YAML validation uses
the locked validation environment. The local workbench runs no models, synchronizes no
GitHub/Jira trackers and is not a distributed coordination service. Host integrations
supply model execution, discovery, permissions and any supported delegation.

Use the [runbook](../toolkit/REPOSITORY-WORKFLOW.md) for commands, [runtime guide](../toolkit/RUNTIMES.md)
for exporters and [API guide](../toolkit/API.md) for HTTP behavior. [toolkit/](../toolkit/README.md)
contains the methods and documentation; this directory implements executable behavior.

Export updates preserve license notices, validate manifest paths, coordinate writers and
recover incomplete file updates. See [update and recovery](../toolkit/RUNTIMES.md#updates-and-privacy)
for interrupted exports. These protections do not make the local workbench a distributed
team scheduler.
