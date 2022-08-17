#Entradas: [str(palabras)] , str(caracter)
#Salida str(final) (palabras concatenadas)

a = ["Luciano","Juan","Rodrigo","Pedro"]
b = "-"

def union(a,b):
    final = ""
    for x in a:
        if x == a[-1]:
            final += x
        else: final += x + b
    return final

print(union(a,b))
