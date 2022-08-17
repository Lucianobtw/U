#Datos de entradas: Numero
"""Proceso: Solicito ingresar un numero, si es decimal se imprimira una mensaje en pantalla, si no, calculara si el numero es par o impar,
esto mediamte el resto, si resto=0 entonces el numero es par si no, es impar... por otro lado si numero>0 entonces el numer oes positivo,
de lo contrario el numero sera negativo."""
#Datos de salida: Clasificacion del numero ingresado. (Ejemplo: "- El numero ingresado es impar negativo.")
espacio=("   ")
print(espacio)
numero=float(input("- Ingrese un numero: "))
resto=numero%2
par=resto==0
impar=resto==1
positivo=numero>0
negativo=numero<0
neutro=numero==0
print(espacio)
if numero==float(numero):
    print("- Usted ha ingresado un numero decimal.")
else:
    if par == True:
        print ("- El numero ingresado es par positivo.")
    elif impar == True:
        print ("- El numero ingresado es impar positivo.")

print(espacio)
