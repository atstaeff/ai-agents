---
name: frontend-patterns
description: Modern frontend patterns, TypeScript best practices, and production-grade standards for Vue.js and Angular
---

# Frontend Patterns Skill

## Instructions for AI

Apply modern frontend patterns, TypeScript best practices, and production-grade standards for Vue.js and Angular applications. Use this skill when writing, reviewing, or refactoring frontend code.

## Core Patterns

### 1. Composable / Hook Pattern (Vue)

Extract reusable stateful logic into composable functions.

```typescript
import { ref, computed, onUnmounted, type Ref } from 'vue'

interface UsePaginationOptions {
  pageSize?: number
  initialPage?: number
}

interface UsePaginationReturn<T> {
  currentPage: Ref<number>
  pageSize: Ref<number>
  totalPages: Ref<number>
  paginatedItems: Ref<T[]>
  next: () => void
  prev: () => void
  goTo: (page: number) => void
}

export function usePagination<T>(
  items: Ref<T[]>,
  options: UsePaginationOptions = {}
): UsePaginationReturn<T> {
  const currentPage = ref(options.initialPage ?? 1)
  const pageSize = ref(options.pageSize ?? 10)

  const totalPages = computed(() =>
    Math.ceil(items.value.length / pageSize.value)
  )

  const paginatedItems = computed(() => {
    const start = (currentPage.value - 1) * pageSize.value
    return items.value.slice(start, start + pageSize.value)
  })

  const goTo = (page: number) => {
    currentPage.value = Math.max(1, Math.min(page, totalPages.value))
  }

  const next = () => goTo(currentPage.value + 1)
  const prev = () => goTo(currentPage.value - 1)

  return { currentPage, pageSize, totalPages, paginatedItems, next, prev, goTo }
}
```

### 2. Service Injection Pattern (Angular)

Typed, injectable services with clean separation of concerns.

```typescript
import { Injectable, inject } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Observable, catchError, map } from 'rxjs'

export interface User {
  id: string
  name: string
  email: string
  role: 'admin' | 'user' | 'viewer'
}

type CreateUserDTO = Omit<User, 'id'>

@Injectable({ providedIn: 'root' })
export class UserService {
  private readonly http = inject(HttpClient)
  private readonly baseUrl = '/api/users'

  getAll(): Observable<User[]> {
    return this.http.get<User[]>(this.baseUrl)
  }

  getById(id: string): Observable<User> {
    return this.http.get<User>(`${this.baseUrl}/${id}`)
  }

  create(dto: CreateUserDTO): Observable<User> {
    return this.http.post<User>(this.baseUrl, dto)
  }

  update(id: string, dto: Partial<CreateUserDTO>): Observable<User> {
    return this.http.patch<User>(`${this.baseUrl}/${id}`, dto)
  }

  delete(id: string): Observable<void> {
    return this.http.delete<void>(`${this.baseUrl}/${id}`)
  }
}
```

### 3. Store Pattern (Pinia)

Type-safe, composable state management.

```typescript
import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import type { User } from '@/types'
import { userApi } from '@/services/userApi'

export const useUserStore = defineStore('users', () => {
  // State
  const users = ref<User[]>([])
  const loading = ref(false)
  const error = ref<string | null>(null)
  const selectedUserId = ref<string | null>(null)

  // Getters
  const selectedUser = computed(() =>
    users.value.find(u => u.id === selectedUserId.value) ?? null
  )

  const userCount = computed(() => users.value.length)

  const usersByRole = computed(() =>
    users.value.reduce<Record<string, User[]>>((acc, user) => {
      ;(acc[user.role] ??= []).push(user)
      return acc
    }, {})
  )

  // Actions
  async function fetchUsers(): Promise<void> {
    loading.value = true
    error.value = null
    try {
      users.value = await userApi.getAll()
    } catch (e) {
      error.value = e instanceof Error ? e.message : 'Failed to load users'
    } finally {
      loading.value = false
    }
  }

  function selectUser(id: string | null): void {
    selectedUserId.value = id
  }

  return {
    users, loading, error, selectedUserId,
    selectedUser, userCount, usersByRole,
    fetchUsers, selectUser,
  }
})
```

### 4. Signal Store Pattern (Angular with NgRx Signals)

```typescript
import { signalStore, withState, withComputed, withMethods, patchState } from '@ngrx/signals'
import { computed, inject } from '@angular/core'
import { UserService, type User } from './user.service'
import { rxMethod } from '@ngrx/signals/rxjs-interop'
import { pipe, switchMap, tap } from 'rxjs'

type UsersState = {
  users: User[]
  loading: boolean
  error: string | null
  filter: string
}

const initialState: UsersState = {
  users: [],
  loading: false,
  error: null,
  filter: '',
}

export const UsersStore = signalStore(
  withState(initialState),
  withComputed(({ users, filter }) => ({
    filteredUsers: computed(() =>
      users().filter(u => u.name.toLowerCase().includes(filter().toLowerCase()))
    ),
    userCount: computed(() => users().length),
  })),
  withMethods((store, userService = inject(UserService)) => ({
    setFilter(filter: string) {
      patchState(store, { filter })
    },
    loadUsers: rxMethod<void>(
      pipe(
        tap(() => patchState(store, { loading: true, error: null })),
        switchMap(() =>
          userService.getAll().pipe(
            tap({
              next: users => patchState(store, { users, loading: false }),
              error: err => patchState(store, { error: err.message, loading: false }),
            })
          )
        )
      )
    ),
  }))
)
```

### 5. Render Pattern — Smart vs. Dumb Components

```typescript
// ✅ Dumb/Presentational Component — Only receives props, emits events
// UserCard.vue
interface Props {
  user: User
  selected?: boolean
}

interface Emits {
  (e: 'select', userId: string): void
  (e: 'delete', userId: string): void
}

const props = withDefaults(defineProps<Props>(), { selected: false })
const emit = defineEmits<Emits>()

// ✅ Smart/Container Component — Manages state, passes to dumb components
// UserListPage.vue
const store = useUserStore()
const { users, loading, selectedUserId } = storeToRefs(store)

function handleSelect(userId: string) {
  store.selectUser(userId)
}

function handleDelete(userId: string) {
  store.deleteUser(userId)
}
```

### 6. Type-Safe Form Pattern (Vue)

```typescript
import { reactive, computed } from 'vue'
import { z } from 'zod'

const UserFormSchema = z.object({
  name: z.string().min(2, 'Name must be at least 2 characters'),
  email: z.string().email('Invalid email address'),
  role: z.enum(['admin', 'user', 'viewer']),
})

type UserFormData = z.infer<typeof UserFormSchema>

export function useForm<T extends z.ZodObject<any>>(schema: T) {
  type FormData = z.infer<T>

  const data = reactive<FormData>({} as FormData)
  const errors = reactive<Record<string, string>>({})
  const touched = reactive<Record<string, boolean>>({})

  const isValid = computed(() => {
    const result = schema.safeParse(data)
    return result.success
  })

  function validate(): boolean {
    const result = schema.safeParse(data)
    if (!result.success) {
      for (const issue of result.error.issues) {
        const field = issue.path.join('.')
        errors[field] = issue.message
      }
      return false
    }
    Object.keys(errors).forEach(key => delete errors[key])
    return true
  }

  function reset(initial: Partial<FormData> = {}): void {
    Object.assign(data, initial)
    Object.keys(errors).forEach(key => delete errors[key])
    Object.keys(touched).forEach(key => delete touched[key])
  }

  return { data, errors, touched, isValid, validate, reset }
}
```

### 7. Route Guard Pattern (Angular)

```typescript
import { inject } from '@angular/core'
import { Router, type CanActivateFn } from '@angular/router'
import { AuthService } from '@/core/services/auth.service'

export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService)
  const router = inject(Router)

  if (auth.isAuthenticated()) {
    return true
  }

  return router.createUrlTree(['/login'], {
    queryParams: { returnUrl: router.url },
  })
}

export const roleGuard = (...allowedRoles: string[]): CanActivateFn => {
  return () => {
    const auth = inject(AuthService)
    const router = inject(Router)

    if (auth.isAuthenticated() && allowedRoles.includes(auth.currentUser()?.role ?? '')) {
      return true
    }

    return router.createUrlTree(['/forbidden'])
  }
}

// Usage in routes
export const routes: Routes = [
  { path: 'admin', component: AdminPage, canActivate: [authGuard, roleGuard('admin')] },
  { path: 'dashboard', component: DashboardPage, canActivate: [authGuard] },
]
```

## Anti-Patterns to Avoid

### ❌ Prop Drilling

Pass state through many layers of components. **Fix:** Use provide/inject (Vue) or services (Angular).

### ❌ Massive Components

Single component files with 500+ lines. **Fix:** Extract composables, split into smart/dumb components.

### ❌ Using `any` in TypeScript

Disables type checking entirely. **Fix:** Use `unknown`, generics, or proper type narrowing.

### ❌ Direct DOM Manipulation

Using `document.querySelector` in frameworks. **Fix:** Use template refs, ViewChild, or framework APIs.

### ❌ Untyped API Responses

Trusting API responses without validation. **Fix:** Use Zod, io-ts, or class-validator for runtime validation.

### ❌ Subscribing Without Cleanup (Angular)

Memory leaks from unmanaged subscriptions. **Fix:** Use `takeUntilDestroyed()`, `toSignal()`, or `async` pipe.

## Testing Patterns

### Component Test with Testing Library

```typescript
import { render, screen, within } from '@testing-library/vue'
import userEvent from '@testing-library/user-event'
import { createTestingPinia } from '@pinia/testing'
import UserList from '@/components/UserList.vue'

describe('UserList', () => {
  const mockUsers = [
    { id: '1', name: 'Alice', email: 'alice@test.com', role: 'admin' },
    { id: '2', name: 'Bob', email: 'bob@test.com', role: 'user' },
  ]

  it('renders all users', () => {
    render(UserList, {
      props: { users: mockUsers },
      global: { plugins: [createTestingPinia()] },
    })

    expect(screen.getByText('Alice')).toBeInTheDocument()
    expect(screen.getByText('Bob')).toBeInTheDocument()
  })

  it('emits select event on user click', async () => {
    const user = userEvent.setup()
    const { emitted } = render(UserList, { props: { users: mockUsers } })

    await user.click(screen.getByText('Alice'))

    expect(emitted().select[0]).toEqual(['1'])
  })
})
```

### E2E Test with Playwright

```typescript
import { test, expect } from '@playwright/test'

test.describe('User Management', () => {
  test('should create a new user', async ({ page }) => {
    await page.goto('/users')

    await page.getByRole('button', { name: 'Add User' }).click()
    await page.getByLabel('Name').fill('Charlie')
    await page.getByLabel('Email').fill('charlie@test.com')
    await page.getByRole('combobox', { name: 'Role' }).selectOption('user')
    await page.getByRole('button', { name: 'Save' }).click()

    await expect(page.getByText('User created successfully')).toBeVisible()
    await expect(page.getByText('Charlie')).toBeVisible()
  })
})
```
