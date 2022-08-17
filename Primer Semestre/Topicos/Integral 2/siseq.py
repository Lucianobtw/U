#!/usr/bin/python3
import os
# se verifica si existe la libreria numpy.

try: import numpy as np #.........si hay existencias, se importa numpy.
except:
    os.system("python -m pip install numpy")#... de lo contrario, se instala numpy.

# Funcion que identifica si el sistema no posee soluciones.
def sinSoluciones(a, b): 
    if a[0] == b[0] \
    and a[1] == b[1] \
    and a[2] == b[2] \
    and a[3] != b[3]:
        print("Sistema sin soluciones")
        exit(0) #........... Se finaliza la ejecucion del programa

# Funcion que identifica si el sistema infinitas soluciones.
def infinitasSoluciones(a, b):
    if a[0] == b[0] \
    and a[1] == b[1] \
    and a[2] == b[2] \
    and a[3] == b[3]:
        print("El sistema posee Infinitas Soluciones")
        exit(0) #........... Se finaliza la ejecucion del programa


def main():
    print("Se debe reemplazar aij, bij por valores numéricos")
    eqs = np.zeros((3, 3))
    results = np.zeros(3)

    for i in range(3):
        for j in range(3):
            eq = float(input(f"Ingrese el valor numérico de a{i+1}{j+1}\n> "))
            eqs[i][j] = eq
        res = float(input(f"Ingrese el valor numérico de b{i+1}\n> "))
        results[i] = res

    eqAux1 = np.array([eqs[0][0], eqs[0][1], eqs[0][2], results[0]]) * results[1]
    eqAux2 = np.array([eqs[1][0], eqs[1][1], eqs[1][2], results[1]]) * results[0]

    infinitasSoluciones(eqAux1, eqAux2)

    eqAux1 = np.array([eqs[0][0], eqs[0][1], eqs[0][2], results[0]]) * results[2]
    eqAux2 = np.array([eqs[2][0], eqs[2][1], eqs[2][2], results[2]]) * results[0]

    infinitasSoluciones(eqAux1, eqAux2)

    eqAux1 = np.array([eqs[1][0], eqs[1][1], eqs[1][2], results[1]]) * results[2]
    eqAux2 = np.array([eqs[2][0], eqs[2][1], eqs[2][2], results[2]]) * results[1]

    infinitasSoluciones(eqAux1, eqAux2)

    eqAux1 = np.array([eqs[0][0], eqs[0][1], eqs[0][2], results[0]])
    eqAux2 = np.array([eqs[1][0], eqs[1][1], eqs[1][2], results[1]])

    sinSoluciones(eqAux1, eqAux2)

    eqAux1 = np.array([eqs[0][0], eqs[0][1], eqs[0][2], results[0]])
    eqAux2 = np.array([eqs[2][0], eqs[2][1], eqs[2][2], results[2]])

    sinSoluciones(eqAux1, eqAux2)

    eqAux1 = np.array([eqs[1][0], eqs[1][1], eqs[1][2], results[1]])
    eqAux2 = np.array([eqs[2][0], eqs[2][1], eqs[2][2], results[2]])

    sinSoluciones(eqAux1, eqAux2)

    c = np.linalg.solve(eqs, results)
    print(c)


if __name__ == '__main__':
    main()
