---
title: Customer workspace
description: Business purpose and entry points for the document portal example.
---

# Alpenblick Services document portal

Fictional customer example. CUSTOMER_* URLs are placeholders.

## Outcome and value chain

Service staff need one reliable document reference for each upload attempt, including retries.
The business flow is document intake, validation, processing, case assignment and a staff decision.
Technical success supports the business goal: fewer duplicate cases and less manual cleanup.

Success for the worked increment means a retry reuses the same document reference;
a deliberate new upload can still create a separate document. Production impact needs
customer measurements; this example provides no measured business result.

## Working entry points

- [Customer GitHub Project](https://github.com/orgs/CUSTOMER_ORG/projects/1): priority and iteration.
- [Working agreement](working-agreement.md): delivery, acceptance and communication rules.
- [Stakeholders](stakeholders.md): who decides and reviews.
- [Upload process draft](knowledge/upload-retries.md): relevant domain knowledge.
- [Decision draft ADR-0001](decisions/0001-retry-safe-upload.md): rationale and alternatives.
- [Dependent decision draft ADR-0002](decisions/0002-atomic-upload-claim.md): concurrency and recovery.
- [Iteration I1 draft](iterations/I1.md): concise outcome report.
- [Knowledge map](knowledge-map.md): generated index, statuses and explicit relationships.

Keep the current project goal here. Keep each live plan in its GitHub issue.
Load individual decision and process documents only when relevant.
The docs website reads this directory as source. A reserved compiled `docs/` directory
contains generated output and is rebuilt from these files; AI work uses the Markdown sources.
