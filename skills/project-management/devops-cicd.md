# DevOps and CI/CD

## Instructions for AI

Implement DevOps practices and CI/CD pipelines for efficient software delivery:

## DevOps Culture

### Core Principles

**Collaboration**
- Break down silos between Dev and Ops
- Shared responsibility for quality and reliability
- Cross-functional teams
- Blameless post-mortems

**Automation**
- Automate repetitive tasks
- Infrastructure as Code
- Automated testing and deployment
- Self-service capabilities

**Continuous Improvement**
- Measure everything
- Iterate and optimize
- Learn from failures
- Experiment and innovate

**Customer Focus**
- Deliver value frequently
- Fast feedback loops
- Respond to user needs quickly
- Monitor user experience

## CI/CD Pipeline

### Continuous Integration (CI)

**Build Stage**
- Triggered by code commit
- Compile/build application
- Restore dependencies
- Fast feedback (< 10 minutes)

**Test Stage**
- Unit tests
- Integration tests
- Code quality checks (linting, static analysis)
- Security scanning
- Fail fast on issues

**Artifact Stage**
- Create deployable artifacts
- Docker images, binaries, packages
- Version and tag artifacts
- Store in artifact repository

### Continuous Delivery (CD)

**Deploy to Staging**
- Automated deployment to staging environment
- Run automated tests (E2E, performance)
- Manual approval gate (optional)
- Smoke tests

**Deploy to Production**
- Automated or manual deployment
- Deployment strategies (blue-green, canary)
- Automated rollback on failure
- Health checks and monitoring

### Pipeline Best Practices

**Fast Feedback**
- Run fastest tests first
- Parallel execution where possible
- Fail fast on errors
- Clear error messages

**Idempotent Deployments**
- Running pipeline multiple times produces same result
- No manual steps required
- Automated rollback capability

**Environment Parity**
- Dev, staging, production as similar as possible
- Same configuration management
- Same deployment process
- Infrastructure as Code

**Pipeline as Code**
- Version control pipeline definitions
- Jenkinsfile, .gitlab-ci.yml, GitHub Actions workflows
- Review changes to pipeline
- Reusable pipeline components

## Infrastructure as Code (IaC)

### Benefits
- Version controlled infrastructure
- Reproducible environments
- Documentation as code
- Disaster recovery
- Consistent deployments

### Tools

**Terraform**
- Multi-cloud support
- Declarative configuration
- State management
- Modules for reusability

**Ansible**
- Configuration management
- Agentless (SSH-based)
- Playbooks for automation
- Idempotent operations

**CloudFormation / ARM Templates**
- Cloud-specific IaC
- Native integration
- Stack-based management

**Pulumi**
- Use programming languages (TypeScript, Python, Go)
- Rich type system
- Modern development workflow

### Best Practices
- Store in version control
- Review infrastructure changes
- Use modules/reusable components
- Separate environments (workspaces/folders)
- Plan before apply
- Automate through CI/CD

## Configuration Management

### Approaches

**Environment Variables**
- 12-factor app principle
- Different values per environment
- No secrets in code
- Injected at runtime

**Configuration Files**
- appsettings.json, config.yaml
- Environment-specific overrides
- Not for secrets
- Version controlled (except secrets)

**Secrets Management**
- HashiCorp Vault
- AWS Secrets Manager
- Azure Key Vault
- Never in source code

**Feature Flags**
- Toggle features without deployment
- A/B testing
- Gradual rollout
- Quick rollback
- Tools: LaunchDarkly, Split.io

## Deployment Strategies

### Rolling Deployment
- Gradually replace instances
- No downtime
- Slower rollout
- Easy rollback

### Blue-Green Deployment
- Two identical environments
- Switch traffic to new version
- Instant rollback (switch back)
- Requires double resources

### Canary Deployment
- Deploy to small subset of users
- Monitor metrics
- Gradually increase percentage
- Rollback if issues detected

### A/B Testing
- Deploy two versions simultaneously
- Different features/implementations
- Measure user behavior
- Data-driven decisions

## Monitoring and Observability

### Application Monitoring

**Metrics**
- Response time, throughput, error rate
- Resource utilization (CPU, memory)
- Custom business metrics
- Aggregation and visualization

**Logging**
- Centralized logging (ELK, Splunk)
- Structured logging (JSON)
- Log levels (DEBUG, INFO, WARN, ERROR)
- Correlation IDs

**Tracing**
- Distributed tracing (Jaeger, Zipkin)
- Request flow across services
- Performance bottlenecks
- Service dependencies

**Alerting**
- Proactive notification of issues
- Actionable alerts only
- Multiple channels (email, Slack, PagerDuty)
- Escalation policies
- Alert fatigue prevention

### Infrastructure Monitoring

**System Metrics**
- CPU, memory, disk, network
- Container/pod metrics
- Database performance
- Load balancer health

**Uptime Monitoring**
- External health checks
- SLA monitoring
- Availability metrics
- Multi-region checks

### SRE Practices

**SLIs (Service Level Indicators)**
- Quantitative measures of service
- Example: Request latency, error rate, availability

**SLOs (Service Level Objectives)**
- Target values for SLIs
- Example: 99.9% availability, <100ms p95 latency

**SLAs (Service Level Agreements)**
- Formal commitments to customers
- Penalties for not meeting
- Based on SLOs

**Error Budgets**
- Acceptable amount of unreliability
- Balance velocity with reliability
- 99.9% SLO = 0.1% error budget
- Use budget for experiments

## GitOps

### Principles
- Git as single source of truth
- Declarative infrastructure and apps
- Automated synchronization
- Pull-based deployment

### Tools
- ArgoCD (Kubernetes)
- Flux (Kubernetes)
- Jenkins X
- GitLab with Kubernetes integration

### Benefits
- Audit trail in Git history
- Easy rollback (git revert)
- Consistency between environments
- Self-healing systems

## Security in DevOps (DevSecOps)

### Shift Left Security
- Security early in development
- Automated security scanning
- Developer security training
- Security as code

### Security Practices

**Static Analysis (SAST)**
- Scan code for vulnerabilities
- Early in CI pipeline
- Tools: SonarQube, Checkmarx

**Dynamic Analysis (DAST)**
- Test running application
- Find runtime vulnerabilities
- Tools: OWASP ZAP, Burp Suite

**Dependency Scanning**
- Check for vulnerable dependencies
- Automated updates (Dependabot)
- Fail build on critical issues

**Container Scanning**
- Scan Docker images
- Check base images
- Tools: Trivy, Clair, Snyk

**Secrets Scanning**
- Detect secrets in code
- Pre-commit hooks
- Tools: git-secrets, truffleHog

## Testing Automation

### Test Levels
- Unit tests (70%)
- Integration tests (20%)
- E2E tests (10%)

### Test Automation Strategy
- Run in CI pipeline
- Parallel execution
- Test data management
- Environment provisioning
- Reporting and analytics

### Performance Testing
- Load testing (JMeter, Gatling)
- Stress testing
- Soak testing
- Spike testing
- Run in CI for baseline

## Metrics and KPIs

### DORA Metrics

**Deployment Frequency**
- How often deployments to production
- High performers: Multiple times per day

**Lead Time for Changes**
- Time from commit to production
- High performers: < 1 day

**Mean Time to Recovery (MTTR)**
- Time to restore service after incident
- High performers: < 1 hour

**Change Failure Rate**
- % of changes causing failure
- High performers: 0-15%

### Other Metrics
- Build success rate
- Test pass rate
- Code coverage
- Deployment success rate
- Incident frequency

## Example Prompts

"Design a CI/CD pipeline for a Node.js microservice"

"Create a Terraform configuration for a three-tier web application"

"Set up monitoring and alerting for a production API"

"Implement a blue-green deployment strategy"

"Write a Jenkinsfile for building and testing a Java application"

"Design a security scanning process for CI/CD pipeline"

"Create runbooks for common production incidents"
