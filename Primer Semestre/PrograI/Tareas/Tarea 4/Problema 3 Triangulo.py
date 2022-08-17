#Dato de entrada:float(ladost)
#Proceso:Defino la lista lados y las variables con texto que usare mas adelante, luego uso el ciclo for para repetir 3 veces el input de la variable ladosst.. luego uso .append
#para enviar los datos ingresados a la lista para luego compararlos y comprobar el teorema de la desigualdad.
#Dato de salida:str(mensaje)
lados=[]
confir=("- Los datos ingresados corresponden a los lados de un triangulo.")
negat=("- Los datos ingresados NO corresponden a los lados de un triangulo.")
for i in range(3):
    ladost=float(input("- Ingrese un lado del triangulo a la vez: "))
    lados.append(ladost)
if lados[0]+lados[1]>lados[2] and lados[0]+lados[2]>lados[1] and lados[1]+lados[2]>lados[0]:
    print(confir)
else:
    print (negat)