#Importar la libreria math para operaciones matematicas como aproximacion
import math
print(" ")
print("Ejercicio 5: Numero de micros Discos 3.5 necesarios")
print(" ")
#Pedir el ingreso de los datos 
print("Ingrese GB: ")
GB=float(input())
#Realizar operaciones para encontrar el Numero de discos 3.5
MG=GB*1024
MD=MG/1.44
#Dar a conocer la cantidad de discos 3.5 necesarios sin aproximacion
print(MD)
#Dar a conocer la cantidad de discos 3.5 necesarios con aproximacion
print("Numero de discos necesarios:",math.ceil(MD))