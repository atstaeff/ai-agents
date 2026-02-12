# DevOps & CI/CD

> CI/CD Pipelines, GitOps, Deployment Strategies und Infrastructure Automation.

---

## Pipeline-Design

### Phasen

```mermaid
graph LR
    A[Build] --> B[Test]
    B --> C[Security Scan]
    C --> D[Package]
    D --> E[Deploy Staging]
    E --> F[Integration Tests]
    F --> G[Deploy Production]
```

### Prinzipien

| Prinzip | Beschreibung |
|---------|-------------|
| Pipeline as Code | Pipelines in Version Control definieren |
| Fast Feedback | Schnelle Stages zuerst, parallelisieren |
| Immutable Artifacts | Ein Build-Artifact durch alle Environments |
| Automated Everything | Kein manueller Schritt im Happy Path |
| Rollback Ready | Jedes Deployment schnell rueckgaengig machbar |

## Deployment Strategies

| Strategie | Risiko | Downtime | Kosten |
|-----------|--------|----------|--------|
| Rolling Update | Niedrig | Keine | Normal |
| Blue/Green | Niedrig | Keine | Doppelte Infra |
| Canary | Sehr niedrig | Keine | Etwas mehr |
| Recreate | Hoch | Ja | Niedrig |

## GitOps

- Deklarativer Zustand in Git
- Automatische Synchronisierung
- Pull-basierter Deployment-Ansatz
- Single Source of Truth

## Verwandte Skills

- [GCP Patterns](gcp-patterns.md) — Cloud-spezifische Pipelines
- [Cloud-Native](cloud-native.md) — Container, Serverless

---

*Quelldatei: [`skills/project-management/devops-cicd.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/project-management/devops-cicd.md)*
