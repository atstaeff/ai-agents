---
name: flutter-patterns
description: Modern Flutter and Dart patterns, production-grade standards, and iOS-optimized practices
---

# Flutter Patterns Skill

## Instructions for AI

Apply modern Flutter and Dart patterns, production-grade standards, and iOS-optimized practices. Use this skill when writing, reviewing, or refactoring Flutter/Dart code. Follow Clean Architecture with clear separation of presentation, domain, and data layers.

## Core Patterns

### 1. BLoC Pattern — Events, States, BLoC

Separate user interactions (events) from UI representation (states) via a BLoC mediator.

```dart
// Events — what the user does
@freezed
class ProductEvent with _$ProductEvent {
  const factory ProductEvent.load({String? category}) = _Load;
  const factory ProductEvent.search(String query) = _Search;
  const factory ProductEvent.addToCart(String productId) = _AddToCart;
}

// States — what the UI shows
@freezed
class ProductState with _$ProductState {
  const factory ProductState.initial() = _Initial;
  const factory ProductState.loading() = _Loading;
  const factory ProductState.loaded({
    required List<Product> products,
    required String? activeCategory,
  }) = _Loaded;
  const factory ProductState.error(String message) = _Error;
}

// BLoC — transforms events into states
class ProductBloc extends Bloc<ProductEvent, ProductState> {
  final GetProducts _getProducts;
  final AddToCart _addToCart;

  ProductBloc({
    required GetProducts getProducts,
    required AddToCart addToCart,
  })  : _getProducts = getProducts,
        _addToCart = addToCart,
        super(const ProductState.initial()) {
    on<_Load>(_onLoad);
    on<_Search>(_onSearch);
    on<_AddToCart>(_onAddToCart);
  }

  Future<void> _onLoad(_Load event, Emitter<ProductState> emit) async {
    emit(const ProductState.loading());
    final result = await _getProducts(GetProductsParams(category: event.category));
    result.fold(
      (failure) => emit(ProductState.error(failure.message)),
      (products) => emit(ProductState.loaded(
        products: products,
        activeCategory: event.category,
      )),
    );
  }
}
```

### 2. Riverpod Provider Pattern

```dart
// Providers — declarative dependency injection
final orderRepositoryProvider = Provider<OrderRepository>((ref) {
  return OrderRepositoryImpl(
    remote: ref.watch(orderRemoteDataSourceProvider),
    local: ref.watch(orderLocalDataSourceProvider),
    networkInfo: ref.watch(networkInfoProvider),
  );
});

final ordersProvider = FutureProvider.autoDispose<List<Order>>((ref) async {
  final repo = ref.watch(orderRepositoryProvider);
  final result = await repo.getOrders();
  return result.fold(
    (failure) => throw failure,
    (orders) => orders,
  );
});

// AsyncNotifier for complex state
class OrderNotifier extends AutoDisposeAsyncNotifier<List<Order>> {
  @override
  Future<List<Order>> build() async {
    final repo = ref.watch(orderRepositoryProvider);
    final result = await repo.getOrders();
    return result.fold((f) => throw f, (orders) => orders);
  }

  Future<void> placeOrder(PlaceOrderCommand command) async {
    state = const AsyncLoading();
    final repo = ref.read(orderRepositoryProvider);
    final result = await repo.placeOrder(command);
    result.fold(
      (failure) => state = AsyncError(failure, StackTrace.current),
      (_) => ref.invalidateSelf(),
    );
  }
}

final orderNotifierProvider =
    AutoDisposeAsyncNotifierProvider<OrderNotifier, List<Order>>(OrderNotifier.new);

// Widget — consuming providers
class OrdersPage extends ConsumerWidget {
  const OrdersPage({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final ordersAsync = ref.watch(orderNotifierProvider);

    return ordersAsync.when(
      loading: () => const Center(child: CircularProgressIndicator.adaptive()),
      error: (error, stack) => ErrorDisplay(
        message: error.toString(),
        onRetry: () => ref.invalidate(orderNotifierProvider),
      ),
      data: (orders) => OrdersList(orders: orders),
    );
  }
}
```

### 3. Use Case / Interactor Pattern

```dart
// Abstract use case with Either return type
abstract class UseCase<T, Params> {
  Future<Either<Failure, T>> call(Params params);
}

class NoParams {
  const NoParams();
}

// Concrete use case — single responsibility
class GetOrderById implements UseCase<Order, String> {
  final OrderRepository _repository;

  const GetOrderById(this._repository);

  @override
  Future<Either<Failure, Order>> call(String id) {
    return _repository.getOrderById(id);
  }
}

// Use case with validation
class PlaceOrder implements UseCase<Order, PlaceOrderCommand> {
  final OrderRepository _repository;
  final PaymentService _paymentService;

  const PlaceOrder(this._repository, this._paymentService);

  @override
  Future<Either<Failure, Order>> call(PlaceOrderCommand params) async {
    // Validate
    if (params.items.isEmpty) {
      return Left(ValidationFailure('Order must have at least one item'));
    }

    // Process payment
    final paymentResult = await _paymentService.charge(params.total);
    if (paymentResult.isLeft()) return paymentResult.map((_) => throw 'unreachable');

    // Create order
    return _repository.placeOrder(params);
  }
}
```

### 4. Freezed Models — Immutable Domain Objects

```dart
@freezed
class User with _$User {
  const User._(); // Private constructor for custom methods

  const factory User({
    required String id,
    required String name,
    required String email,
    required UserRole role,
    DateTime? lastLoginAt,
    @Default([]) List<String> permissions,
  }) = _User;

  // Custom computed properties
  bool get isAdmin => role == UserRole.admin;
  String get displayName => name.isNotEmpty ? name : email;
}

enum UserRole {
  admin,
  editor,
  viewer;

  String get label => switch (this) {
    admin => 'Administrator',
    editor => 'Editor',
    viewer => 'Viewer',
  };
}
```

### 5. Error Handling with Either (dartz / fpdart)

```dart
// Domain failures — typed, not string-based
abstract class Failure {
  final String message;
  const Failure(this.message);
}

class ServerFailure extends Failure {
  final int? statusCode;
  const ServerFailure(super.message, {this.statusCode});
}

class CacheFailure extends Failure {
  const CacheFailure(super.message);
}

class ValidationFailure extends Failure {
  final Map<String, String> fieldErrors;
  const ValidationFailure(super.message, {this.fieldErrors = const {}});
}

class NetworkFailure extends Failure {
  const NetworkFailure(super.message);
}

// Repository returns Either — no exceptions escape
@override
Future<Either<Failure, List<Order>>> getOrders() async {
  try {
    if (!await _networkInfo.isConnected) {
      final cached = await _local.getCachedOrders();
      return Right(cached.map((m) => m.toDomain()).toList());
    }
    final models = await _remote.getOrders();
    await _local.cacheOrders(models);
    return Right(models.map((m) => m.toDomain()).toList());
  } on ServerException catch (e) {
    return Left(ServerFailure(e.message, statusCode: e.statusCode));
  } on CacheException catch (e) {
    return Left(CacheFailure(e.message));
  } catch (e) {
    return Left(ServerFailure('Unexpected error: $e'));
  }
}
```

### 6. GoRouter — Declarative Navigation

```dart
final routerProvider = Provider<GoRouter>((ref) {
  final authState = ref.watch(authStateProvider);

  return GoRouter(
    initialLocation: '/',
    redirect: (context, state) {
      final isLoggedIn = authState.isAuthenticated;
      final isLoginRoute = state.matchedLocation == '/login';

      if (!isLoggedIn && !isLoginRoute) return '/login';
      if (isLoggedIn && isLoginRoute) return '/';
      return null;
    },
    routes: [
      GoRoute(
        path: '/',
        builder: (context, state) => const HomePage(),
        routes: [
          GoRoute(
            path: 'orders',
            builder: (context, state) => const OrdersPage(),
            routes: [
              GoRoute(
                path: ':id',
                builder: (context, state) => OrderDetailPage(
                  orderId: state.pathParameters['id']!,
                ),
              ),
            ],
          ),
        ],
      ),
      GoRoute(
        path: '/login',
        builder: (context, state) => const LoginPage(),
      ),
    ],
  );
});
```

### 7. Responsive & Adaptive Widgets

```dart
// Breakpoint-aware layout
class BreakpointLayout extends StatelessWidget {
  final Widget Function(BuildContext) mobile;
  final Widget Function(BuildContext)? tablet;
  final Widget Function(BuildContext)? desktop;

  const BreakpointLayout({
    super.key,
    required this.mobile,
    this.tablet,
    this.desktop,
  });

  static const mobileBreakpoint = 600.0;
  static const tabletBreakpoint = 1200.0;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        if (constraints.maxWidth >= tabletBreakpoint && desktop != null) {
          return desktop!(context);
        }
        if (constraints.maxWidth >= mobileBreakpoint && tablet != null) {
          return tablet!(context);
        }
        return mobile(context);
      },
    );
  }
}

// Platform-adaptive dialog
Future<bool?> showAdaptiveConfirmDialog(
  BuildContext context, {
  required String title,
  required String content,
}) {
  if (Platform.isIOS) {
    return showCupertinoDialog<bool>(
      context: context,
      builder: (context) => CupertinoAlertDialog(
        title: Text(title),
        content: Text(content),
        actions: [
          CupertinoDialogAction(
            isDestructiveAction: true,
            onPressed: () => Navigator.pop(context, false),
            child: const Text('Cancel'),
          ),
          CupertinoDialogAction(
            onPressed: () => Navigator.pop(context, true),
            child: const Text('Confirm'),
          ),
        ],
      ),
    );
  }

  return showDialog<bool>(
    context: context,
    builder: (context) => AlertDialog(
      title: Text(title),
      content: Text(content),
      actions: [
        TextButton(onPressed: () => Navigator.pop(context, false), child: const Text('Cancel')),
        FilledButton(onPressed: () => Navigator.pop(context, true), child: const Text('Confirm')),
      ],
    ),
  );
}
```

### 8. Theme System

```dart
class AppTheme {
  static ThemeData light() => ThemeData(
    useMaterial3: true,
    colorSchemeSeed: const Color(0xFF1A73E8),
    brightness: Brightness.light,
    textTheme: _textTheme,
    inputDecorationTheme: _inputDecoration,
    cardTheme: const CardTheme(elevation: 0, shape: RoundedRectangleBorder(
      borderRadius: BorderRadius.all(Radius.circular(12)),
    )),
  );

  static ThemeData dark() => ThemeData(
    useMaterial3: true,
    colorSchemeSeed: const Color(0xFF1A73E8),
    brightness: Brightness.dark,
    textTheme: _textTheme,
    inputDecorationTheme: _inputDecoration,
  );

  static const _textTheme = TextTheme(
    headlineLarge: TextStyle(fontWeight: FontWeight.w700),
    titleMedium: TextStyle(fontWeight: FontWeight.w600),
    bodyMedium: TextStyle(height: 1.5),
  );

  static const _inputDecoration = InputDecorationTheme(
    border: OutlineInputBorder(borderRadius: BorderRadius.all(Radius.circular(8))),
    filled: true,
  );
}
```

## Testing Patterns

### Widget Test with mocktail

```dart
void main() {
  late MockOrderBloc mockBloc;

  setUp(() {
    mockBloc = MockOrderBloc();
  });

  testWidgets('shows loading indicator when loading', (tester) async {
    when(() => mockBloc.state).thenReturn(const OrderState.loading());

    await tester.pumpWidget(
      MaterialApp(
        home: BlocProvider<OrderBloc>.value(
          value: mockBloc,
          child: const OrdersPage(),
        ),
      ),
    );

    expect(find.byType(CircularProgressIndicator), findsOneWidget);
  });

  testWidgets('shows error message with retry button', (tester) async {
    when(() => mockBloc.state).thenReturn(
      const OrderState.error('Network error'),
    );

    await tester.pumpWidget(
      MaterialApp(
        home: BlocProvider<OrderBloc>.value(
          value: mockBloc,
          child: const OrdersPage(),
        ),
      ),
    );

    expect(find.text('Network error'), findsOneWidget);
    expect(find.text('Retry'), findsOneWidget);
  });
}
```

### Golden Tests

```dart
testWidgets('OrderCard renders correctly', (tester) async {
  await tester.pumpWidget(
    MaterialApp(
      home: Scaffold(
        body: OrderCard(order: testOrder),
      ),
    ),
  );

  await expectLater(
    find.byType(OrderCard),
    matchesGoldenFile('goldens/order_card.png'),
  );
});
```

## Best Practices

✅ Use `const` constructors everywhere for performance
✅ Prefer `StatelessWidget` — only `StatefulWidget` when needed
✅ `freezed` for all domain models (immutable, generated equality)
✅ `Either<Failure, T>` for error handling — no exceptions across layers
✅ Feature-first folder structure (not layer-first)
✅ BLoC or Riverpod for state management — pick one per project
✅ Widget tests for all critical UI components
✅ `very_good_analysis` for strict linting
✅ Support light + dark themes from day one
✅ Accessibility: `Semantics`, sufficient contrast, screen reader labels

## Anti-Patterns

❌ Business logic in widgets
❌ `setState` for complex state flows
❌ Mutable models without `freezed`
❌ Deep widget trees without extraction
❌ Ignoring `const` constructors
❌ Hard-coded strings (use `l10n`)
❌ `print()` instead of proper logging
❌ Blocking UI thread with heavy computation
❌ Single massive `lib/` without feature folders
❌ Skipping widget tests

## Example Prompts

- "Design a Flutter feature with BLoC, freezed models, and offline-first"
- "Write widget tests and BLoC tests for this order management feature"
- "Refactor this StatefulWidget to use Riverpod with proper separation"
- "Create a responsive, adaptive layout for iOS and Android"

## Related Skills

- [Flutter & iOS Expert Agent](../../agents/flutter-ios-expert.agent.md)
- [Clean Code](../software-engineering/clean-code.md)
- [Design Patterns](../software-engineering/design-patterns.md)
- [Testing Strategies](../software-engineering/testing-strategies.md)
- [Anti-Patterns](../anti-patterns/SKILL.md)
