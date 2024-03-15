# Numeros aleatorios de python
# Para generar numeros aleatorios en python , usamos la libreria random

# entrada
from random import randint


numero_ingresado = int(input("ingrese un numero del 1 al 30 :"))

 # proceso

numero_generado = randint(1, 30)

if numero_ingresado == numero_generado:
    print("felicitaciones,adivinaste el numero ")

elif numero_ingresado < numero_generado:
    print("el numero a adivinar es mayor a ",str(numero_ingresado),"era el",str(numero_generado))
else:
    print("el numero a aadivinar es menor a",str(numero_ingresado),"era el",str(numero_generado))



