# GCP Patterns

> Google Cloud Platform Patterns: Cloud Run, Pub/Sub, BigQuery, Terraform und serverlose Architekturen.

---

## Kernpatterns

### Cloud Run Service

- FastAPI / Flask auf Cloud Run
- Automatic Scaling, min/max Instances
- VPC Connector fuer interne Kommunikation
- Secret Manager Integration

### Event-Driven Processing

- Pub/Sub fuer asynchrone Kommunikation
- Cloud Functions als Event Handler
- Dead Letter Topics fuer fehlgeschlagene Messages
- Push vs. Pull Subscriptions

### Infrastructure as Code

- Terraform Module pro Service / Ressource
- Remote State in GCS Bucket
- Workload Identity fuer CI/CD
- Environment-spezifische `tfvars`

## Service-Auswahl

| Anforderung | GCP Service |
|-------------|------------|
| Web API / Microservice | Cloud Run |
| Event Handler | Cloud Functions |
| Async Messaging | Pub/Sub |
| Data Warehouse | BigQuery |
| NoSQL Database | Firestore |
| Relational DB | Cloud SQL |
| Object Storage | Cloud Storage |
| Container Orchestration | GKE |

## Verwandte Skills

- [Cloud-Native](cloud-native.md) — Cloud-native Prinzipien
- [DevOps & CI/CD](devops-cicd.md) — Deployment Pipelines

---

*Quelldatei: [`skills/gcp-patterns/SKILL.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/gcp-patterns/SKILL.md)*
