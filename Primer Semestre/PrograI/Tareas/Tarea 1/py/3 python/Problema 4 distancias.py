#Datos y variables de entrada: Digito1 y Digito1_2
#Proceso: Ingreso los parametros para calcular la distancia entre ambos numeros)
#Datos de salida: Resultados (Distancia entre ambos numeros)
espacio=("    ")
print("o-------------------------------------------------o")
print ("            DISTANCIA ENTRE 2 NUMEROS            ")
print (espacio)
#Datos de entrada
numero1= float(input("- Ingrese el primer numero: "))
numero2= float(input("- Ingrese el segundo numero: "))
print (espacio)
print("o-------------------------------------------------o")
print("                   RESULTADOS           ")
print (espacio)
#Proceso
if numero1>numero2:
    diferencia=numero1-numero2
else: diferencia=numero2-numero1
if diferencia==int(diferencia):
    #Datos de salida
    print (("- La distancia entre ambos digitos es de:"), int(diferencia))
else: print (("- La distancia entre ambos digitos es de:"),(float(diferencia)))
print (espacio)
print ("---o---o--- Fin del programa---o---o---")
