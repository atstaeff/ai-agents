# Microservices Architecture

## Instructions for AI

Design and implement microservices following these principles and patterns:

## Core Principles

### Service Boundaries
- Define services around business capabilities/domains
- Each service owns its data and database
- Align with bounded contexts from DDD
- Keep services loosely coupled
- Services should be independently deployable

### Communication Patterns

**Synchronous (Request/Response):**
- REST APIs with HTTP/HTTPS
- gRPC for high-performance scenarios
- GraphQL for flexible querying
- Use for immediate response requirements

**Asynchronous (Event-Driven):**
- Message queues (RabbitMQ, Kafka, Azure Service Bus)
- Pub/Sub patterns
- Event sourcing and CQRS
- Use for eventual consistency and decoupling

### Data Management
- Database per service pattern
- Avoid shared databases across services
- Use API composition or CQRS for queries across services
- Implement saga pattern for distributed transactions
- Consider event sourcing for audit and temporal queries

## Key Patterns

### API Gateway
- Single entry point for clients
- Route requests to appropriate services
- Handle cross-cutting concerns (auth, rate limiting, logging)
- Protocol translation
- Request aggregation

### Service Discovery
- Dynamic service registration and discovery
- Use tools like Consul, Eureka, or Kubernetes DNS
- Health checks and load balancing
- Circuit breaking with Hystrix/Resilience4j

### Circuit Breaker
- Prevent cascading failures
- Fail fast when dependent service is down
- Implement fallback mechanisms
- Monitor and auto-recover

### Saga Pattern
- Manage distributed transactions
- Choreography vs Orchestration
- Compensating transactions for rollback
- Example: Order → Payment → Inventory → Shipping

### Sidecar Pattern
- Deploy helper services alongside main service
- Handle logging, monitoring, service mesh
- Examples: Envoy proxy, Dapr

### Strangler Fig
- Gradually migrate from monolith to microservices
- Route new features to microservices
- Incrementally move existing features
- Eventually "strangle" the monolith

## Design Considerations

### Service Size
- Not too big (loses microservice benefits)
- Not too small (excessive complexity)
- Team can own and maintain it
- Can be rewritten in 2-4 weeks if needed

### Resilience
- Implement retries with exponential backoff
- Use timeouts for all external calls
- Circuit breakers for cascading failure prevention
- Bulkhead pattern for resource isolation
- Graceful degradation

### Observability
- Centralized logging (ELK, Splunk)
- Distributed tracing (Jaeger, Zipkin)
- Metrics and monitoring (Prometheus, Grafana)
- Health check endpoints
- Correlation IDs for request tracking

### Security
- Service-to-service authentication
- API Gateway for external authentication
- JWT tokens or mutual TLS
- Secrets management (Vault, Key Vault)
- Network segmentation

### Deployment
- Containerization (Docker)
- Orchestration (Kubernetes, ECS, AKS)
- CI/CD pipelines per service
- Blue-green or canary deployments
- Infrastructure as Code (Terraform, ARM)

## Anti-Patterns to Avoid

❌ Distributed monolith (tightly coupled services)
❌ Shared database across services
❌ Chatty services (too many inter-service calls)
❌ Lack of proper monitoring and logging
❌ No versioning strategy for APIs
❌ Synchronous dependencies everywhere
❌ No fault tolerance mechanisms

## Migration Strategy

1. **Identify Bounded Contexts**: Use DDD to identify service boundaries
2. **Start Small**: Extract one service at a time
3. **Build Infrastructure First**: Logging, monitoring, CI/CD
4. **Use Strangler Pattern**: Gradually replace monolith
5. **Data Migration**: Strategy for moving data to new services
6. **Test Thoroughly**: Integration and end-to-end tests

## Technology Stack Considerations

**Languages**: Match service needs (Java, Go, Node.js, Python, C#)
**Communication**: REST, gRPC, message queues
**Data**: SQL, NoSQL based on service requirements
**Infrastructure**: Kubernetes, Docker, service mesh
**Monitoring**: Prometheus, Grafana, ELK stack

## Example Prompts

"Design a microservices architecture for an e-commerce platform"

"Implement service-to-service authentication with JWT"

"Create an API Gateway with rate limiting and routing"

"Design a saga pattern for order processing"

"Set up distributed tracing with correlation IDs"
