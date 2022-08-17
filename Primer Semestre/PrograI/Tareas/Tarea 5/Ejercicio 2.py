#Entrada: int or float(n1),int or float(n2),int or float(n3)
#Salida: int, float or str(resultado)

def menor(n1,n2,n3):
    igualestxt="-Todos los numeros son iguales"
    if n1<n2 and n1<n3: resultado = n1
    elif n2<n1 and n2<n3: resultado = n2
    elif n3<n2 and n3<n1: resultado = n3
    elif n3 == n2 == n1:
        resultado=igualestxt
    return resultado

n1 = float(input("-Ingrese el primer numero: "))
n2 = float(input("-Ingrese el primer numero: "))
n3 = float(input("-Ingrese el primer numero: "))
print(menor(n1,n2,n3))