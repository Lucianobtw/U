import numpy as num
from numpy import *

print("Ingrese la PRIMERA ecuacion del sistema: ")
x1 = float(input("Coheficiente x: ")) ; y1 = float(input("Coheficiente y: ")) ; z1 = float(input("Coheficiente z: "))
res1 = float(input("Resultado de la ecuacion: "))

print("Ingrese la SEGUNDA ecuacion del sistema: ")
x2 = float(input("Coheficiente x: ")) ; y2 = float(input("Coheficiente y: ")) ; z2 = float(input("Coheficiente z: "))
res2 = float(input("Resultado de la ecuacion: "))

print("Ingrese la TERCERA ecuacion del sistema: ")
x3 = float(input("Coheficiente x: ")) ; y3 = float(input("Coheficiente y: ")) ; z3 = float(input("Coheficiente z: "))
res3 = float(input("resultado de la ecuacion: "))

a = num.array ([[x1,y1,z1],[x2,y2,z2],[x3,y3,z3]])
b  = num.array ([[res1],[res2],[res3]])
c = num.linalg.solve(a,b)
print(f'El valor de X es: {c[0]}\nEl valor de Y es: {c[1]}\nEl valor de Z es: {c[2]}')

"""𝑥 + 𝑦 + 𝑧 = 1
𝑥 + 2𝑦 + 2𝑧 = −1
𝑥 + 𝑦 + 𝑧 = 2"""

