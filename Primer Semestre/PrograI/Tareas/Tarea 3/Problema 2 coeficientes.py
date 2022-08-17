#Datosde entrada: Coheficiente A, B y C.
""" Proceso: Se ingresan los 3 coheficientes y en base a eso se calculan las variables definidas,
luego se imprimen en pantalla las raices de la ecuacion planteada."""
#Datos de salida: Raices de la ecuacion.
cA=float(input("- Ingrese el coeficiente A: "))
cB=float(input("- Ingrese el coeficiente B: "))
cC=float(input("- Ingrese el coeficiente C: "))
disc=((cA**2)-4*cA*cC)
preal=((-cB)/(2*cA))
pimag=(((-disc)/(2*cA))**0.5)
if disc<0:
    print (("Raiz 1 : "),(preal),"+",(pimag),"i")
    print (("Raiz 2 : "),(preal),"-",(pimag),"i")

else:
    if disc==0:
        r=((cB)/(2*cA))
        print(("Raiz 1 = Raiz 2"), r)
    else:
        r1=(((-cB)+((disc)**0.5))/(2*cA))
        r2=(((-cB)-((disc)**0.5))/(2*cA))
        print(("Raiz 1: "), r1)
        print(("Raiz 2: "), r2)
print("Fin del programa")