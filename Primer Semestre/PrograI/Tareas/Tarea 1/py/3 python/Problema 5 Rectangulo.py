#Datos y variables de entrada: Base y altura
#Proceso: Defino y aplico las formulas de perimetro y area del rectangulo
#Datos de salida: Resultados (perimetro y area)
espacio=("     ")
print("o-------------------------------------------------o")
print ("            Area y Perimetro del Rectangulo           ")
print (espacio)
altura = float(input("- Ingrese la altura: "))
base = float(input("- Ingrese la base: "))
print("o-------------------------------------------------o")
#Proceso
perimetro=((altura*2)+(base*2))
area=(altura*base)
print("                   RESULTADOS           ")
print (espacio)
#Datos de Salida
if int(perimetro):
    print (("- El perimetro del rectangulo es:"), int(perimetro))
    print (espacio)
else: print (("- El perimetro del rectangulo es:"),(float(perimetro)))
if int(area):
    print (("- El area del rectangulo es:"), int(area))
    print (espacio)
else: print (("- El area del rectangulo es:"),(float(area)))
print ("---o---o---o--- Fin del programa -o---o---o---")
print (espacio)
