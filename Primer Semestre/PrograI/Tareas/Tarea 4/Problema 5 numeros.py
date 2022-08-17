#Dato de entrada: int or float (number)
#Proceso: defino "listan" y "selectrandom", para que en caso de haber 2 numeros iguales elija cualquiera de los 2,
#luego uso ciclo for para repetir 2 veces el ingreso de la variable number.. continuo definiento los casos posibles
# y uso condicionales para comprobarlos luego ingreso otro numero y lo multiplico por el numero menor anterior para despues comproabar si el resultado es 
# menor, mayor o igual al anteror numero menor.
#Dato de salida: str(mensaje)

import random
def selectRandom(listan):
    return random.choice(listan)
listan=[]
for i in range(2):
    number=float(input("- Ingrese un numero a la vez: "))
    listan.append(number)
menortxt="- El numero menor es: "
multitxt="- El resultado de la multiplicacion es: "
menor0= (listan[0])<(listan[1])
menor1= (listan[0])>(listan[1])
same= (listan[0])==(listan[1])

if menor0==True:
    print (menortxt,(listan[0]))
    result=listan[0]
elif menor1==True:
    print (menortxt,(listan[1]))
    result=listan[1]
elif same==True:
    print (menortxt,(selectRandom(listan)))
    result=(selectRandom(listan))

num3=float(input("- Ingrese un nuevo numero: "))
multi= ((num3)*float(result))

if multi==int(multi):
    print (multitxt,(int(multi)))
else: print (multitxt,(float(multi)))

if multi>float(result):
    print ("- La multiplicacion es mayor que el anterior numero menor.")
elif multi<float(result):
    print ("- La multiplicacion es menor que el anterior numero menor.")
else: 
    print ("- La multiplicacion es igual que el anterior numero menor.")