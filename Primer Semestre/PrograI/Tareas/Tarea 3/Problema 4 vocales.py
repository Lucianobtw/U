#Dato de entrada: Caracter
"""Proceso: uso condicionales para indicar a que caracter corresponde, si lo es imprimira un mensaje en pantalla, 
de lo contrario, mediante "else" imprimira otro mensaje pero indicando que el caracter ingresado no es una vocal"""
#Dato de salida: mensaje de confirmación o negación dependiendo si se ingresa una vocal o no.
espacio=("   ")
print (espacio)
caracter=(input("- ingrese un caracter: "))
print(espacio)
if caracter==("a"or"e"or"i"or"o"or"u"or"A"or"E"or"I"or"O"or"U"or"á"or"é"or"í"or"ó"or"ú"or"Á"or"É"or"Í"or"Ó"or"Ú"):
    print ("- El caracter ingresado corresponde a una vocal")
else: 
    print("- El caracter ingresado NO corresponde a una vocal")
print (espacio)

