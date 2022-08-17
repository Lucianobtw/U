spacetxt = (" ")
pricetxt = ("- El precio del boleto seleccionado es: ")
errorvalor = ("- El numero ingresado es incorrecto.")
totalprice=("- En total usted pagará: $")
ironman=1000 #1
america=1200 #2
spider=1400  #3
thor=1600    #4
veng=2000    #5

print (spacetxt)
print ("[1) Iron man] [2) Capitan America] [ 3) Spiderman] [4) Thor] [5) Avengers]")
print (spacetxt)
numero = int(input("- Seleccione el numero de la pelicula que desea ver: "))
print(spacetxt)
if numero >5 :
    print("- El numero ingresado no corresponde a las peliculas disponibles.")
    print(spacetxt)
elif numero <1 :
    print("- El numero ingresado no corresponde a las peliculas disponibles.")
    print(spacetxt)
else:
    if numero==1:
        print (pricetxt,"$", ironman)
    elif numero==2:
        print (pricetxt,"$", america)
    elif numero==3:
        print (pricetxt,"$", spider)
    elif numero==4:
        print (pricetxt,"$", thor)
    elif numero==5:
        print (pricetxt,"$", veng)
print(spacetxt)
cantbol=int(input("- Ingrese la cantidad de boletos que desea comprar: "))
print (spacetxt)
if numero==1:
    print (totalprice, (ironman*cantbol))
elif numero==2:
    print (totalprice, (america*cantbol))
elif numero==3:
    print (totalprice, (spider*cantbol))
elif numero==4:
    print (totalprice, (thor*cantbol))
elif numero==5:
    print (totalprice, (veng*cantbol))
print(spacetxt)
final=input("- Escriba PAGAR para continuar y RECHAZAR para cancelar la compra: ")
print(spacetxt)
if final!=("PAGAR" or "RECHAZAR"):
    print ("- Palabra incorrecta")
elif final=="PAGAR":
    print("- Gracias por su compra, disfrute de la función")
elif final=="RECHAZAR":
    print("- Que tenga un buen dia.")


