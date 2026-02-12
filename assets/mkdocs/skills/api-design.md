# API Design

> REST, gRPC, Versionierung, Error Handling und bewährte API-Design-Prinzipien.

---

## REST API Design

### URL-Konventionen

| Pattern | Beispiel |
|---------|---------|
| Collection | `GET /api/v1/users` |
| Resource | `GET /api/v1/users/{id}` |
| Sub-Resource | `GET /api/v1/users/{id}/orders` |
| Action | `POST /api/v1/users/{id}/activate` |

### HTTP-Methoden

| Methode | Aktion | Idempotent |
|---------|--------|------------|
| GET | Lesen | Ja |
| POST | Erstellen | Nein |
| PUT | Vollstaendig ersetzen | Ja |
| PATCH | Teilweise aendern | Nein |
| DELETE | Loeschen | Ja |

### HTTP-Statuscodes

| Code | Bedeutung |
|------|----------|
| 200 | Erfolg |
| 201 | Erstellt |
| 204 | Kein Inhalt (Loeschung) |
| 400 | Ungueltige Anfrage |
| 401 | Nicht authentifiziert |
| 403 | Nicht autorisiert |
| 404 | Nicht gefunden |
| 409 | Konflikt |
| 422 | Validierungsfehler |
| 500 | Serverfehler |

## Versionierung

| Strategie | Beispiel | Empfehlung |
|-----------|---------|------------|
| URL Path | `/api/v1/users` | Am verbreitetsten |
| Header | `Accept: application/vnd.api.v1+json` | Sauberer, komplexer |
| Query | `/api/users?version=1` | Einfach, aber unsauber |

## Error Response Format

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Die Anfrage enthaelt ungueltige Daten.",
    "details": [
      {
        "field": "email",
        "message": "Ungueltige E-Mail-Adresse"
      }
    ]
  }
}
```

## Verwandte Skills

- [Microservices](microservices.md) — Service-Kommunikation
- [Security](security.md) — API Security

---

*Quelldatei: [`skills/architecture/api-design.md`](https://github.com/atstaeff/ai-agents/blob/main/skills/architecture/api-design.md)*
