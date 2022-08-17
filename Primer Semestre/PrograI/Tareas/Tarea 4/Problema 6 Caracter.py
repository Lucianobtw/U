#Dato de entrada: str(character)
#Proceso: muestro por pantalla mensaje que indica que no se pueden ingresar caracteres especiales, luego
#solicito ingresar un caracter, ya sea numero o letra, y  mediante condicionales el programa detectara si el caracter es u numero o una letra.
#Dato de salida: str(mensaje)
print ("No se admiten simbolos especiales (parentesis, signos de interrogacion, exclamacion, etc.)")
character=input("- Ingrese un caracter:")

if character<="0":
    print("- El caracter ingresado es un numero.")
elif len(character)>1:
    print("solo se admite 1 caracter")

elif(character <= "9"):
    print("- El caracter ingresado es un numero.")

else: print("- El caracter ingresado es una letra.")