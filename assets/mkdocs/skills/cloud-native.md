# Cloud-Native Architecture

> 12-Factor App, Container, Serverless und Cloud-native Patterns fuer skalierbare, resiliente Systeme.

---

## 12-Factor App

| Factor | Beschreibung |
|--------|-------------|
| Codebase | Eine Codebase pro App, viele Deploys |
| Dependencies | Explizit deklarieren und isolieren |
| Config | Konfiguration in Umgebungsvariablen |
| Backing Services | Als angeheftete Ressourcen behandeln |
| Build, Release, Run | Strikt getrennte Phasen |
| Processes | Stateless Prozesse |
| Port Binding | Services ueber Port-Binding exportieren |
| Concurrency | Horizontal skalieren ueber Prozesse |
| Disposability | Schnell starten, graceful shutdown |
| Dev/Prod Parity | Environments so aehnlich wie moeglich |
| Logs | Als Event-Streams behandeln |
| Admin Processes | Als einmalige Tasks ausfuehren |

## Resilience Patterns

| Pattern | Beschreibung |
|---------|-------------|
| Circuit Breaker | Fehlerhafte Services absichern |
| Retry + Backoff | Transiente Fehler wiederholen |
| Bulkhead | Ausfaelle isolieren |
| Health Checks | Liveness + Readiness Probes |
| Graceful Degradation | Funktionalitaet reduzieren statt ausfallen |

## Container Best Practices

- Multi-Stage Builds fuer kleine Images
- Non-Root User im Container
- Health Check Endpoint
- Structured Logging (JSON)
- Graceful Shutdown (SIGTERM Handler)

## Verwandte Skills

- [Microservices](microservices.md) — Microservice-Architektur
- [GCP Patterns](gcp-patterns.md) — GCP-spezifische Patterns
- [Security](security.md) — Cloud Security

---

*Quelldatei: [`skills/architecture/cloud-native.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/architecture/cloud-native.md)*
