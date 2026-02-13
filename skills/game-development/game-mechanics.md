````skill
# Game Mechanics & Systems

## Instructions for AI

Apply these game mechanics patterns when implementing physics, AI behaviors, procedural generation, collision systems, and interactive game systems. Use concrete, engine-agnostic patterns that can be adapted to Godot, Phaser, Unity, PyGame, or custom engines.

## Physics & Movement

### Platformer Physics — The Good Feel

```gdscript
# Responsive 2D platformer controller with coyote time and input buffering
extends CharacterBody2D

@export_group("Movement")
@export var max_speed := 300.0
@export var acceleration := 2000.0
@export var friction := 1800.0
@export var air_friction := 200.0

@export_group("Jumping")
@export var jump_force := -450.0
@export var gravity := 1200.0
@export var fall_gravity_multiplier := 1.6    # Snappier fall
@export var max_fall_speed := 600.0
@export var coyote_time := 0.1                # Forgiveness window
@export var jump_buffer_time := 0.12          # Input buffering

var coyote_timer := 0.0
var jump_buffer_timer := 0.0
var was_on_floor := false

func _physics_process(delta: float) -> void:
    _apply_gravity(delta)
    _handle_horizontal(delta)
    _handle_jump(delta)
    move_and_slide()
    _update_timers(delta)

func _apply_gravity(delta: float) -> void:
    if not is_on_floor():
        var grav := gravity
        # Heavier gravity when falling → snappy arc
        if velocity.y > 0:
            grav *= fall_gravity_multiplier
        # Variable jump height: release jump early → fall faster
        elif velocity.y < 0 and not Input.is_action_pressed("jump"):
            grav *= 2.0
        velocity.y = minf(velocity.y + grav * delta, max_fall_speed)

func _handle_horizontal(delta: float) -> void:
    var input_dir := Input.get_axis("move_left", "move_right")
    if input_dir != 0:
        velocity.x = move_toward(velocity.x, input_dir * max_speed, acceleration * delta)
    else:
        var fric := friction if is_on_floor() else air_friction
        velocity.x = move_toward(velocity.x, 0, fric * delta)

func _handle_jump(delta: float) -> void:
    # Coyote time: can still jump shortly after leaving ledge
    if was_on_floor and not is_on_floor():
        coyote_timer = coyote_time
    was_on_floor = is_on_floor()

    # Buffer jump input
    if Input.is_action_just_pressed("jump"):
        jump_buffer_timer = jump_buffer_time

    # Execute jump if conditions met
    var can_jump := is_on_floor() or coyote_timer > 0
    if jump_buffer_timer > 0 and can_jump:
        velocity.y = jump_force
        coyote_timer = 0
        jump_buffer_timer = 0

func _update_timers(delta: float) -> void:
    coyote_timer = maxf(coyote_timer - delta, 0)
    jump_buffer_timer = maxf(jump_buffer_timer - delta, 0)
```

### Top-Down Movement with Steering

```typescript
// Smooth top-down movement with acceleration and steering behaviors
interface Vec2 { x: number; y: number; }

class TopDownController {
  position: Vec2 = { x: 0, y: 0 };
  velocity: Vec2 = { x: 0, y: 0 };

  constructor(
    private maxSpeed: number = 200,
    private acceleration: number = 800,
    private friction: number = 600
  ) {}

  update(inputDir: Vec2, delta: number): void {
    const magnitude = Math.sqrt(inputDir.x ** 2 + inputDir.y ** 2);

    if (magnitude > 0.1) {
      // Normalize input
      const nx = inputDir.x / magnitude;
      const ny = inputDir.y / magnitude;
      // Accelerate toward input direction
      this.velocity.x = this.moveToward(this.velocity.x, nx * this.maxSpeed, this.acceleration * delta);
      this.velocity.y = this.moveToward(this.velocity.y, ny * this.maxSpeed, this.acceleration * delta);
    } else {
      // Apply friction when no input
      this.velocity.x = this.moveToward(this.velocity.x, 0, this.friction * delta);
      this.velocity.y = this.moveToward(this.velocity.y, 0, this.friction * delta);
    }

    this.position.x += this.velocity.x * delta;
    this.position.y += this.velocity.y * delta;
  }

  private moveToward(current: number, target: number, maxDelta: number): number {
    if (Math.abs(target - current) <= maxDelta) return target;
    return current + Math.sign(target - current) * maxDelta;
  }
}
```

## AI Behaviors

### Finite State Machine (Enemy AI)

```python
# Clean FSM for enemy AI — extensible and testable
from enum import Enum, auto
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class AIContext:
    """Shared data that all states can read/write."""
    position: tuple[float, float]
    target_position: tuple[float, float] | None
    health: float
    detection_range: float = 200.0
    attack_range: float = 50.0

class AIState(ABC):
    @abstractmethod
    def enter(self, ctx: AIContext) -> None: ...
    
    @abstractmethod
    def update(self, ctx: AIContext, delta: float) -> "AIState | None":
        """Return new state to transition, or None to stay."""
        ...
    
    @abstractmethod
    def exit(self, ctx: AIContext) -> None: ...

class PatrolState(AIState):
    def __init__(self, waypoints: list[tuple[float, float]]):
        self.waypoints = waypoints
        self.current_wp = 0

    def enter(self, ctx: AIContext) -> None:
        pass  # Start patrol animation

    def update(self, ctx: AIContext, delta: float) -> AIState | None:
        # Move toward current waypoint
        target = self.waypoints[self.current_wp]
        dist = distance(ctx.position, target)
        
        if dist < 5.0:
            self.current_wp = (self.current_wp + 1) % len(self.waypoints)
        
        # Transition: player detected → chase
        if ctx.target_position and distance(ctx.position, ctx.target_position) < ctx.detection_range:
            return ChaseState()
        
        return None

    def exit(self, ctx: AIContext) -> None:
        pass

class ChaseState(AIState):
    def enter(self, ctx: AIContext) -> None:
        pass  # Play alert animation, sound

    def update(self, ctx: AIContext, delta: float) -> AIState | None:
        if ctx.target_position is None:
            return PatrolState(default_waypoints)
        
        dist = distance(ctx.position, ctx.target_position)
        
        # Move toward player
        move_toward(ctx, ctx.target_position, 150.0 * delta)
        
        # Close enough to attack
        if dist < ctx.attack_range:
            return AttackState()
        
        # Lost the player
        if dist > ctx.detection_range * 1.5:
            return PatrolState(default_waypoints)
        
        return None

    def exit(self, ctx: AIContext) -> None:
        pass

class EnemyAI:
    def __init__(self, initial_state: AIState, context: AIContext):
        self.state = initial_state
        self.ctx = context
        self.state.enter(self.ctx)

    def update(self, delta: float) -> None:
        new_state = self.state.update(self.ctx, delta)
        if new_state is not None:
            self.state.exit(self.ctx)
            self.state = new_state
            self.state.enter(self.ctx)
```

### Behavior Tree (Complex AI)

```typescript
// Behavior Tree nodes for composable AI logic
type BTStatus = 'success' | 'failure' | 'running';

abstract class BTNode {
  abstract tick(context: AIContext): BTStatus;
}

// Composites
class Sequence extends BTNode {
  constructor(private children: BTNode[]) { super(); }

  tick(context: AIContext): BTStatus {
    for (const child of this.children) {
      const status = child.tick(context);
      if (status !== 'success') return status; // Fail or running → stop
    }
    return 'success'; // All succeeded
  }
}

class Selector extends BTNode {
  constructor(private children: BTNode[]) { super(); }

  tick(context: AIContext): BTStatus {
    for (const child of this.children) {
      const status = child.tick(context);
      if (status !== 'failure') return status; // Success or running → stop
    }
    return 'failure'; // All failed
  }
}

// Conditions
class IsPlayerInRange extends BTNode {
  constructor(private range: number) { super(); }

  tick(context: AIContext): BTStatus {
    return context.distanceToPlayer < this.range ? 'success' : 'failure';
  }
}

class IsHealthLow extends BTNode {
  constructor(private threshold: number = 0.3) { super(); }

  tick(context: AIContext): BTStatus {
    return context.healthPercent < this.threshold ? 'success' : 'failure';
  }
}

// Actions
class ChasePlayer extends BTNode {
  tick(context: AIContext): BTStatus {
    context.moveToward(context.playerPosition, context.chaseSpeed);
    return context.distanceToPlayer < context.attackRange ? 'success' : 'running';
  }
}

class AttackPlayer extends BTNode {
  tick(context: AIContext): BTStatus {
    context.performAttack();
    return 'success';
  }
}

class Flee extends BTNode {
  tick(context: AIContext): BTStatus {
    context.moveAwayFrom(context.playerPosition, context.fleeSpeed);
    return context.distanceToPlayer > context.safeDistance ? 'success' : 'running';
  }
}

// Usage: Composing a smart enemy
const enemyBrain = new Selector([
  // Priority 1: Flee when health is low
  new Sequence([new IsHealthLow(0.2), new Flee()]),
  // Priority 2: Attack when in range
  new Sequence([new IsPlayerInRange(50), new AttackPlayer()]),
  // Priority 3: Chase when player detected
  new Sequence([new IsPlayerInRange(200), new ChasePlayer()]),
  // Default: Patrol
  new Patrol(),
]);
```

## Procedural Generation

### BSP Dungeon Generator

```python
from dataclasses import dataclass
from random import randint, random

@dataclass
class Rect:
    x: int
    y: int
    w: int
    h: int

    @property
    def center(self) -> tuple[int, int]:
        return (self.x + self.w // 2, self.y + self.h // 2)

class BSPDungeon:
    """Binary Space Partitioning dungeon generator."""

    def __init__(self, width: int, height: int, min_room_size: int = 6):
        self.width = width
        self.height = height
        self.min_room_size = min_room_size
        self.rooms: list[Rect] = []
        self.grid = [['#'] * width for _ in range(height)]

    def generate(self, max_depth: int = 5) -> list[list[str]]:
        root = Rect(1, 1, self.width - 2, self.height - 2)
        self._split(root, max_depth)
        self._connect_rooms()
        return self.grid

    def _split(self, area: Rect, depth: int) -> None:
        if depth == 0 or area.w < self.min_room_size * 2 or area.h < self.min_room_size * 2:
            self._place_room(area)
            return

        if area.w > area.h:
            split = randint(self.min_room_size, area.w - self.min_room_size)
            self._split(Rect(area.x, area.y, split, area.h), depth - 1)
            self._split(Rect(area.x + split, area.y, area.w - split, area.h), depth - 1)
        else:
            split = randint(self.min_room_size, area.h - self.min_room_size)
            self._split(Rect(area.x, area.y, area.w, split), depth - 1)
            self._split(Rect(area.x, area.y + split, area.w, area.h - split), depth - 1)

    def _place_room(self, area: Rect) -> None:
        margin = 1
        room = Rect(
            area.x + margin,
            area.y + margin,
            max(3, area.w - margin * 2 - randint(0, 3)),
            max(3, area.h - margin * 2 - randint(0, 3)),
        )
        for y in range(room.y, room.y + room.h):
            for x in range(room.x, room.x + room.w):
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.grid[y][x] = '.'
        self.rooms.append(room)

    def _connect_rooms(self) -> None:
        for i in range(len(self.rooms) - 1):
            cx1, cy1 = self.rooms[i].center
            cx2, cy2 = self.rooms[i + 1].center
            # L-shaped corridor
            if random() > 0.5:
                self._h_corridor(cx1, cx2, cy1)
                self._v_corridor(cy1, cy2, cx2)
            else:
                self._v_corridor(cy1, cy2, cx1)
                self._h_corridor(cx1, cx2, cy2)

    def _h_corridor(self, x1: int, x2: int, y: int) -> None:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[y][x] = '.'

    def _v_corridor(self, y1: int, y2: int, x: int) -> None:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[y][x] = '.'
```

### Wave Function Collapse (Simplified)

```typescript
// Simplified WFC for tile-based level generation
interface TileRule {
  tile: string;
  allowedNeighbors: {
    up: string[];
    down: string[];
    left: string[];
    right: string[];
  };
  weight: number; // How likely this tile is chosen
}

class WaveFunctionCollapse {
  private grid: (string | null)[][];
  private possibilities: Set<string>[][];

  constructor(
    private width: number,
    private height: number,
    private rules: TileRule[]
  ) {
    const allTiles = rules.map(r => r.tile);
    this.grid = Array.from({ length: height }, () => Array(width).fill(null));
    this.possibilities = Array.from({ length: height }, () =>
      Array.from({ length: width }, () => new Set(allTiles))
    );
  }

  generate(): string[][] {
    while (this.hasUncollapsed()) {
      const [x, y] = this.findLowestEntropy();
      this.collapse(x, y);
      this.propagate(x, y);
    }
    return this.grid as string[][];
  }

  private hasUncollapsed(): boolean {
    return this.grid.some(row => row.some(cell => cell === null));
  }

  private findLowestEntropy(): [number, number] {
    let minEntropy = Infinity;
    let candidates: [number, number][] = [];

    for (let y = 0; y < this.height; y++) {
      for (let x = 0; x < this.width; x++) {
        if (this.grid[y][x] !== null) continue;
        const entropy = this.possibilities[y][x].size;
        if (entropy < minEntropy) {
          minEntropy = entropy;
          candidates = [[x, y]];
        } else if (entropy === minEntropy) {
          candidates.push([x, y]);
        }
      }
    }
    return candidates[Math.floor(Math.random() * candidates.length)];
  }

  private collapse(x: number, y: number): void {
    const possible = [...this.possibilities[y][x]];
    // Weighted random selection
    const weights = possible.map(t => this.rules.find(r => r.tile === t)!.weight);
    const totalWeight = weights.reduce((a, b) => a + b, 0);
    let r = Math.random() * totalWeight;
    for (let i = 0; i < possible.length; i++) {
      r -= weights[i];
      if (r <= 0) {
        this.grid[y][x] = possible[i];
        this.possibilities[y][x] = new Set([possible[i]]);
        return;
      }
    }
    this.grid[y][x] = possible[possible.length - 1];
  }

  private propagate(x: number, y: number): void {
    const stack: [number, number][] = [[x, y]];
    while (stack.length > 0) {
      const [cx, cy] = stack.pop()!;
      const currentPossible = this.possibilities[cy][cx];
      const neighbors: [number, number, keyof TileRule['allowedNeighbors']][] = [
        [cx, cy - 1, 'up'], [cx, cy + 1, 'down'],
        [cx - 1, cy, 'left'], [cx + 1, cy, 'right'],
      ];

      for (const [nx, ny, dir] of neighbors) {
        if (nx < 0 || nx >= this.width || ny < 0 || ny >= this.height) continue;
        if (this.grid[ny][nx] !== null) continue;

        const allowed = new Set<string>();
        for (const tile of currentPossible) {
          const rule = this.rules.find(r => r.tile === tile)!;
          for (const neighbor of rule.allowedNeighbors[dir]) {
            allowed.add(neighbor);
          }
        }

        const neighborPossible = this.possibilities[ny][nx];
        const before = neighborPossible.size;
        for (const tile of [...neighborPossible]) {
          if (!allowed.has(tile)) neighborPossible.delete(tile);
        }
        if (neighborPossible.size < before) {
          stack.push([nx, ny]); // Re-propagate
        }
      }
    }
  }
}
```

## Collision & Spatial Systems

### Spatial Hash Grid

```typescript
// O(1) broad-phase collision detection using spatial hashing
class SpatialHashGrid<T extends { x: number; y: number; width: number; height: number }> {
  private cells = new Map<string, Set<T>>();

  constructor(private cellSize: number = 64) {}

  private getKey(cx: number, cy: number): string {
    return `${cx},${cy}`;
  }

  private getCells(entity: T): [number, number][] {
    const cells: [number, number][] = [];
    const startX = Math.floor(entity.x / this.cellSize);
    const startY = Math.floor(entity.y / this.cellSize);
    const endX = Math.floor((entity.x + entity.width) / this.cellSize);
    const endY = Math.floor((entity.y + entity.height) / this.cellSize);

    for (let cx = startX; cx <= endX; cx++) {
      for (let cy = startY; cy <= endY; cy++) {
        cells.push([cx, cy]);
      }
    }
    return cells;
  }

  insert(entity: T): void {
    for (const [cx, cy] of this.getCells(entity)) {
      const key = this.getKey(cx, cy);
      if (!this.cells.has(key)) this.cells.set(key, new Set());
      this.cells.get(key)!.add(entity);
    }
  }

  query(entity: T): Set<T> {
    const nearby = new Set<T>();
    for (const [cx, cy] of this.getCells(entity)) {
      const cell = this.cells.get(this.getKey(cx, cy));
      if (cell) {
        for (const other of cell) {
          if (other !== entity) nearby.add(other);
        }
      }
    }
    return nearby;
  }

  clear(): void {
    this.cells.clear();
  }
}
```

## A* Pathfinding

```python
import heapq
from dataclasses import dataclass, field

@dataclass(order=True)
class AStarNode:
    f_cost: float
    position: tuple[int, int] = field(compare=False)
    g_cost: float = field(default=0.0, compare=False)
    parent: "AStarNode | None" = field(default=None, compare=False)

def astar(
    grid: list[list[int]],
    start: tuple[int, int],
    goal: tuple[int, int],
    allow_diagonal: bool = True,
) -> list[tuple[int, int]]:
    """A* pathfinding on a 2D grid. 0 = walkable, 1 = wall."""
    rows, cols = len(grid), len(grid[0])

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    if allow_diagonal:
        directions += [(1, 1), (1, -1), (-1, 1), (-1, -1)]

    def heuristic(a: tuple[int, int], b: tuple[int, int]) -> float:
        return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

    open_set: list[AStarNode] = []
    start_node = AStarNode(f_cost=heuristic(start, goal), position=start, g_cost=0)
    heapq.heappush(open_set, start_node)
    closed_set: set[tuple[int, int]] = set()

    while open_set:
        current = heapq.heappop(open_set)

        if current.position == goal:
            path = []
            node: AStarNode | None = current
            while node:
                path.append(node.position)
                node = node.parent
            return list(reversed(path))

        closed_set.add(current.position)

        for dx, dy in directions:
            nx, ny = current.position[0] + dx, current.position[1] + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in closed_set:
                move_cost = 1.414 if abs(dx) + abs(dy) == 2 else 1.0
                g = current.g_cost + move_cost
                f = g + heuristic((nx, ny), goal)
                neighbor = AStarNode(f_cost=f, position=(nx, ny), g_cost=g, parent=current)
                heapq.heappush(open_set, neighbor)

    return []  # No path found
```

## Best Practices

✅ Use delta time for ALL movement calculations — never frame-dependent code
✅ Implement coyote time (80-120ms) and input buffering (100-150ms) for platformers
✅ Choose the right AI pattern: FSM for simple, Behavior Trees for complex, Utility AI for emergent
✅ Use spatial partitioning for collision (hash grid, quadtree) — never N² checks
✅ Make procedural generation seeded for reproducibility and debugging
✅ Separate physics from rendering (fixed timestep for physics, variable for rendering)

## Anti-Patterns

❌ Frame-dependent movement (`position += speed` instead of `position += speed * delta`)
❌ N² collision checks without broad phase
❌ Hard-coded magic numbers for physics values
❌ AI that cheats (perfect knowledge) instead of being smart within constraints
❌ Generating entire levels at once instead of streaming/chunking for large worlds
❌ Mixing physics logic with rendering logic

## Example Prompts

"Implement a platformer controller with coyote time, input buffering, and wall sliding"

"Build an enemy AI with patrol, chase, and attack states using a behavior tree"

"Create a procedural dungeon generator with BSP and corridor connections"

"Implement A* pathfinding with diagonal movement and path smoothing"

"Build a spatial hash grid for efficient 2D collision detection"

## Related Skills

- `game-development/game-design.md` — Design principles and balancing
- `game-development/game-architecture.md` — ECS, event systems, scene management
- `game-development/prototyping.md` — Rapid prototyping patterns

## References

- [Game Programming Patterns — Robert Nystrom](https://gameprogrammingpatterns.com/)
- [Red Blob Games — Amit Patel](https://www.redblobgames.com/)
- [AI for Games — Ian Millington](https://www.ai4g.com/)
- [Fix Your Timestep — Glenn Fiedler](https://gafferongames.com/post/fix_your_timestep/)
````
