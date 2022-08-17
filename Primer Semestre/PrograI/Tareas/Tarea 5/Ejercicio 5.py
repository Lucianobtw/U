#Entrada: Funcion multi3
#Salida: Lista[] multiplos de 3 entre 0 y 100 (int)
def multi3(m):
    n = 0
    lista = []
    while n <= m:
        lista.append(n)
        n += 3
    return lista

print(multi3(150))