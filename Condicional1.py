'''
Script que identifica si un
numero Z ingresado por el usuario
es PAR.
Validaciones:
El numero debe ser positivo
'''
import os

os.system("cls")

num = 0

print("Ingrese un numero entero: ")
num = int(input())

if num >= 0 :
    if num % 2 == 0 :
        print("El numero es PAR")
    else :
        print("El numero es IMPAR")
else :
    print("::: NO SE ACEPTAN VALORES NEGATIVOS ::: ")        