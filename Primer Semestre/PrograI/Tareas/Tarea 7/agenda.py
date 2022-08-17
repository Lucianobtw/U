#===============================================================================================#
#                                          OPCION 1 (Muestra)                                   #
#===============================================================================================#

def uno():
    print(line,separador,line)
    with open("contactos.txt", "r") as c:
        print(contactos, line)
        print(order, line)
        while(True):
            linea = c.readline()
            print(linea)
            if not linea:
                break
        print(line,realizado,line,separador,line)
    return

#===============================================================================================#
#                                         OPCION 2  (Agrega)                                    # 
#===============================================================================================#

def dos():
    print(line,separador,line)
    print(ctinfo,line)
    with open("contactos.txt", "r") as c:
        listagenda = c.readlines()
    with open("contactos.txt", "a") as c:
        nombres = input(nametxt)
        apellidoP = input(apellidoptxt)
        apellidoM = input(apellidomtxt)
        telefono = input(telefonotxt)
        direccion = input(direcciontxt)
        rut = input(rutxt)
        bandera = False
        for i in listagenda:
            if rut in i:
                bandera = True
        if bandera:
            print(existrut,line,separador)
        else:
            c.write(line+nombres + " " + apellidoP + " " + apellidoM +
                    " " + telefono + " " + direccion + " " + rut)
            print(realizado,line,separador),line
    return

#===============================================================================================#
#                                        OPCION 3  (Elimina)                                    #
#===============================================================================================#

def tres():
    print(line,separador,line)
    with open("contactos.txt", "r") as c:
        listagenda = c.readlines()
        rut = input(delrut)
        c.close()
        for i in listagenda:
            if rut in i:
                with open("contactos.txt", "w") as s:
                    print(ctcselect, line, i)
                    indice = listagenda.index(i)
                    listagenda.pop(indice)
                    for x in listagenda:
                        s.write(x)
                    c.close()
                    print(realizado, line, separador)
                    return
        print(line, wrongrut, line, separador,line)
        return

#===============================================================================================#
#                                        OPCION 4    (Edita)                                    #
#===============================================================================================#

def cuatro():
    print(line,separador,line)
    with open("contactos.txt", "r") as c:
        listagenda = c.readlines()
        c.close()
        select = input(editrut)
        for i in listagenda:
            if select in i:
                with open("contactos.txt", "w") as s:
                    print(ctcselect, line, i)
                    indice = listagenda.index(i)
                    nombres = input(nametxt)
                    apellidoP = input(apellidoptxt)
                    apellidoM = input(apellidomtxt)
                    telefono = input(telefonotxt)
                    direccion = input(direcciontxt)
                    rut = input(rutxt)
                    listagenda.pop(indice)
                    listagenda.insert(indice, nombres + " " + apellidoP + " " +
                                    apellidoM + " " + telefono + " " + direccion + " " + rut + line)
                    for x in listagenda:
                        s.write(x)
                    s.close()
                    print(realizado, line, separador)
                    return
        print(line, wrongrut, line, separador,line)
        return

#===============================================================================================#
#                                            OPCION 5                                           #
#===============================================================================================#

def cinco():
    print(line,separador,line)
    print(setoff,line,separador,line)
    return

#===============================================================================================#
#                                 Textos,Variables y Constantes                                 #
#===============================================================================================#

order = "Nombres        Apellidos   N.Telefonico  Direccion,    Rut"
contactos = "- Los contactos registrados son: "
outofrg = "- Usted ha ingresado un numero/caracter que se encuentra fuera del rango de opciones."
entrada = "- Ingrese el numero correspondiente a la accion a realizar: "
rutxt = "- Ingrese el rut correspondiente al contacto: "
ctinfo = "- El orden correcto de escritura es: Nombres - Apellidos - NumeroTel - Direccion - Rut"
realizado = "Accion realizada con exito!"
setoff = "- Usted ha decidido apagar la libreta, Gracia spor usarla :D"
nametxt = "- Ingrese los nombres del contacto: "
ctcselect = "- El contacto seleccionado es: "
apellidoptxt = "- Ingrese el apellido paterno del contacto:"
apellidomtxt = "- Ingrese el apellido materno del contacto: "
telefonotxt = "- Ingrese el numero telefonico del contacto: "
direcciontxt = "- Ingrese la direccion del contacto: "
editrut = "- Ingrese el rut del contacto a editar  "
wrongrut = "- El rut ingresado no corresponde a un contacto registrado"
delrut = "- Ingrese el rut del contacto a eliminar: "
existrut = "- El rut ingresado ya se encuentra en la lista de contactos."
line = "\n"
separador = "o==================================================================================o"
ToF = True

#===============================================================================================#
#                                     WHILE PRINCIPAL                                           #
#===============================================================================================#

while ToF:
    menu = ["1) Ver contactos ", "2) Nuevo Contacto",
            "3) Eliminar contacto", "4) Editar Contacto", "5) Apagar"]

    for i in menu:
        print(i, line)

    seleccion = int(input(entrada))
    print(line)

    if seleccion > 6 or seleccion < 0:
        print(outofrg)
    elif seleccion == 1:
        uno()
    elif seleccion == 2:
        dos()
    elif seleccion == 3:
        tres()
    elif seleccion == 4:
        cuatro()
    elif seleccion == 5:
        cinco()
        ToF = False
