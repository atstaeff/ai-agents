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

Exports include supported document, configuration, script, fixture and asset file types
from the six canonical source folders. The same explicit path/type policy applies to Git
checkouts and unpacked source archives before any source bytes are read. Hidden state,
environment files, credential/key names in any path component, nested private/local state, dependency/build/cache
directories and unsupported file types are omitted. References to excluded sources fail
before writing a bundle. Public skill scripts, images and document templates remain available
in the reference catalog, including Herd imports. The policy does not inspect file contents
for secrets; review publishable source contents before distribution.

Work-record updates recheck the caller's content hash after flushing the prepared file;
creation never replaces an existing file. Archiving creates a fresh archive copy and checks
the active record before removing it. These checks preserve editor saves made during
preparation. Existing-file replacement and removal still have a short check-to-operation
window: they do not provide compare-and-swap across processes. Stop other writers for
operations that require stronger coordination. Handled archive failures remove only the
unchanged archive created by that operation, leaving archive edits intact. An interruption
or failed cleanup can leave both copies; inspect them before retrying.
