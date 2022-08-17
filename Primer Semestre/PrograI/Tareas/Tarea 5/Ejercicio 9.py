#Entrada: int(a) e int(b)
#Salida:  int(mcm)

a=(int(input("ingrese el primer numero: ")))
b=(int(input("ingrese el segundo numero: ")))
def mcd(a,b): 
    mcd=1
    if a > b: 
        if a % b == 0:
            return b
        for i in range(int(b/2),0,-1):
            mcd == i
        return mcd
    elif b>a:
        if b % a == 0:
            return a
        for i in range(int(a/2),0,-1):
            mcd == i
        return mcd
print 

def mcm(a,b):
    return (a*b)/(mcd(a,b))

suma=((mcd(a,b)+(mcm(a,b))))
print ("El max comun divisor es: ", mcd(a,b), "\nEl min comun multiplo es: ", round(mcm(a,b)))
print ("La suma resulta: ",(round(suma)))

if suma > 1:
    for i in range(2, int(suma/2)+1):
        if (suma % i) == 0:
            print(round(suma),"No corresponde a un numero primo")
            break
        else:
            print(round(suma),"Corresponde a un numero primo")
else:
    print (round(suma),"No corresponde aun numero primo")