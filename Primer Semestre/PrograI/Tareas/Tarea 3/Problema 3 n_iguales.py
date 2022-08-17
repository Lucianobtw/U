#Datos de entrada: 3 numeros
""""Proceso: Primero defino una lista y luego envio los 3 numeros a ella, tambien incluyo "round(variable)" para redondear
a emtero el numero si se ingreso un entero, si no, se mantiene como decimal, luego uso condicionales para comparar los casos 
posibles e imprimo en pantalla los posibles datos de salida."""
#Datos de salida: numero menor, pareja de numeros iguales menores, 3 numeros iguales. (resultado del problema)
espacio=(" ")
menortxt=("- El numero menor es: ")
lista_n=[]
print(espacio)
n_1=(float(input("- Ingrese un numero: ")))
if n_1==int(n_1):
    lista_n.append(round(n_1))
else:lista_n.append(n_1)
print(espacio)
n_2=(float(input("- Ingrese un numero: ")))
if n_2==int(n_2):
    lista_n.append(round(n_2))
else:lista_n.append(n_2)
print(espacio)
n_3=(float(input("- Ingrese un numero: ")))
if n_3==int(n_3):
    lista_n.append(round(n_3))
else:lista_n.append(n_3)
print(espacio)
parejamin=("- La pareja de numeros iguales corresponde al dato menor.")
solomax=("- El numero unico es menor.")
igualesmin=(lista_n[0]==lista_n[1]<lista_n[2]) or (lista_n[1]==lista_n[2]<lista_n[0])or (lista_n[2]==lista_n[0]<lista_n[1])
igualesmax=(lista_n[0]==lista_n[1]>lista_n[2]) or (lista_n[1]==lista_n[2]>lista_n[0])or (lista_n[2]==lista_n[0]>lista_n[1])
if lista_n[0]==lista_n[1]==lista_n[2]:
    print("- Los numeros ingresados son iguales.")
elif igualesmin==True:
    print (parejamin)
elif igualesmax==True:
    print(solomax)
else:
    print((menortxt),(min(lista_n)))
print(espacio)

