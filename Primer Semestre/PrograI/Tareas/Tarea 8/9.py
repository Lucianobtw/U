"""9. Genera una función que recibe como parámetro una matriz, la función debe retornar un
tupla que en indica la posición de fila y columna donde encuentra el número más alto que
existe en la matriz. La matriz debe ser de n*m donde n y m se deben solicitar al usuario, la
matriz será rellenada con número enteros aleatorios entre -10 hasta 10 (-10 y 10 están
incluidos). Finalmente mostrar por pantalla la tupla, el valor más alto y la matriz generada.
(10 Pts)"""

#Entrada: int(n);int(m); (a) donde a es una matriz de nxm con numeros aleatorios entre -10 y 10.
#Salida: str(mensaje); int(majlist) ; tupla de posicion

import random as rd

#n = filas
#m = columnas
try:
    n = int(input("- Ingrese la cantidad de filas de la matriz: "))
    if n == 0:
        print ("- Matriz vacia")
        exit(1)
    m = int(input("- Ingrese la cantidad de columnas de la matriz: "))
    if n == 0:
            print ("- Matriz vacia")
            exit(1)
    a = [[rd.randint(-10,10) for i in range(0,m)] 
                            for i in range(0,n)]
except:
    (ValueError,NameError)
    print ("- Para esta seccion solo se admiten numeros naturales")
    exit(1)


def pos(s):
    busqueda = ((x,  y) for x,  row in enumerate(a)
                        for y,  elemento in enumerate(row)  if elemento == (s))

    for e in busqueda:
        print(e)


def mayor():
    filaslist = []
    for i in a:
        print(i)
        mayor = max(i)
        filaslist.append(mayor)
    majlist = max(filaslist)
    print("- El numero mayor es: ",majlist)
    pos(majlist)
    return majlist

mayor()
