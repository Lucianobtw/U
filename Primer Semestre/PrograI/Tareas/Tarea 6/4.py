def fcontactos():
    contacto = open('contacto.txt', 'w')
    lista = [
        ["Ignacio", 25, "19/06/1996", "+56911111111"],
        ["Cristin",22, "14/05/1999", "+56922222222"],
        ["Claudio", 18, "15/03/2005", "+56933333333"],
        ["Manuela", 17, "14/08/2000", "+56944444444"],
        ["Fernando",16, "10/12/2001", "+56955555555"]
        ]

    for i in lista:
        contacto.write(f"{i[0]} {i[1]} {i[2]} {i[3]}")
        contacto.write("\n")
    contacto.close
    return

fcontactos()


