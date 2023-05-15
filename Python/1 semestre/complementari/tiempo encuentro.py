print(" ")
print("Complemento 8: Tiempo de encuentro")
print(" ")
#Pedir el ingreso de las velocidades de ambos objetos y guardarlos en sus respectivas variables
print("Ingrese las velocidades:")
va=float(input("Velocidad primer objeto: "))
vb=float(input("Velocidad segundo objeto: "))
#Pedir el ingreso de la distancia que los separa y guardarla en su variable
print("Ingrese la distancia que los separa: ")
d=float(input())
#Operacion para encontrar a cuanto tiempo se encontraran ambos objetos
te=d/(va+vb)
#Dar a conocer el tiempo en el que se encontraran ambos objetos
print("Los cuerpos se encontraran en: ",te," segundos.")