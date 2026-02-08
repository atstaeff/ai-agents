# API Design Skill

## Objective
Create APIs that are intuitive, consistent, and pleasant to use.

## Design Philosophy

**User-Centered Thinking**
Design from the API consumer's perspective, not the internal implementation.

**Consistency Matters**
Use predictable patterns throughout. Similar things should work similarly.

**Clear Over Clever**
Explicit, obvious designs beat clever, terse ones.

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

### Step 3: Design URL Structure

**Resource Organization**
Use nouns for resources, not verbs:
- Good: `/books`
- Avoid: `/getBooks`

**Hierarchy and Relationships**
Show relationships through URL structure:
- `/authors/123/books` - books by author 123
- `/members/456/loans` - loans for member 456

**Naming Conventions**
- Use plural nouns: `/books` not `/book`
- Use lowercase with hyphens: `/book-reviews` not `/bookReviews`
- Keep URLs concise but clear

### Step 4: Choose HTTP Methods Appropriately

**Standard Operations**
```
GET /books - Retrieve list of books
GET /books/123 - Retrieve specific book
POST /books - Create new book
PUT /books/123 - Replace entire book
PATCH /books/123 - Update specific fields
DELETE /books/123 - Remove book
```

**Action Endpoints** (when CRUD doesn't fit)
For operations that don't map to CRUD:
```
POST /books/123/reserve - Reserve a book
POST /loans/456/return - Return a loan
POST /books/789/rate - Rate a book
```

### Step 5: Design Request and Response Formats

**Request Bodies**
Keep input schemas simple and focused:
```json
{
  "title": "The Great Gatsby",
  "author_id": 123,
  "isbn": "978-0-7432-7356-5",
  "published_year": 1925
}
```

**Response Bodies**
Include relevant data without over-fetching:
```json
{
  "id": 789,
  "title": "The Great Gatsby",
  "author": {
    "id": 123,
    "name": "F. Scott Fitzgerald"
  },
  "isbn": "978-0-7432-7356-5",
  "published_year": 1925,
  "available": true,
  "created_at": "2026-01-15T10:30:00Z",
  "updated_at": "2026-02-01T14:22:00Z"
}
```

**Consistent Patterns**
Use the same field names across endpoints:
- If it's `created_at` in one place, use `created_at` everywhere
- Keep date formats consistent (ISO 8601 recommended)
- Use the same casing (snake_case or camelCase, not mixed)

### Step 6: Handle Errors Thoughtfully

**HTTP Status Codes**
Use appropriate codes:
- 200 OK - Request succeeded
- 201 Created - Resource created successfully
- 204 No Content - Success with no body to return
- 400 Bad Request - Client sent invalid data
- 401 Unauthorized - Authentication required
- 403 Forbidden - Authenticated but not allowed
- 404 Not Found - Resource doesn't exist
- 422 Unprocessable Entity - Validation failed
- 429 Too Many Requests - Rate limit exceeded
- 500 Internal Server Error - Server-side problem

**Error Response Format**
Provide useful error information:
```json
{
  "error": {
    "code": "validation_failed",
    "message": "Book creation failed due to invalid data",
    "details": [
      {
        "field": "isbn",
        "issue": "ISBN format is invalid"
      },
      {
        "field": "published_year",
        "issue": "Year must be between 1000 and current year"
      }
    ]
  }
}
```

### Step 7: Design for Pagination

**List Endpoints**
Always paginate collections:
```
GET /books?page=2&limit=20
```

**Response with Metadata**
Include pagination info in response:
```json
{
  "data": [...],
  "pagination": {
    "current_page": 2,
    "total_pages": 15,
    "total_items": 287,
    "items_per_page": 20
  }
}
```

**Cursor-Based Alternative**
For large datasets:
```
GET /books?cursor=abc123&limit=20

Response includes next cursor:
{
  "data": [...],
  "next_cursor": "def456"
}
```

### Step 8: Support Filtering and Sorting

**Query Parameters**
```
GET /books?author=123&year_from=2020&sort=title_asc
GET /books?status=available&category=fiction
```

**Document Allowed Filters**
Clearly specify what filters and sorts are supported.

### Step 9: Version Your API

**URL Versioning** (clear and explicit)
```
/v1/books
/v2/books
```

**Header Versioning** (cleaner URLs)
```
Accept: application/vnd.library.v1+json
```

**Version Compatibility**
- Don't break existing versions
- Support older versions for a defined period
- Communicate deprecation timelines clearly

### Step 10: Document Thoroughly

**Essential Documentation**
- Authentication requirements
- Request/response examples for each endpoint
- Error codes and their meanings
- Rate limits and quotas
- Pagination details
- Common use case examples

**Interactive Documentation**
Provide tools like Swagger/OpenAPI that let developers test endpoints directly.

## Security Considerations

**Authentication**
- Use industry-standard approaches (OAuth 2.0, API keys)
- Transmit credentials securely
- Don't pass sensitive data in URLs

**Authorization**
- Validate permissions for each request
- Don't expose internal IDs if they reveal information
- Filter responses based on user access

**Input Validation**
- Validate all inputs
- Sanitize data to prevent injection
- Limit request sizes
- Rate limit to prevent abuse

## Testing Your API

**Consumer Perspective**
- Can someone understand what endpoints do without implementation code?
- Are error messages helpful for debugging?
- Is the API predictable based on patterns?

**Technical Validation**
- Test all endpoints with valid and invalid inputs
- Verify error responses are correct
- Check edge cases (empty lists, missing fields, etc.)
- Load test to understand performance characteristics

## Evolution Strategy

**Backward Compatibility**
- Add new fields, don't remove old ones (initially)
- Make new fields optional
- Provide sensible defaults

**Deprecation Process**
When you must remove something:
1. Announce deprecation well in advance
2. Provide migration guide
3. Give ample time (6-12 months)
4. Monitor usage before removing
5. Offer support during migration
