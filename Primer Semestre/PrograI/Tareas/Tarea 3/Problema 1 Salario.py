#Datos de entrada: nombre, salario fijo y valor total de las ventas.
"""Proceso: Creo una lista para almacenar y ordenar los 3 datos de entrada, continuo con un condicional 
if para evitar que se ingresen numeros en la variable "nombre", luego mediante ".append" envio la variable 
a la casilla [0] de la lista y asi sucesivamente con las variables restantes. Finalmente calculo la comision 
obtenida al calcular el 10% del total de ventas ("totalvent" *0.1), esta se suma con la variable "salariofj"
y se obtiene el sueldo final."""
#Dato de salida: Sueldo final (sueldo_fn).

lista_datos=[]
espacio=(" ")
print (espacio)
nombre = (input("- Ingrese su nombre: "))
lista_datos.append(nombre)
print (espacio)
salariofj = int(input("- Ingrese su salario fijo (valor numerico): "))
lista_datos.append(salariofj)
print (espacio)
totalvent= int(input("- Ingrese el total de sus ventas: "))
print (espacio)
lista_datos.append(totalvent)
comision=((lista_datos[2])*(0.1))
print (("- La comision obtenida por ventas es: "),(comision))
sueldo_fn= (lista_datos[1]+(comision))
print (espacio)
print (("- Su sueldo final es: "),(sueldo_fn))
print (espacio)
print (("-"),(lista_datos))
print (espacio)

