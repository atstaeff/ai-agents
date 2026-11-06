# Architecture decision records

Record consequential architectural choices when they arise, not only after implementation.
Start with proposed status and name the accountable decision owner. Record acceptance only
when it occurred. Link implementation and verification as evidence becomes available.

Each ADR needs a stable ID, title, status, scope, owner, context, realistic alternatives,
decision, consequences and relevant evidence. Use the catalog's architecture decision
template or an existing project format; this index contains no actual project decisions.

Maintain an index with ID/title, status, affected component/topic and record link as records
appear. Find relevant decisions by scope/status and follow links; never load all ADRs into
every session. Preserve accepted reasons. An accepted replacement links supersedes and is
linked back from the superseded record; a proposal does not replace accepted policy.

ADRs retain rationale, while [current knowledge](../knowledge/README.md) describes verified
behavior and issues/PRs retain execution history. Plain Markdown is sufficient. Optional
metadata/relations can support Docusaurus or graph views without a workspace manifest.
Keep public/private publication boundaries explicit.
