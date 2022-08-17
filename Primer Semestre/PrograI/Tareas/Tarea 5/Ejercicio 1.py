#Entrada: int or float(a), int or float(b)
#Salida: suma(a,b)
def suma(x,y):
      resultado = x + y
      if resultado == int(resultado):
            resultado = round(resultado)
      else: resultado = float(resultado)
      return resultado

a = float(input("-Ingrese el primer numero: "))
b = float(input("-Ingrese el segundo numero: "))

print ("El resultado es",(suma(a,b)))

