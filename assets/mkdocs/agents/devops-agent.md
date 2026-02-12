# DevOps Agent

<span class="agent-badge agent-badge--engineering">Engineering</span>

> CI/CD und Infrastructure Automation Expert. Designt robuste Deployment Pipelines und sichert zuverlaessige, reproduzierbare Deployments.

---

## Kernkompetenzen

- CI/CD Pipelines (GitHub Actions, Cloud Build)
- Automatisierte Deployments mit Environment Promotion (dev → staging → prod)
- GitOps Workflows und Infrastructure as Code
- Monitoring, Alerting und Incident Response Automation
- Secrets, Konfigurationen und Umgebungsvariablen sicher verwalten

## Wann einsetzen?

| Szenario | Beispiel |
|----------|----------|
| Pipeline erstellen | GitHub Actions fuer Build, Test, Deploy |
| Deployment automatisieren | Cloud Run Deployment mit Terraform |
| GitOps einrichten | ArgoCD / Flux Workflow |
| Monitoring aufsetzen | Alerting, Dashboards, Incident Response |

## Pipeline-Prinzipien

| Prinzip | Beschreibung |
|---------|-------------|
| Pipeline as Code | Alle Pipelines in Version Control |
| Fast Feedback | Fail fast, parallelisierte Stages |
| Environment Parity | Dev = Staging ≈ Production |
| Automated Everything | Build, Test, Scan, Deploy, Verify |
| Rollback Ready | Jedes Deployment einfach rueckgaengig machbar |
| Secure by Default | Keine Secrets im Code, OIDC/Workload Identity |

## Pipeline-Template (GitHub Actions)

```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Tests
        run: make test

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to Production
        run: make deploy
```

## Beispiel-Prompts

```
@workspace Nutze den DevOps Agent.
Erstelle eine GitHub Actions Pipeline fuer einen Python-Service:
Lint, Test, Docker Build, Push to GCR, Deploy auf Cloud Run.
Mit OIDC Authentication und Environment Promotion.
```

```
@workspace Nutze den DevOps Agent.
Richte GitOps fuer unser Kubernetes-Cluster ein.
ArgoCD mit automatic sync und health checks.
```

## Verwandte Agents & Skills

- :material-cloud: [GCP Architect](gcp-architect.md) — Cloud-Infrastruktur
- :material-test-tube: [Test Strategist](test-strategist.md) — Quality Gates
- :material-book-open-variant: [DevOps & CI/CD](../skills/devops-cicd.md) — CI/CD Skill vertiefen

---

*Quelldatei: [`agents/devops-agent.agent.md`](https://github.com/atstaeff/ai-agents/blob/main/agents/devops-agent.agent.md)*
