import random
# Entrada: int(user)
# Salida: str(mensaje) int(countintent)
aleatorio = random.randint(0,100)
print (aleatorio)
Congrats = "Felicidades has acertado!!!"
May = "El numero que ingresaste es mayor, tienes mas intentos."
Min = "El numero que ingresaste es menor, tienes mas intentos."
countintent = 1 
while True:
    user=int(input("- Intente acertar el numero aleatorio entre 1 y 100: "))
    if user == aleatorio:
        print(Congrats,"\n",countintent)
        break
    elif user>aleatorio:
        print(May)
        countintent = countintent + 1
    elif user<aleatorio:
        print(Min)
        countintent = countintent + 1

