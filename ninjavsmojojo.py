import random

hp_ninja = 100

hp_mojojojo = 120

pocion = 3

nombre_ninja = ""

nombre_mojojojo = "mojojojo"


def enemy_turn(hp_ninja, hp_mojojojo):

 # el enemigo golpea con daño aletorio
    damage = random.randint(10, 20)

 # se le resta el mdaño al hp del ninja
    hp_ninja -= damage
    print(
        f"The enemy attacks and deals {damage} of damage, HP Ninja:{hp_ninja}")
    return hp_ninja, hp_mojojojo
# verificar de ganador


def verify_winner(hp_ninja, hp_mojojojo):

    # si el ninja o el enemigo llegan a 0 hay un ganador

    if hp_mojojojo <= 0:
        print("👑YOU WON! The enemy has been defeated 🏆")
        print("⚔️You are the champion of the battlefield")
        return True
    elif hp_ninja <= 0:
        print("🕊️YOU LOST! Your life reaches zero 🕊️")
        print("The enemy has defeated you 👻")
        return True

    return False
