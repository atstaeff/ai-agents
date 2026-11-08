# Background examples

Use focused sections only when needed. The current skill entry, project conventions and user constraints govern the work. Examples illustrate particular choices; they do not mandate a framework, test library or architecture.

# API Design Best Practices

## Instructions for AI

Design robust, scalable, and developer-friendly APIs.

## Design Philosophy

- **User-Centered Thinking**: Design from the API consumer's perspective, not the internal implementation
- **Consistency Matters**: Use predictable patterns throughout — similar things should work similarly
- **Clear Over Clever**: Explicit, obvious designs beat clever, terse ones

## Design Process

### Step 1: Understand the Use Cases
Before designing endpoints:
- What tasks will developers accomplish with this API?
- What data flows through these tasks?
- Which operations happen frequently vs. rarely?
- What errors might occur?

### Step 2: Define Resource Model
Identify the core concepts:
- What entities exist in your domain?
- How do they relate to each other?
- What operations make sense for each entity?

Example for a library system:
```
Resources: books, authors, members, loans
Relationships: authors write books, members borrow books creating loans
Operations: list, create, retrieve, update, delete (where applicable)
```

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
- 412 Precondition Failed: A request precondition did not match current state
- 422 Unprocessable Content: Understood content that cannot be processed

**Server Errors:**
- 500 Internal Server Error: Generic error
- 502 Bad Gateway: Invalid response from upstream
- 503 Service Unavailable: Temporary unavailability
- 504 Gateway Timeout: Upstream timeout

### Versioning
Preserve the existing contract and versioning convention. Add a distinct version only
when consumers need incompatible contracts to coexist. A URL prefix such as `/v1/users`
is visible in routes; header-based negotiation keeps URLs stable but requires clients
and caches to account for the negotiated representation.

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
Reuse the project's established identity and token or session profile. A JWT is a
token format; OAuth 2.0 is an authorization framework. A validated identity alone does
not authorize an action on a resource. See [security review](../../../quality/security/references/security.md#identity-and-resource-authorization).

### Rate Limiting
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 995
X-RateLimit-Reset: 1614556800
```

### CORS
Configure origins and credentials for the actual browser clients. CORS controls browser
access to responses; it does not replace server-side authorization or CSRF protection.

### Input Validation
Validate type, size and business constraints on the server. Use parameterized queries
and context-specific output encoding where appropriate; schema validation alone does
not prevent injection.

## Performance

### Caching
For a public resource with the same representation for all callers, a shared cache can
reduce repeated work:

```http
Cache-Control: public, max-age=3600
ETag: "abc123"
Last-Modified: Thu, 05 Feb 2026 19:00:00 GMT
```

Use `private` when only a private cache may retain a caller-specific response, or
`no-store` when it must not be stored. `public` can permit shared reuse even for a
request with an `Authorization` header. Test with two identities through the cache
when the response depends on the caller. See [HTTP caching](https://www.rfc-editor.org/rfc/rfc9111.html#section-3.5).

### Concurrent Writes and Retries

Where lost updates matter, use an atomic version check. For HTTP, one option is a
strong `ETag` with `If-Match`; reject a stale precondition with `412` and preserve the
newer write. For a retried operation that creates an effect, define how the server
recognizes the same operation and returns its outcome without repeating the effect.

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

## Testing Your API

**Consumer Perspective**
- Can someone understand what endpoints do without implementation code?
- Are error messages helpful for debugging?
- Is the API predictable based on patterns?

**Technical Validation**
- Test all endpoints with valid and invalid inputs
- Verify error responses are correct
- Check edge cases (empty lists, missing fields)
- Load test to understand performance characteristics

## Evolution Strategy

### Backward Compatibility
- Add new fields, don't remove old ones initially
- Make new fields optional
- Provide sensible defaults

### Deprecation Process
1. Announce deprecation well in advance
2. Provide migration guide
3. Set a migration window with affected consumers and the contract owner
4. Monitor usage before removing
5. Offer support during migration

## Best Practices Checklist

✅ Use proper HTTP methods and status codes
✅ Preserve compatibility or agree an explicit migration with affected consumers
✅ Implement consistent error handling
✅ Add pagination to list endpoints
✅ Document with OpenAPI/Swagger
✅ Implement authentication and authorization
✅ Bound resource usage; rate-limit where the abuse or capacity model calls for it
✅ Enable CORS properly
✅ Validate input and use the right injection defenses at each boundary
✅ Use HTTPS everywhere
✅ Log useful request metadata without credentials or private data
✅ Monitor performance and errors
✅ Provide changelog for updates
✅ Support filtering and sorting
✅ Use appropriate caching headers

## Anti-Patterns

❌ Verbs in URLs (`/getUser`)
❌ Inconsistent naming conventions
❌ Exposing internal implementation details
❌ Missing or poor error messages
❌ Changing a consumer contract without a compatibility plan
❌ Returning 200 OK for errors
❌ Overly nested URLs
❌ Allowing expensive operations to exhaust shared capacity
❌ Returning entire objects when not needed

## Example Prompts

"Design a REST API for an e-commerce system"

"Create OpenAPI specification for a user management API"

"Implement rate limiting for an API endpoint"

"Design error responses following best practices"

"Create a GraphQL schema for a blog platform"

"Implement API versioning strategy"
