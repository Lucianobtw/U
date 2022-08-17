"""3 - Genera una matriz de 5x5 con números aleatorios, luego columna por medio asignar 0 a los
valores, finalmente mostrar por pantalla la matriz. (10 Pts)"""

#Entrada : (a,b) donde a es una matriz de 5x5 con numeros aleatorios entre -10 y 10.
#Salida : matriz de 10x10 con modificacion de datos.

#Comentario: si al ejecutar aparecen 0 consecutivos es por los numeros random.

import random as rd

def Matriz(filas,columnas):
    return [[rd.randint(0,100) for i in range(0,columnas)] 
                        for i in range(0,filas)]


def ceros():
    for i in range(filas):
            for x in range (0,filas,2):
                test[i][x] = 0
    for i in test:
        print(i)
    return

filas = 5
columnas = 5

test = Matriz(filas,columnas)
ceros()
