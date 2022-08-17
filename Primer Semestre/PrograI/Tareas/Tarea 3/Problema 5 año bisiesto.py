#Dato de entrada: Año
"""Defino la variable anio, luego uso el condicional if para calcular si el modulo
del año ingresado/4 o 400 =0, si esto es verdadero, entonces el año ingresado es 
bisiesto, de lo contrario mediante "else" se indicara que el año no es bisiesto."""
#Dato de salida: "Año bisiesto" o "No bisiesto"

anio=int(input("- Ingrese un año"))
if ((anio % 4==0) and (anio%400==0)):
	print("- El año ingresado es bisiesto.")
else: print("- El año ingresado NO es bisiesto.")
