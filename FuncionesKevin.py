import random
hp_ninja = 100
hp_mojojojo = 120
potions = 3
nombre_mojojojo = "Mojojojo"

# generador de daño toma de parametros el rango de daño y returna un número aleatorio entre el rango que metimos.
def damage_generator (minimo, maximo):
    return random.randint(minimo, maximo)

def show_status (nombre_ninja, hp_ninja, nombre_mojojojo, hp_mojojojo):
    
    def barra_vida (hp_actual, hp_maximo):
        lleno = max(0, round((hp_actual / hp_maximo) * 10))
        vacio = 10 - lleno
        return f"[{'#' * lleno} {'-' * vacio}]"
    
    hp_ninja = max(0, hp_ninja)
    hp_mojojojo = max(0, hp_mojojojo)
    print("\n" + "=" * 40)
    print(f" {nombre_ninja: <10} {barra_vida(hp_ninja, 100)} {hp_ninja} HP")
    print(f" {nombre_mojojojo: <10} {barra_vida(hp_mojojojo, 120)} {hp_mojojojo} HP")
    print("=" * 40)


def player_turn (hp_ninja, hp_enemigo, potions):
    
    accion_valida = False

    while not accion_valida:
        print(f"\n Potions: {potions}")
        print(" 1. Attack               (daño: 15-25)")
        print(" 2. heal                 (Recupera 20 HP)")
        print(" 3. Special Attack       (daño: 30-50, falla 50%)")

        eleccion = input("\n Elige  tu accion (1/2/3): ").strip()

        if eleccion == "1":
            damage = damage_generator(10, 25)
            critico = random.random() <0.10
            if critico:
                damage *= 2
                print(" *** GOLPE CRITICO! ***")
            hp_enemigo -= damage
            print(f"The Ninja {nombre_ninja} hits {nombre_mojojojo} -{damage} damage.")
            accion_valida = True
        elif eleccion == "2":
            if potions <= 0:
                print(" You have 0 potions left! Choose another action.")
            else:
                hp_ninja += 20
                hp_ninja = min(hp_ninja, 100)
                potions -= 1
                print(f" The Ninja {nombre_ninja} used a potion and got 20 HP ")
                accion_valida = True
        elif eleccion == "3":
            fallo = random.random() <0.50
            if fallo:
                print(f" The Ninja {nombre_ninja} tried the Special Attack... But failed!")
            else:
                damage = damage_generator (30, 50)
                critico = random.random() <0.10
                if critico:
                    damage *= 2
                    print(" *** GOLPE CRITICO! ***")
                hp_mojojojo -= damage
                print(f" Ninja {nombre_ninja} used his Special Attack and hits {nombre_mojojojo} -{damage} damage.")
                accion_valida = True
        else:
            print(" Invalid Option. Choose either 1,2, or 3.")
    
    return hp_ninja, hp_mojojojo, potions  