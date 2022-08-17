#Entrada: 5 numeros aleatorios enteros entre -1000 y 1000
#Salida: Suma de los elementos generados en la lista
import random as rd
lista = []
for i in range(5):
    numeros = rd.randint(-1000,1000)
    lista.append(numeros)
print (lista)
def suma():
    suma = (lista[0]+lista[1]+lista[2]+lista[3]+lista[4])
    return suma
print (suma())
