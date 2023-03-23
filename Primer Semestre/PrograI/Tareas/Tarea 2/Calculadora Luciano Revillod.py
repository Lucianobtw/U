#Defino terminos que ocupare frecuentemente en el codigo

espacio = ("           ")
side=("|                                                 |")
suma = "+"
resta = "-"
multiplicacion = "*"
division = "/"
resultadotxt = ("   - El resultado es: ")
indeterminacion=("   - Dividir por 0 causa indeterminación.")
separador = ("o-------------------------------------------------o")
print (espacio)
lista_n = []
lista_ope = []
lista_fn = []
contador = 0
print (separador)
print ("|             Calculadora Cientifica              |")
print (separador)

#- Datos de entrada, variables y ciclos para repetir cada pregunta 3 y 2 veces respectivamente.
#- Uso listas para mezclar los digitos y las operaciones ingresadas "[1,2,3] + [+,+] = [1+2+3]".

while contador<3:
    print(side)
    numero = input("   - Ingrese un numero: ")
    lista_n.append(numero)
    numero=0
    contador=contador+1
contador=0

while contador<2:
    print(side)
    operacion = input("   - Ingrese sus operaciones: ")
    lista_ope.append(operacion)
    operacion=0
    contador=contador+1
print(side)

lista_fn = lista_n[0] + lista_ope[0] + lista_n[1] + lista_ope[1] + lista_n[2]
print (("   - Usted ha Ingresado: "),(lista_fn))
print(side)

#Proceso y datos de salida.
#Ingreso cada uno de los casos posibles ademas de las prioridades de multiplicacion y division.

#------------------------------------Suma y Resta--------------------------------------- #
if lista_ope[0] == suma and lista_ope[1] == suma:
    print(separador)
    print(side)
    print ((resultadotxt), ((float(lista_n[0]))+(float(lista_n[1]))+(float(lista_n[2]))))
elif lista_ope[0] == suma and lista_ope[1] == resta:
    print(separador)
    print(side)
    print ((resultadotxt),((float(lista_n[0]))+(float(lista_n[1]))-(float(lista_n[2]))))

if lista_ope[0] == resta and lista_ope[1] == resta:
    print(separador)
    print(side)
    print ((resultadotxt),((float(lista_n[0]))-(float(lista_n[1]))-(float(lista_n[2]))))
elif lista_ope[0] == resta and lista_ope[1] == suma:
    print(separador)
    print(side)
    print ((resultadotxt),((float(lista_n[0]))-(float(lista_n[1]))+(float(lista_n[2]))))

#--------------------------------- Multiplicacion-------------------------------------------#
if lista_ope[0] == multiplicacion and lista_ope[1] == multiplicacion:
    print(separador)
    print(side)
    print ((resultadotxt),((float(lista_n[0]))*(float(lista_n[1]))*(float(lista_n[2]))))
elif lista_ope[0] == multiplicacion and lista_ope[1] == suma:
    print(separador)
    print(side)
    print ((resultadotxt),((float(lista_n[0]))*(float(lista_n[1]))+(float(lista_n[2]))))
elif lista_ope[0] == multiplicacion and lista_ope[1] == resta:
    print(separador)
    print(side)
    print ((resultadotxt),((float(lista_n[0]))*(float(lista_n[1]))-(float(lista_n[2]))))
elif lista_ope[0] == suma and lista_ope[1] == multiplicacion:
    print(separador)
    print(side)
    print ((resultadotxt),((float(lista_n[1]))*(float(lista_n[2]))+(float(lista_n[0]))))

#--------------------------------------Division---------------------------------------------#
if lista_ope[0] == division and lista_ope[1] == division:
    print(separador)
    print(side)
    try: print ((resultadotxt),((float(lista_n[0]))/(float(lista_n[1]))/(float(lista_n[2]))))
    except:ZeroDivisionError and print (indeterminacion)
elif lista_ope[0] == division and lista_ope[1] == suma:
    print(separador)
    print(side)
    try: print ((resultadotxt),((float(lista_n[0]))/(float(lista_n[1]))+(float(lista_n[2]))))
    except:ZeroDivisionError and print (indeterminacion)
elif lista_ope[0] == division and lista_ope[1] == resta:
    print(separador)
    print(side)
    try: print ((resultadotxt),((float(lista_n[0]))/(float(lista_n[1]))-(float(lista_n[2]))))
    except:ZeroDivisionError and print (indeterminacion)
elif lista_ope[0] == division and lista_ope[1] == multiplicacion:
    print(separador)
    print(side)
    try: print ((resultadotxt),((float(lista_n[0]))/(float(lista_n[1]))*(float(lista_n[2]))))
    except:ZeroDivisionError and  print (indeterminacion)
elif lista_ope[0] == multiplicacion and lista_ope[1] == division:
    print(separador)
    print(side)
    try: print ((resultadotxt),((float(lista_n[0]))*(float(lista_n[1]))/(float(lista_n[2]))))
    except:ZeroDivisionError and  print (indeterminacion)
elif lista_ope[0] == suma and lista_ope[1] == division:
    print(separador)
    print(side)
    try: print ((resultadotxt),((float(lista_n[1]))/(float(lista_n[2]))+(float(lista_n[0]))))
    except:ZeroDivisionError and  print (indeterminacion)

#--------------------------------------Prioridades-------------------------------------------#
if lista_ope[0] == resta and lista_ope[1] == multiplicacion:
    print ((resultadotxt),(float(lista_n[0]))-(((float(lista_n[1]))*(float(lista_n[2])))))
if lista_ope[0] == resta and lista_ope[1] == division:
    print(separador)
    print(side)
    try: print ((resultadotxt),(float(lista_n[0]))-(((float(lista_n[1]))/(float(lista_n[2])))))
    except:ZeroDivisionError and print (indeterminacion)

print(side)
print (separador)
print(espacio)
