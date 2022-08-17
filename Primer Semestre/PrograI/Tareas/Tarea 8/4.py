"""4. Genera una función que recibe como parámetro una matriz y un número entero que debe
ser mayor a 0 y menor a la cantidad de filas que posee la matriz, la función debe devolver la
suma de fila indicada en el segundo parámetro. La matriz debe ser de n*m donde n y m se
deben solicitar al usuario, la matriz será rellenada con número enteros aleatorios entre -10
hasta 10 (-10 y 10 están incluidos). Mostrar por pantalla la suma final y la matriz. (10 Pts)"""

#Entrada : int(n);int(m);(a,b) donde a es una matriz de 5x5 con numeros aleatorios entre -10 y 10.
#Salida : str(mensaje) ; int(final)

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
    b = int(input("-Ingrese el numero de una fila; numero entero mayor a 0 y  menor o igual a el numero asignado a la fila: "))
    if n == 0:
        print ("- Para esta seccion solo se admiten numeros naturales")
        exit(1)
except:
    (ValueError,NameError)
    print ("- Para esta seccion solo se admiten numeros naturales")
    exit(1)

#numero entero menor a la cantidad de n
#numero visual de la fila, no su indice.
#ejemplo b = 1 => indice [0]

#la suma se ejecuta en la 3ra fila contable, no fila[3].

def matriz(a,b):
    indiceb = b - 1
    for i in a:
        print(i)
    for i in range(len(a)):
        if i == indiceb:
            for x in a[i]:
                suma = sum(a[i])
                return suma
final = matriz(a,b)

print("- La suma de los numeros corresponde a:",final)
