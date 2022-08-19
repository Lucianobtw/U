# importamos la libreria random para llenar la cola
import random as ra

# creamos la cola(queue) añadiendo numeros alatorios añadiendo los
# elementos al final de esta.
queue = []
for x in range(5):
    queue.append(ra.randint(0,10))

print(queue)

# sacamos el primer elemento de la cola.
for j in range(5):
    print(queue.pop(0))

# si ejecutamos la sgte. sentencia dara un Index Error
# por falta de elementos en la cola.
# queue.pop()

# try except para evitar que el programa deje de funcionar.
try:
    queue.pop()
except IndexError:
    print("queue is empty")
except:
    print("Something else went wrong")