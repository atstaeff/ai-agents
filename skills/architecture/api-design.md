# API Design Best Practices

## Instructions for AI

Design robust, scalable, and developer-friendly APIs:

## REST API Design

### Resource Naming
- Use nouns, not verbs
- Plural for collections: `/users`, `/orders`
- Hierarchical relationships: `/users/{id}/orders`
- Use lowercase and hyphens: `/user-profiles`
- Avoid deep nesting (max 2-3 levels)

### HTTP Methods
- **GET**: Retrieve resources (idempotent, safe)
- **POST**: Create new resources
- **PUT**: Update entire resource (idempotent)
- **PATCH**: Partial update
- **DELETE**: Remove resource (idempotent)
- **HEAD**: Like GET but no body
- **OPTIONS**: Describe communication options

### Status Codes
**Success:**
- 200 OK: Successful GET, PUT, PATCH
- 201 Created: Successful POST
- 204 No Content: Successful DELETE

**Client Errors:**
- 400 Bad Request: Invalid request
- 401 Unauthorized: Authentication required
- 403 Forbidden: Not permitted
- 404 Not Found: Resource doesn't exist
- 409 Conflict: Conflicting state
- 422 Unprocessable Entity: Validation errors

**Server Errors:**
- 500 Internal Server Error: Generic error
- 502 Bad Gateway: Invalid response from upstream
- 503 Service Unavailable: Temporary unavailability
- 504 Gateway Timeout: Upstream timeout

### Versioning
**URL Versioning**: `/v1/users` (Recommended)
- Clear and explicit
- Easy to route

**Header Versioning**: `Accept: application/vnd.api+json; version=1`
- Cleaner URLs
- More complex

**Query Parameter**: `/users?version=1`
- Not recommended

### Pagination
```json
GET /users?page=2&size=50

Response:
{
  "data": [...],
  "pagination": {
    "page": 2,
    "size": 50,
    "total": 500,
    "totalPages": 10
  }
}
```

**Cursor-Based** (for large datasets):
```json
GET /users?cursor=abc123&limit=50

Response:
{
  "data": [...],
  "cursor": {
    "next": "def456",
    "hasMore": true
  }
}
```

### Filtering, Sorting, Searching
```
GET /users?status=active&sort=-createdAt&search=john
```

### Response Format
```json
{
  "data": {
    "id": "123",
    "type": "user",
    "attributes": {
      "name": "John Doe",
      "email": "john@example.com"
    }
  },
  "meta": {
    "timestamp": "2026-02-05T19:00:00Z"
  }
}
```

### Error Response
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input",
    "details": [
      {
        "field": "email",
        "message": "Invalid email format"
      }
    ]
  }
}
```

## Security

### Authentication
- **JWT**: Stateless, good for microservices
- **OAuth 2.0**: Industry standard for authorization
- **API Keys**: Simple, for service-to-service
- **Session-based**: Traditional web apps

### Rate Limiting
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 995
X-RateLimit-Reset: 1614556800
```

### CORS
- Configure allowed origins
- Whitelist specific domains
- Avoid wildcard (*) in production

### Input Validation
- Validate all inputs server-side
- Sanitize against injection attacks
- Use schema validation (JSON Schema)
- Whitelist vs blacklist approach

## Performance

### Caching
```
Cache-Control: public, max-age=3600
ETag: "abc123"
Last-Modified: Thu, 05 Feb 2026 19:00:00 GMT
```

### Compression
- Enable gzip/brotli compression
- Reduces bandwidth
- Configurable per endpoint

### Field Selection
```
GET /users/123?fields=id,name,email
```

### Batch Operations
```
POST /users/bulk
{
  "operations": [
    {"method": "POST", "body": {...}},
    {"method": "PATCH", "id": "123", "body": {...}}
  ]
}
```

## Documentation

### OpenAPI/Swagger
- Standard specification
- Auto-generate documentation
- Client SDK generation
- Interactive API explorer

### Include in Docs
- Endpoint descriptions
- Request/response examples
- Authentication requirements
- Error codes and meanings
- Rate limits
- Changelog/versioning

## GraphQL Alternative

### Advantages
- Client specifies exact data needed
- Single endpoint
- Strong typing
- Reduces over-fetching/under-fetching

### Schema Example
```graphql
type User {
  id: ID!
  name: String!
  email: String!
  orders: [Order!]!
}

type Query {
  user(id: ID!): User
  users(limit: Int, offset: Int): [User!]!
}

type Mutation {
  createUser(input: CreateUserInput!): User!
}
```

### When to Use
- Complex, nested data requirements
- Multiple client types (web, mobile)
- Need to minimize requests
- Frequently changing requirements

## gRPC Alternative

### Advantages
- High performance (binary protocol)
- Strong typing (Protocol Buffers)
- Bidirectional streaming
- Code generation

### Protocol Buffers Example
```protobuf
service UserService {
  rpc GetUser(GetUserRequest) returns (User);
  rpc CreateUser(CreateUserRequest) returns (User);
}

message User {
  string id = 1;
  string name = 2;
  string email = 3;
}
```

### When to Use
- Microservice communication
- Performance critical
- Strongly typed contracts
- Streaming requirements

## Best Practices Checklist

✅ Use proper HTTP methods and status codes
✅ Version your API from day one
✅ Implement consistent error handling
✅ Add pagination to list endpoints
✅ Document with OpenAPI/Swagger
✅ Implement authentication and authorization
✅ Add rate limiting
✅ Enable CORS properly
✅ Validate and sanitize inputs
✅ Use HTTPS everywhere
✅ Log requests for debugging
✅ Monitor performance and errors
✅ Provide changelog for updates
✅ Support filtering and sorting
✅ Use appropriate caching headers

## Anti-Patterns

❌ Verbs in URLs (`/getUser`)
❌ Inconsistent naming conventions
❌ Exposing internal implementation details
❌ Missing or poor error messages
❌ No API versioning
❌ Returning 200 OK for errors
❌ Overly nested URLs
❌ No rate limiting
❌ Returning entire objects when not needed
❌ Breaking changes without versioning

## Example Prompts

"Design a REST API for an e-commerce system"

"Create OpenAPI specification for a user management API"

"Implement rate limiting for an API endpoint"

"Design error responses following best practices"

"Create a GraphQL schema for a blog platform"

"Implement API versioning strategy"
