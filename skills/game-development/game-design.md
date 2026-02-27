# Game Design Principles

## Instructions for AI

Apply these game design principles when designing game mechanics, progression systems, difficulty curves, and player experiences. Use this skill to create games that are fun, balanced, and engaging. Always prioritize player experience and iterate based on the core loop.

## Core Loop Design

Every great game is built around a compelling **core loop** — the atomic unit of gameplay that players repeat.

### The 3-Part Core Loop
1. **Action** → What does the player DO? (jump, shoot, build, match, explore)
2. **Reward** → What do they GET? (points, items, story, mastery, social validation)
3. **Decision** → What do they CHOOSE? (risk/reward, resource allocation, strategy)

### Loop Nesting
Games often have nested loops at different time scales:

```
Micro Loop (seconds):   Aim → Shoot → Hit/Miss → Adjust
Core Loop (minutes):     Enter Room → Fight Enemies → Collect Loot → Choose Path
Meta Loop (hours):       Complete Dungeon → Level Up → Unlock Abilities → Harder Dungeon
Long Loop (days/weeks):  Complete Season → Earn Rewards → Set New Goals → New Season
```

### Core Loop Examples by Genre

| Genre | Action | Reward | Decision |
|-------|--------|--------|----------|
| **Platformer** | Jump, run, dodge | Coins, new area | Which path, when to risk |
| **RPG** | Fight, explore, talk | XP, items, story | Build, party, quests |
| **Puzzle** | Match, rotate, place | Score, new levels | Which moves, order |
| **Tower Defense** | Place, upgrade, sell | Resources, waves cleared | Tower positioning, timing |
| **Roguelike** | Explore, fight, die | Unlocks, knowledge | Risk vs. safety, builds |
| **Sandbox** | Build, gather, craft | New tools, structures | What to build, where |

## Game Design Document (GDD) Template

```markdown
# [Game Title]

## Elevator Pitch
One sentence that captures the game's essence.
"It's [Known Game A] meets [Known Game B] with [Unique Twist]."

## Core Fantasy
What experience/feeling does the player live?
Example: "You are a tiny robot repairing a giant sleeping creature's body from the inside."

## Core Mechanics
1. Primary mechanic (what you do 80% of the time)
2. Secondary mechanic (variety/depth)
3. Progression mechanic (what keeps you playing)

## Core Loop
Action → Reward → Decision → (repeat)

## Target Audience
- Age range
- Gaming experience level
- Platform preference

## Unique Selling Points (USPs)
1. What makes this game special?
2. Why would someone choose THIS over alternatives?

## Art Style
Visual references, mood board description.

## Audio Direction
Music style, key sound effects, ambiance.

## Technical Scope
- Platform(s): Web / Mobile / Desktop
- Engine: Godot / Phaser / Unity
- Estimated dev time: [x] weeks
- Team size: [x] people

## Minimum Viable Product (MVP)
The absolute minimum to test if the core loop is fun:
1. [Core mechanic works]
2. [One level/environment]
3. [Basic feedback (visual + audio)]
4. [Win/lose condition]
```

## Difficulty Design

### Difficulty Curve Types

```
Difficulty
    │
    │    ╱ Linear (Tetris)
    │   ╱
    │  ╱
    │ ╱
    └──────── Time

    │     ┌─ Stepped (Zelda)
    │   ┌─┘
    │ ┌─┘
    │─┘
    └──────── Time

    │  ╱╲  ╱╲   Wave (Left 4 Dead)
    │ ╱  ╲╱  ╲
    │╱        ╲╱
    └──────── Time
```

### Flow State — The Sweet Spot
- **Too easy** → Boredom → Player quits
- **Too hard** → Frustration → Player quits
- **Just right** → Flow state → Player is engaged

### Dynamic Difficulty Adjustment (DDA)
```python
# Simple DDA system
class DifficultyDirector:
    def __init__(self):
        self.player_deaths = 0
        self.player_kills = 0
        self.difficulty_level = 1.0

    def on_player_death(self):
        self.player_deaths += 1
        # Make it slightly easier after deaths
        self.difficulty_level = max(0.5, self.difficulty_level - 0.1)

    def on_enemy_killed(self):
        self.player_kills += 1
        # Increase difficulty when player is dominating
        if self.player_kills % 5 == 0:
            self.difficulty_level = min(2.0, self.difficulty_level + 0.05)

    @property
    def enemy_health_multiplier(self) -> float:
        return self.difficulty_level

    @property
    def enemy_spawn_rate(self) -> float:
        return 1.0 + (self.difficulty_level - 1.0) * 0.5
```

## Progression Systems

### Types of Progression
1. **Power Progression** — Player gets stronger (RPG levels, upgrades)
2. **Knowledge Progression** — Player learns mechanics (puzzle games, Souls-like)
3. **Content Progression** — New areas, story, characters unlock
4. **Social Progression** — Ranks, leaderboards, cosmetics
5. **Mastery Progression** — Same mechanics, higher skill ceiling (rhythm games)

### Reward Scheduling
```
Fixed Ratio:     Every 10 kills = reward        (predictable, grindable)
Variable Ratio:  Random drop after kills         (addictive, exciting — loot boxes)
Fixed Interval:  Daily login bonus               (habitual)
Variable Interval: Random events/encounters      (surprising, exploratory)
```

### Unlockable Design Pattern
```typescript
interface Unlockable {
  id: string;
  name: string;
  description: string;
  requirement: UnlockRequirement;
  reward: Reward;
  isSecret: boolean;        // Hidden until discovered
}

interface UnlockRequirement {
  type: 'score' | 'level' | 'achievement' | 'collection' | 'time';
  threshold: number;
  progress: number;         // Current progress (0–threshold)
}

// Examples:
const unlockables: Unlockable[] = [
  {
    id: 'double_jump',
    name: 'Wing Boots',
    description: 'Unlocks double jump ability',
    requirement: { type: 'level', threshold: 5, progress: 0 },
    reward: { type: 'ability', value: 'double_jump' },
    isSecret: false,
  },
  {
    id: 'secret_character',
    name: '???',
    description: 'Complete the game without dying',
    requirement: { type: 'achievement', threshold: 1, progress: 0 },
    reward: { type: 'character', value: 'ghost_player' },
    isSecret: true,
  },
];
```

## Player Psychology

### Bartle's Player Types
| Type | Motivation | Design For |
|------|-----------|------------|
| **Achiever** | Goals, completion | Achievements, 100%, collectibles |
| **Explorer** | Discovery, secrets | Hidden areas, lore, easter eggs |
| **Socializer** | Connection, cooperation | Multiplayer, chat, guilds |
| **Killer** | Competition, dominance | PvP, leaderboards, rankings |

### Motivation Framework (Self-Determination Theory)
1. **Autonomy** — Player feels in control of choices
2. **Competence** — Player feels skilled and improving  
3. **Relatedness** — Player feels connected to others or the world

## Balancing

### Resource Economy Basics
```
Income Sources → Player Wallet → Spending Sinks
  (drops, quests,      ↕           (upgrades, items,
   rewards)         Balance         consumables, cosmetics)
```

**Golden rule:** Sinks must grow proportionally to sources, or inflation breaks the economy.

### Playtesting Questions
- Is the core loop fun in the first 30 seconds?
- Can a new player understand the main mechanic without a tutorial?
- What's the "one more try" factor?
- Where do players quit? (frustration point analysis)
- What do players do that you didn't expect? (emergent behavior)
- Is there a dominant strategy? (balance issue)

## Best Practices

✅ Prototype the core loop FIRST — before art, story, or polish
✅ Playtest early and often — your own fun-test is not enough
✅ Give clear goals but let players find their own way
✅ Teach through play, not text tutorials
✅ Reward curiosity and exploration
✅ Make failure interesting (roguelikes: death = knowledge)
✅ Consider accessibility (remappable controls, colorblind modes, difficulty options)

## Anti-Patterns

❌ Feature creep before core loop validation
❌ Balancing by spreadsheet without playtesting
❌ Punishing the player instead of teaching them
❌ Forced tutorials that take control away
❌ Pay-to-win mechanics that break fairness
❌ Difficulty spikes without player agency
❌ Grinding without meaningful choices

## Example Prompts

"Design a core loop for a city-builder with roguelike elements"

"Create a progression system with unlockable abilities for a metroidvania"

"Write a GDD for a 48-hour game jam — theme: 'connected'"

"Design difficulty curves for a puzzle game that teaches mechanics gradually"

"Balance an RPG economy with crafting, shops, and loot drops"

## Related Skills

- `game-development/game-mechanics.md` — Physics, AI, procedural generation
- `game-development/game-architecture.md` — ECS, scene graphs, event systems
- `game-development/prototyping.md` — Rapid prototyping and playtesting

## References

- [A Theory of Fun — Raph Koster](https://www.theoryoffun.com/)
- [The Art of Game Design — Jesse Schell](https://www.schellgames.com/art-of-game-design)
- [Game Balance — Ian Schreiber](https://gamebalanceconcepts.wordpress.com/)
- [Designing Games — Tynan Sylvester](https://tynansylvester.com/book/)
- [GDC Vault — Free Talks](https://gdcvault.com/free)
