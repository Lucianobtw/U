#Datos de entrada: Numeros aleatorios
"""Proceso: utilizo la biblioteca "random" para generar 3 numeros aleatorios
(uso "random.uniform(0,7)") para cumplir con lo solicitado en la actividad)),
luego defino la suma de los 3 numeros generados y finalmente el resultado se divide por 3 para calcular el promedio."""
#Datos de salida: Promedio de 3 numeros.
from random import random
import random
espacio=(" ")
num1=random.uniform(0, 7)
num2=random.uniform(0, 7)
num3=random.uniform(0, 7)
print (espacio)
print (("- Los numeros aleatorios son:"),(num1, num2, num3))
suma=(num1+num2+num3) 
print (espacio)
print (("- El promedio es de los numeros es:"),(suma/3))
print (espacio)