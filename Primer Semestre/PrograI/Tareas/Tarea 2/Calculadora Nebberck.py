espacio=("           ")
print (espacio)
separador=("o-------------------------------------------------o")
espacio=("           ")
lista_n=[]
lista_ope=[]
lista_fn=[]
contador=0
print (separador)
print ("                   Calculadora")
print (separador)
print (espacio)
while contador<3:
    #Datos de entrada
    numero = (input("- Ingrese un numero: "))
    lista_n.append(numero)
    numero=0
    contador=contador+1
print (espacio)

contador=0
while contador<2:
    operacion = input("- Ingrese sus operaciones: ")
    lista_ope.append(operacion)
    operacion=0
    contador=contador+1
print(espacio)
contador=0

lista_fn = lista_n[0] + lista_ope[0] + lista_n[1] + lista_ope[1] + lista_n[2]
if lista_ope[1]=="/"or"*":
    lista_fn = lista_n[1] , lista_ope[1] , lista_n[2]
else: 
    print (lista_fn)
    while contador<2:
        if lista_fn[contador]== "/":
            print( float (lista_fn[0])/float(lista_fn[2]))
            contador=contador+1
        elif lista_fn[contador]=="*":
            print ( float (lista_fn[0])*float(lista_fn[2]))
            contador=contador+1
        else:
            if lista_ope[contador]=="-":
                print("resta")
                contador=contador+1
            elif lista_ope[contador]=="+":
                print("suma")
                contador=contador+1
    





   #2-3/3
