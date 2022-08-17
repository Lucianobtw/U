#Dato de entrada: str(nombre1) y str(nombre2)
#Proceso: solicito ingresar dos datos para ingresarlas a variables, tambien uso .lower para convertir las mayusculas en minusculas, 
#luego comparo la primera letra y ultima letra de cada variable para ver si existe coincidencia.
#Dato de salida: str(mensaje)
nombre1=input("- Ingrese el primer nombre: ").lower()
nombre2=input("- Ingrese el segundo nombre: ").lower()
cointxt=("- Hay coincidencia.")
notxt=("- No hay coincidencia.")
if (nombre1[0]==nombre2[0]):
    print(cointxt)
elif (nombre1[-1]==nombre2[-1]):
    print(cointxt)
else: print (notxt)