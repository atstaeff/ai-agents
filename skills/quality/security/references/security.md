# Focused security review

Use the section that matches a concrete trust boundary. Project policy and the affected
product determine required controls; this reference is not a certification checklist.

## Frame the finding

Identify the asset, attacker capability, entry point and unauthorized effect. Trace a
plausible path in the current revision. Return location, preconditions, impact, evidence
and a minimal repair; label an untested hypothesis separately from a reproduced defect.

## Identity and resource authorization

Use the established authentication library and token/session profile. Verify identity
and permission for the requested resource and action on the server, including tenant
scope. A valid login, role name or hidden UI button does not authorize every resource.
Test another user's identifier, a denied action and absent/expired credentials.

For JWT access tokens, verify the signature using configured trusted keys and allowed
algorithms. Validate required issuer, audience and time claims for the actual token
profile, and reject malformed/missing claims. Define key rotation and revoked/disabled
identity behavior. Do not copy a partial decode snippet as a complete auth system.
See [OWASP REST security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html).

For browser sessions, check cookie attributes, session lifetime and state-changing
request protection. CORS controls browser response access; it does not authenticate a
caller or replace CSRF protection. Match allowed origins and credential handling to the
actual client. Keep session/token contents out of URLs, logs and error messages.

## Input, output and resource access

- Validate type, size, range and business constraints at the relevant boundary. Keep
  validation distinct from context-specific output encoding; HTML-escaping stored data
  is not a universal injection defense.
- Parameterize data queries. Pass structured arguments to subprocess tools rather than
  building shell commands from untrusted strings. A library or ORM does not make its
  raw query/command escape hatches safe.
- Render user content as text or use the product's trusted sanitizer for permitted
  markup. Use context-appropriate encoding for HTML, URL and script boundaries.
- For files, constrain the resolved path and allowed operation. Check traversal,
  symlinks where relevant, collisions, upload size/type and archive expansion limits.
- For outbound fetches, review allowed destinations, schemes, redirects, DNS resolution
  and network egress controls. Validate each effective destination; a hostname string
  check alone does not establish protection against SSRF.
- Bound expensive requests, queues and retained data. Verify the failure response and
  isolation between callers; do not present a rate limiter as complete denial-of-service protection.

## Local browser-accessible services

Binding to loopback reduces exposure but does not make browser-originated input
trusted. Check Host/Origin handling, DNS rebinding, state-changing requests, websocket
origins and file access against the product's actual trust model. Verify denied-origin
and unintended-network-access cases when those boundaries are affected.

## Secrets, dependencies and deployment

Keep secrets in the established secret mechanism with scoped access and rotation.
Inspect log/error/artifact paths and CI trust boundaries; untrusted contributions must
not run with release credentials. Lock and review dependencies according to project
policy, check relevant advisories and verify the deployed artifact's source identity.
Never infer absence of vulnerabilities from a clean scanner result.

Use [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html),
[SSRF guidance](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)
and the affected framework's official security documentation for the specific control.
Verify current standards or advisory details when they affect the assignment rather
than keeping an undated Top 10 list or fixed cryptographic parameters here.

## Evidence and limits

Exercise the allowed path and the plausible denied/abuse path within authorized scope.
Without the application, identity provider or test environment, return a static finding
or proposed reproduction and name that limit. Do not claim exploitation, remediation,
compliance or production verification that did not occur. Use
[incident response](../../incident-response/SKILL.md) for an active exposure or outage.
