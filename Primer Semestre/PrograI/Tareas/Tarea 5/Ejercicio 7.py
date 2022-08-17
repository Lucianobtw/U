#Entrada: Funcion Primos
#Salida:numeros primos desde 0 al 100
def primos(numero):
    valor= range(2,numero)
    contador = 0
    if numero == 0 or numero == 1:
        return False
    for n in valor:
        if numero % n == 0:
            contador +=1
    if contador > 0 :
        return False 
    else:
        return True


for i in range(0,101):
    if primos(i):
        print(i)
