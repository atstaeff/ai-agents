---
title: ADR-0008 Local runtime services
knowledge_id: ADR-0008
slug: decisions/adr-0008
status: proposed
owner: repository-owner
relations:
  relates_to:
    - ADR-0006
    - ADR-0007
---

# ADR-0008: Local runtime services

## Context

The tools should remain available on the developer's Linux or WSL machine without
keeping a terminal open. Project procedure and authorized assignments remain in
their Markdown and tracker sources.

## Options and proposed decision

Use two native user services managed by systemd. The CLI generates one named
Herdr session and one loopback OpenCode endpoint per project. A shared target
manages their lifecycle; independent restart limits handle repeated failures.
Use the existing host configuration and keep provider credentials out of the units.

A detached shell script would need its own process ownership, stale PID cleanup
and restart behavior. A central scheduler would add a second source of assignments.
The native service manager already owns startup, restart, status and logs.

## Consequences

This requires a running Linux user manager and supported installed binaries.
WSL distribution lifecycle is separate. An active service does not authorize a model
turn or imply restored agent state. Stop or uninstall only the project's managed
units and keep shared knowledge at its project source.

The [runtime guide](../../scripts/README.md) describes setup and rollback.
This record proposes the source change; it is not evidence of installation on a
developer machine or acceptance by the repository owner.
