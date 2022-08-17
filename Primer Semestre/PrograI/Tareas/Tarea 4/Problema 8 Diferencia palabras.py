#Dato de entrada: str(palabra)"listap" y algunas otras variables de texto que ocupare en lineas posteriores
#continuo con un ciclo "for" de dos repeticiones el cual recibe 2 palabras y las guarda en la "listap"
#luego mediante condicionales y la funcion len() se determina cual es la diferencia numerica de caracteres que existe entre ambas palabras.
#Proceso: comienzo definiendo la 
#Dato de salida: str(mensaje)
listap=[]
lenghtxt=("- La palabra con mas caracteres es ")
dif=("y la diferencia es de ")
iguales=("- Ambas palabras contienen la misma cantidad de caracteres.")
character=("caracter.")
for i in range(2):
    palabra=(input("- Ingrese una palabra a la vez: "))
    listap.append(palabra)
len01=((len(listap[0]))-(len(listap[1])))
len10=((len(listap[1]))-(len(listap[0])))

if len(listap[0])>len(listap[1]):
    print (lenghtxt, (listap[0]),dif, (len01), character)
elif len(listap[0])<len(listap[1]):
    print (lenghtxt, (listap[1]),dif, (len10), character)
else: 
    print (iguales)