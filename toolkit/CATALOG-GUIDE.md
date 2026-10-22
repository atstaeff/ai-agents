# Manage agents and skills

Agents define roles, decision boundaries and expected handoffs. Skills provide reusable
procedures and focused references. A skill can be used in the current session; selecting
another profile does not automatically start another agent.

## One catalog, seven disciplines

Browse [agents](../agents/README.md) and [skills](../skills/README.md). Canonical sources
use `agents/<domain>/<name>.agent.md` and `skills/<domain>/<name>/SKILL.md`.
[Domain metadata](catalog-domains.json) drives the catalog, website and local filter.
Names remain unique across each kind so exported native IDs stay predictable.

| Domain | Responsibility |
| --- | --- |
| general | Foundations, selection and bounded coordination |
| delivery | Product discovery, project flow, scope and stakeholder decisions |
| architecture | Domain modeling, interfaces and consequential system decisions |
| engineering | Application/platform implementation and specialized products |
| languages | Language and framework practices |
| quality | Verification, security, performance and recovery |
| knowledge | Project memory, private knowledge work and communication |

Roles and disciplines overlap in real work. Choose one primary home and link relevant
expertise rather than maintaining copies under several categories. Keep runtime-specific
tools and permissions in exporters; a Python skill does not require a Python-only agent.

## Select by uncertainty and outcome

Start with the assignment and its quality constraints. Load the narrowest useful skill.
Use a specialist for a bounded uncertainty or deliverable; add a separate session only
when the host supports it, authorization permits it and coordination is worthwhile.

```sh
python3 tools/ai_toolkit.py catalog --kind skill --domain architecture
python3 tools/ai_toolkit.py catalog --kind agent --format markdown
```

The local catalog can filter by type, discipline and search text. Public profile URLs
and exported names remain stable even when source directories are reorganized. The
website creates profile pages and navigation from the catalog; do not add page stubs.

## Add or improve expertise

1. Inspect existing metadata and choose whether an existing skill/agent already owns
   the outcome. Improve it before adding a competing generalist.
2. Choose a discipline and a stable lowercase hyphenated name. Use the
   [skill template](../templates/catalog/skill-template.md) or
   [agent template](../templates/catalog/agent-template.md).
3. Write a concrete selection description. Specify useful inputs, actions, output and
   evidence. Give an agent its role/authority boundary; give a skill its procedure.
4. Put long examples in that skill's `references/`, or its agent domain's `references/`.
   Link focused sections from the entry. Keep private project facts in the customer workspace.
5. Run catalog/link checks, export tests and strict docs build. For consequential
   behavior, forward-test a realistic assignment, missing-tool case and small bypass.
6. Review the diff, actual observations and limitations. Version the canonical source
   through a PR; re-export deliberately into the host after integration.

Keep frontmatter to portable `name` and `description`. Existing flat agent sources and
legacy topic skill files remain readable by the loader for older catalog fixtures;
new repository contributions use the normalized domain layout. Generated exports are
deployment artifacts, not another source to edit.

## Generated indexes and exports

Refresh the GitHub entry indexes after metadata changes:

```sh
python3 tools/ai_toolkit.py catalog --kind agent --format markdown > agents/README.md
python3 tools/ai_toolkit.py catalog --kind skill --format markdown > skills/README.md
python3 tools/ai_toolkit.py check
```

The check detects stale generated indexes. Runtime adapters flatten category paths into
their native layout and rebase references. The manifest preserves human edits and removes
only verified obsolete owned files. Updating a catalog does not update an installed bundle
until it is re-exported. Perform the [host check](PORTABILITY.md#verify-a-new-host-once)
after changing host/version or effective permissions.

## Quality of the catalog itself

Judge entries by correct selection, useful output, preserved constraints and actual
verification. A count of agents or many framework names is not evidence of engineering
expertise. Remove demonstrated duplication deliberately, preserving compatibility or
documenting a migration for stable names. Avoid speculative role inflation.

See the [bounded forward observations](evaluations/catalog-restructure-20261022.md) for the current restructure and their limitations.
