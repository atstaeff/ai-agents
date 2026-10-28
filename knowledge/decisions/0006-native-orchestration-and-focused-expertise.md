---
title: ADR-0006 Native orchestration and focused expertise
knowledge_id: ADR-0006
slug: decisions/adr-0006
status: proposed
owner: repository-owner
relations:
  relates_to: [ADR-0004, ADR-0005]
sources: []
---

# ADR-0006: Native orchestration and focused expertise

## Context

Teams need an adoption path covering product intent, implementation, evidence and durable
knowledge. The existing portable catalog has useful boundaries, but lacks native fleet
imports, focused Terraform/documentation expertise and a clear lead/specialist contract.
Some copyable templates contradict the private-planning policy.

## Options

1. Add more generalist profiles and universal prompt rules. This increases discovery and
   context without establishing actual scheduling or stronger acceptance.
2. Build a new scheduler and memory service in the local toolkit. This duplicates host
   capabilities and expands infrastructure and security responsibility.
3. Keep shared process and expertise portable; export native packages and delegate
   execution, provider configuration and permissions to adopted hosts.

## Proposed choice

Use option 3. Retain project-owned AGENTS.md navigation, assignments and knowledge homes.
Express optional product, engineering and delivery leads with one integration owner.
Give specialists bounded task packets and test the integrated result. Add focused
Terraform and technical-writing procedures while improving existing stack guidance.

Provide native packages and schema-v2 import bundles for NickGuAI/Herd, pinned to its
observed upstream schema. Name Herdr and other Herd projects separately. Actual model,
worker routing and access policies remain host configuration. Ponytail and Graphify
are opt-in native integrations; the toolkit copies neither their implementation nor their rules.

## Consequences and evidence

The default process remains usable in one session. Multiple commanders and specialties
are explicit selections. Import files contain reusable catalog data, not customer memory,
credentials or scheduled actions. Canonical Markdown remains the editable source;
Docusaurus and bounded knowledge maps remain derived views.

Safe export updates require manifest validation, coordinated writes and recovery from
partial failure. Contract tests establish generated shape and update behavior; an
installed-host exercise is still necessary before relying on live orchestration.
This record proposes the approach for review; implementation, authorized acceptance,
integration and deployment remain separate states.

## Sources

- [Orchestration contract](../../toolkit/ORCHESTRATION.md)
- [Integration guide](../../toolkit/INTEGRATIONS.md)
- [Operating model](../../toolkit/OPERATING-MODEL.md)
- [ADR-0004: Private plans and shared knowledge](0004-private-plans-shared-knowledge.md)
- [ADR-0005: Bounded knowledge views](0005-bounded-knowledge-views.md)
