# Work with AI as a teammate

Start from `AGENTS.md`, implement a small complete change, verify it, and preserve the
knowledge needed to maintain the result. People own priorities and consequential choices.
Agents are optional roles; skills are reusable procedures, loaded only when useful.

## Keep three kinds of information separate

| Information | Home | Shared with the team? |
| --- | --- | --- |
| Personal working plan, experiments and resume notes | The user's private Second Brain project folder | No, unless collaboration requires it |
| Scope, acceptance, assignment and review feedback | Existing issue/ticket and PR | Yes |
| Implemented behavior, relevant decisions and operating knowledge | Project code, ADRs and documentation | Yes |

The team needs the result and its rationale. Do not copy a private plan into an issue,
PR or repository simply to complete a process. A shared execution plan is appropriate
when several contributors actually depend on its steps; agree one home for that plan.
Customer restrictions still determine whether any project material may enter a personal vault.

## The delivery loop

1. **Understand.** Read the request, applicable rules, relevant code and decisions.
   Define observable acceptance. A clear small fix can proceed directly.
2. **Plan when useful.** Keep one personal plan in the configured Second Brain. Capture
   the outcome, next steps and verification. Obtain plan review only when the user or
   project actually requires it; share only the necessary review extract.
3. **Build and check.** Reuse the stack, make the smallest complete change and exercise
   relevant behavior and failure cases. Record actual results in the change/PR.
4. **Preserve and finish.** Update affected project knowledge. Record significant
   decisions with context, alternatives and consequences; a routine edit needs no ADR.
   Close the personal plan when verified. Review, merge and deployment remain distinct.

See the [working contract](WORKFLOW.md) for execution and [quality standard](QUALITY-STANDARD.md)
for selecting checks. Use [the worked assignment](../templates/customer-workspace/examples/issue-42.md)
as a fictional team-delivery example; its shared plan is optional for personal execution.

## Minimal project setup

A short `AGENTS.md` names the outcome/scope, owners, process, code and knowledge homes,
commands and existing review policy. Link real Markdown documents or authoritative URLs,
including Docusaurus pages. Load a linked page when it is relevant; links do not imply
that a host reads every page automatically. Use local source Markdown while editing.
No mandatory `workspace/`, YAML manifest, extra tracker or agent team is needed.
Choose one of the [instruction templates](../templates/agent-instructions/README.md).

## Continue and scale

Resume personal work from its private plan plus current code and decisions. A teammate
continues from the issue, PR, code and shared knowledge; the private plan is not a dependency.
Save only current progress, tested revision, blockers and one next action. Follow the
[recovery guide](CONTEXT-RECOVERY.md) for an interrupted change.

Start with one session. Add a specialist or independent review only when the task and
host justify it. Keep writers separate and verify integrated changes. Multiple tools
or agents do not require multiple task lists.

Docusaurus and a knowledge graph are derived views of selected shared Markdown. The
[runnable demo](../examples/engineering-demo/README.md) links decisions, components and
AI topics without importing personal plans. The legacy local [work record](WORK-RECORDS.md)
remains available by explicit choice; it is not a required step.
