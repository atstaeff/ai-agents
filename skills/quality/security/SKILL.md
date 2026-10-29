---
name: "security"
description: "Review a concrete trust boundary, authentication, authorization, secret handling or vulnerability fix."
---

# Security

## Workflow

1. Identify assets, actors, trust boundaries and plausible abuse cases proportional to the application.
2. Enforce authorization server-side at the resource boundary; validate input, encode output and use parameterized data access.
3. Use established cryptographic and authentication libraries. Keep secrets and personal data out of commits, logs and fixtures.
4. For browser-accessible local services, consider origin checks, DNS rebinding, CSRF, path traversal and unintended network exposure.
5. Return prioritized findings with location, preconditions, impact, evidence and a minimal remedy. Exercise allowed and denied behavior within authorized scope; label static hypotheses and unavailable environment checks.

## Focused references

- [Detailed examples](references/security.md): load only the section relevant to the task.
