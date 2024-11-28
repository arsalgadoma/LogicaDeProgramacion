#Declarar random, para eleccion aleatoria de numeros
from random import *

while True:
  #  Mensaje de Bienvenida
  print("\n---------------------------------------------------------\n")
  print("***Bienvenido a tu juego de Pierda, Papel o Tijeras***")
  print("1. Piedra")
  print("2. Papel")
  print("3. Tijera")
  print("4. Salir")

  #Solicitar opción de usuario
  OP_JUGADOR = (input("Selecciona una opción (1-3): "))

  #Eleccion de computadora
  OP_COMP=choice(["1", "2", "3"])

  if  OP_JUGADOR=="1" or OP_JUGADOR=="2" or OP_JUGADOR=="3":
    #Mostrar eleccion del computadora
    if  OP_COMP=="1":
      print ("La opcion de la computadora es: Piedra")
    elif OP_COMP=="2":
      print ("La opcion de la computadora es: Papel")
    else:
      print ("La opcion de la computadora es: Tijera")

    #Mostrar eleccion del jugador
    if  OP_JUGADOR=="1":
      print ("Tu elección fue: Piedra")
    elif OP_JUGADOR=="2":
      print ("Tu elección fue: Papel")
    elif OP_JUGADOR=="3":
      print ("Tu elección fue: Tijera")

    #Mostrar resultado

    if  OP_JUGADOR==OP_COMP:
      print ("\n\t>>> EMPATE <<<")
    elif (OP_JUGADOR=="1" and OP_COMP=="3") or (OP_JUGADOR=="2" and OP_COMP=="1") or (OP_JUGADOR=="3" and OP_COMP=="2"):
      print ("\n\t>>> GANASTE <<<")
    elif (OP_JUGADOR=="1" and OP_COMP=="2") or (OP_JUGADOR=="2" and OP_COMP=="3") or (OP_JUGADOR=="3" and OP_COMP=="1"):
      print ("\n\t>>> PERDISTE <<<")    

    #Preguntar si desea continuar con el juego
    respuesta = input("\n¿Quieres seguir jugando? (s/n): ")
    if respuesta != "s" and respuesta != "Si" and respuesta != "si" and respuesta != "S" and respuesta != "SI":
        print("Gracias por participar")
        break # Salir del bucle y terminar el programa

  elif OP_JUGADOR=="4":
    print ("Gracias por jugar")
    break # Salir del bucle y terminar el programa
  else:
    print("Opción incorrecta. Por favor, elige una opción ente 1- 3.")
