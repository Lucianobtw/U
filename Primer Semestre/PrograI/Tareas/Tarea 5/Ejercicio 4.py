#Entrada: Numero minimo = 0  numero maximo = 100
#Salida: lista[] contiene los numeros pares del 0 al 100

def Pares(m):
    n = 0
    lista = []
    while n <= m:
        lista.append(n)
        n += 2
    return lista

print(Pares(100))
