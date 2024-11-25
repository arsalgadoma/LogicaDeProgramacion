#Declarar random, para eleccion aleatoria de numeros
from random import *

#  Mensaje de Bienvenida
print("Bienvenido a tu juevo de Pierda, Papel o Tijeras")


#Elejir una opción de usuario
print("1. Piedra")
print("2. Papel")
print("3. Tijera")
OP_JUGADDOR=int(input("Elige una opción:"))

#Eleccion de computadora
OP_COMP=randint(1, 3)
print ("La opcion de la computadora es:", OP_COMP)
