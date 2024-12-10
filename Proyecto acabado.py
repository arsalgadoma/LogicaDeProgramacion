#Declarar random, para eleccion aleatoria de numeros
from random import *

while True:
  #  Mensaje de Bienvenida
  print("\n***Bienvenido a tu juevo de Pierda, Papel o Tijeras***")
  print("1. Piedra")
  print("2. Papel")
  print("3. Tijera")
  print("4. Salir")

  #Solicitar opción de usuario
  OP_JUGADDOR = input("Selecciona una opción (1-3): ")

  if  OP_JUGADDOR == "1" or OP_JUGADDOR == "2" or OP_JUGADDOR == "3":
    #Eleccion de computadora
    OP_COMP = choice(["1", "2", "3"])

    #Mostrar eleccion del computadora
    if  OP_COMP == "1":
      print ("La opcion de la computadora es: Piedra")
    elif OP_COMP == "2":
      print ("La opcion de la computadora es: Papel")
    else:
      print ("La opcion de la computadora es: Tijera")

    #Mostrar eleccion del jugador
    if  OP_JUGADDOR == "1":
      print ("Tu elección fue: Piedra")
    elif OP_JUGADDOR == "2":
      print ("Tu elección fue: Papel")
    else:
      print ("Tu elección fue: Tijera")

    #Mostrar resultado
    if  OP_JUGADDOR == OP_COMP:
      print ("\n\t>>> EMPATE <<<")
    elif (OP_JUGADDOR == "1" and OP_COMP == "3") or (OP_JUGADDOR == "2" and OP_COMP == "1") or (OP_JUGADDOR == "3" and OP_COMP == "2"):
      print ("\n\t>>> GANASTE <<<")
    elif (OP_JUGADDOR == "1" and OP_COMP == "2") or (OP_JUGADDOR == "2" and OP_COMP == "3") or (OP_JUGADDOR == "3" and OP_COMP == "1"):
      print ("\n\t>>> PERDISTE <<<") 
    
    #Preguntar si desea continuar con el juego
    respuesta = input("\n¿Quieres seguir jugando? (s/n): ").lower()
    if respuesta != "s" and respuesta != "Si" and respuesta != "si":
        print("Saliendo del programa...")
        break # Salir del bucle y terminar el programa
  
  elif OP_JUGADDOR == "4":
    print ("Gracias por jugar")
    break # Salir del bucle y terminar el programa
  else:
    print("Opción incorrecta. Por favor, elige una opción ente 1- 3.")


