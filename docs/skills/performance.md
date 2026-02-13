# Performance

> Performance-Optimierung: Caching, Indexing, Profiling und Monitoring fuer schnelle, skalierbare Systeme.

---

## Performance-Dimensionen

| Dimension | Metrik | Ziel |
|-----------|--------|------|
| Latenz | p50, p95, p99 | p95 < 200ms |
| Throughput | Requests/sec | Service-spezifisch |
| Resource Usage | CPU, Memory, I/O | < 70% normal |
| Error Rate | Fehler/Requests | < 0.1% |

## Caching-Strategien

| Strategie | Anwendung |
|-----------|----------|
| Cache-Aside | Applikation liest/schreibt Cache und DB |
| Read-Through | Cache laedt Daten automatisch aus DB |
| Write-Behind | Cache schreibt asynchron zurueck |
| TTL-based | Zeitbasiertes Expiry |

### Caching-Schichten

```
Browser Cache → CDN → API Gateway Cache → App Cache → DB Cache
```

## Datenbank-Performance

- Indexe auf haeufig abgefragte Spalten
- EXPLAIN ANALYZE fuer Query-Optimierung
- N+1 Queries vermeiden (Eager Loading)
- Connection Pooling
- Read Replicas fuer Leselasten

## Profiling

| Tool | Sprache | Zweck |
|------|---------|-------|
| cProfile / py-spy | Python | CPU Profiling |
| pprof | Go | CPU + Memory |
| Chrome DevTools | Frontend | Network, Rendering |
| Lighthouse | Frontend | Web Vitals |

## Verwandte Skills

- [Microservices](microservices.md) — Skalierung
- [Cloud-Native](cloud-native.md) — Cloud-Performance

---

*Quelldatei: [`skills/architecture/performance.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/architecture/performance.md)*
