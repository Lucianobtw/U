"""6. Genera una función que recibe como parámetro una matriz, la función debe retornar la
cantidad de números 1 que existen dentro de la matriz. La matriz debe ser de n*m donde n y
m se deben solicitar al usuario, la matriz será rellenada con números enteros aleatorios entre
-10 hasta 10 (-10 y 10 están incluidos). Mostrar por pantalla la cantidad de números 1 y la
matriz. (10 Pts)"""


#Entrada: int(n);int(m); Matriz 10x10
#Salida: str(mensaje); int(contador)

import random as rd

#n = filas
#m = columnas

try:
    n = int(input("- Ingrese la cantidad de filas de la matriz: "))
    if n == 0:
        print ("- Para esta seccion solo se admiten numeros naturales")
        exit(1)
    m = int(input("- Ingrese la cantidad de columnas de la matriz: "))
    if m == 0:
        print ("- Para esta seccion solo se admiten numeros naturales")
        exit(1)
except:
    (ValueError,NameError)
    print ("- Para esta seccion solo se admiten numeros naturales")
    exit(1)

def Matriz(n,m):
    return [[rd.randint(-10,10) for i in range(0,m)] 
                        for i in range(0,n)]

def ejercicio():
    contador = 0
    for i in range(len(test)):
        print (test[i])
    for i in range(len(test)):
        for x in range (len(test[i])):
            if test[i][x] == 1:
                contador += 1
    print(cantxt,contador)
    return

cantxt = "La cantidad de 1 es: "

test = Matriz(n,m)
ejercicio()

