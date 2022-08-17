#Entradas: int(cantidad) ; (cantidad a iterar la secuencia)
#Salida: Secuencia fibonacci en funcion a la cantidad de entrada.

def fibonacci(cantidad):
    if cantidad < 2:
        return cantidad
    return fibonacci(cantidad-1) + fibonacci(cantidad-2)

cantidad = (int(input("- Ingrese la cantidad a a iterar:")))
l_fibo = []
for i in range(cantidad):
    l_fibo.append(fibonacci(i))
print(l_fibo)

