---
name: golang-patterns
description: Idiomatic Go patterns, modern best practices, and production-grade code standards
---

# Golang Patterns Skill

## Instructions for AI

Apply idiomatic Go patterns, modern best practices, and production-grade code standards. Use this skill when writing, reviewing, or refactoring Go code. Follow Go's philosophy: simplicity, clarity, composition.

Reference: [Effective Go](https://go.dev/doc/effective_go), [Go Code Review Comments](https://github.com/golang/go/wiki/CodeReviewComments), [Uber Go Style Guide](https://github.com/uber-go/guide/blob/master/style.md).

## Core Patterns

### 1. Repository Pattern with Interfaces

Abstraction over data access, enabling testability and swappable backends.

```go
type OrderRepository interface {
    Create(ctx context.Context, order *Order) error
    GetByID(ctx context.Context, id uuid.UUID) (*Order, error)
    List(ctx context.Context, filter OrderFilter) ([]Order, error)
    Update(ctx context.Context, order *Order) error
    Delete(ctx context.Context, id uuid.UUID) error
}

// PostgreSQL implementation
type postgresOrderRepo struct {
    db *sql.DB
}

func NewPostgresOrderRepo(db *sql.DB) OrderRepository {
    return &postgresOrderRepo{db: db}
}

func (r *postgresOrderRepo) GetByID(ctx context.Context, id uuid.UUID) (*Order, error) {
    var o Order
    err := r.db.QueryRowContext(ctx,
        `SELECT id, customer_id, total, status, created_at
         FROM orders WHERE id = $1`, id,
    ).Scan(&o.ID, &o.CustomerID, &o.Total, &o.Status, &o.CreatedAt)

    if errors.Is(err, sql.ErrNoRows) {
        return nil, fmt.Errorf("order %s: %w", id, ErrNotFound)
    }
    if err != nil {
        return nil, fmt.Errorf("querying order %s: %w", id, err)
    }
    return &o, nil
}
```

### 2. Service Layer with Dependency Injection

Business logic encapsulated in services with injected dependencies.

```go
type OrderService struct {
    repo   OrderRepository
    events EventPublisher
    logger *slog.Logger
}

func NewOrderService(repo OrderRepository, events EventPublisher, logger *slog.Logger) *OrderService {
    return &OrderService{repo: repo, events: events, logger: logger}
}

func (s *OrderService) PlaceOrder(ctx context.Context, cmd PlaceOrderCommand) (*Order, error) {
    order, err := NewOrder(cmd.CustomerID, cmd.Items)
    if err != nil {
        return nil, fmt.Errorf("creating order: %w", err)
    }

    if err := s.repo.Create(ctx, order); err != nil {
        return nil, fmt.Errorf("saving order: %w", err)
    }

    if err := s.events.Publish(ctx, "orders.placed", OrderPlacedEvent{
        OrderID:    order.ID,
        CustomerID: order.CustomerID,
        Total:      order.Total,
    }); err != nil {
        s.logger.WarnContext(ctx, "event publish failed", slog.String("error", err.Error()))
    }

    return order, nil
}
```

### 3. Domain Errors — Sentinel + Wrapping

```go
// Sentinel errors for domain-level error classification
var (
    ErrNotFound      = errors.New("not found")
    ErrAlreadyExists = errors.New("already exists")
    ErrUnauthorized  = errors.New("unauthorized")
    ErrForbidden     = errors.New("forbidden")
    ErrValidation    = errors.New("validation error")
    ErrConflict      = errors.New("conflict")
)

// Structured validation error
type FieldError struct {
    Field   string `json:"field"`
    Message string `json:"message"`
}

type ValidationErrors struct {
    Errors []FieldError `json:"errors"`
}

func (e *ValidationErrors) Error() string {
    return fmt.Sprintf("validation failed: %d errors", len(e.Errors))
}

func (e *ValidationErrors) Unwrap() error {
    return ErrValidation
}

// Map domain errors to HTTP in handler
func mapError(err error) (int, string) {
    switch {
    case errors.Is(err, ErrNotFound):
        return http.StatusNotFound, "Resource not found"
    case errors.Is(err, ErrUnauthorized):
        return http.StatusUnauthorized, "Unauthorized"
    case errors.Is(err, ErrForbidden):
        return http.StatusForbidden, "Forbidden"
    case errors.Is(err, ErrValidation):
        return http.StatusBadRequest, err.Error()
    case errors.Is(err, ErrConflict):
        return http.StatusConflict, "Resource conflict"
    default:
        return http.StatusInternalServerError, "Internal server error"
    }
}
```

### 4. Functional Options Pattern

```go
type ClientOption func(*Client)

func WithTimeout(d time.Duration) ClientOption {
    return func(c *Client) { c.timeout = d }
}

func WithRetries(n int) ClientOption {
    return func(c *Client) { c.maxRetries = n }
}

func WithBaseURL(url string) ClientOption {
    return func(c *Client) { c.baseURL = url }
}

func NewClient(opts ...ClientOption) *Client {
    c := &Client{
        timeout:    30 * time.Second,
        maxRetries: 3,
        baseURL:    "https://api.example.com",
        httpClient: http.DefaultClient,
    }
    for _, opt := range opts {
        opt(c)
    }
    return c
}
```

### 5. Worker Pool with errgroup

```go
import "golang.org/x/sync/errgroup"

func ProcessBatch(ctx context.Context, items []Item, concurrency int) error {
    g, ctx := errgroup.WithContext(ctx)
    g.SetLimit(concurrency)

    for _, item := range items {
        item := item // capture loop variable (Go < 1.22)
        g.Go(func() error {
            select {
            case <-ctx.Done():
                return ctx.Err()
            default:
                return processItem(ctx, item)
            }
        })
    }

    return g.Wait()
}
```

### 6. Middleware Chain (HTTP)

```go
type Middleware func(http.Handler) http.Handler

func Chain(handler http.Handler, middlewares ...Middleware) http.Handler {
    for i := len(middlewares) - 1; i >= 0; i-- {
        handler = middlewares[i](handler)
    }
    return handler
}

func RequestIDMiddleware() Middleware {
    return func(next http.Handler) http.Handler {
        return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
            requestID := r.Header.Get("X-Request-ID")
            if requestID == "" {
                requestID = uuid.NewString()
            }
            ctx := context.WithValue(r.Context(), requestIDKey, requestID)
            w.Header().Set("X-Request-ID", requestID)
            next.ServeHTTP(w, r.WithContext(ctx))
        })
    }
}

func TimeoutMiddleware(d time.Duration) Middleware {
    return func(next http.Handler) http.Handler {
        return http.TimeoutHandler(next, d, "request timeout")
    }
}
```

### 7. Table-Driven Tests with Subtests

```go
func TestParseAmount(t *testing.T) {
    tests := []struct {
        name    string
        input   string
        want    float64
        wantErr bool
    }{
        {name: "valid integer", input: "100", want: 100.0},
        {name: "valid decimal", input: "99.99", want: 99.99},
        {name: "negative", input: "-50", want: -50.0},
        {name: "empty string", input: "", wantErr: true},
        {name: "not a number", input: "abc", wantErr: true},
        {name: "overflow", input: "1e309", wantErr: true},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got, err := ParseAmount(tt.input)
            if tt.wantErr {
                if err == nil {
                    t.Fatal("expected error, got nil")
                }
                return
            }
            if err != nil {
                t.Fatalf("unexpected error: %v", err)
            }
            if got != tt.want {
                t.Errorf("ParseAmount(%q) = %v, want %v", tt.input, got, tt.want)
            }
        })
    }
}
```

### 8. Fake Implementations for Testing

```go
// Fake repository for unit tests — no external dependencies
type FakeOrderRepo struct {
    mu     sync.Mutex
    orders map[uuid.UUID]*Order
}

func NewFakeOrderRepo() *FakeOrderRepo {
    return &FakeOrderRepo{orders: make(map[uuid.UUID]*Order)}
}

func (r *FakeOrderRepo) Create(_ context.Context, order *Order) error {
    r.mu.Lock()
    defer r.mu.Unlock()
    if _, exists := r.orders[order.ID]; exists {
        return fmt.Errorf("order %s: %w", order.ID, ErrAlreadyExists)
    }
    r.orders[order.ID] = order
    return nil
}

func (r *FakeOrderRepo) GetByID(_ context.Context, id uuid.UUID) (*Order, error) {
    r.mu.Lock()
    defer r.mu.Unlock()
    order, ok := r.orders[id]
    if !ok {
        return nil, fmt.Errorf("order %s: %w", id, ErrNotFound)
    }
    return order, nil
}
```

### 9. Configuration with Environment Variables

```go
type Config struct {
    ServerAddr   string        `env:"SERVER_ADDR" default:":8080"`
    DatabaseURL  string        `env:"DATABASE_URL" required:"true"`
    RedisURL     string        `env:"REDIS_URL" default:"redis://localhost:6379"`
    LogLevel     string        `env:"LOG_LEVEL" default:"info"`
    ReadTimeout  time.Duration `env:"READ_TIMEOUT" default:"15s"`
    WriteTimeout time.Duration `env:"WRITE_TIMEOUT" default:"15s"`
}

func LoadConfig() (*Config, error) {
    cfg := &Config{}
    if err := envconfig.Process("", cfg); err != nil {
        return nil, fmt.Errorf("loading config: %w", err)
    }
    return cfg, nil
}
```

### 10. Graceful Shutdown

```go
func Run(ctx context.Context, cfg *Config, logger *slog.Logger) error {
    srv := &http.Server{
        Addr:         cfg.ServerAddr,
        Handler:      setupRouter(cfg, logger),
        ReadTimeout:  cfg.ReadTimeout,
        WriteTimeout: cfg.WriteTimeout,
    }

    errCh := make(chan error, 1)
    go func() {
        logger.Info("server starting", slog.String("addr", cfg.ServerAddr))
        if err := srv.ListenAndServe(); err != nil && !errors.Is(err, http.ErrServerClosed) {
            errCh <- err
        }
    }()

    select {
    case err := <-errCh:
        return fmt.Errorf("server error: %w", err)
    case <-ctx.Done():
        logger.Info("shutting down...")
        shutdownCtx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
        defer cancel()
        return srv.Shutdown(shutdownCtx)
    }
}

func main() {
    ctx, stop := signal.NotifyContext(context.Background(), syscall.SIGINT, syscall.SIGTERM)
    defer stop()

    logger := slog.New(slog.NewJSONHandler(os.Stdout, nil))
    cfg, err := LoadConfig()
    if err != nil {
        logger.Error("config error", slog.String("error", err.Error()))
        os.Exit(1)
    }

    if err := Run(ctx, cfg, logger); err != nil {
        logger.Error("server failed", slog.String("error", err.Error()))
        os.Exit(1)
    }
}
```

## Project Structure

```
cmd/
├── api/main.go              # API entrypoint
└── worker/main.go           # Worker entrypoint
internal/
├── domain/                  # Pure domain logic, no external deps
│   ├── order.go
│   ├── order_test.go
│   └── errors.go
├── service/                 # Application use cases
│   ├── order_service.go
│   └── order_service_test.go
├── repository/              # Interfaces + implementations
│   ├── interfaces.go
│   └── postgres/
├── handler/                 # HTTP/gRPC transport
│   └── order_handler.go
├── middleware/               # Cross-cutting concerns
└── config/                  # Configuration
pkg/                         # Public reusable code (optional)
├── httputil/
└── testutil/
```

## Best Practices

✅ Accept interfaces, return structs
✅ Handle every error — wrap with `fmt.Errorf("context: %w", err)`
✅ Use `context.Context` as the first parameter
✅ Prefer composition over embedding for non-trivial types
✅ Use `slog` for structured logging
✅ Table-driven tests with `t.Run` subtests
✅ `internal/` for private application code
✅ Functional options for configurable constructors
✅ `errgroup` for concurrent operations with error handling
✅ `go vet`, `golangci-lint`, `-race` in CI

## Anti-Patterns

❌ `init()` with side effects
❌ `context.Context` stored in structs
❌ Ignoring errors with `_`
❌ `interface{}` / `any` when generics or specific types work
❌ Global mutable state
❌ `panic` for expected errors
❌ Premature interfaces — wait until you need 2+ implementations
❌ Giant `main()` functions — extract into `Run(ctx, cfg)` functions
❌ Naked returns in complex functions

## Example Prompts

- "Refactor this Go code to use interfaces and dependency injection"
- "Write table-driven tests for this Go function including edge cases"
- "Design a concurrent pipeline with worker pool and graceful shutdown"
- "Review this Go code for idiomatic patterns and error handling"

## Related Skills

- [Golang Expert Agent](../../agents/golang-expert.agent.md)
- [Clean Code](../software-engineering/clean-code.md)
- [Design Patterns](../software-engineering/design-patterns.md)
- [Testing Strategies](../software-engineering/testing-strategies.md)
- [GCP Patterns](../gcp-patterns/SKILL.md)
- [Anti-Patterns](../anti-patterns/SKILL.md)
