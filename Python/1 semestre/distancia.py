print(" ")
print("Ejercicio 6: Distancia entre los puntos A y B, en 2D")
print(" ")
#Pedir el ingreso de las coordenadas de ambos puntos
print("Ingrese la coordenadas del punto A:")
AX=float(input("Ax: "))
AY=float(input("Ay: "))
print("Ingrese las coordenas del punto B:")
BX=float(input("Bx: "))
BY=float(input("By: "))
#Operacion para encontrar la distancia entre los dos puntos A y B
D=((AX-BX)**2+(AY-BY)**2)**0.5
print("-------------------")
#Dar a conocer la distancia entre ambos puntos
print("Distancia entre los puntos A y B es:",D)