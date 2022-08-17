#Dato de entrada: int (randint)(num)
#Proceso: importo libreria random, defino la lista "listarand", continuo con un ciclo "for" con una duracion de 5 repeticiones,
#este ciclo genera un numero random entero entre 10 y 100, luego se envia el dato a la "listarand" mediante .append.. defino la suma y el promedio
#(se usaran en lineas posteriores) finalmente se muestra la suma y el promedio de los numeros generados.
#Dato de salida: int or float(suma) y (promedio)
import random
listarand=[]
for i in range(5):
    num=random.randint(10,100)
    listarand.append(num)
suma=sum(listarand)
promedio=(sum(listarand)/len(listarand))
promediotxt=("\n- El promedio de los numeros es: ")
print (("\n- Los numeros generados son: "),(listarand))
print (("\n- La suma de los numeros es: "),(suma))
if promedio==int(promedio):
  print (promediotxt,round(promedio))
else:
  print (promediotxt,promedio)