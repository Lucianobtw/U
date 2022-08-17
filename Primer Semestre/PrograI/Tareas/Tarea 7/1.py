#Entradas: (str)lista[nombres] ; (str) lista[dominios]
#Salida: str(lista) ; contiene los correos generados aleatoriamente en funcion a las dos entradas.

import random

def uno(nombres,dominios):
    email = []
    for x in nombres:
        email.append(x + "@" + dominios[(random.randint(0,9))])
    return email

nombres = ["Luciano","Claudio","Gladys","Ignacio","Nicolas"]
dominios = ["gmail.com","outlook.com","yahoo.es","uct.cl","hotmail.com","ufro.cl",
        "blizzard.net","valve.org","twitter.com","mojang.com"]

print(uno(nombres,dominios))

