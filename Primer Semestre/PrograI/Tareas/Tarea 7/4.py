# Entradas: str(a) ; str(b)
# Salida: str(mensaje) ; True or False, dependiendo si hay coincidencia entre ambas entradas.

def caracteres(a,b):
    print(any(i == b for i in a))
    return

a = input("- Ingrese una cadena de caracteres: ")
b = input("- Ingrese el caracter a analizar: ")
caracteres(a,b)