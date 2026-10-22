# Event-Driven Python

> Referenz-Patterns fuer event-getriebene Python-Architekturen auf Google Cloud Platform.

---

## Architektur

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   API        │────▶│  Pub/Sub    │────▶│  Workers    │
│  (Cloud Run) │     │  Topics     │     │ (Cloud Func)│
└─────────────┘     └─────────────┘     └─────────────┘
       │                   │                    │
       ▼                   ▼                    ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Cloud SQL   │     │  Dead Letter│     │  BigQuery   │
│ (PostgreSQL) │     │  Queue      │     │ (Analytics) │
└─────────────┘     └─────────────┘     └─────────────┘
```

## Key Patterns

### Domain Events

Unveraenderliche Events die fachliche Ereignisse repraesentieren:

- `OrderCreated`, `PaymentProcessed`, `ShipmentDispatched`
- Enthalten alle notwendigen Daten fuer Consumer
- Serialisiert als JSON ueber Pub/Sub

### Event Processing

| Pattern | Beschreibung |
|---------|-------------|
| At-Least-Once Delivery | Pub/Sub garantiert mindestens einmalige Zustellung |
| Idempotent Handlers | Handler muessen mehrfache Ausfuehrung vertragen |
| Dead Letter Queue | Fehlgeschlagene Messages fuer Analyse aufbewahren |
| Event Ordering | Bei Bedarf ueber Ordering Keys sicherstellen |

### Resilience

- Retry mit Exponential Backoff
- Circuit Breaker fuer externe Services
- Dead Letter Topics fuer fehlgeschlagene Events
- Health Checks und Monitoring

## Tech Stack

| Komponente | Technologie |
|------------|------------|
| API | FastAPI auf Cloud Run |
| Messaging | Google Cloud Pub/Sub |
| Workers | Cloud Functions (Gen 2) |
| Database | Cloud SQL (PostgreSQL) |
| Analytics | BigQuery |
| IaC | Terraform |

## Verwandte Agents

- :material-robot: [Python Expert](../agents/python-expert.md)
- :material-robot: [GCP Architect](../agents/gcp-architect.md)

---

*Quelldatei: [`reference-repos/event-driven-python/README.md`](https://github.com/atstaeff/ai-agents/blob/main/reference-repos/event-driven-python/README.md)*
