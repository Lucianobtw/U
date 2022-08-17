#Dato de entrada: str(voto)
#Proceso: Primero defino las 5 variables con el texto correspondiente al candidato y su color, luego mediante un input se ingresa la letra,
#y finalmente con condicionales compruebo si las letras ingresadas corresponden a algun candidato.
#Dato de salida: srt(mensaje)
g="Gabriel Boric, Verde"         #G  
m="Marco Enriquez Ominami, Azul" #M
s="Sebastian Sichel, Amarillo"   #S
j="Jose Kast, Rojo"              #J
f="Franco Parisi, Cafe"          #F
voto=(input("- Ingrese la letra correspondiente al candidato de su preferencia: ")).lower()
if voto=="g":
    print (g)
elif voto=="m":
    print (m)
elif voto=="s":
    print (s)
elif voto=="j":
    print (j)
elif voto=="f":
    print (f)
else: 
    print ("- El caracter ingresado NO pertenece a los candidato inscritos.")
