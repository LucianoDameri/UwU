from funciones import *

nombres=[]


for x in range(3):
    nombre=input("Ingrese nombre: ")
    nombres.append(nombre)
print(nombres)

 
nombre_ml(nombres)
crear_csv(nombres)