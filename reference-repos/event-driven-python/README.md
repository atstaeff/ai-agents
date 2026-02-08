# Event-Driven Python Reference

This directory contains the reference patterns for event-driven Python architectures on GCP.

## Architecture

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

### 1. Domain Events

```python
from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4

@dataclass(frozen=True)
class DomainEvent:
    event_id: UUID = field(default_factory=uuid4)
    occurred_at: datetime = field(default_factory=datetime.utcnow)
    correlation_id: UUID | None = None

@dataclass(frozen=True)
class OrderPlaced(DomainEvent):
    order_id: UUID
    customer_id: UUID
    total_amount: float
```

### 2. Event Publisher (Pub/Sub)

```python
from google.cloud import pubsub_v1
import json

class PubSubEventBus:
    def __init__(self, project_id: str):
        self._publisher = pubsub_v1.PublisherClient()
        self._project_id = project_id

    async def publish(self, topic: str, event: DomainEvent) -> None:
        topic_path = self._publisher.topic_path(self._project_id, topic)
        data = json.dumps(asdict(event), default=str).encode("utf-8")
        future = self._publisher.publish(
            topic_path,
            data,
            event_type=type(event).__name__,
            correlation_id=str(event.correlation_id or ""),
        )
        future.result()
```

### 3. Idempotent Event Handler

```python
class IdempotentHandler:
    def __init__(self, store: ProcessedEventStore):
        self._store = store

    async def handle(self, event_id: str, handler_fn, *args):
        if await self._store.is_processed(event_id):
            return  # Already processed, skip
        
        await handler_fn(*args)
        await self._store.mark_processed(event_id)
```

### 4. Saga Pattern

```python
class OrderSaga:
    """Coordinates multi-step order process across services."""

    async def execute(self, order: Order) -> SagaResult:
        steps = [
            ("reserve_inventory", self._reserve_inventory, self._release_inventory),
            ("process_payment", self._process_payment, self._refund_payment),
            ("confirm_order", self._confirm_order, self._cancel_order),
        ]

        completed = []
        for name, execute_fn, compensate_fn in steps:
            try:
                await execute_fn(order)
                completed.append((name, compensate_fn))
            except Exception as e:
                # Compensate in reverse order
                for comp_name, comp_fn in reversed(completed):
                    await comp_fn(order)
                return SagaResult.failed(name, str(e))

        return SagaResult.success()
```

## Project Structure

```
src/
├── domain/
│   ├── events.py          # Domain events
│   ├── models.py          # Aggregates, entities
│   └── sagas.py           # Saga orchestrators
├── handlers/
│   ├── order_handlers.py  # Event handlers
│   └── payment_handlers.py
├── infrastructure/
│   ├── pubsub.py          # Pub/Sub client
│   ├── idempotency.py     # Deduplication store
│   └── database.py        # PostgreSQL
├── api/
│   └── main.py            # FastAPI entry point
└── functions/
    ├── process_order.py   # Cloud Function
    └── analytics.py       # BigQuery loader
```

## Principles

1. **Idempotency** — All event handlers are idempotent
2. **At-Least-Once Delivery** — Design for duplicate messages
3. **Dead Letter Queues** — Failed messages are captured, not lost
4. **Correlation IDs** — Trace events across services
5. **Schema Versioning** — Events have explicit versions
6. **Saga Pattern** — Distributed transactions via compensation
