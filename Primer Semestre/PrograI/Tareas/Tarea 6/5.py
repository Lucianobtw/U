
contacto = open('contacto.txt', 'r')
def matriz():
    lineas = contacto.readlines()
    matriz = []
    for i in lineas:
        i = i.replace("\n","").split(" ")
        matriz.append(i)
    return matriz

def diesiocho():
    contactos = matriz()
    for contacto in contactos:
        if int(contacto[1])>=18:
            print(contacto)
    return

diesiocho()
