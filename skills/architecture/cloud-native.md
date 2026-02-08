# Cloud-Native Architecture

## Instructions for AI

Design applications optimized for cloud environments following these principles:

## Core Principles

### 12-Factor App Methodology

1. **Codebase**: One codebase tracked in version control, many deploys
2. **Dependencies**: Explicitly declare and isolate dependencies
3. **Config**: Store config in environment variables
4. **Backing Services**: Treat as attached resources
5. **Build, Release, Run**: Strictly separate stages
6. **Processes**: Execute as stateless processes
7. **Port Binding**: Export services via port binding
8. **Concurrency**: Scale out via process model
9. **Disposability**: Fast startup and graceful shutdown
10. **Dev/Prod Parity**: Keep development and production similar
11. **Logs**: Treat logs as event streams
12. **Admin Processes**: Run as one-off processes

### Cloud Design Patterns

#### Scalability Patterns

**Auto-Scaling**
- Scale horizontally based on metrics (CPU, memory, requests)
- Use cloud provider auto-scaling (AWS Auto Scaling, Azure VMSS)
- Scale services independently
- Design for elastic scale-out and scale-in

**Load Balancing**
- Distribute traffic across instances
- Health checks and automatic removal of unhealthy instances
- Multiple levels: external, internal, service mesh
- Session affinity when needed

**Queue-Based Load Leveling**
- Use message queues to smooth out load spikes
- Decouple producers from consumers
- Process messages asynchronously at steady rate
- Prevent service overload

**Throttling**
- Limit resource consumption per user/tenant
- Prevent resource exhaustion
- Graceful degradation under high load
- Return 429 (Too Many Requests) when exceeded

#### Resilience Patterns

**Circuit Breaker**
- Detect failures and prevent cascading
- Fail fast instead of waiting for timeout
- Automatic recovery attempts
- Fallback mechanisms

**Retry Pattern**
- Transient fault handling
- Exponential backoff
- Maximum retry attempts
- Idempotent operations

**Bulkhead**
- Isolate resources for different workloads
- Prevent one failing component from taking down entire system
- Separate thread pools, connection pools
- Example: Critical vs non-critical operations

**Health Endpoint Monitoring**
- Expose health check endpoints
- Monitor service availability
- Automated remediation (restart, replace)
- Detailed health status (dependencies, database)

#### Data Patterns

**Database per Service**
- Each microservice owns its data
- Prevents tight coupling
- Allows independent scaling
- Choose appropriate database type per service

**CQRS (Command Query Responsibility Segregation)**
- Separate read and write models
- Optimize reads and writes independently
- Use different data stores
- Handle eventual consistency

**Event Sourcing**
- Store events instead of current state
- Replay events to rebuild state
- Complete audit trail
- Enables temporal queries

**Cache-Aside**
- Application manages cache
- Load from cache if present
- Load from database and cache if not
- Set expiration policies

**Sharding**
- Partition data across multiple databases
- Distribute load
- Scale beyond single database limits
- Consider shard key carefully

#### Messaging Patterns

**Publisher/Subscriber**
- Decouple producers from consumers
- Multiple subscribers per message
- Topics and subscriptions
- Filter messages at subscription level

**Competing Consumers**
- Multiple consumers process from same queue
- Parallel processing
- Load distribution
- Idempotent message handling

**Priority Queue**
- Process high-priority messages first
- Separate queues by priority
- Ensure critical operations complete quickly

## Cloud-Native Technologies

### Containerization
- Docker for packaging applications
- Container images with all dependencies
- Immutable deployments
- Fast startup times

### Container Orchestration
- **Kubernetes**: Industry standard
  - Pods, Deployments, Services
  - ConfigMaps and Secrets
  - Horizontal Pod Autoscaler
  - Ingress controllers
- **Docker Swarm**: Simpler alternative
- **Cloud-specific**: ECS, AKS, GKE

### Service Mesh
- **Istio**, **Linkerd**, **Consul Connect**
- Service-to-service communication
- Traffic management and routing
- Security (mTLS)
- Observability (tracing, metrics)

### Serverless/Functions
- AWS Lambda, Azure Functions, Google Cloud Functions
- Event-driven execution
- Pay per execution
- Auto-scaling
- Suitable for event processing, webhooks, scheduled tasks

## Infrastructure as Code (IaC)

### Tools
- **Terraform**: Multi-cloud, declarative
- **AWS CloudFormation**: AWS-specific
- **Azure ARM Templates/Bicep**: Azure-specific
- **Pulumi**: Code-based (TypeScript, Python, Go)

### Best Practices
- Version control infrastructure code
- Separate environments (dev, staging, prod)
- Use modules for reusability
- Implement proper state management
- Apply infrastructure through CI/CD

## Observability

### Three Pillars

**Logging**
- Centralized logging (ELK, Splunk, CloudWatch)
- Structured logging (JSON format)
- Correlation IDs across services
- Different log levels (DEBUG, INFO, WARN, ERROR)

**Metrics**
- Application metrics (Prometheus, CloudWatch)
- Infrastructure metrics
- Business metrics
- RED method: Rate, Errors, Duration
- USE method: Utilization, Saturation, Errors

**Tracing**
- Distributed tracing (Jaeger, Zipkin, X-Ray)
- Track requests across services
- Identify bottlenecks
- Understand dependencies

### Monitoring & Alerting
- Set up dashboards (Grafana, CloudWatch)
- Define SLIs, SLOs, SLAs
- Alert on actionable issues
- Avoid alert fatigue
- Runbooks for common issues

## Security in Cloud

### Identity & Access Management
- Principle of least privilege
- Use IAM roles, not access keys
- Service accounts for applications
- Multi-factor authentication
- Regular access reviews

### Network Security
- Virtual Private Cloud (VPC)
- Security groups and network ACLs
- Private subnets for backend services
- VPN or Direct Connect for hybrid
- WAF for web applications

### Data Security
- Encryption at rest and in transit
- Key management (AWS KMS, Azure Key Vault)
- Secrets management (HashiCorp Vault)
- Data classification and compliance
- Backup and disaster recovery

### Security Best Practices
- Regular security audits
- Vulnerability scanning
- Penetration testing
- Security monitoring and SIEM
- Incident response plan

## CI/CD for Cloud-Native

### Pipeline Stages
1. **Source**: Git trigger
2. **Build**: Compile, run unit tests
3. **Test**: Integration and E2E tests
4. **Package**: Create container image
5. **Deploy**: Deploy to environment
6. **Monitor**: Health checks and metrics

### Deployment Strategies
- **Rolling Update**: Gradual replacement
- **Blue-Green**: Switch between environments
- **Canary**: Test with small percentage
- **A/B Testing**: Compare versions

### Tools
- Jenkins, GitLab CI, GitHub Actions
- AWS CodePipeline, Azure DevOps
- ArgoCD, Flux for GitOps
- Spinnaker for multi-cloud

## Cost Optimization

- Right-size resources
- Use auto-scaling
- Leverage spot/preemptible instances
- Reserved instances for stable workloads
- Optimize storage (lifecycle policies)
- Monitor and analyze costs regularly
- Use cost allocation tags

## Example Prompts

"Design a cloud-native architecture for a SaaS application"

"Implement auto-scaling with health checks for a microservice"

"Set up distributed tracing with correlation IDs"

"Create infrastructure as code for a multi-tier application"

"Design a resilient system with circuit breakers and retries"

"Implement CQRS pattern with separate read/write databases"
