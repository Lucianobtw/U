"""1. Genera una matriz de 10x10 con números aleatorios y muestra por pantalla (10 Pts)"""


#Entrada : int(filas), int(columnas) corresponden a la cantidad de filas y columnas de la matriz 
#Salida : matriz de 10x10 que contiene numeros aleatorios entre 0 y 100

import random as rd

filas = 10
columnas = 10

def Matriz(filas,columnas):
    return [[rd.randint(0,100) for i in range(0,columnas)] 
                        for i in range(0,filas)]

test = Matriz(filas,columnas)

for i in test:
    print(i)
