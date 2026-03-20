import random


def enemy_turn(hp_ninja, hp_mojojojo):

    umbral = 120 * 0.20    # 20% de 120 = 24 HP

    if hp_mojojojo <= umbral:
        # IA básica: el enemigo se cura si está muy bajo
        hp_mojojojo += 25
        hp_mojojojo = min(hp_mojojojo, 120)
        print(f"  {nombre_mojojojo} is critically low... and heals 25 HP!")
    else:
        damage = random.randint(15, 20)
        critico = random.random() < 0.10
        if critico:
            damage *= 2
            print("  * MOJOJOJO CRITICAL HIT! *")
        hp_ninja -= damage
        print(f"  {nombre_mojojojo} attacks {nombre_ninja} for -{damage} damage!")

    return hp_ninja, hp_mojojojo


def verify_winner(hp_ninja, hp_mojojojo):

    # si el ninja o el enemigo llegan a 0 hay un ganador

    if hp_mojojojo <= 0:
        print(f"👑YOU WON Ninja {nombre_ninja}! The enemy has been defeated 🏆")
        print("⚔️You are the champion of the battlefield")
        return True
    elif hp_ninja <= 0:
        print(f"🕊️YOU LOST Ninja {nombre_ninja}! Your life reaches zero 🕊️")
        print("The enemy has defeated you 👻")
        return True

    return False
