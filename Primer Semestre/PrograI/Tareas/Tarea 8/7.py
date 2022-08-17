"""7. Genera una función que recibe como parámetro una matriz, la función debe retornar un
índice que indica cual es la columna que posee la suma más alta. La matriz debe ser de n*m
donde n y m se deben solicitar al usuario, la matriz será rellenada con números enteros
aleatorios entre -10 hasta 10 (-10 y 10 están incluidos). Mostrar por pantalla el índice de la
columna con suma más alta y la matriz. (10 Pts)"""

#n = filas
#m = columnas

#Entrada : int(n);int(m); matriz de 5x5 con numeros aleatorios entre -10 y 10.
#Salida : str(mensaje);int(mayor);int(indice)

import random as rd

#n = filas
#m = columnas

try:
    n = int(input("- Ingrese la cantidad de filas de la matriz: "))
    if n == 0:
        print ("- Para esta seccion solo se admiten numeros naturales")
        exit(1)
    m = int(input("- Ingrese la cantidad de columnas de la matriz: "))
    if n == 0:
        print ("- Para esta seccion solo se admiten numeros naturales")
        exit(1)

    a = [[rd.randint(-10,10) for i in range(0,m)] 
                            for i in range(0,n)]
except:
    (ValueError,NameError)
    print ("- Para esta seccion solo se admiten numeros naturales")
    exit(1)

def matriz(a):
    matrizm = []
    resultados = []
    for i in a:
        print(i)
    for x in range(len(a[0])):
        matrizm.append([])
        for i in range(len(a)):
            matrizm[x].append(a[i][x])
    for i in matrizm:
        suma = sum(i)
        resultados.append(suma)
        mayor = max(resultados)
        indice = resultados.index(mayor)
    print(matrizm)
    print("El mayor es:", mayor,"indice:",indice)
final = matriz(a)
