# Local work API

Start `python3 tools/ai_toolkit.py serve --workspace /path/to/project`.
The server binds only to `127.0.0.1`, default port **4097**. It manages local files,
not models or chat sessions.

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/api/v1/catalog` | Agent/skill metadata |
| GET | `/api/v1/work` | Active record summaries |
| GET | `/api/v1/work/{id}` | Markdown, tasks and ETag |
| POST | `/api/v1/work` | Create from `{id, title, kind}` |
| POST | `/api/v1/work/{id}/feedback` | Append `{text}` |
| PATCH | `/api/v1/work/{id}/tasks/{taskId}` | Update `{status, evidence}` |
| GET | `/api/v1/openapi.json` | [OpenAPI contract](openapi.json) |

Writes use `application/json`, up to 16 KiB. Feedback/task changes require `If-Match`
with the ETag from a current read. Changed records return **412**; missing `If-Match`
returns **428**. Reload and retry explicitly, preserving unsent comments.
Validation returns 400, missing routes/records 404, untrusted hosts/origins 403.

Host, Origin and cross-site checks guard loopback use. Paths reject traversal and
symlinks; records are size-limited and writes atomic. The frontend has no external
assets. Do not expose this service publicly. Other processes running as your user can
still access the loopback service and your files.

```sh
curl -i http://127.0.0.1:4097/api/v1/work/customer-portal
curl http://127.0.0.1:4097/api/v1/work/customer-portal/feedback \
  -H 'Content-Type: application/json' -H 'If-Match: "paste-current-hash"' \
  -d '{"text":"Please keep the existing sign-in flow."}'
```
