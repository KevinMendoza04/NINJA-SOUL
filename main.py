import random
from FuncionesKevin import *
from selector_arma import*
from funcionessebastian import *


# Variables iniciales
hp_ninja = 100
hp_mojojojo = 120
potions = 3
nombre_mojojojo = "Mojojojo"


# Pedimos el nombre del ninja al inicio
print("=" * 40)
print("      SOULS NINJA 🥷")
print("=" * 40)
nombre_ninja = input("  Enter your ninja's name: ").strip()
print("\n🔥🔥🔥 WEAPONS 🔥🔥🔥")
print("1. 🔨 Mace: short distance damage")
print("2. 🥷  Shuriken: medium distance damage")
print("3. 🏹 Crossbow: long distance damage")
weapon = input("\n Choose your weapon (1/2/3): ")
print(f"\n  {nombre_ninja} VS {nombre_mojojojo}")
print("  The battle begins!\n")

# EL BUCLE PRINCIPAL
while not verify_winner (hp_ninja, hp_mojojojo,nombre_ninja):

    # 1. Mostrar estado actual
    show_status(nombre_ninja, hp_ninja, nombre_mojojojo, hp_mojojojo)

    # 2. Turno del jugador
    hp_ninja, hp_mojojojo, potions = player_turn(hp_ninja,hp_mojojojo, potions,nombre_ninja)

    # 3. Verificar si el enemigo murió con el ataque del jugador
    if verify_winner(hp_ninja, hp_mojojojo,nombre_ninja):
        break 

    # 4. Turno del enemigo
    hp_ninja, hp_mojojojo = enemy_turn(hp_ninja, hp_mojojojo,nombre_ninja,nombre_mojojojo)

# Estado final
show_status(nombre_ninja, hp_ninja, nombre_mojojojo, hp_mojojojo)
print("\n  Thanks for playing Terminal Souls!")