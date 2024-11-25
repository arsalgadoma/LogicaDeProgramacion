#Declarar random, para eleccion aleatoria de números
from random import *
#  Mensaje de Bienvenida
print("Bienvenido a tu juevo de Pierda, Papel o Tijeras")


#Elejir una opción de usuario
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
OP_JUGADDOR = int(input("Elige una opción: "))

#Eleccion de computadora
OP_COMP=int(1)
print ("La opcion de la computadora es:", OP_COMP)

#Mostrar elección de jugador
if  OP_JUGADDOR == 1:
    print ("Tu elección fue: Piedra")
elif OP_JUGADDOR == 2:
    print ("Tu elección fue: Papel")
elif OP_JUGADDOR == 3:
     print ("Tu elección fue: Tijera")
else:
    print ("Escogiste una opcion incorrecta")

#Mostrar opción de computador
if  OP_COMP == 1:
    print ("La opcion de la computadora: Piedra")
elif OP_COMP == 2:
    print ("La opcion de la computadora: Papel")
else:
    print ("La opcion de la computadora: Tijera")

#Comparar resulados
if  OP_JUGADDOR == OP_COMP:
    print ("Empate")
elif (OP_JUGADDOR == 1 & OP_COMP == 3) or (OP_JUGADDOR == 2 & OP_COMP == 1) or (OP_JUGADDOR == 3 & OP_COMP == 2):
    print ("Ganaste")
elif (OP_JUGADDOR == 1 & OP_COMP == 2) or (OP_JUGADDOR == 2 & OP_COMP == 3) or (OP_JUGADDOR == 3 & OP_COMP == 1):
    print ("Perdiste")    
else :
    print ("Hubo un error")
