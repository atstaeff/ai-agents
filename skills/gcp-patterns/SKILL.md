# GCP Patterns Skill

## Instructions for AI

Apply Google Cloud Platform best practices for serverless, event-driven architectures. Use this skill when designing, implementing, or reviewing GCP-based systems.

## Core Service Patterns

### 1. Cloud Run API Service

```python
# main.py — FastAPI on Cloud Run
from fastapi import FastAPI, Depends
from google.cloud import secretmanager

app = FastAPI(title="Order Service")

def get_secret(secret_id: str) -> str:
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{PROJECT_ID}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")

@app.get("/health")
async def health():
    return {"status": "healthy"}
```

### 2. Pub/Sub Event Processing

```python
# Cloud Function triggered by Pub/Sub
import functions_framework
from cloudevents.http import CloudEvent
import json

@functions_framework.cloud_event
def process_order_event(cloud_event: CloudEvent) -> None:
    data = json.loads(base64.b64decode(cloud_event.data["message"]["data"]))
    order_id = data["order_id"]
    
    # Process with retry-safe idempotency
    if already_processed(order_id):
        return
    
    process_order(data)
    mark_processed(order_id)
```

### 3. BigQuery Analytics Pipeline

```python
from google.cloud import bigquery

def load_to_bigquery(data: list[dict], table_id: str) -> None:
    client = bigquery.Client()
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        schema_update_options=[
            bigquery.SchemaUpdateOption.ALLOW_FIELD_ADDITION,
        ],
    )
    job = client.load_table_from_json(data, table_id, job_config=job_config)
    job.result()  # Wait for completion
```

### 4. Terraform Module Pattern

```hcl
# modules/pubsub-topic/main.tf
variable "topic_name" { type = string }
variable "project_id" { type = string }
variable "subscribers" {
  type = list(object({
    name     = string
    endpoint = string
  }))
  default = []
}

resource "google_pubsub_topic" "topic" {
  name    = var.topic_name
  project = var.project_id

  message_retention_duration = "86400s"
}

resource "google_pubsub_topic_iam_member" "dead_letter" {
  topic   = google_pubsub_topic.dead_letter.name
  role    = "roles/pubsub.publisher"
  member  = "serviceAccount:service-${data.google_project.project.number}@gcp-sa-pubsub.iam.gserviceaccount.com"
}

resource "google_pubsub_subscription" "sub" {
  for_each = { for s in var.subscribers : s.name => s }

  name  = each.value.name
  topic = google_pubsub_topic.topic.name

  push_config {
    push_endpoint = each.value.endpoint
  }

  dead_letter_policy {
    dead_letter_topic     = google_pubsub_topic.dead_letter.id
    max_delivery_attempts = 5
  }

  retry_policy {
    minimum_backoff = "10s"
    maximum_backoff = "600s"
  }
}
```

## Architecture Patterns

### Event-Driven Microservices on GCP

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Cloud Run   │────▶│   Pub/Sub   │────▶│ Cloud Run   │
│  Service A   │     │   Topic     │     │  Service B  │
└─────────────┘     └─────────────┘     └─────────────┘
                          │
                          ▼
                    ┌─────────────┐
                    │ Cloud Func  │
                    │ (Analytics) │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │  BigQuery   │
                    └─────────────┘
```

### Security Layers

| Layer | Service | Purpose |
|-------|---------|---------|
| **Edge** | Cloud Armor | WAF, DDoS protection |
| **Identity** | Identity-Aware Proxy | Authentication |
| **Network** | VPC / Private Google Access | Network isolation |
| **Secrets** | Secret Manager | Credential storage |
| **IAM** | Service Accounts | Least-privilege access |
| **Encryption** | Cloud KMS | Key management |
| **Audit** | Cloud Audit Logs | Activity tracking |

## Cost Optimization

| Service | Cost Strategy |
|---------|--------------|
| Cloud Run | Scale to zero, min instances = 0 |
| Cloud Functions | Pay per invocation, <100ms = cheap |
| BigQuery | Use partitioned tables, set slot reservations |
| Cloud Storage | Lifecycle rules, nearline/coldline tiers |
| Cloud SQL | Use smallest instance, stop dev instances at night |

## Best Practices

✅ Use Workload Identity Federation (no service account keys)
✅ Implement idempotent event handlers (Pub/Sub at-least-once delivery)
✅ Use dead letter queues for failed messages
✅ Enable structured logging for Cloud Logging integration
✅ Tag all resources with `environment`, `team`, `cost-center`
✅ Use Terraform modules for reusable infrastructure
✅ Set budget alerts at 50%, 80%, 100%

## Anti-Patterns

❌ Service account key files (use Workload Identity)
❌ Over-provisioned always-on GKE for simple APIs (use Cloud Run)
❌ Storing secrets in environment variables
❌ Missing dead letter queues on Pub/Sub subscriptions
❌ No retry policy on Pub/Sub subscriptions
❌ Broad IAM roles (`roles/editor`, `roles/owner`)

## Example Prompts

- "Design an event-driven data pipeline on GCP with Pub/Sub and BigQuery"
- "Create Terraform modules for a Cloud Run service with Pub/Sub trigger"
- "Optimize this GCP architecture for cost and security"
- "Set up a dead-letter queue pattern for Pub/Sub message processing"

## Related Skills

- [Cloud-Native Architecture](../architecture/cloud-native.md)
- [Security Best Practices](../architecture/security.md)
