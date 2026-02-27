# Rapid Prototyping & Playtesting

## Instructions for AI

Apply these prototyping patterns when building game prototypes, creative app MVPs, or game jam projects. Focus on speed: get to a playable/usable state in hours, not weeks. Use the simplest tools and patterns that validate whether the core idea is fun or useful. Polish comes later — **fun comes first**.

## Prototyping Philosophy

### The 30-Second Rule
Your prototype should answer ONE question in the first 30 seconds of play:
- "Is the core mechanic fun?"
- "Does this interaction feel good?"
- "Is this concept understandable without explanation?"

If it takes 5 minutes to get to the interesting part, your prototype is too complex.

### What to Prototype vs. What to Skip

| Prototype (Must Have) | Skip (Add Later) |
|----------------------|-----------------|
| Core mechanic / interaction | Menus, settings |
| Basic visual feedback | Polished art |
| Win/lose or success/fail state | Save system |
| One complete loop | Multiple levels |
| Placeholder sounds | Music, voice |
| Keyboard/mouse input | Gamepad support |

## Speed Prototyping Toolkit

### 1-Hour Game Prototype (Phaser + TypeScript)

```typescript
// Minimal Phaser 3 game — everything in one file for speed
// Goal: Playable in <1 hour of dev time

import Phaser from 'phaser';

class PrototypeScene extends Phaser.Scene {
  private player!: Phaser.Physics.Arcade.Sprite;
  private coins!: Phaser.Physics.Arcade.Group;
  private enemies!: Phaser.Physics.Arcade.Group;
  private score = 0;
  private scoreText!: Phaser.GameObjects.Text;
  private cursors!: Phaser.Types.Input.Keyboard.CursorKeys;

  create() {
    // Use colored rectangles instead of sprites — FAST
    this.player = this.physics.add.sprite(400, 500, '__DEFAULT')
      .setDisplaySize(32, 32)
      .setTint(0x4ecdc4);
    this.player.setCollideWorldBounds(true);

    // Spawn coins
    this.coins = this.physics.add.group();
    for (let i = 0; i < 10; i++) {
      const coin = this.physics.add.sprite(
        Phaser.Math.Between(50, 750), Phaser.Math.Between(50, 400), '__DEFAULT'
      ).setDisplaySize(16, 16).setTint(0xffd93d);
      this.coins.add(coin);
    }

    // Spawn enemies
    this.enemies = this.physics.add.group();
    for (let i = 0; i < 3; i++) {
      const enemy = this.physics.add.sprite(
        Phaser.Math.Between(100, 700), Phaser.Math.Between(100, 300), '__DEFAULT'
      ).setDisplaySize(24, 24).setTint(0xff6b6b);
      enemy.setVelocity(
        Phaser.Math.Between(-100, 100),
        Phaser.Math.Between(-100, 100)
      );
      enemy.setBounce(1);
      enemy.setCollideWorldBounds(true);
      this.enemies.add(enemy);
    }

    // Collisions
    this.physics.add.overlap(this.player, this.coins, this.collectCoin, undefined, this);
    this.physics.add.overlap(this.player, this.enemies, this.hitEnemy, undefined, this);

    // HUD
    this.scoreText = this.add.text(16, 16, 'Score: 0', {
      fontSize: '24px', color: '#fff',
    });

    this.cursors = this.input.keyboard!.createCursorKeys();
  }

  update() {
    const speed = 250;
    this.player.setVelocity(0);
    if (this.cursors.left.isDown) this.player.setVelocityX(-speed);
    if (this.cursors.right.isDown) this.player.setVelocityX(speed);
    if (this.cursors.up.isDown) this.player.setVelocityY(-speed);
    if (this.cursors.down.isDown) this.player.setVelocityY(speed);
  }

  private collectCoin(_: any, coin: any) {
    coin.destroy();
    this.score += 10;
    this.scoreText.setText(`Score: ${this.score}`);
    // Simple juice: screen flash
    this.cameras.main.flash(100, 255, 255, 100);
    if (this.coins.countActive() === 0) {
      this.scoreText.setText(`YOU WIN! Score: ${this.score}`);
    }
  }

  private hitEnemy() {
    this.cameras.main.shake(200, 0.01);
    this.scene.restart();
    this.score = 0;
  }
}

new Phaser.Game({
  type: Phaser.AUTO,
  width: 800,
  height: 600,
  backgroundColor: '#1a1a2e',
  physics: { default: 'arcade', arcade: { debug: false } },
  scene: PrototypeScene,
});
```

### PyGame Prototype Template

```python
"""
Minimal PyGame prototype — <100 lines, playable immediately.
Usage: python prototype.py
"""
import pygame
from random import randint
from dataclasses import dataclass

WIDTH, HEIGHT = 800, 600
FPS = 60

@dataclass
class Player:
    x: float = 400
    y: float = 500
    size: int = 30
    speed: float = 300
    color: tuple = (78, 205, 196)

@dataclass
class Coin:
    x: float = 0
    y: float = 0
    size: int = 12
    color: tuple = (255, 217, 61)
    collected: bool = False

@dataclass
class Enemy:
    x: float = 0
    y: float = 0
    size: int = 20
    vx: float = 0
    vy: float = 0
    color: tuple = (255, 107, 107)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    player = Player()
    coins = [Coin(x=randint(50, WIDTH - 50), y=randint(50, HEIGHT - 200)) for _ in range(10)]
    enemies = [
        Enemy(x=randint(100, 700), y=randint(100, 400), vx=randint(-150, 150), vy=randint(-150, 150))
        for _ in range(3)
    ]
    score = 0
    game_over = False
    font = pygame.font.Font(None, 36)

    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                return main()  # Restart

        if not game_over:
            # Input
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                player.x -= player.speed * dt
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                player.x += player.speed * dt
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                player.y -= player.speed * dt
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                player.y += player.speed * dt

            # Clamp player
            player.x = max(0, min(WIDTH - player.size, player.x))
            player.y = max(0, min(HEIGHT - player.size, player.y))

            # Move enemies (bounce)
            for e in enemies:
                e.x += e.vx * dt
                e.y += e.vy * dt
                if e.x <= 0 or e.x >= WIDTH - e.size: e.vx *= -1
                if e.y <= 0 or e.y >= HEIGHT - e.size: e.vy *= -1

            # Collision: coins
            pr = pygame.Rect(player.x, player.y, player.size, player.size)
            for coin in coins:
                if not coin.collected:
                    cr = pygame.Rect(coin.x, coin.y, coin.size, coin.size)
                    if pr.colliderect(cr):
                        coin.collected = True
                        score += 10

            # Collision: enemies
            for e in enemies:
                er = pygame.Rect(e.x, e.y, e.size, e.size)
                if pr.colliderect(er):
                    game_over = True

            # Win check
            if all(c.collected for c in coins):
                game_over = True

        # Draw
        screen.fill((26, 26, 46))
        for coin in coins:
            if not coin.collected:
                pygame.draw.rect(screen, coin.color, (coin.x, coin.y, coin.size, coin.size))
        for e in enemies:
            pygame.draw.rect(screen, e.color, (e.x, e.y, e.size, e.size))
        pygame.draw.rect(screen, player.color, (player.x, player.y, player.size, player.size))

        # HUD
        txt = font.render(f"Score: {score}  |  R = Restart", True, (255, 255, 255))
        screen.blit(txt, (16, 16))
        if game_over:
            msg = "YOU WIN!" if all(c.collected for c in coins) else "GAME OVER"
            go_txt = font.render(msg, True, (255, 255, 100))
            screen.blit(go_txt, (WIDTH // 2 - 80, HEIGHT // 2))

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
```

### HTML5 Canvas Prototype (Zero Dependencies)

```html
<!DOCTYPE html>
<html><head><title>Prototype</title>
<style>
  body { margin: 0; background: #1a1a2e; display: flex; 
         justify-content: center; align-items: center; height: 100vh; }
  canvas { border: 2px solid #333; }
</style></head>
<body>
<canvas id="game" width="800" height="600"></canvas>
<script>
const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');

// === GAME STATE ===
const player = { x: 400, y: 500, w: 30, h: 30, speed: 250, color: '#4ecdc4' };
const keys = {};
let score = 0;
let lastTime = performance.now();

// Spawn collectibles
const items = Array.from({ length: 10 }, () => ({
  x: 50 + Math.random() * 700, y: 50 + Math.random() * 400,
  w: 14, h: 14, color: '#ffd93d', active: true,
}));

// Input
addEventListener('keydown', e => keys[e.key] = true);
addEventListener('keyup', e => keys[e.key] = false);

// === GAME LOOP ===
function loop(now) {
  const dt = (now - lastTime) / 1000;
  lastTime = now;

  // Move
  if (keys['ArrowLeft'] || keys['a'])  player.x -= player.speed * dt;
  if (keys['ArrowRight'] || keys['d']) player.x += player.speed * dt;
  if (keys['ArrowUp'] || keys['w'])    player.y -= player.speed * dt;
  if (keys['ArrowDown'] || keys['s'])  player.y += player.speed * dt;
  player.x = Math.max(0, Math.min(canvas.width - player.w, player.x));
  player.y = Math.max(0, Math.min(canvas.height - player.h, player.y));

  // Collect
  items.forEach(item => {
    if (!item.active) return;
    if (player.x < item.x + item.w && player.x + player.w > item.x &&
        player.y < item.y + item.h && player.y + player.h > item.y) {
      item.active = false;
      score += 10;
    }
  });

  // Draw
  ctx.fillStyle = '#1a1a2e';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  items.forEach(i => { if (i.active) { ctx.fillStyle = i.color; ctx.fillRect(i.x, i.y, i.w, i.h); }});
  ctx.fillStyle = player.color;
  ctx.fillRect(player.x, player.y, player.w, player.h);
  ctx.fillStyle = '#fff';
  ctx.font = '20px monospace';
  ctx.fillText(`Score: ${score}`, 16, 30);

  if (items.every(i => !i.active)) {
    ctx.fillStyle = '#ffd93d';
    ctx.font = '40px monospace';
    ctx.fillText('YOU WIN!', 300, 300);
  }

  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
</script></body></html>
```

## Playtesting Framework

### Playtesting Session Template

```markdown
## Playtest Session — [Date]

### Setup
- Build version: [hash/tag]
- Playtest duration: [x] minutes
- Tester type: [ ] Developer  [ ] Friend  [ ] Target audience  [ ] Stranger

### Observation Method
- [ ] Silent observation (don't help, don't explain)
- [ ] Think-aloud (tester narrates their thoughts)
- [ ] Task-based (give specific goals)

### Key Questions
1. What did the player do first? (intuitive?)
2. Where did they get stuck? (frustration points)
3. Did they understand the goal without being told?
4. What did they find fun? (double down on this)
5. What did they try to do that the game doesn't support? (missing features)
6. When did they stop? Why?

### Observations
| Time | Action | Emotion | Note |
|------|--------|---------|------|
| 0:00 | Started playing | Curious | |
| 0:15 | Found jump | Surprised | Tried wall-jump (not implemented) |
| 0:45 | Died to spikes | Frustrated | No feedback on what killed them |
| 1:20 | Beat first level | Excited | Asked "is there a level 2?" |

### Action Items
- [ ] Add death feedback (flash, shake, sound)
- [ ] Consider adding wall-jump
- [ ] Add visual indicator for hazards
- [ ] Build level 2 with increased difficulty
```

### Automated Metrics Collection

```typescript
// Lightweight telemetry for prototype playtesting
class PlaytestMetrics {
  private events: { type: string; data: any; time: number }[] = [];
  private startTime = Date.now();

  track(type: string, data: any = {}): void {
    this.events.push({
      type,
      data,
      time: Date.now() - this.startTime,
    });
  }

  // Track common game events
  trackDeath(position: { x: number; y: number }, cause: string): void {
    this.track('death', { position, cause });
  }

  trackLevelComplete(level: number, timeMs: number): void {
    this.track('level_complete', { level, timeMs });
  }

  trackQuit(level: number, playTimeMs: number): void {
    this.track('session_end', { level, playTimeMs });
  }

  // Generate report
  report(): string {
    const deaths = this.events.filter(e => e.type === 'death');
    const completes = this.events.filter(e => e.type === 'level_complete');
    const sessionTime = (Date.now() - this.startTime) / 1000;

    return [
      `=== Playtest Report ===`,
      `Session: ${sessionTime.toFixed(0)}s`,
      `Deaths: ${deaths.length}`,
      `Levels completed: ${completes.length}`,
      `Death causes: ${this.summarize(deaths, d => d.data.cause)}`,
      `Death heatmap data: ${JSON.stringify(deaths.map(d => d.data.position))}`,
    ].join('\n');
  }

  private summarize(events: any[], keyFn: (e: any) => string): string {
    const counts = new Map<string, number>();
    events.forEach(e => {
      const key = keyFn(e);
      counts.set(key, (counts.get(key) ?? 0) + 1);
    });
    return [...counts.entries()].map(([k, v]) => `${k}: ${v}`).join(', ');
  }

  // Export for analysis
  exportJSON(): string {
    return JSON.stringify({
      sessionDuration: Date.now() - this.startTime,
      eventCount: this.events.length,
      events: this.events,
    }, null, 2);
  }
}
```

## Game Jam Strategies

### 48-Hour Game Jam Timeline

```
Hour 0-2:   Brainstorm → Pick ONE idea → Write 3-sentence GDD
Hour 2-4:   Core mechanic prototype (colored rectangles, no art)
Hour 4-6:   PLAYTEST CORE LOOP — Is it fun? If not, pivot NOW
Hour 6-12:  Build 3 levels/scenarios around core mechanic
Hour 12-16: Add juice (particles, shake, sounds, tweens)
Hour 16-20: Add progression (score, lives, difficulty curve)
Hour 20-24: Create simple art (pixel art, geometric, generative)
Hour 24-30: Polish, bug fixes, tutorial/onboarding
Hour 30-36: Music, sound design, menu screens
Hour 36-44: Final testing, edge cases, balance tweaks
Hour 44-48: Build final version, submit, write description
```

### Game Jam Survival Rules
1. **Scope SMALL** — Cut your idea in half. Then cut it in half again.
2. **Core loop by hour 4** — If you can't play it, you can't test it
3. **Placeholder everything** — Colored squares > art pipeline
4. **Version control from minute 1** — `git commit` every milestone
5. **Sleep** — A 36-hour awake jam produces worse results than a rested 24-hour one
6. **Submit early** — Upload a working version at 50%, keep updating until deadline

## Best Practices

✅ Build the minimum needed to test the idea — then test it
✅ Use placeholder art (colored shapes) until the mechanic is proven
✅ Playtest with someone else, not just yourself
✅ Track where players die, quit, or get confused
✅ Kill ideas that aren't fun after 3 iterations — don't polish a broken core
✅ Keep a "juice backlog" — list of small additions that make it feel better
✅ Version control from the very first line of code

## Anti-Patterns

❌ Building a full engine before testing the game idea
❌ Spending hours on art before the mechanic is fun
❌ Testing only by yourself — your brain compensates for bad design
❌ Ignoring playtest feedback because "they didn't understand my vision"
❌ Adding features instead of fixing the core loop
❌ Perfectionism during prototyping phase

## Example Prompts

"Build a playable prototype for a puzzle-platformer in under 100 lines"

"Create a PyGame prototype for a top-down shooter with 3 enemy types"

"Set up a zero-dependency HTML5 Canvas game prototype"

"Design a playtesting session plan for my roguelike prototype"

"Create an automated death-heatmap system for playtest analysis"

"Generate a 48-hour game jam timeline for a team of 2"

## Related Skills

- `game-development/game-design.md` — Design principles and core loops
- `game-development/game-mechanics.md` — Physics, AI, collision patterns
- `game-development/game-architecture.md` — ECS, scene management
- `creative-apps/creative-app-patterns.md` — Creative app prototyping

## References

- [Ludum Dare — Game Jam Community](https://ldjam.com/)
- [Global Game Jam](https://globalgamejam.org/)
- [How to Playtest — GDC Talk](https://www.gdcvault.com/)
- [The Art of Game Design — Chapter: Playtesting](https://www.schellgames.com/art-of-game-design)
- [itch.io — Game Jam Platform](https://itch.io/jams)
