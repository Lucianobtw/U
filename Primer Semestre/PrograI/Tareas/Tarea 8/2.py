"""2. Genera una matriz de 5x5 con números aleatorios, luego fila por medio asignar 0 a los
valores, luego mostrar por pantalla (10 Pts)"""


#Entrada : int(filas), int(columnas) corresponden a la cantidad de filas y columnas de la matriz.
#Salida : matriz de 10x10 con modificacion de datos.

#Comentario: si al ejecutar aparecen 0 consecutivos es por los numeros random.

import random as rd

filas = 5
columnas = 5

def Matriz(filas,columnas):
    return [[rd.randint(0,100) for i in range(0,columnas)] 
                        for i in range(0,filas)]

def ceros():
    for i in range(len(test)):
        if i%2 == 0:
            for x in range (len(test[i])):
                test[i][x] = 0
    for i in test:
        print(i)
    return

test = Matriz(filas,columnas)
ceros()

