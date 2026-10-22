# Lean project starter

Start a small project with three maintained entry files, one current assignment and
knowledge created only when the work needs it. This is the default starter; the
[extended customer example](../customer-workspace/README.md) adds board roles, review
examples and publication options for larger coordination needs.

## Adopt in a new or existing repository

1. Inspect existing instructions, tracker, code, CI and known decisions. Reuse their
   authoritative homes. Preserve human wording and do not overwrite existing files.
2. Merge the rules from [AGENTS.md](AGENTS.md) into the project's agent entry. Adapt
   [workspace/README.md](workspace/README.md): goal, boundaries, owner and actual commands.
3. Adapt [workspace/workspace.yml](workspace/workspace.yml). Its initial local configuration
   selects an optional work record, not a real connected tracker. If Jira/GitHub already
   owns work, map that system instead; do not retain a second editable local plan.
4. Merge [.gitignore](.gitignore) into existing ignore rules. Do not copy this README,
   fictional examples or the entire toolkit into the customer's workspace.
5. Validate using the toolkit checkout's `tools/project_config.py --config` with the
   adopted config's absolute path. The validator's optional dependencies are supplied by
   `uv run --locked --group validation python` from the toolkit checkout. It validates
   structure; it does not prove tool access or execute commands.
6. Take one real authorized assignment through clarification, a short plan, build,
   meaningful checks and required acceptance/integration. Try a fresh session before
   expanding automation or parallelism.

The workspace entry initially owns the short working agreement and decision-owner map.
The YAML points both required fields there; separate stakeholder or agreement files are
unnecessary until the team needs them. Keep actual tooling locations only in YAML.

## Use it on the next assignment

Open the adopted project in your existing AI host. If it does not load `AGENTS.md`
automatically, name that entry explicitly. Use a request such as:

```text
Read AGENTS.md and the workspace entry/config. Work on [assigned issue or outcome].
Use the project's current sources, acceptance and permissions. Keep a short plan,
feedback, evidence and handoff at the existing work home. Add durable knowledge or a
significant decision only when needed. Report the result and actual remaining gaps.
```

For larger local work without an assigned tracker, the optional toolkit can create the
single record from any directory. Pass the project root, not its `workspace/` subdirectory:

```sh
python3 /path/to/ai-agents/tools/ai_toolkit.py work --workspace /path/to/project new upload-retries \
  --title "Make upload retries safe" --kind software
```

An ordinary small correction needs no record. Installing profiles or running a local
workbench is optional; the shared file convention works with the project's current host.
Use [runtime setup](../../toolkit/RUNTIMES.md) if native catalog discovery is needed.

## Add records when needed

| Need | Reuse | Suggested project home |
| --- | --- | --- |
| Capture an opportunity | [Ideas list](../knowledge/ideas.md) | Existing idea intake or `workspace/ideas.md` |
| Explain an uncertain solution or feature contract | [Concept/spec](../knowledge/concept.md) | Existing specification home or `workspace/concepts/` |
| Preserve a significant choice | [Decision](../knowledge/decision.md) | The configured decision home, initially the entry's short decision section |
| Keep implemented behavior understandable | [Current knowledge](../knowledge/current.md) | Existing docs or `workspace/knowledge/` |
| Coordinate an increment | [Compact assignment](../delivery/assignment.md) | Assigned ticket; one optional local record only without a tracker |
| Learn from a significant/repeated failure | [Incident review](../quality/incident-review.md) | Existing incident system or `workspace/incidents/` |

Create no empty folders for future work. If decisions outgrow the entry, move them to
`workspace/decisions/`, preserve IDs/links and update the YAML location in the same change.
Knowledge graphs and a documentation site are optional views of explicitly selected sources.
Ideas, concepts and incidents are not automatically included in the extended customer's
publication allowlist; review access and publication scope before adding them.

## Completion and sessions

Keep current knowledge current, accepted rationale historical, and completed plans at
their original work home. Link actual source revisions and check evidence. No document
alone proves implementation, approval or deployment. Retain reusable conclusions before
removing disposable artifacts; do not depend solely on Git history for finding current facts.

Before a session change, leave one bounded handoff in the existing assignment: result,
sources/revisions, evidence/limits, blocker, pending writes and next action. The next
session checks those sources rather than following stale instructions blindly.

See the [operating model](../../toolkit/OPERATING-MODEL.md),
[worked example](../../toolkit/examples/lean-project.md) and
[knowledge lifecycle](../../toolkit/PROJECT-KNOWLEDGE.md) for the full default.
