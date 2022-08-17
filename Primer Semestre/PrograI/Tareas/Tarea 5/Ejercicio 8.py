#Entrada: int(numero)
#Salida: int factorial(numero)
def fact(numero):
    if numero == 0:
        return 1
    else:
        f = 1
        while(numero>1):
            f = f*numero
            numero = numero-1
        return f

numero=(int(input("Para obtener factorial ingrese un numero natural:")))
floatxt="Solo se admiten naturales"
if numero < 0:
    print(floatxt)
else: print("El factorial es: " ,fact(numero))

