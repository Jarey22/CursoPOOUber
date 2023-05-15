#importamos la libreria math para que nos permita realizar operaciones matematicas como sacar el coseno del angulo
import math
print(" ")
print("Complemento 7: Hallar la medida del tercer lado del triangulo")
print(" ")
#Definir cuanto vale la variable PI
PI=3.1416
#Pedir el ingreso de los lados B y C y guardarlos en sus variables
print("Ingrese cuanto mide cada lado del triangulo:")
b=float(input("Lado B: "))
c=float(input("Lado C: "))
#Pedir el ingreso del angulo que se encuentra entre el lado B y C  y guardarlo en su variable para hallar la medida del angulo A
print("Ingrese el angulo en grados sexadesimales:")
alfa=float(input())
#Operacion para poder encontrar cuanto mide el lado A segun los datos anteriormente ingresados
a=(b**2+c**2-2*b*c*math.cos(alfa*PI/180))**0.50
#Dar a conocer el resultado obtenido de la operacion anterior
print("El lado A mide: ",a)