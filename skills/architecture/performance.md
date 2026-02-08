# Performance Optimization

## Instructions for AI

Optimize application performance across multiple layers:

## General Principles

### Measure First
- Profile before optimizing
- Use profiling tools
- Identify bottlenecks
- Set performance budgets
- Monitor in production

### Premature Optimization
- "Premature optimization is the root of all evil" - Donald Knuth
- Optimize when it matters
- Focus on bottlenecks (80/20 rule)
- Don't sacrifice readability for minor gains

## Application Layer

### Algorithm Optimization
- Choose appropriate data structures
- Time complexity (Big O notation)
- Space complexity trade-offs
- Example: O(n²) → O(n log n) sorting

### Caching Strategies

**In-Memory Cache**
- Redis, Memcached
- Cache frequently accessed data
- Set appropriate TTL
- Cache invalidation strategy

**Application Cache**
- Local memory cache
- HTTP response cache
- Computed results cache
- Cache aside pattern

**CDN Caching**
- Static assets (images, CSS, JS)
- Edge locations
- Reduce latency globally
- CloudFront, CloudFlare, Akamai

### Lazy Loading
- Load data only when needed
- Defer non-critical resources
- Pagination for large lists
- Infinite scroll pattern

### Connection Pooling
- Database connection pools
- HTTP connection reuse
- Thread pools
- Prevent connection overhead

## Database Optimization

### Query Optimization

**Use Indexes**
```sql
-- Add index on frequently queried columns
CREATE INDEX idx_user_email ON users(email);
CREATE INDEX idx_order_date ON orders(created_at);

-- Composite indexes for multiple columns
CREATE INDEX idx_user_name_email ON users(last_name, first_name);
```

**Avoid N+1 Queries**
```csharp
// ❌ N+1 Problem
foreach (var order in orders) {
    var customer = db.Customers.Find(order.CustomerId); // N queries
}

// ✅ Eager Loading
var orders = db.Orders
    .Include(o => o.Customer) // 1 query with JOIN
    .ToList();
```

**Select Only Needed Columns**
```sql
-- ❌ Fetch all columns
SELECT * FROM users WHERE id = 123;

-- ✅ Fetch specific columns
SELECT id, name, email FROM users WHERE id = 123;
```

**Optimize Joins**
- Index join columns
- Avoid unnecessary joins
- Consider denormalization for reads
- Use appropriate join types

**Query Analysis**
```sql
-- PostgreSQL
EXPLAIN ANALYZE SELECT * FROM orders WHERE status = 'pending';

-- MySQL
EXPLAIN SELECT * FROM orders WHERE status = 'pending';
```

### Database Design

**Normalization vs Denormalization**
- Normalize for write-heavy workloads
- Denormalize for read-heavy workloads
- Consider materialized views
- Balance consistency and performance

**Partitioning**
- Horizontal partitioning (sharding)
- Vertical partitioning
- Range partitioning
- Hash partitioning

**Read Replicas**
- Separate read and write loads
- Route reads to replicas
- Eventual consistency
- Geographic distribution

## Network Optimization

### Reduce Payload Size

**Compression**
- gzip/brotli for HTTP responses
- Minify CSS, JavaScript
- Image compression
- Use WebP for images

**Data Transfer**
- Send only necessary data
- Pagination instead of full lists
- Field selection in APIs
- Delta updates

### Reduce Round Trips

**Batch Requests**
- Combine multiple requests
- GraphQL for flexible queries
- Bulk APIs
- WebSocket for real-time

**HTTP/2 Benefits**
- Multiplexing
- Server push
- Header compression
- Single connection

### Content Delivery

**CDN Usage**
- Serve static assets from CDN
- Edge caching
- Reduced latency
- Geographic distribution

**Asset Optimization**
- Code splitting
- Tree shaking (remove unused code)
- Lazy load images
- Responsive images

## Frontend Optimization

### JavaScript Performance

**Avoid Memory Leaks**
```javascript
// ❌ Memory leak
element.addEventListener('click', handler);

// ✅ Clean up
element.removeEventListener('click', handler);
```

**Debouncing and Throttling**
```javascript
// Debounce: Execute after delay
const debouncedSearch = debounce(search, 300);

// Throttle: Execute at most once per interval
const throttledScroll = throttle(handleScroll, 100);
```

**Optimize Loops**
```javascript
// ❌ Inefficient
for (let i = 0; i < arr.length; i++) {
    // length calculated each iteration
}

// ✅ Cache length
const len = arr.length;
for (let i = 0; i < len; i++) {
    // ...
}

// ✅ Even better: use appropriate method
arr.forEach(item => { /* ... */ });
```

### Rendering Performance

**Virtual DOM**
- React, Vue use virtual DOM
- Minimize re-renders
- Use keys in lists
- Memoization (React.memo, useMemo)

**CSS Optimization**
- Minimize reflows/repaints
- Use CSS transforms for animations
- Avoid expensive selectors
- Critical CSS inlining

**Image Optimization**
- Appropriate format (JPEG, PNG, WebP)
- Responsive images (srcset)
- Lazy loading
- Image compression
- Use SVG for icons

## Backend Optimization

### Asynchronous Processing

**Background Jobs**
- Use queues for long-running tasks
- Celery, Sidekiq, Bull
- Don't block request/response
- Retry failed jobs

**Parallel Processing**
```python
# Sequential (slow)
for item in items:
    process(item)

# Parallel (fast)
with ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(process, items)
```

### Caching Layers

**Application Cache**
```csharp
// Cache expensive computation
if (cache.TryGetValue(key, out var result)) {
    return result;
}
result = ExpensiveOperation();
cache.Set(key, result, TimeSpan.FromMinutes(10));
return result;
```

**HTTP Caching**
```
Cache-Control: public, max-age=3600
ETag: "abc123"
```

### Code-Level Optimizations

**Avoid Premature Object Creation**
```java
// ❌ Creates unnecessary objects
String result = "";
for (String s : strings) {
    result += s; // Creates new string each time
}

// ✅ Use StringBuilder
StringBuilder sb = new StringBuilder();
for (String s : strings) {
    sb.append(s);
}
String result = sb.toString();
```

**Use Appropriate Data Structures**
- HashMap for O(1) lookups
- TreeMap for sorted data
- ArrayList vs LinkedList
- HashSet for uniqueness

## Monitoring & Profiling

### Application Performance Monitoring (APM)
- New Relic, Datadog, AppDynamics
- Track response times
- Identify slow endpoints
- Database query performance
- Error rates

### Profiling Tools

**Backend**
- Java: JProfiler, YourKit
- .NET: dotTrace, PerfView
- Python: cProfile, py-spy
- Node.js: Chrome DevTools, clinic.js

**Frontend**
- Chrome DevTools Performance tab
- Lighthouse
- WebPageTest
- Real User Monitoring (RUM)

### Key Metrics

**Response Time**
- p50, p95, p99 percentiles
- Average can be misleading
- Track over time

**Throughput**
- Requests per second
- Transactions per second
- Capacity planning

**Resource Utilization**
- CPU usage
- Memory usage
- Disk I/O
- Network bandwidth

**Error Rate**
- 4xx and 5xx errors
- Application exceptions
- Timeout rates

## Load Testing

### Tools
- Apache JMeter
- Gatling
- k6
- Locust
- Artillery

### Test Types

**Load Testing**
- Expected peak load
- Identify breaking point
- Response time under load

**Stress Testing**
- Beyond expected load
- Find system limits
- Recovery behavior

**Soak Testing**
- Extended duration
- Identify memory leaks
- Resource exhaustion

**Spike Testing**
- Sudden load increases
- Auto-scaling behavior
- System resilience

## Performance Budgets

### Define Budgets
- Page load time < 3 seconds
- Time to Interactive < 5 seconds
- Bundle size < 200KB
- API response time p95 < 100ms

### Enforcement
- CI/CD integration
- Fail build if exceeded
- Lighthouse CI
- Bundlesize package

## Best Practices Checklist

✅ Profile before optimizing
✅ Implement caching at multiple layers
✅ Use database indexes appropriately
✅ Optimize database queries
✅ Minimize network round trips
✅ Compress responses
✅ Use CDN for static assets
✅ Implement lazy loading
✅ Use connection pooling
✅ Monitor performance in production
✅ Set performance budgets
✅ Regular load testing
✅ Optimize images and assets
✅ Use async processing for long tasks
✅ Implement proper error handling

## Example Prompts

"Identify performance bottlenecks in this code"

"Optimize this database query"

"Implement caching strategy for this API"

"Reduce page load time for this web application"

"Design a load testing strategy for this system"

"Optimize this N+1 query problem"

"Set up performance monitoring for a microservice"
