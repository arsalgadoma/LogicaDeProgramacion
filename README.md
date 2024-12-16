from random import choice

#  Mensaje de Bienvenida
def mostrar_menu():
    print("\n***Bienvenido a tu juego de Piedra, Papel o Tijeras***")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")

#Eleccion de computadora
def eleccion_computadora():
    return choice(["1", "2", "3"])

#Mostrar eleccion del computadora
def mostrar_eleccion_computadora(OP_COMP):
    if OP_COMP == "1":
        print("La opción de la computadora es: Piedra")
    elif OP_COMP == "2":
        print("La opción de la computadora es: Papel")
    else:
        print("La opción de la computadora es: Tijera")

#Mostrar eleccion del jugado
def mostrar_eleccion_jugador(OP_JUGADOR):
    if OP_JUGADOR == "1":
        print("Tu elección fue: Piedra")
    elif OP_JUGADOR == "2":
        print("Tu elección fue: Papel")
    else:
        print("Tu elección fue: Tijera")

#Realizar comparación
def determinar_resultado(OP_JUGADOR, OP_COMP):
    if OP_JUGADOR == OP_COMP:
        return "\n\t>>> EMPATE <<<"
    elif (OP_JUGADOR == "1" and OP_COMP == "3") or (OP_JUGADOR == "2" and OP_COMP == "1") or (OP_JUGADOR == "3" and OP_COMP == "2"):
        return "\n\t>>> GANASTE <<<"
    else:
        return "\n\t>>> PERDISTE <<<"

#Iniciar juego
def jugar():
    while True:
        mostrar_menu()

        # Solicitar opción de usuario
        OP_JUGADOR = input("Selecciona una opción (1-3): ")

        if OP_JUGADOR in ["1", "2", "3"]:
            # Elección de computadora
            OP_COMP = eleccion_computadora()

            # Mostrar elecciones
            mostrar_eleccion_computadora(OP_COMP)
            mostrar_eleccion_jugador(OP_JUGADOR)

            # Determinar y mostrar resultado
            resultado = determinar_resultado(OP_JUGADOR, OP_COMP)
            print(resultado)

            # Preguntar si desea continuar
            respuesta = input("\n¿Quieres seguir jugando? (s/n): ")
            if respuesta not in ["s", "si", "SI", "Si"]:
                print("Saliendo del programa...")
                break  # Salir del bucle y terminar el programa

        elif OP_JUGADOR == "4":
            print("Gracias por jugar")
            break  # Salir del bucle y terminar el programa
        else:
            print("Opción incorrecta. Por favor, elige una opción entre 1-3.")

# Iniciar el juego
jugar()
