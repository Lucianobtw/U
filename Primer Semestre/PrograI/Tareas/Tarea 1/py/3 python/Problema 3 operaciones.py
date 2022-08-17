text = "ingrese el numero a operar: "
another = "desea realizar otr op?"
inc = "Seleccion incorrecta"
ToF = True
list = []


while ToF:
    for i in range(2):
        num = int(input(text))
        list.append(num)
    
    suma = (list[0] + list[1])
    resta = (list[0] - list[1])
    multi = (list[0] * list[1])

    

    try: div = (list[0] / list[1])
    except: ZeroDivisionError ; print (suma, resta, multi, "no se p") ; break

    print (suma, resta, multi, div)
    fin = input(another)

    if fin == "Si": 
        ToF = True
    elif fin == "No":
        ToF = False
    elif fin != "Si" or another != "No":
        print (inc)
        ToF = False
