
def idficha(): 
    fic = 0 ; est = 0 ; uni = 0 ; car = 0 ; tal = 0 
    ser = 0 ; can = 0 ; coma = ","

    for i in range(50):
        line = fic + 1, est + 1, uni + 1, car + 1, tal + 1, ser + 1, can + 1
        print((line),coma)

        fic += 1 ; est += 1 ; uni += 1 
        car += 1 ; tal += 1 ; ser += 1  ; can += 1

        if uni == 6 : uni = 0
        if car == 18: car = 0
        if tal == 15: tal = 0
        if ser == 10: ser = 0
        if can == 10: can = 0
    return

idficha()
