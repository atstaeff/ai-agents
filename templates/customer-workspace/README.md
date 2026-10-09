# Customer workspace template

This is a reusable starter with a fictional planning example for Alpenblick Services
and a document portal. It is stored under `templates/customer-workspace/` in AI Agents;
the paths below describe files in the customer's repository after adoption.
It contains no customer data, application implementation or running automation.
All CUSTOMER_* accounts, URLs, issue numbers, approvals and results are placeholders.
Markdown is reusable across GitHub, an AI host and an existing documentation site.

## Start with the minimum

1. Merge the relevant rules from [AGENTS.md](AGENTS.md) into the project's existing
   `AGENTS.md`; preserve local rules and review the action scope with the customer.
2. Copy and adapt [workspace/README.md](workspace/README.md),
   [working-agreement.md](workspace/working-agreement.md) and
   [stakeholders.md](workspace/stakeholders.md). Replace the fictional context and roles.
3. Configure one customer-owned GitHub Project using [the board example](examples/github-project.md).
4. Create a real issue from [the worked assignment](examples/issue-42.md).
5. Start Jörg manually with that issue in the customer's repository, using your host's
   installed AI Agents profiles. Adopt [plan comments and approval](examples/plan-review.md)
   before Build when required. Add a local runner only after the manual flow works.
6. For a documentation site, adopt [the local Docusaurus integration](examples/docusaurus-integration.md)
   and generate the knowledge index before building the existing website.

The Project owns priority, iteration and status. The issue owns the current plan and
questions. The repository owns durable knowledge. Documentation sites are generated
views of that knowledge. General agent skills stay in the toolkit; customer facts stay here.

Keep the customer's root README and existing `.github/` configuration. If useful,
copy [the issue form](.github/ISSUE_TEMPLATE/change.yml) into its issue templates and
the selected `examples/` files into an appropriate example directory. Do not overwrite
existing files; update paths if you choose different folder names. The toolkit's profile
export bundles this starter as reference material; it does not apply it to a project.

The `workspace/` name covers product context, people, working agreements and durable
knowledge. If that name already has a technical purpose in the target repository, use
`context/` and update the entry links and website content path. Keep live plans in issues;
add knowledge pages only when a decision or completed increment warrants them.
When the customer already uses Jira for product scope and capacity planning, preserve
that ownership and link engineering issues to the existing delivery object.

## One place for each kind of information

| Information | Canonical place | Update when |
| --- | --- | --- |
| Product goal and value chain | [Workspace entry](workspace/README.md) | The outcome or business context changes |
| Priority, iteration, status and assignment | Customer GitHub Project | Work is selected or changes state |
| Current plan, acceptance and open questions | Assigned GitHub issue | A material increment, question or answer changes the plan |
| Implementation and verification | Linked pull request | The change becomes reviewable or evidence changes |
| Significant decision and rationale | `workspace/decisions/` ADR | A consequential choice needs a decision |
| Current domain, architecture or operational knowledge | `workspace/knowledge/` | Accepted behavior changes |
| Iteration outcomes and open work | `workspace/iterations/` | An iteration closes |
| Knowledge index, relationships and website | Generated views | Source records change, before the site build |

Draft significant decisions during the work. The responsible human accepts or rejects
them; an accepted ADR does not imply implemented, merged or deployed code. Preserve
accepted rationale and use a new ADR to replace a substantive decision. At iteration
close, link existing ADRs and draft only missing significant decisions. Keep the closeout
report short and link it from the Project update. Every completed task does not need an ADR.

Let AI draft updates from actual issue, PR and review evidence. Ask people to resolve
consequential questions and review meaning, rather than re-entering the same status in
several files. Load only the current issue and relevant knowledge; archive history out
of routine context. The worked files stay drafts until a real project's evidence exists.

## Optional worked documents

- [Question and resumption](examples/discussion-42.md)
- [Plan comments, revision and approval](examples/plan-review.md)
- [Proposed PR](examples/pull-request-57.md)
- [Decision draft](workspace/decisions/0001-retry-safe-upload.md)
- [Dependent decision draft](workspace/decisions/0002-atomic-upload-claim.md)
- [Process knowledge draft](workspace/knowledge/upload-retries.md)
- [Iteration report draft](workspace/iterations/I1.md)
- [Local runner contract](examples/local-runner.md)
- [Docusaurus options fragment](examples/docusaurus-workspace.cjs)
- [Generated knowledge index and map](workspace/knowledge-map.md)
- [Local graph generator](examples/knowledge_graph.py)

Decision, knowledge and iteration drafts demonstrate format, not established behavior.
Create these files in a real project only when the corresponding work warrants them.
Replace placeholders and obtain actual evidence before accepting or publishing drafts.
Keep website access consistent with the customer's repository visibility.
`workspace/` holds editable Markdown; a root `docs/` used for compiled Pages output stays generated.

## References

- [GitHub Projects practices](https://docs.github.com/en/issues/planning-and-tracking-with-projects/learning-about-projects/best-practices-for-projects)
- [Project filters](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/filtering-projects)
- [Iteration fields](https://docs.github.com/en/issues/planning-and-tracking-with-projects/understanding-fields/about-iteration-fields)
- [Docusaurus content directory options](https://docusaurus.io/docs/api/plugins/@docusaurus/plugin-content-docs)
- [MADR decision format](https://adr.github.io/madr/)
