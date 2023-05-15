print(" ")
print("Ejercicio 3: Puntaje final")
print(" ")
#Pedir el ingreso de los datos y guardarlos en su respectiva variable
print("Ingrese el numero de respuestas correctas: ")
RC=int(input())
print("Ingrese el numero de respuestas incorrectas: ")
RI=int(input())
print("Ingrese el numero de respuestas en blanco: ")
RB=int(input())
#Operaciones para encontrar el resultado de cada respuesta y luego sumarlas para dar el total
PCR=RC*3
PRI=RI*-1
PRB=RB*0
PF=PCR+RI+RB
#Total
print("El puntaje final es: ",PF)