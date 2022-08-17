#Dato de entrada: Numero
"""Proceso: uso condicional "if", si el numero es mayor a 0 se mostrara el numero ingresado, en cambio si es menor
a 0, se mostrara el numero ingresado*-1. """
#Dato de salida: Valor absoluto del numero ingresado.

numero=(int(input("- Ingrese un numero para calcular su valor absoluto: ")))
abstxt=("- El valor absoluto del numero ingresado es:")

if numero>0:
    print (abstxt, numero)
elif numero<0:
    print (abstxt, (numero)*-1)
