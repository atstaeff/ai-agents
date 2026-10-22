# A small project kernel

The kernel is one filled project.yaml at the repository root. It locates purpose,
responsibilities, working instructions, tools and durable knowledge. All linked document
names and folders are project choices. Several fields may point to one document.

## Complete illustrative manifest

This is a fictional GitHub project. Replace its name, addresses and source references;
the snippet describes no existing connected project and does not establish source readiness.

```yaml
schema_version: 2
project_name: Customer Portal

context:
  vision: product/overview.md#vision
  goals: product/overview.md#goals
  scope_and_boundaries: product/overview.md#scope-and-boundaries

responsibilities: team/responsibilities.md
contribution_guide: CONTRIBUTING.md
delivery_method: lean

work_tracking:
  system: github-issues
  location: https://github.com/example/customer-portal/issues

code_review:
  system: github-pull-requests
  location: https://github.com/example/customer-portal/pulls

knowledge_base:
  system: repository
  location: knowledge/

decision_records:
  system: repository
  location: architecture/decisions/

communication:
  system: work-item-comments
  location: Comments on the assigned issue or linked pull request
```

The schema version identifies the manifest format, not the product release.
`delivery_method` is optional; the contribution guide defines the actual procedure.
Only project.yaml is a fixed filename. For example, contribution_guide could instead
point to ways-of-working/development.md without changing an agent or skill.

## What the referenced documents contain

| Source | Smallest useful content |
| --- | --- |
| Vision | Intended users, problem and useful long-term change |
| Goals | Current observable outcomes, success signals and acceptance source |
| Scope and boundaries | Included responsibilities, explicit exclusions and material constraints |
| Responsibilities | Priority/acceptance owner, technical decision owner, contributor/reviewer responsibilities and conflict route |
| Contribution guide | Clarify/plan/build/verify/integrate flow, ready/done rules, required review, relevant skills and verification commands |
| Knowledge base | Current contracts, architecture and operating knowledge, maintained from evidence |
| Decision records | Significant choices, alternatives, reasons, status, owner and replacement links |

## How a team and AI use it

1. The host's agent instructions point to project.yaml. A session reads its required
   context, responsibilities and contribution guide, then the affected project sources.
2. The contribution guide selects the narrowest relevant skill: product-discovery for
   uncertain value/scope, work-management for coordination, a language/engineering skill
   for implementation, testing and pr-crafting for verification and review.
3. The assigned issue owns the live plan, acceptance, progress, feedback and handoff.
   The linked PR owns implementation and review evidence. The manifest stays stable;
   it does not become a per-session task list.
4. Each increment has an accountable owner. If several people/sessions work concurrently,
   give them bounded scopes, effective shared claims and a named integrator. A YAML entry
   alone provides no lock or delegation capability.
5. Record significant rationale at decision_records and maintain affected knowledge_base
   sources. Before a pause, save revisions, evidence/limits, blockers, pending writes
   and one next action in the same assignment. The next session verifies those sources.

Run the normal [manifest validator](../PROJECT-CONFIG.md#validate-before-adoption) in CI.
It rejects missing required fields, invalid types, conflicting conventional maps, and
missing/empty/obviously unfilled required local source sections. Review the content and
actual tool access separately. For this illustrative snippet, referenced files and remote
locations still need to be supplied by the adopting project.

Use the [lean starter](../../templates/lean-project/README.md) for small adaptable source
files, or inspect [this repository's filled manifest](../../project.yaml) as a real example.
