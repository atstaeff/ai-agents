# Shared working contract

Use this contract across projects. Project instructions contain only local constraints,
paths and verification commands. The current user's request and host instructions take
precedence. Keep documentation proportional to the work.

## Start from an outcome

Inspect the relevant project, instructions and current work before changing files. Reuse
existing technology. For new Python work prefer dataclasses, explicit validation, uv and
unittest; use Typer when a richer CLI justifies the dependency. For a modest new web
interface consider HTML, Flask/Jinja or HTMX. Do not migrate an established stack merely
to match these preferences.

A small edit needs no process file. For larger work create one
`.ai/work/<slug>.md` using the [work template](../templates/work-item.md). It holds the
goal, acceptance criteria, plan, tasks, feedback, decisions and evidence. Keep `docs/`
available for its existing purpose, including GitHub Pages.

## Plan, implement, verify

1. Define observable acceptance criteria and a short plan. Resolve routine reversible
   choices independently. Ask only for missing information that changes a consequential
   decision or for authorization the current request does not provide.
2. Select a few relevant skills from catalog metadata. Read their instructions and load
   deeper references only when needed. Jörg routes general work to the appropriate
   expertise; a profile does not create tools or account access.
3. Implement the smallest complete increment. Use native delegation only when the host
   supports it and its instructions authorize it. Give a specialist a bounded goal,
   context, allowed files, acceptance criteria and expected evidence. Avoid concurrent
   writers to the same file.
4. Run proportionate checks that verify behavior and important failure cases. Fix
   failures within scope and record actual results. Do not label an unrun test as passed
   or repeat broad testing without a new reason.
5. Update task states and preserve human comments verbatim. A completed task needs
   evidence. Resolve feedback explicitly and keep consequential decisions with their
   reasons in the same record.
6. Give the user the result, relevant pointers, verification and material limits. Keep
   summaries concise. Never invent successful handoffs, background jobs or publication.

## Finish without a documentation burden

Archive a completed record in `.ai/archive/` after checking acceptance criteria and
unresolved feedback. Extract only reusable knowledge to an existing appropriate
documentation location or the private Obsidian vault. Link rather than duplicate.
CSV is an optional generated task export, not another source of truth.

Keep archives out of routine context loading. Repository owners choose whether work
records are committed; private data never belongs in public repositories. Keep secrets,
vault paths and personal notes in local configuration. Sending messages, publishing,
merging and destructive reorganization require authorization appropriate to the action.

## PARA knowledge

Use Projects for finite outcomes, Areas for ongoing responsibilities, Resources for
reusable knowledge and Archive for inactive material. Follow the vault's existing
folder names and note conventions. Preserve note properties, aliases, backlinks and
original human wording. A filesystem move needs explicit link verification.
