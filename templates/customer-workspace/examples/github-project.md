# Customer GitHub Project setup

Fictional example. Replace CUSTOMER_* URLs and accounts; setup is not applied to GitHub.

Use one Project for this customer product, including related customer repositories.
Create only Status, Iteration and Priority as custom fields. Use built-in Assignees
and Repository metadata; avoid duplicate owner or repository text fields.

Status values: Todo, In Progress, In Review, Done. Ready is an admission condition.
Blocked is an additional property with reason, owner and resume condition; keep the flow position and WIP.
Priority values: High, Normal, Low. Iteration length: two weeks in this example.

| View | Filter | Purpose |
| --- | --- | --- |
| NOW | iteration:@current | Current iteration, grouped by Status |
| REVIEWS | status:"In Review" | Outcomes awaiting review |
| BLOCKED | Existing blocking label/dependency view | Questions or dependencies needing a decision |

Start with one active issue per runner. Ready means the customer has cleared the outcome
for work; the authorized assignee decides which worker may take it.

## Project README to paste

Product: Alpenblick Services document portal, a fictional example.

- [Customer workspace](https://github.com/CUSTOMER_ORG/CUSTOMER_REPO/blob/main/workspace/README.md)
- [Working agreement](https://github.com/CUSTOMER_ORG/CUSTOMER_REPO/blob/main/workspace/working-agreement.md)
- [Stakeholders](https://github.com/CUSTOMER_ORG/CUSTOMER_REPO/blob/main/workspace/stakeholders.md)
- [Knowledge index and map](https://github.com/CUSTOMER_ORG/CUSTOMER_REPO/blob/main/workspace/knowledge-map.md)

Use NOW for the current iteration. Priority, status and iteration are maintained in this
Project. The issue contains its current plan; durable knowledge belongs to the linked workspace.

## Automation scope

Do not map every closure to delivered Done. Distinguish delivered, cancelled, duplicate
and not implemented using the actual platform capabilities. Delivery requires the agreed
evidence, required review and authorized integration at the defined completion point. Prepare a single iteration report in the
repository and link it from a Project status update. A local runner supplies the AI execution.
Keep the update to changed outcomes, material blockers and the report link. The repository
report remains the canonical closeout record. Do not create a copied report or an ADR
for every closed issue. A decision owner explicitly approves decision status changes.
