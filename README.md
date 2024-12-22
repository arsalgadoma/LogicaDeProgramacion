from random import choice

#Mensaje de Binevanida, en esta función podemos encontraron el menú de opciones a escoger para poder llevar a cabo el juego de piedra papel o tijeras

def mostrar_menu():
    print("\n***Bienvenido a tu juego de Piedra, Papel o Tijeras***")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")


#Eleccion de computadora, en esta sección la computadora va a tomar un valor randomico entre 1 y 3.

def eleccion_computadora():
    return choice(["1", "2", "3"])


#Mostrar eleccion del computadora, este apartado permite que el usurio tenga conocimiento de cual fue la opción escogida por el usuario, dentro de esta función permite que el código pase la opcion de 1, 2 o 3 a piedra papel o tijeras

def mostrar_eleccion_computadora(OP_COMP):
    if OP_COMP == "1":
        print("La opción de la computadora es: Piedra")
    elif OP_COMP == "2":
        print("La opción de la computadora es: Papel")
    else:
        print("La opción de la computadora es: Tijera")


#Mostrar eleccion del jugado, esta función el código muestra la oopcion ingresada por el usuario (1, 2, 3) pero como la opción de piedra, papel o tijera

def mostrar_eleccion_jugador(OP_JUGADOR):
    if OP_JUGADOR == "1":
        print("Tu elección fue: Piedra")
    elif OP_JUGADOR == "2":
        print("Tu elección fue: Papel")
    else:
        print("Tu elección fue: Tijera")


#Realizar comparación, mediante el condicioanl if se va a realizar la comparación de la opción del computador con la del usuario para saber quien fue el ganador o perdedor, o si fue un empate

def determinar_resultado(OP_JUGADOR, OP_COMP):
    if OP_JUGADOR == OP_COMP:
        return "\n\t>>> EMPATE <<<"
    elif (OP_JUGADOR == "1" and OP_COMP == "3") or (OP_JUGADOR == "2" and OP_COMP == "1") or (OP_JUGADOR == "3" and OP_COMP == "2"):
        return "\n\t>>> GANASTE <<<"
    else:
        return "\n\t>>> PERDISTE <<<"


#Iniciar juego, se tiene el bucle principal en donde se tiene el desarrollo del juego

def jugar():
    while True:
        mostrar_menu() #Se muestra el menú
        
        # El juego solicita al usuario que ingrese su eleccion
        OP_JUGADOR = input("Selecciona una opción (1-3): ")

        if OP_JUGADOR in ["1", "2", "3"]:
            OP_COMP = eleccion_computadora()

            # # Se muestran la elecciones del jugador y de computador
            mostrar_eleccion_computadora(OP_COMP)
            mostrar_eleccion_jugador(OP_JUGADOR)

            # Mostrar el resultado despues de comparar las elecciones
            resultado = determinar_resultado(OP_JUGADOR, OP_COMP)
            print(resultado)

            # Preguntar si desea continuar
            respuesta = input("\n¿Quieres seguir jugando? (s/n): ")
            if respuesta not in ["s", "S", "si", "SI", "Si"]:
                print("Saliendo del programa...")
                break  # Salir del bucle y terminar el programa

            #En caso de que el cliente no desee jugar y haya ingresado al juego, podrá tener la opción de salir de él
        elif OP_JUGADOR == "4":
            print("Gracias por jugar")
            break  # Salir del bucle y terminar el programa
        else:
            # El usuario debe escoger la opción entre 1 y 3 patra jugar o el numero 4 para salir, de lo contrario no se va a poder ingresar a la condicional y avanzar con el juego
            print("Opción incorrecta. Por favor, elige una opción entre 1-3.")

# Iniciar el juego
jugar()
