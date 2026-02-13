````skill
# Creative App Patterns

## Instructions for AI

Apply these patterns when building interactive, creative, and delightful applications. Focus on user engagement through micro-interactions, generative design, gamification, and sensory feedback. Every interaction should feel satisfying. Use these patterns for apps that go beyond utility — apps that spark joy, creativity, and "wow" moments.

## Animation & Motion Design

### Spring Physics for Natural Motion

```typescript
// Spring-based animation — feels organic, not robotic
class Spring {
  value: number;
  velocity = 0;
  target: number;

  constructor(
    initial: number,
    private stiffness = 180,
    private damping = 12,
    private mass = 1
  ) {
    this.value = initial;
    this.target = initial;
  }

  update(delta: number): number {
    const force = -this.stiffness * (this.value - this.target);
    const dampingForce = -this.damping * this.velocity;
    const acceleration = (force + dampingForce) / this.mass;

    this.velocity += acceleration * delta;
    this.value += this.velocity * delta;

    return this.value;
  }

  get isAtRest(): boolean {
    return (
      Math.abs(this.velocity) < 0.01 &&
      Math.abs(this.value - this.target) < 0.01
    );
  }
}

// Usage: Smooth cursor-following element
const xSpring = new Spring(0, 120, 14);
const ySpring = new Spring(0, 120, 14);

function onMouseMove(e: MouseEvent) {
  xSpring.target = e.clientX;
  ySpring.target = e.clientY;
}

function animate() {
  xSpring.update(1 / 60);
  ySpring.update(1 / 60);
  element.style.transform = `translate(${xSpring.value}px, ${ySpring.value}px)`;
  requestAnimationFrame(animate);
}
```

### Easing Functions Library

```typescript
// Essential easing functions for creative animations
const Easing = {
  // Smooth start
  easeInQuad:    (t: number) => t * t,
  easeInCubic:   (t: number) => t * t * t,
  easeInExpo:    (t: number) => t === 0 ? 0 : Math.pow(2, 10 * (t - 1)),

  // Smooth end
  easeOutQuad:   (t: number) => t * (2 - t),
  easeOutCubic:  (t: number) => 1 - Math.pow(1 - t, 3),
  easeOutExpo:   (t: number) => t === 1 ? 1 : 1 - Math.pow(2, -10 * t),

  // Smooth both
  easeInOutCubic: (t: number) =>
    t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2,

  // Bounce
  easeOutBounce: (t: number) => {
    if (t < 1 / 2.75) return 7.5625 * t * t;
    if (t < 2 / 2.75) return 7.5625 * (t -= 1.5 / 2.75) * t + 0.75;
    if (t < 2.5 / 2.75) return 7.5625 * (t -= 2.25 / 2.75) * t + 0.9375;
    return 7.5625 * (t -= 2.625 / 2.75) * t + 0.984375;
  },

  // Elastic — great for attention-grabbing UI
  easeOutElastic: (t: number) => {
    if (t === 0 || t === 1) return t;
    return Math.pow(2, -10 * t) * Math.sin((t * 10 - 0.75) * (2 * Math.PI) / 3) + 1;
  },

  // Back — overshoots slightly, feels anticipatory
  easeOutBack: (t: number) => {
    const c = 1.70158;
    return 1 + (c + 1) * Math.pow(t - 1, 3) + c * Math.pow(t - 1, 2);
  },
} as const;

// Animation helper with easing
function animate(
  from: number,
  to: number,
  duration: number,
  easing: (t: number) => number,
  onUpdate: (value: number) => void,
  onComplete?: () => void
): void {
  const start = performance.now();

  function tick(now: number) {
    const elapsed = now - start;
    const t = Math.min(elapsed / duration, 1);
    const easedT = easing(t);
    const value = from + (to - from) * easedT;

    onUpdate(value);

    if (t < 1) {
      requestAnimationFrame(tick);
    } else {
      onComplete?.();
    }
  }
  requestAnimationFrame(tick);
}
```

## Generative Design

### Perlin Noise Color Palettes

```typescript
import { createNoise2D } from 'simplex-noise';

class PaletteGenerator {
  private noise = createNoise2D();

  /**
   * Generate harmonious color palette using noise-based HSL traversal.
   */
  generate(count: number, seed: number = 0): string[] {
    const colors: string[] = [];
    const baseHue = (this.noise(seed, 0) + 1) * 180; // 0–360

    for (let i = 0; i < count; i++) {
      const t = i / count;
      const hueOffset = this.noise(t * 3, seed) * 60; // ±60° variation
      const saturation = 50 + this.noise(t * 2, seed + 1) * 30; // 20–80%
      const lightness = 30 + this.noise(t * 2, seed + 2) * 35; // 30–65%

      const hue = (baseHue + hueOffset + i * (360 / count)) % 360;
      colors.push(`hsl(${hue.toFixed(0)}, ${saturation.toFixed(0)}%, ${lightness.toFixed(0)}%)`);
    }
    return colors;
  }

  /**
   * Generate complementary pair.
   */
  complementary(seed: number): [string, string] {
    const h = (this.noise(seed, 0) + 1) * 180;
    return [
      `hsl(${h.toFixed(0)}, 70%, 50%)`,
      `hsl(${((h + 180) % 360).toFixed(0)}, 70%, 50%)`,
    ];
  }

  /**
   * Generate analogous palette (3 colors close on wheel).
   */
  analogous(seed: number): string[] {
    const h = (this.noise(seed, 0) + 1) * 180;
    return [-30, 0, 30].map(
      offset => `hsl(${((h + offset + 360) % 360).toFixed(0)}, 65%, 50%)`
    );
  }
}
```

### Particle System for UI Effects

```typescript
// Lightweight particle system for celebrations, backgrounds, transitions
interface Particle {
  x: number; y: number;
  vx: number; vy: number;
  life: number; maxLife: number;
  size: number;
  color: string;
  rotation: number;
  rotationSpeed: number;
  shape: 'circle' | 'square' | 'star' | 'emoji';
  emoji?: string;
}

class ParticleSystem {
  private particles: Particle[] = [];

  emit(config: {
    x: number; y: number;
    count: number;
    spread?: number;
    speed?: number;
    gravity?: number;
    lifetime?: number;
    colors?: string[];
    shapes?: Particle['shape'][];
    emojis?: string[];
  }): void {
    const {
      x, y, count, spread = Math.PI * 2, speed = 200,
      lifetime = 1.5, colors = ['#ff6b6b', '#ffd93d', '#6bcb77', '#4d96ff'],
      shapes = ['circle'], emojis = ['🎉'],
    } = config;

    for (let i = 0; i < count; i++) {
      const angle = Math.random() * spread - spread / 2 - Math.PI / 2;
      const velocity = speed * (0.5 + Math.random() * 0.5);
      const shape = shapes[Math.floor(Math.random() * shapes.length)];

      this.particles.push({
        x, y,
        vx: Math.cos(angle) * velocity,
        vy: Math.sin(angle) * velocity,
        life: lifetime,
        maxLife: lifetime,
        size: 4 + Math.random() * 8,
        color: colors[Math.floor(Math.random() * colors.length)],
        rotation: Math.random() * Math.PI * 2,
        rotationSpeed: (Math.random() - 0.5) * 10,
        shape,
        emoji: shape === 'emoji' ? emojis[Math.floor(Math.random() * emojis.length)] : undefined,
      });
    }
  }

  /**
   * Confetti burst — perfect for achievements and celebrations.
   */
  confetti(x: number, y: number): void {
    this.emit({
      x, y, count: 50, spread: Math.PI,
      speed: 400, lifetime: 2.5,
      colors: ['#ff6b6b', '#ffd93d', '#6bcb77', '#4d96ff', '#c084fc', '#fb923c'],
      shapes: ['square', 'circle'],
    });
  }

  update(delta: number, gravity: number = 300): void {
    for (let i = this.particles.length - 1; i >= 0; i--) {
      const p = this.particles[i];
      p.life -= delta;
      if (p.life <= 0) {
        this.particles.splice(i, 1);
        continue;
      }
      p.vy += gravity * delta;
      p.x += p.vx * delta;
      p.y += p.vy * delta;
      p.vx *= 0.99; // Air resistance
      p.rotation += p.rotationSpeed * delta;
    }
  }

  render(ctx: CanvasRenderingContext2D): void {
    for (const p of this.particles) {
      const alpha = p.life / p.maxLife;
      ctx.save();
      ctx.globalAlpha = alpha;
      ctx.translate(p.x, p.y);
      ctx.rotate(p.rotation);

      if (p.shape === 'emoji' && p.emoji) {
        ctx.font = `${p.size * 2}px serif`;
        ctx.fillText(p.emoji, -p.size, p.size);
      } else if (p.shape === 'circle') {
        ctx.fillStyle = p.color;
        ctx.beginPath();
        ctx.arc(0, 0, p.size / 2, 0, Math.PI * 2);
        ctx.fill();
      } else if (p.shape === 'square') {
        ctx.fillStyle = p.color;
        ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
      }

      ctx.restore();
    }
  }

  get isActive(): boolean {
    return this.particles.length > 0;
  }
}
```

## Gamification Patterns

### Achievement System

```typescript
interface Achievement {
  id: string;
  name: string;
  description: string;
  icon: string;
  requirement: AchievementRequirement;
  unlockedAt: Date | null;
  isSecret: boolean;
  rarity: 'common' | 'rare' | 'epic' | 'legendary';
}

interface AchievementRequirement {
  type: string;
  threshold: number;
}

class AchievementSystem {
  private achievements: Achievement[] = [];
  private trackers = new Map<string, number>();
  private onUnlock?: (achievement: Achievement) => void;

  constructor(achievements: Achievement[], onUnlock?: (achievement: Achievement) => void) {
    this.achievements = achievements;
    this.onUnlock = onUnlock;
  }

  track(eventType: string, value: number = 1): void {
    const current = (this.trackers.get(eventType) ?? 0) + value;
    this.trackers.set(eventType, current);

    // Check if any achievement triggered
    for (const achievement of this.achievements) {
      if (achievement.unlockedAt) continue; // Already unlocked
      if (achievement.requirement.type !== eventType) continue;
      if (current >= achievement.requirement.threshold) {
        achievement.unlockedAt = new Date();
        this.onUnlock?.(achievement);
      }
    }
  }

  getProgress(id: string): { current: number; threshold: number; percent: number } {
    const achievement = this.achievements.find(a => a.id === id);
    if (!achievement) throw new Error(`Unknown achievement: ${id}`);
    const current = this.trackers.get(achievement.requirement.type) ?? 0;
    return {
      current,
      threshold: achievement.requirement.threshold,
      percent: Math.min(100, (current / achievement.requirement.threshold) * 100),
    };
  }
}

// Example achievements
const achievements: Achievement[] = [
  {
    id: 'first_creation', name: 'Hello World', icon: '🌱',
    description: 'Create your first artwork',
    requirement: { type: 'creations', threshold: 1 },
    unlockedAt: null, isSecret: false, rarity: 'common',
  },
  {
    id: 'streak_7', name: 'On Fire', icon: '🔥',
    description: 'Maintain a 7-day streak',
    requirement: { type: 'streak_days', threshold: 7 },
    unlockedAt: null, isSecret: false, rarity: 'rare',
  },
  {
    id: 'night_owl', name: 'Night Owl', icon: '🦉',
    description: 'Create something between 2-4 AM',
    requirement: { type: 'night_creation', threshold: 1 },
    unlockedAt: null, isSecret: true, rarity: 'epic',
  },
  {
    id: 'colors_1000', name: 'Chromatic Master', icon: '🌈',
    description: 'Use 1000 different colors',
    requirement: { type: 'unique_colors', threshold: 1000 },
    unlockedAt: null, isSecret: false, rarity: 'legendary',
  },
];
```

### XP & Leveling System

```typescript
class LevelSystem {
  private xp = 0;
  private level = 1;
  private onLevelUp?: (level: number, rewards: string[]) => void;

  private readonly levelThresholds = this.generateThresholds(100);
  private readonly levelRewards: Record<number, string[]> = {
    2: ['🎨 New brush: Soft Round'],
    5: ['🖌️ Unlocked: Gradient tool', '🎵 New background music'],
    10: ['✨ Particle effects pack', '🏆 Title: Artist'],
    25: ['🌟 Golden palette', '🎭 Custom avatar frame'],
    50: ['💎 Diamond tools', '🏆 Title: Master Creator'],
  };

  constructor(onLevelUp?: (level: number, rewards: string[]) => void) {
    this.onLevelUp = onLevelUp;
  }

  /**
   * XP curve: each level requires progressively more XP
   * Formula: base * level^1.5
   */
  private generateThresholds(maxLevel: number): number[] {
    const base = 100;
    return Array.from({ length: maxLevel }, (_, i) =>
      Math.floor(base * Math.pow(i + 1, 1.5))
    );
  }

  addXP(amount: number, reason?: string): void {
    this.xp += amount;

    while (
      this.level < this.levelThresholds.length &&
      this.xp >= this.levelThresholds[this.level - 1]
    ) {
      this.xp -= this.levelThresholds[this.level - 1];
      this.level++;
      const rewards = this.levelRewards[this.level] ?? [];
      this.onLevelUp?.(this.level, rewards);
    }
  }

  get currentXP(): number { return this.xp; }
  get currentLevel(): number { return this.level; }
  get xpToNextLevel(): number { return this.levelThresholds[this.level - 1] - this.xp; }
  get progressPercent(): number {
    return (this.xp / this.levelThresholds[this.level - 1]) * 100;
  }
}
```

## Audio Design for Apps

```typescript
// Minimal sound system for UI feedback
class UIAudio {
  private ctx: AudioContext | null = null;
  private buffers = new Map<string, AudioBuffer>();

  /**
   * Procedural UI sounds — no audio files needed!
   */
  playTone(type: 'success' | 'error' | 'click' | 'whoosh' | 'levelup'): void {
    if (!this.ctx) this.ctx = new AudioContext();
    const ctx = this.ctx;

    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain);
    gain.connect(ctx.destination);

    const now = ctx.currentTime;

    switch (type) {
      case 'click':
        osc.frequency.setValueAtTime(800, now);
        osc.frequency.exponentialRampToValueAtTime(600, now + 0.05);
        gain.gain.setValueAtTime(0.1, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);
        osc.start(now);
        osc.stop(now + 0.05);
        break;

      case 'success':
        osc.frequency.setValueAtTime(523, now);        // C5
        osc.frequency.setValueAtTime(659, now + 0.1);  // E5
        osc.frequency.setValueAtTime(784, now + 0.2);  // G5
        gain.gain.setValueAtTime(0.15, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.4);
        osc.start(now);
        osc.stop(now + 0.4);
        break;

      case 'error':
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(200, now);
        osc.frequency.exponentialRampToValueAtTime(100, now + 0.2);
        gain.gain.setValueAtTime(0.1, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.2);
        osc.start(now);
        osc.stop(now + 0.2);
        break;

      case 'whoosh':
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(100, now);
        osc.frequency.exponentialRampToValueAtTime(2000, now + 0.15);
        gain.gain.setValueAtTime(0.05, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
        osc.start(now);
        osc.stop(now + 0.15);
        break;

      case 'levelup':
        // Arpeggio: C-E-G-C'
        const notes = [523, 659, 784, 1047];
        notes.forEach((freq, i) => {
          const o = ctx.createOscillator();
          const g = ctx.createGain();
          o.connect(g);
          g.connect(ctx.destination);
          o.frequency.setValueAtTime(freq, now + i * 0.1);
          g.gain.setValueAtTime(0.15, now + i * 0.1);
          g.gain.exponentialRampToValueAtTime(0.001, now + i * 0.1 + 0.3);
          o.start(now + i * 0.1);
          o.stop(now + i * 0.1 + 0.3);
        });
        break;
    }
  }
}
```

## Export & Sharing

```typescript
// Export user creations to shareable formats
class ExportManager {
  /**
   * Export canvas to PNG with metadata.
   */
  static canvasToPNG(canvas: HTMLCanvasElement, filename: string = 'creation.png'): void {
    const link = document.createElement('a');
    link.download = filename;
    link.href = canvas.toDataURL('image/png');
    link.click();
  }

  /**
   * Export canvas to animated GIF (requires gif.js library).
   */
  static async canvasToGIF(
    renderFrame: (ctx: CanvasRenderingContext2D, frame: number) => void,
    width: number,
    height: number,
    frames: number = 60,
    delay: number = 33
  ): Promise<Blob> {
    const { default: GIF } = await import('gif.js');
    const gif = new GIF({ width, height, quality: 10, workers: 2 });
    const canvas = document.createElement('canvas');
    canvas.width = width;
    canvas.height = height;
    const ctx = canvas.getContext('2d')!;

    for (let i = 0; i < frames; i++) {
      ctx.clearRect(0, 0, width, height);
      renderFrame(ctx, i);
      gif.addFrame(ctx, { delay, copy: true });
    }

    return new Promise((resolve) => {
      gif.on('finished', (blob: Blob) => resolve(blob));
      gif.render();
    });
  }

  /**
   * Generate Open Graph share card.
   */
  static generateShareCard(
    canvas: HTMLCanvasElement,
    title: string,
    author: string
  ): HTMLCanvasElement {
    const card = document.createElement('canvas');
    card.width = 1200;
    card.height = 630;
    const ctx = card.getContext('2d')!;

    // Background
    ctx.fillStyle = '#1a1a2e';
    ctx.fillRect(0, 0, 1200, 630);

    // Creation thumbnail (centered, with padding)
    const thumbSize = 400;
    ctx.drawImage(canvas, 50, 115, thumbSize, thumbSize);

    // Title
    ctx.fillStyle = '#ffffff';
    ctx.font = 'bold 48px Inter, sans-serif';
    ctx.fillText(title, 520, 250, 620);

    // Author
    ctx.fillStyle = '#a0a0b0';
    ctx.font = '28px Inter, sans-serif';
    ctx.fillText(`by ${author}`, 520, 310);

    // Branding
    ctx.fillStyle = '#6366f1';
    ctx.font = 'bold 24px Inter, sans-serif';
    ctx.fillText('Made with CreativeApp', 520, 500);

    return card;
  }
}
```

## Best Practices

✅ Respect `prefers-reduced-motion` — provide toggle for animations
✅ Use spring physics for natural-feeling motion, not linear tweens
✅ Layer feedback: visual + audio + haptic = satisfying interaction
✅ Make exported creations shareable (include branding subtly)
✅ Use procedural audio for UI sounds — no loading, always available
✅ Celebrate user milestones (first creation, streaks, achievements)
✅ Let users undo EVERYTHING — generous undo history
✅ Auto-save frequently and silently

## Anti-Patterns

❌ Animations that can't be disabled (accessibility violation)
❌ Sounds without volume control or mute option
❌ Gamification that feels manipulative (dark patterns)
❌ Splash screens or loading that blocks without feedback
❌ Forcing account creation before the user can try the app
❌ Exporting creations without the user's choice of format/quality
❌ UI that looks creative but is impossible to navigate

## Example Prompts

"Build an interactive particle canvas where users draw with physics-based particles"

"Create a confetti celebration component for achievement unlocks"

"Implement a gamification system with XP, levels, and unlockable tools"

"Design procedural UI sounds using Web Audio API — no audio files needed"

"Build a generative color palette tool using noise functions"

"Create an export system for user creations: PNG, GIF, and share cards"

## Related Skills

- `game-development/game-design.md` — Gamification principles
- `game-development/prototyping.md` — Rapid prototyping techniques
- `frontend-patterns/SKILL.md` — Core frontend patterns

## References

- [The Coding Train — Creative Coding](https://thecodingtrain.com/)
- [Framer Motion — Animation Library](https://www.framer.com/motion/)
- [Laws of UX](https://lawsofux.com/)
- [Generative Design Book](http://www.generative-gestaltung.de/)
- [p5.js — Creative Coding Library](https://p5js.org/)
- [The Nature of Code — Daniel Shiffman](https://natureofcode.com/)
````
