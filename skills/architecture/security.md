# Security Best Practices

## Instructions for AI

Implement comprehensive security measures following industry standards:

## Security Principles

### Defense in Depth
- Multiple layers of security
- No single point of failure
- Assume breach mentality
- Reduce blast radius

### Least Privilege
- Minimum necessary access
- Time-limited permissions
- Regular access reviews
- Just-in-time access

### Zero Trust
- Never trust, always verify
- Verify identity and device
- Micro-segmentation
- Continuous monitoring

### Security by Design
- Consider security from start
- Threat modeling
- Secure defaults
- Fail securely

## OWASP Top 10

### A01: Broken Access Control
**Risk:** Unauthorized access to resources

**Prevention:**
- Implement proper authorization checks
- Deny by default
- Validate permissions server-side
- Use framework security features
- Log access control failures

### A02: Cryptographic Failures
**Risk:** Sensitive data exposure

**Prevention:**
- Encrypt data at rest and in transit
- Use TLS 1.2+ for transport
- Strong encryption algorithms (AES-256)
- Proper key management
- Don't store unnecessary sensitive data

### A03: Injection
**Risk:** SQL injection, command injection, LDAP injection

**Prevention:**
- Use parameterized queries/prepared statements
- ORM frameworks
- Input validation and sanitization
- Whitelist allowed values
- Least privilege database accounts

**Example (SQL Injection Prevention):**
```csharp
// ❌ Vulnerable
string query = $"SELECT * FROM Users WHERE Id = {userId}";

// ✅ Secure
string query = "SELECT * FROM Users WHERE Id = @UserId";
command.Parameters.AddWithValue("@UserId", userId);
```

### A04: Insecure Design
**Risk:** Architectural flaws

**Prevention:**
- Threat modeling in design phase
- Security architecture review
- Secure design patterns
- Security requirements
- Defense in depth

### A05: Security Misconfiguration
**Risk:** Unnecessary features, default credentials

**Prevention:**
- Minimal platform installations
- Remove unused features/accounts
- Secure defaults
- Regular security updates
- Configuration management

### A06: Vulnerable Components
**Risk:** Using components with known vulnerabilities

**Prevention:**
- Inventory dependencies
- Regular updates
- Monitor security advisories
- Automated dependency scanning
- Remove unused dependencies

### A07: Authentication Failures
**Risk:** Weak authentication

**Prevention:**
- Multi-factor authentication (MFA)
- Strong password policies
- Account lockout mechanisms
- No default credentials
- Secure session management
- Rate limiting on login

### A08: Software and Data Integrity Failures
**Risk:** Insecure CI/CD, unsigned updates

**Prevention:**
- Digital signatures for code
- Verify integrity of dependencies
- Secure CI/CD pipeline
- Code signing
- Review code changes

### A09: Logging & Monitoring Failures
**Risk:** Delayed breach detection

**Prevention:**
- Log security events
- Centralized logging
- Alerting on suspicious activity
- Regular log reviews
- Tamper-proof logs
- Incident response plan

### A10: Server-Side Request Forgery (SSRF)
**Risk:** Application fetches remote resources without validation

**Prevention:**
- Validate and sanitize URLs
- Whitelist allowed domains
- Disable HTTP redirections
- Use network segmentation
- Don't return raw responses

## Authentication & Authorization

### Authentication Best Practices
- Use industry-standard protocols (OAuth 2.0, OpenID Connect)
- Implement MFA
- Secure password storage (bcrypt, Argon2)
- Account lockout after failed attempts
- Password reset security
- Session timeout

### JWT Security
```javascript
// Good practices:
- Short expiration (15-30 minutes)
- Refresh token pattern
- Verify signature server-side
- Don't store sensitive data in payload
- Use HTTPS only
- Proper key management
```

### Authorization Patterns
- **RBAC** (Role-Based Access Control): Permissions via roles
- **ABAC** (Attribute-Based Access Control): Policy-based
- **ACL** (Access Control Lists): Per-resource permissions

## Secure Coding Practices

### Input Validation
```javascript
// Whitelist approach
const allowedFields = ['name', 'email', 'age'];
const sanitized = pick(input, allowedFields);

// Validation
if (!validator.isEmail(email)) {
  throw new ValidationError('Invalid email');
}
```

### Output Encoding
- HTML encoding for web output
- URL encoding for URLs
- JSON encoding for APIs
- Context-specific encoding

### Secrets Management
- Never commit secrets to git
- Use secret management tools (Vault, AWS Secrets Manager)
- Environment variables for configuration
- Rotate secrets regularly
- Encrypt secrets at rest

### Error Handling
```javascript
// ❌ Exposes internal details
catch (error) {
  res.status(500).send(error.stack);
}

// ✅ Generic error message
catch (error) {
  logger.error('Database error', error);
  res.status(500).send('Internal server error');
}
```

## API Security

### Rate Limiting
- Prevent brute force attacks
- Protect against DoS
- Per user/IP limits
- Different limits per endpoint

### CORS Configuration
```javascript
// ❌ Insecure
Access-Control-Allow-Origin: *

// ✅ Specific origins
Access-Control-Allow-Origin: https://trusted-domain.com
```

### API Keys
- Don't pass in URL
- Use headers (Authorization: Bearer)
- Rotate regularly
- Scope to minimal permissions
- Monitor usage

## Database Security

### Practices
- Principle of least privilege
- Separate accounts for read/write
- Encrypt sensitive fields
- Regular backups (encrypted)
- Audit trail for changes
- Network isolation

### SQL Injection Prevention
```python
# ❌ Vulnerable
cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")

# ✅ Parameterized
cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
```

## Cloud Security

### AWS
- IAM roles, not access keys
- Enable MFA
- CloudTrail for audit logs
- Security groups (least privilege)
- Encrypt EBS volumes and S3 buckets
- VPC for network isolation

### Azure
- Managed identities
- Azure AD for authentication
- Key Vault for secrets
- Network Security Groups
- Azure Security Center

### GCP
- Service accounts with minimal permissions
- Cloud IAM
- VPC Service Controls
- Security Command Center

## Container Security

### Docker
- Use minimal base images (Alpine)
- Don't run as root
- Scan images for vulnerabilities
- Multi-stage builds
- Sign images
- Regularly update base images

### Kubernetes
- RBAC for access control
- Network policies
- Pod Security Policies
- Secrets management
- Regular updates
- Runtime security (Falco)

## Compliance & Standards

### Common Standards
- **PCI DSS**: Payment card data
- **HIPAA**: Healthcare data (US)
- **GDPR**: Privacy (EU)
- **SOC 2**: Service organization controls
- **ISO 27001**: Information security management

### Compliance Practices
- Data classification
- Privacy by design
- Data retention policies
- Right to deletion
- Breach notification procedures
- Regular audits

## Security Testing

### Types
- **SAST** (Static): Analyze source code
- **DAST** (Dynamic): Test running application
- **IAST** (Interactive): Combine SAST and DAST
- **SCA** (Software Composition): Dependency vulnerabilities
- **Penetration Testing**: Simulated attacks

### Tools
- SonarQube, Checkmarx (SAST)
- OWASP ZAP, Burp Suite (DAST)
- Snyk, WhiteSource (SCA)
- Nessus, Qualys (Vulnerability scanning)

## Incident Response

### Preparation
- Incident response plan
- Define roles and responsibilities
- Contact lists
- Communication templates
- Runbooks for common scenarios

### Detection & Analysis
- Monitor security logs
- SIEM (Security Information and Event Management)
- Alert triage
- Determine scope and impact

### Containment & Recovery
- Isolate affected systems
- Preserve evidence
- Apply fixes
- Restore from backups
- Verify security

### Post-Incident
- Root cause analysis
- Document lessons learned
- Update security measures
- Train team
- Improve detection

## Security Checklist

✅ Authentication and authorization implemented
✅ Input validation on all endpoints
✅ Output encoding for context
✅ SQL injection prevention
✅ XSS prevention
✅ CSRF protection
✅ Secure session management
✅ HTTPS everywhere
✅ Security headers configured
✅ Secrets not in code
✅ Dependencies regularly updated
✅ Security logging enabled
✅ Regular security testing
✅ Incident response plan
✅ Access control reviewed regularly

## Example Prompts

"Review this code for security vulnerabilities"

"Implement input validation for this API endpoint"

"Design an authentication system with MFA"

"Create a secrets management strategy"

"Set up security headers for a web application"

"Implement rate limiting to prevent brute force"

"Design an incident response plan for a data breach"
