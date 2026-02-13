````skill
# Game Architecture Patterns

## Instructions for AI

Apply these architecture patterns when structuring game projects. Use Entity-Component-System (ECS) for data-driven games, scene-graph for hierarchy-heavy games, and event-driven decoupling for maintainable, testable game systems. Choose architecture based on game complexity and engine.

## Entity-Component-System (ECS)

ECS separates **data** (components) from **logic** (systems), enabling massive flexibility and performance.

### ECS Core Concepts

```
Entity     = Just an ID (number). No data, no logic.
Component  = Pure data. No methods. Attached to entities.
System     = Pure logic. Processes all entities with matching components.
```

### ECS Implementation

```typescript
// Lightweight ECS for web games
type Entity = number;

class World {
  private nextId: Entity = 0;
  private components = new Map<string, Map<Entity, any>>();
  private systems: System[] = [];

  createEntity(): Entity {
    return this.nextId++;
  }

  addComponent<T>(entity: Entity, type: string, data: T): void {
    if (!this.components.has(type)) {
      this.components.set(type, new Map());
    }
    this.components.get(type)!.set(entity, data);
  }

  getComponent<T>(entity: Entity, type: string): T | undefined {
    return this.components.get(type)?.get(entity);
  }

  removeComponent(entity: Entity, type: string): void {
    this.components.get(type)?.delete(entity);
  }

  destroyEntity(entity: Entity): void {
    for (const store of this.components.values()) {
      store.delete(entity);
    }
  }

  query(...componentTypes: string[]): Entity[] {
    const entities: Entity[] = [];
    const firstStore = this.components.get(componentTypes[0]);
    if (!firstStore) return entities;

    for (const entity of firstStore.keys()) {
      if (componentTypes.every(type => this.components.get(type)?.has(entity))) {
        entities.push(entity);
      }
    }
    return entities;
  }

  addSystem(system: System): void {
    this.systems.push(system);
  }

  update(delta: number): void {
    for (const system of this.systems) {
      system.update(this, delta);
    }
  }
}

interface System {
  update(world: World, delta: number): void;
}

// --- Components (pure data) ---
interface Position { x: number; y: number; }
interface Velocity { vx: number; vy: number; }
interface Sprite { texture: string; width: number; height: number; }
interface Health { current: number; max: number; }
interface Collider { width: number; height: number; layer: string; }

// --- Systems (pure logic) ---
class MovementSystem implements System {
  update(world: World, delta: number): void {
    for (const entity of world.query('position', 'velocity')) {
      const pos = world.getComponent<Position>(entity, 'position')!;
      const vel = world.getComponent<Velocity>(entity, 'velocity')!;
      pos.x += vel.vx * delta;
      pos.y += vel.vy * delta;
    }
  }
}

class RenderSystem implements System {
  constructor(private ctx: CanvasRenderingContext2D) {}

  update(world: World, _delta: number): void {
    for (const entity of world.query('position', 'sprite')) {
      const pos = world.getComponent<Position>(entity, 'position')!;
      const sprite = world.getComponent<Sprite>(entity, 'sprite')!;
      // Draw sprite at position
      this.ctx.drawImage(
        this.getTexture(sprite.texture),
        pos.x, pos.y, sprite.width, sprite.height
      );
    }
  }

  private getTexture(name: string): HTMLImageElement { /* asset manager lookup */ }
}

class DamageSystem implements System {
  update(world: World, _delta: number): void {
    for (const entity of world.query('health')) {
      const health = world.getComponent<Health>(entity, 'health')!;
      if (health.current <= 0) {
        world.destroyEntity(entity); // Or add 'dead' component for death animation
      }
    }
  }
}

// --- Usage ---
const world = new World();
world.addSystem(new MovementSystem());
world.addSystem(new DamageSystem());
world.addSystem(new RenderSystem(ctx));

// Create player entity
const player = world.createEntity();
world.addComponent(player, 'position', { x: 100, y: 200 });
world.addComponent(player, 'velocity', { vx: 0, vy: 0 });
world.addComponent(player, 'health', { current: 100, max: 100 });
world.addComponent(player, 'sprite', { texture: 'player', width: 32, height: 32 });

// Create enemy — same components, different data
const enemy = world.createEntity();
world.addComponent(enemy, 'position', { x: 400, y: 200 });
world.addComponent(enemy, 'velocity', { vx: -50, vy: 0 });
world.addComponent(enemy, 'health', { current: 30, max: 30 });
world.addComponent(enemy, 'sprite', { texture: 'slime', width: 24, height: 24 });
```

## Event Bus (Decoupled Communication)

```gdscript
# Godot Autoload — global event bus for decoupled game systems
# scripts/autoload/event_bus.gd
extends Node

# Game flow events
signal game_started
signal game_paused
signal game_over(reason: String)
signal level_completed(level_id: int, time: float, score: int)

# Player events
signal player_spawned(player: Node2D)
signal player_damaged(amount: int, source: Node2D)
signal player_healed(amount: int)
signal player_died

# Combat events
signal enemy_spawned(enemy: Node2D)
signal enemy_killed(enemy: Node2D, killer: Node2D)
signal damage_dealt(amount: int, target: Node2D, source: Node2D)

# Economy events
signal coin_collected(amount: int)
signal item_purchased(item_id: String, cost: int)
signal score_changed(new_score: int, delta: int)

# UI events
signal show_dialog(text: String, speaker: String)
signal show_notification(message: String, type: String)
signal achievement_unlocked(achievement_id: String)
```

```gdscript
# Usage — Systems connect to signals without knowing each other
# score_system.gd
extends Node

var score: int = 0

func _ready() -> void:
    EventBus.coin_collected.connect(_on_coin_collected)
    EventBus.enemy_killed.connect(_on_enemy_killed)

func _on_coin_collected(amount: int) -> void:
    score += amount * 10
    EventBus.score_changed.emit(score, amount * 10)

func _on_enemy_killed(_enemy: Node2D, _killer: Node2D) -> void:
    score += 100
    EventBus.score_changed.emit(score, 100)


# audio_system.gd — Reacts to game events, zero coupling
extends Node

func _ready() -> void:
    EventBus.coin_collected.connect(func(_a): play("coin_pickup"))
    EventBus.player_damaged.connect(func(_a, _b): play("player_hit"))
    EventBus.enemy_killed.connect(func(_a, _b): play("enemy_death"))
    EventBus.achievement_unlocked.connect(func(_a): play("achievement_fanfare"))
```

## Game Loop Architecture

### Fixed + Variable Timestep

```typescript
// Correct game loop: Fixed updates for physics, variable for rendering
class GameLoop {
  private lastTime = 0;
  private accumulator = 0;
  private readonly fixedDelta = 1 / 60; // 60Hz physics

  constructor(
    private update: (delta: number) => void,  // Physics/logic (fixed step)
    private render: (alpha: number) => void   // Rendering (variable)
  ) {}

  start(): void {
    this.lastTime = performance.now() / 1000;
    requestAnimationFrame(this.loop.bind(this));
  }

  private loop(timeMs: number): void {
    const time = timeMs / 1000;
    let frameTime = time - this.lastTime;
    this.lastTime = time;

    // Cap frame time to avoid spiral of death
    if (frameTime > 0.25) frameTime = 0.25;

    this.accumulator += frameTime;

    // Fixed-step updates (deterministic physics)
    while (this.accumulator >= this.fixedDelta) {
      this.update(this.fixedDelta);
      this.accumulator -= this.fixedDelta;
    }

    // Render with interpolation factor
    const alpha = this.accumulator / this.fixedDelta;
    this.render(alpha);

    requestAnimationFrame(this.loop.bind(this));
  }
}
```

## Scene / State Management

```typescript
// Scene manager with lifecycle hooks and transitions
interface GameScene {
  key: string;
  enter(data?: any): void | Promise<void>;
  update(delta: number): void;
  render(ctx: CanvasRenderingContext2D): void;
  exit(): void | Promise<void>;
}

class SceneManager {
  private scenes = new Map<string, GameScene>();
  private current: GameScene | null = null;
  private stack: GameScene[] = []; // For pause menus, overlays

  register(scene: GameScene): void {
    this.scenes.set(scene.key, scene);
  }

  async switchTo(key: string, data?: any): Promise<void> {
    if (this.current) await this.current.exit();
    this.current = this.scenes.get(key) ?? null;
    if (this.current) await this.current.enter(data);
  }

  async push(key: string, data?: any): Promise<void> {
    if (this.current) this.stack.push(this.current);
    this.current = this.scenes.get(key) ?? null;
    if (this.current) await this.current.enter(data);
  }

  async pop(): Promise<void> {
    if (this.current) await this.current.exit();
    this.current = this.stack.pop() ?? null;
  }

  update(delta: number): void {
    this.current?.update(delta);
  }

  render(ctx: CanvasRenderingContext2D): void {
    // Render stack (for transparent overlays like pause menus)
    for (const scene of this.stack) {
      scene.render(ctx);
    }
    this.current?.render(ctx);
  }
}
```

## Save / Load System

```python
import json
from pathlib import Path
from dataclasses import dataclass, asdict
from datetime import datetime

@dataclass
class SaveData:
    version: int = 1
    timestamp: str = ""
    player_position: tuple[float, float] = (0, 0)
    player_health: int = 100
    score: int = 0
    level: int = 1
    inventory: list[str] = None
    unlocked_abilities: list[str] = None
    settings: dict = None

    def __post_init__(self):
        self.inventory = self.inventory or []
        self.unlocked_abilities = self.unlocked_abilities or []
        self.settings = self.settings or {}

class SaveSystem:
    SAVE_DIR = Path.home() / ".mygame" / "saves"

    def __init__(self):
        self.SAVE_DIR.mkdir(parents=True, exist_ok=True)

    def save(self, slot: int, data: SaveData) -> None:
        data.timestamp = datetime.now().isoformat()
        path = self.SAVE_DIR / f"save_{slot}.json"
        path.write_text(json.dumps(asdict(data), indent=2))

    def load(self, slot: int) -> SaveData | None:
        path = self.SAVE_DIR / f"save_{slot}.json"
        if not path.exists():
            return None
        raw = json.loads(path.read_text())
        # Version migration
        if raw.get("version", 0) < SaveData.version:
            raw = self._migrate(raw)
        return SaveData(**raw)

    def list_saves(self) -> list[tuple[int, str]]:
        saves = []
        for f in sorted(self.SAVE_DIR.glob("save_*.json")):
            slot = int(f.stem.split("_")[1])
            data = json.loads(f.read_text())
            saves.append((slot, data.get("timestamp", "unknown")))
        return saves

    def delete(self, slot: int) -> None:
        path = self.SAVE_DIR / f"save_{slot}.json"
        path.unlink(missing_ok=True)

    @staticmethod
    def _migrate(raw: dict) -> dict:
        """Migrate old save formats to current version."""
        if raw.get("version", 0) < 1:
            raw.setdefault("unlocked_abilities", [])
            raw.setdefault("settings", {})
            raw["version"] = 1
        return raw
```

## Asset Management

```typescript
// Centralized asset loader with progress tracking
type AssetType = 'image' | 'audio' | 'json' | 'font';

interface AssetManifest {
  key: string;
  type: AssetType;
  path: string;
}

class AssetManager {
  private cache = new Map<string, any>();
  private loading = 0;
  private loaded = 0;

  get progress(): number {
    return this.loading === 0 ? 1 : this.loaded / this.loading;
  }

  async loadManifest(assets: AssetManifest[]): Promise<void> {
    this.loading = assets.length;
    this.loaded = 0;

    await Promise.all(
      assets.map(async (asset) => {
        try {
          const data = await this.loadAsset(asset);
          this.cache.set(asset.key, data);
        } catch (e) {
          console.error(`Failed to load asset: ${asset.key}`, e);
        } finally {
          this.loaded++;
        }
      })
    );
  }

  private async loadAsset(asset: AssetManifest): Promise<any> {
    switch (asset.type) {
      case 'image': return this.loadImage(asset.path);
      case 'audio': return this.loadAudio(asset.path);
      case 'json': return (await fetch(asset.path)).json();
      case 'font': {
        const font = new FontFace(asset.key, `url(${asset.path})`);
        await font.load();
        document.fonts.add(font);
        return font;
      }
    }
  }

  private loadImage(path: string): Promise<HTMLImageElement> {
    return new Promise((resolve, reject) => {
      const img = new Image();
      img.onload = () => resolve(img);
      img.onerror = reject;
      img.src = path;
    });
  }

  private loadAudio(path: string): Promise<AudioBuffer> {
    const audioCtx = new AudioContext();
    return fetch(path)
      .then(r => r.arrayBuffer())
      .then(buf => audioCtx.decodeAudioData(buf));
  }

  get<T>(key: string): T {
    const asset = this.cache.get(key);
    if (!asset) throw new Error(`Asset not found: ${key}`);
    return asset as T;
  }
}
```

## Best Practices

✅ Separate data from logic (ECS or component-based architecture)
✅ Use an event bus for cross-system communication — avoid direct references
✅ Fixed timestep for physics, variable for rendering
✅ Version your save files and write migration code
✅ Load assets asynchronously with progress feedback
✅ Use scene stacks for overlays (pause menu on top of game)
✅ Keep game state serializable for save/load and networking

## Anti-Patterns

❌ God objects that manage everything (GameManager with 2000 lines)
❌ Deep inheritance hierarchies (Enemy → FlyingEnemy → FlyingBossEnemy → ...)
❌ Tight coupling between systems (audio system directly references player)
❌ Synchronous asset loading that blocks the main thread
❌ Frame-dependent game loops without fixed timestep
❌ Hardcoded save paths without migration support

## Example Prompts

"Set up an ECS architecture for a 2D space shooter in TypeScript"

"Create an event bus system in Godot 4 for decoupled game systems"

"Implement a fixed-timestep game loop with interpolated rendering"

"Build a save/load system with versioning and slot management"

"Design a scene manager with transitions and scene stacking"

## Related Skills

- `game-development/game-design.md` — Design principles
- `game-development/game-mechanics.md` — Physics, AI, procedural generation
- `game-development/prototyping.md` — Rapid prototyping

## References

- [Game Programming Patterns — Robert Nystrom](https://gameprogrammingpatterns.com/)
- [Fix Your Timestep — Glenn Fiedler](https://gafferongames.com/post/fix_your_timestep/)
- [Entity Component System FAQ](https://github.com/SanderMertens/ecs-faq)
- [Godot Best Practices](https://docs.godotengine.org/en/stable/tutorials/best_practices/)
````
