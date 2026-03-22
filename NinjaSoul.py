import random

# global variables
nombre_ninja    = ""
nombre_mojojojo = "Mojojojo"

# ══════════════════════════════════════════════════════
# FUNCTION 1 — damage_generator
# storages a random number between min and max.
# ══════════════════════════════════════════════════════
def damage_generator(minimo, maximo):
    return random.randint(minimo, maximo)


# ══════════════════════════════════════════════════════
# FUNCTION 2 — show_status
# prints life bar for both ninja and enemy
# ══════════════════════════════════════════════════════
def show_status(nombre_ninja, hp_ninja, nombre_mojojojo, hp_mojojojo):

    def barra_vida(hp_actual, hp_maximo):
        lleno = max(0, round((hp_actual / hp_maximo) * 10))
        vacio = 10 - lleno
        return f"[{'#' * lleno}{'-' * vacio}]"

    hp_ninja    = max(0, hp_ninja)
    hp_mojojojo = max(0, hp_mojojojo)

    print("\n" + "=" * 40)
    print(f"  {nombre_ninja:<10} {barra_vida(hp_ninja, 100)}  {hp_ninja} HP")
    print(f"  {nombre_mojojojo:<10} {barra_vida(hp_mojojojo, 120)}  {hp_mojojojo} HP")
    print("=" * 40)


# ══════════════════════════════════════════════════════
# FUNCTION 3 — choose_weapon
# Shows weapon`s menu and storages what was chosen.
# ══════════════════════════════════════════════════════
weapons = {
    "1": "🔨 Mace",
    "2": "🥷  Shuriken",
    "3": "🏹 Crossbow"
}

weapon_damage = {
    "🔨 Mace":      (15, 30),
    "🥷  Shuriken": (10, 25),
    "🏹 Crossbow":  (8,  35)
}

def choose_weapon():
    print("\n  🔥 WEAPONS 🔥")
    print("  1. 🔨 Mace       — short distance  (15-30 damage)")
    print("  2. 🥷  Shuriken   — medium distance (10-25 damage)")
    print("  3. 🏹 Crossbow   — long distance   (8-35 damage)")

    opcion = input("\n  Choose your weapon (1/2/3): ").strip()

    if opcion in weapons:
        arma = weapons[opcion]
        print(f"\n  You chose: {arma}")
    else:
        arma = "🔨 Mace"
        print(f"\n  Invalid input. Default weapon assigned: {arma}")

    return arma


# ══════════════════════════════════════════════════════
# FUNCTION 4 — player_turn
# Manages player`s action every turn.
# Returns: hp_ninja, hp_mojojojo, potions
# ══════════════════════════════════════════════════════
def player_turn(hp_ninja, hp_mojojojo, potions, weapon):

    # Damage range based on chosen gun.
    damage_min, damage_max = weapon_damage.get(weapon, (10, 25))

    accion_valida = False

    while not accion_valida:

        print(f"\n  Potions: {potions}")
        print(f"  1. Attack          (damage: {damage_min}-{damage_max})")
        print("  2. Heal            (recovers 20 HP)")
        print("  3. Special Attack  (damage: 30-50, 50% fail chance)")

        eleccion = input("\n  Choose your action (1/2/3): ").strip()

        if eleccion == "1":
            damage = damage_generator(damage_min, damage_max)
            critico = random.random() < 0.10
            if critico:
                damage *= 2
                print("  *** CRITICAL HIT! ***")
            hp_mojojojo -= damage
            print(f"  {nombre_ninja} hits {nombre_mojojojo} for -{damage} damage!")
            accion_valida = True

        elif eleccion == "2":
            if potions <= 0:
                print("  No potions left! Choose another action.")
            else:
                hp_ninja += 20
                hp_ninja = min(hp_ninja, 100)
                potions -= 1
                print(f"  {nombre_ninja} drinks a potion and recovers 20 HP!")
                accion_valida = True

        elif eleccion == "3":
            fallo = random.random() < 0.50
            if fallo:
                print(f"  {nombre_ninja} tried the Special Attack... but failed!")
            else:
                damage = damage_generator(30, 50)
                critico = random.random() < 0.10
                if critico:
                    damage *= 2
                    print("  *** CRITICAL HIT on SPECIAL ATTACK! ***")
                hp_mojojojo -= damage
                print(f"  {nombre_ninja} unleashes Special Attack on {nombre_mojojojo} for -{damage} damage!")
            accion_valida = True

        else:
            print("  Invalid option. Choose 1, 2 or 3.")

    return hp_ninja, hp_mojojojo, potions


# ══════════════════════════════════════════════════════
# FUNCTION 5 — enemy_turn
# Enemy acts automatically
# Basic AI: enemy heals himself if HP <= 20% off max.
# Returns: hp_ninja, hp_mojojojo
# ══════════════════════════════════════════════════════
def enemy_turn(hp_ninja, hp_mojojojo):

    umbral = 120 * 0.20    # 24 HP

    if hp_mojojojo <= umbral:
        hp_mojojojo += 25
        hp_mojojojo = min(hp_mojojojo, 120)
        print(f"  {nombre_mojojojo} is critically low... and heals 25 HP!")
    else:
        damage = random.randint(15, 20)
        critico = random.random() < 0.10
        if critico:
            damage *= 2
            print(f"  *** {nombre_mojojojo} CRITICAL HIT! ***")
        hp_ninja -= damage
        print(f"  {nombre_mojojojo} attacks {nombre_ninja} for -{damage} damage!")

    return hp_ninja, hp_mojojojo


# ══════════════════════════════════════════════════════
# FUNCTION 6 — verify_winner
# Returns True if a player`s HP is 0
# ══════════════════════════════════════════════════════
def verify_winner(hp_ninja, hp_mojojojo):

    if hp_mojojojo <= 0:
        print(f"\n  👑 YOU WIN, Ninja {nombre_ninja}! {nombre_mojojojo} has been defeated! 🏆")
        print("  ⚔️  You are the champion of the battlefield!")
        return True
    elif hp_ninja <= 0:
        print(f"\n  🕊️  YOU LOST, Ninja {nombre_ninja}... {nombre_mojojojo} defeated you. 👻")
        return True

    return False


# ══════════════════════════════════════════════════════
#   MAIN
# ══════════════════════════════════════════════════════

# Combat Variables
hp_ninja    = 100
hp_mojojojo = 120
potions     = 3

# Start page
print("=" * 40)
print("""
  ███████  ██████  ██    ██ ██
  ██      ██    ██ ██    ██ ██
  ███████ ██    ██ ██    ██ ██
       ██ ██    ██ ██    ██ ██
  ███████  ██████   ██████  ███████

  ███    ██ ██ ███    ██      ██  █████
  ████   ██ ██ ████   ██      ██ ██   ██
  ██ ██  ██ ██ ██ ██  ██      ██ ███████
  ██  ██ ██ ██ ██  ██ ██ ██   ██ ██   ██
  ██   ████ ██ ██   ████  █████  ██   ██
""")
print("=" * 40)

# We storage ninja`s name in the global variable
nombre_ninja = input("  Enter your ninja's name 🥷 : ").strip()
if not nombre_ninja:
    nombre_ninja = "Ninja"
print(f"\n  All set, {nombre_ninja}!")

# Weapon selection
weapon = choose_weapon()

# combact start
print(f"\n  {nombre_ninja}  VS  {nombre_mojojojo}")
print("  The battle begins!\n")


# Main loop
while not verify_winner(hp_ninja, hp_mojojojo):

    # 1. show current status
    show_status(nombre_ninja, hp_ninja, nombre_mojojojo, hp_mojojojo)

    # 2. player`s turn
    hp_ninja, hp_mojojojo, potions = player_turn(hp_ninja, hp_mojojojo, potions, weapon)

    # 3. verify enemy`s life after player`s turn.
    if verify_winner(hp_ninja, hp_mojojojo):
        break

    # 4. enemy`s turn
    hp_ninja, hp_mojojojo = enemy_turn(hp_ninja, hp_mojojojo)

# final stage
show_status(nombre_ninja, hp_ninja, nombre_mojojojo, hp_mojojojo)
print("\n  Thanks for playing Ninja Soul!")