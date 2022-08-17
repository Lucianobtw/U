#Entrada:   Funcion 1000
#Salida: (int(mutiplicacion 1*2*3*4....*1000))
mil = 1000
def multi(mil):
    uno = 1
    while(mil>1):
        uno = mil * uno
        mil -= 1
    return uno

print (multi(mil)) 