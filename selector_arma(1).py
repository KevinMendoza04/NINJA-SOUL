armas: weapons = {
    "1": "🔨 Mace: short distance damage",
    "2": "🥷 Shuriken: medium distance damage",
    "3": "🏹 Crossbow: long distance damage"}


default_weapon = "🔨 Mace"


def choose_weapon():
    print("\n  🔥🔥🔥 WEAPONS 🔥🔥🔥")
    print("  1. 🔨 Mace: short distance damage")
    print("  2. 🥷  Shuriken: medium distance damage")
    print("  3. 🏹 Crossbow: long distance damage")

    opcion = input("\n Choose a number (1/2/3): ").strip()

    if opcion in weapons:
        arma = weapons[opcion]
        print(f"\n You chose: {arma}")
    else:
        arma = default_weapon
        print(f"\n Invalid input. Default assigned weapon: {arma}")

    return arma


if _name_ == "_main_":
    chosen_weapon = choose_weapon()
    print(f"\n🎮 Entering combat with: {chosen_weapon}")
