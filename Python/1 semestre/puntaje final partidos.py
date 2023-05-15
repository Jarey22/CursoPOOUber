print(" ")
print("Ejercicio 4: Puntaje total de partidos")
print(" ")
#Pedir el ingreso de los datos
print("Ingrese la cantidad de partidos ganados: ")
PG=int(input())
print("Ingrese la cantidad de partidos empatados: ")
PE=int(input())
print("Ingrese la cantidad de partidos perdidos:")
PP=int(input())
#Realizar operacion para encontrar el puntaje final
PPG=PG*3
PPE=PE*1
PPP=PP*0
PF=PPG+PPE+PPP
#Dar a conocer el puntaje final
print("Puntaje Final: ",PF)