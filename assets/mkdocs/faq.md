# Frequently asked questions

## Is it an OpenCode session orchestration plugin?

No. It exports native agents, skills and commands. Delegation and session interaction
come from the installed host. The dashboard manages files and does not launch agents.

## Can Plan and Build be customized?

Yes. Edit their canonical profiles and re-export. OpenCode Plan has scoped edit
permissions for work records; its shell/task tools are denied. Review the final merged
host configuration and other installed tools before relying on a read-only boundary.

## Must every task create a document?

No. Small changes use the conversation and existing checks. Larger outcomes use one
`.ai/work/` file, archived at completion. CSV is an export only.

## Does it upload my Obsidian vault?

The toolkit has no remote vault service. An AI host can read an explicitly accessible
vault using its own tools and provider configuration. Keep private notes and paths
outside this public repository.

## Do Obsidian links open from OpenCode Web?

The URI helper produces correctly encoded `obsidian://` links. Clickability depends
on the web renderer and Windows protocol registration. Copy the URI if it is filtered.

## How do I update profiles?

Update the repository and re-export to the same dedicated destination. Edited or
unmanaged files cause a clear error; integrate deliberately or choose another output.
