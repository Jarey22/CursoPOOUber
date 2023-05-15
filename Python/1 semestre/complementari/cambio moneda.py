print(" ")
print("Complemento 3: Cambio de monedas de SOLES a EUROS y DOLARES")
print(" ")
#Definir el precio de los soles en las diversas monedas a cambiar
EU=3.84
DO=2.28
#Pedir el ingreso de los soles a cambiar y guardarlos en su variable
print("Ingrese la cantidad de soles a cambiar: ")
s=float(input())
#Operacion para encontrar la cantidad de cada moneda segun los soles ingresados anteriormente
d=s/DO
e=s/EU
#Dar a conocer cuanto dinero segun la moneda hay ante la cantidad de soles ingresados
print("En ",s," soles hay una cantidad de: ",e," euros.")
print("En ",s," soles hay una cantidad de: ",d," dolares.")