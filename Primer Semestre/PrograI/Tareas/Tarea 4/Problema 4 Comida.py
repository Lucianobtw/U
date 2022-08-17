#Dato de entrada: str(voto)
#Proceso: Primero asigno los valores de cada menu en listas, luego uso print para mostrar todos los platos, ensaladas y bebidas con sus respectivos precios
#seguido... luego de cada menu.. solicito ingresar el numero correspondiente, ese numero sera usado para calcular la posicion en cada lista.
#ejemplo "menu comidas" ingreso el numero 2, como las listas comienzan sus posiciones con el dato 0, le resto 1 al 2, y me queda como resultado 1 que es la 2da posicion de la tabla
#en este caso $3000, luego sumo todos los datos para calcular el precio final, finalmente a traves de condicionales se comprueba si el usuario quiere pagar 
#o rechazar la compra.
#Dato de salida: int(precio final) y str(mensaje)


comida=[5000,3000,4000,5000,2500]
ensalada=[500,700,900,1000,1200]
bebida=[600,500,550,0]
separador = ("o-------------------------------------------------o")

totaltxt=("- El total de su compra es: $")
print(separador)
print("|                  MENU COMIDAS                   |")
print(separador)
print("1- Filete con verduras horneadas:           $5000.\n2- Pollo arvejado:                          $3000.")
print("3- Albondigas de carne y pure picante:      $4000.\n4- Pavo horneado y papas duquesas:          $5000.\n5- Arrollados Primaveras con salsa de soja: $2500.\n")
op1=int(input("- Ingrese el numero de la comida: "))

print(separador)
print("|                  MENU ENSALADAS                 |")
print(separador)
print ("\n1- Ensalada de lechuga:         $500.\n2- Ensalada papas y mayonesa:   $700.\n3- Ensalada de brocoli:         $900.\n4- Ensalada de colifror:        $1000.\n5- Ensalada de Maiz y mayonesa: $1200.\n")
op2=int(input("- Ingrese el numero de la ensalada: "))
print(separador)
print("|                  MENU BEBIDAS                   |")
print(separador)
print ("\n1- Coca cola  $600.\n2- Crush      $500.\n3- Pepsi      $550.\n4- Agua       $GRATIS.\n")
op3=int(input("- Ingrese el numero de la bebida: "))
print(separador)
print("|                     TOTAL                       |")
print(separador)
print ((totaltxt),(comida[op1-1])+(ensalada[op2-1])+(bebida[op3-1]))

print("- Escriba pagar para continuar para finalizar la compra: \n- Escriba rechazar para cancelar la compra: ")
final=input("\n").lower()
if final=="pagar":
    print("- Gracias por su compra.")
elif final=="rechazar":
    print("- Que tenga un buen dia.")
else: print ("- palabra incorrecta.")
