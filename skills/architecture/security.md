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
5. Reproduce and test the affected behavior. Distinguish verified findings from assumptions and prioritize by impact and likelihood.

## Completion

Return the concrete result, verification evidence and any material unresolved limitation. Keep documentation proportional to the change and preserve human feedback.

## Focused references

- [Detailed examples](references/security.md): load only the section relevant to the task.
