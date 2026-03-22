# Ninja Soul 🥷

A turn-based combat simulator built in Python. Fight as a customizable Ninja against the villain **Mojojojo** in a terminal battle where strategy, luck, and your choice of weapon decide the outcome.

> Built at **Riwi Barranquilla** — February 2025  
> Authors: **Kevin Mendoza** & **Joan Sebastian Mantillo**

---

## Table of Contents

- [Description](#description)
- [Gameplay](#gameplay)
- [Functions](#functions)
- [Combat Stats](#combat-stats)
- [Authors](#authors)

---

## Description

Ninja Soul is a terminal-based RPG combat game developed as a pair programming exercise at Riwi Barranquilla. The project was built using **Python 3**, focusing on modular functions, control structures, and state management.

The player chooses a name, selects a weapon, and fights Mojojojo in a turn-by-turn battle. Each decision matters — heal at the right moment, land a critical hit, or risk it all with the Special Attack.

---

## Gameplay

```
========================================

  ███████  ██████  ██    ██ ██
  ...

  Enter your ninja's name: Kem

  All set, Kem!

  🔥 WEAPONS 🔥
  1. 🔨 Mace       — short distance  (15-30 damage)
  2. 🥷  Shuriken   — medium distance (10-25 damage)
  3. 🏹 Crossbow   — long distance   (8-35 damage)

  Choose your weapon (1/2/3): 1

  Kem  VS  Mojojojo
  The battle begins!

========================================
  Kem        [##########]  100 HP
  Mojojojo   [##########]  120 HP
========================================

  Potions: 3
  1. Attack          (damage: 15-30)
  2. Heal            (recovers 20 HP)
  3. Special Attack  (damage: 30-50, 50% fail chance)

  Choose your action (1/2/3):
```

Each turn you pick an action. After your action, Mojojojo attacks automatically. The battle continues until one fighter reaches 0 HP.

---

## Functions

The program is organized into **6 modular functions** plus the main game loop.

---

### `damage_generator(minimo, maximo)`
**Author: Kevin**

Generates a random integer between two values. Used by every attack in the game.

```python
damage_generator(10, 25)   # returns a random int like 17
damage_generator(15, 20)   # returns a random int like 19
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `minimo` | int | Minimum damage value |
| `maximo` | int | Maximum damage value |

Returns: `int`

---

### `show_status(nombre_ninja, hp_ninja, nombre_mojojojo, hp_mojojojo)`
**Author: Kevin**

Displays the current HP of both fighters as a visual health bar using `#` and `-` characters. HP is always shown as 0 or above — never negative.

```
========================================
  Kem        [######----]  60 HP
  Mojojojo   [##########]  120 HP
========================================
```

| Parameter | Type | Description |
|-----------|------|-------------|
| `nombre_ninja` | str | Player's ninja name |
| `hp_ninja` | int | Current ninja HP |
| `nombre_mojojojo` | str | Enemy name |
| `hp_mojojojo` | int | Current enemy HP |

Returns: nothing (prints to terminal)

---

### `choose_weapon()`
**Author: Kevin**

Displays the weapon selection menu before combat starts. The chosen weapon determines the damage range of the player's normal attack. If an invalid option is entered, the Mace is assigned by default.

| Weapon | Range | Style |
|--------|-------|-------|
| 🔨 Mace | 15–30 damage | Short distance, consistent |
| 🥷 Shuriken | 10–25 damage | Medium distance, balanced |
| 🏹 Crossbow | 8–35 damage | Long distance, high variance |

Returns: `str` (weapon name)

---

### `player_turn(hp_ninja, hp_mojojojo, potions, weapon)`
**Author: Kevin**

Handles the player's action each turn. Loops until the player selects a valid option. The damage range of the Attack action changes based on the weapon chosen before combat.

**Actions available:**

| Option | Action | Effect |
|--------|--------|--------|
| 1 | Attack | Deals weapon-based damage to Mojojojo. 10% chance of critical hit (double damage) |
| 2 | Heal | Restores 20 HP (capped at 100). Uses 1 potion. If 0 potions remain, player must choose another action without losing their turn |
| 3 | Special Attack | Deals 30–50 damage with 50% chance of failing completely. Also has 10% critical hit chance |

Returns: `(hp_ninja, hp_mojojojo, potions)`

---

### `enemy_turn(hp_ninja, hp_mojojojo)`
**Author: Joan Sebastian**

Controls Mojojojo's automatic behavior each turn. Implements basic AI: if Mojojojo's HP drops to 20% or below (24 HP), it heals itself instead of attacking. Otherwise it attacks the ninja with a random hit that also has a 10% critical hit chance.

```
Normal attack:  15–20 damage
Critical hit:   30–40 damage (10% chance)
Self-heal:      +25 HP when below 24 HP (capped at 120)
```

Returns: `(hp_ninja, hp_mojojojo)`

---

### `verify_winner(hp_ninja, hp_mojojojo)`
**Author: Joan Sebastian**

Checks after every action whether the battle is over. Returns `True` and prints the result message if either fighter has reached 0 HP or below. Returns `False` if the fight continues.

```python
verify_winner(0, 80)    # → True  (ninja lost)
verify_winner(45, 0)    # → True  (ninja won)
verify_winner(45, 80)   # → False (fight continues)
```

Returns: `bool`

---

## Combat Stats

| | Ninja | Mojojojo |
|--|-------|----------|
| Starting HP | 100 | 120 |
| Attack damage | Weapon-based | 15–20 |
| Critical hit chance | 10% | 10% |
| Critical multiplier | x2 | x2 |
| Healing | 20 HP / potion (3 potions) | 25 HP (AI triggered) |
| Special Attack | 30–50 damage, 50% fail | — |

---

## Authors

| Name | Contributions |
|------|--------------|
| **Kevin Mendoza** | `damage_generator`, `show_status`, `choose_weapon`, `player_turn`, main game loop, weapon system, project integration |
| **Sebastian** | `enemy_turn` (with basic AI healing logic), `verify_winner`, game state verification |

> This project was built as a pair programming exercise at Riwi Barranquilla. We divided the functions between both team members, worked on them independently, and then merged everything into a single working file. We ran into bugs along the way — wrong return values, type mismatches, infinite loops — debugged them together, and delivered a complete, working game.
