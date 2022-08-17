import serial
import pygame
import random as RA
import ctypes as CT
from pygame.locals import *

#========================================================================================#
#                           Definicion de Constantes y Variables                         #
#========================================================================================#

res = (528, 396) ; tileX = 44 ; tileY = 44 ; maxBot = 1 ; tile = 44

maxX = 528       ; maxY = 396

ToF = True       ; mouX = 0   ; mouY = 0   ; rango = 0      

#========================================================================================#
#                        Carga imagenes y convierte formato PyGame                       #
#========================================================================================#

def Load_Image(sFile, transp=False):
    try:
        image = pygame.image.load(sFile)
    except pygame.error.message:
        raise SystemExit.message
    image = image.convert()
    if transp:
        color = image.get_at((0, 0))
        image.set_colorkey(color)
    return image

#========================================================================================#
#                               Inicializa pygame.-                                      #
#========================================================================================#

def Pygame_Innit():
    pygame.init()
    pygame.mouse.set_visible(False)
    pygame.display.set_caption('Mapa Inteligente - Luciano Revillod e Ignacio Sube')
    return pygame.display.set_mode(res)

#========================================================================================#
#                            Inicializa Array de Sprites.                                #
#========================================================================================#

def Fig_Innit():
    aImg = []
    aImg.append(Load_Image('bg.png', False))   # Suelo Tile azul 0
    aImg.append(Load_Image('mu.png', False))   # Barrera azul,   1
    aImg.append(Load_Image('rn.png', True))    # NORTE Bot,      2
    aImg.append(Load_Image('rs.png', True))    # Sur BOT         3
    aImg.append(Load_Image('re.png', True))    # Derecha BOT     4
    aImg.append(Load_Image('ro.png', True))    # Izquierda Bot   5
    aImg.append(Load_Image('rt.png', True))    # Cursor          6
    aImg.append(Load_Image('tf.png', False))   # Meta            7
    aImg.append(Load_Image('ti.png', False))   # Inicio          8
    return aImg

#========================================================================================#
#                                      Pinta Mouse                                       #
#========================================================================================#

def Pinta_Mouse():
    return Screen.blit(aSprt[6], (mouX, mouY))

#========================================================================================#
#                                                                                        #
#                                       Mapa                                             #
#                                                                                        #
#========================================================================================#
#========================================================================================#
#                                   Clase eCelda                                         #
#========================================================================================#

class eCelda(CT.Structure):
    _fields_ = [
        ('nF', CT.c_ubyte),  # Fila de eMapa
        ('nC', CT.c_ubyte),  # Columna de eMapa
        ('n1', CT.c_ubyte),  # RR Oro
        ('n2', CT.c_ubyte),  # RR Acero
        ('n3', CT.c_ubyte),  # RR Litio
        ('n4', CT.c_ubyte),  # RR Niquel
        ('n5', CT.c_ubyte)   # RR Cobre
    ]

#========================================================================================#
#                                    Clase eMapa                                         #
#========================================================================================#

class eMapa:
    _fields_ = [
        ('nF', CT.c_ubyte),  # Fila de eMapa (12) 
        ('nC', CT.c_ubyte)   # Columna de eMapa (9) 
    ]

#========================================================================================#
#                                 Inicializa El Mapa                                     #
#========================================================================================#

def Mapa_Innit():
    for nF in range(0, res[1] / tile):      #res[0] = (396) ; tile = 44 (px)
        for nC in range(0, res[0] / tile):  #res[0] = (528) ; tile = 44 (px)
            Mapa[nF][nC].nF = nF
            Mapa[nF][nC].nC = nC

#========================================================================================#
#                                       Map Blits                                        #
#                  Asigna un sprite para cada tipo de imagen en el mapa                  #
#========================================================================================#

def TileIn(nC, nF): #Inicio
    return Screen.blit(aSprt[8], (Mapa[nF][nC].nC * tile, Mapa[nF][nC].nF * tile))

def TileCam(nC, nF): #Camino
    return Screen.blit(aSprt[0], (Mapa[nF][nC].nC * tile, Mapa[nF][nC].nF * tile))

def TileBar(nC, nF): #Barrera
    return Screen.blit(aSprt[1], (Mapa[nF][nC].nC * tile, Mapa[nF][nC].nF * tile))

def TileMet(nC, nF): #Meta
    return Screen.blit(aSprt[7], (Mapa[nF][nC].nC * tile, Mapa[nF][nC].nF * tile))

#========================================================================================#
#                                   Pinta El Mapa                                        #
#========================================================================================#

def Pinta_Mapa():
    for nC in range(res[0] / tile):
        for nF in range(res[1] / tile):
            if nC == 0:
                if nF == 0:
                    TileIn(nC, nF)
                else:
                    TileCam(nC, nF)
#
            elif nC == 1 or nC == 5:
                if nF == 8:
                    TileCam(nC, nF)
                else:
                    TileBar(nC, nF)
#
            elif nC == 2 or nC == 4:
                TileCam(nC, nF)
#
            elif nC == 3 or nC == 9:
                if nF == 0:
                    TileCam(nC, nF)
                else:
                    TileBar(nC, nF)
#
            elif nC == 6:
                if nF == 3 or nF == 7:
                    TileBar(nC, nF)
                else:
                    TileCam(nC, nF)
#
            elif nC == 7:
                if nF == 1 or nF == 5 or nF == 3 or nF == 7:
                    TileBar(nC, nF)
                else:
                    TileCam(nC, nF)
#
            elif nC == 8:
                if nF == 1 or nF == 5:
                    TileBar(nC, nF)
                else:
                    TileCam(nC, nF)
#
            elif nC == 10:
                if nF == 8:
                    TileMet(nC, nF)
                else:
                    TileCam(nC, nF)
#
            elif nC == 11:
                TileBar(nC, nF)

#========================================================================================#
#                                                                                        #
#                                      Robot                                             #
#                                                                                        #
#========================================================================================#
#========================================================================================#
#                                   Clase eRobot                                         #
#========================================================================================#

class eRobot(CT.Structure):
    _fields_ = [
        ('nF', CT.c_short),     # Sprite
        ('PosX', CT.c_short),   # PosX
        ('PosY', CT.c_short),   # PosY
        ('RanBot', CT.c_short), # Rango de movimiento
        ('DirX', CT.c_short),   # Direccion en X
        ('DirY', CT.c_short),   # Direccion en Y
        ('VelBot', CT.c_short)  # Velocidad BOT
    ]

#========================================================================================#
#                                     Robot Innit                                        #
#                          Inicializa los parametros del robot                           #
#========================================================================================#

def Robot_Innit():
    aBoe[0].nF = 2
    aBoe[0].PosX = 0
    aBoe[0].PosY = 0
    aBoe[0].DirX = 0
    aBoe[0].DirY = 0
    aBoe[0].VelBot = 1
    return

#========================================================================================#
#                                    Pinta El Robot                                      #
#                     Asigna un sprite dependiendo del valor de nF                       #
#========================================================================================#

def Pinta_Robot():
    if aBoe[0].nF == 1:
        Screen.blit(aSprt[2], (aBoe[0].PosX, aBoe[0].PosY))  # Norte
    elif aBoe[0].nF == 2:
        Screen.blit(aSprt[3], (aBoe[0].PosX, aBoe[0].PosY))  # Sur
    elif aBoe[0].nF == 3:
        Screen.blit(aSprt[4], (aBoe[0].PosX, aBoe[0].PosY))  # Derecha
    elif aBoe[0].nF == 4:
        Screen.blit(aSprt[5], (aBoe[0].PosX, aBoe[0].PosY))  # Izquierda

#========================================================================================#
#                                     Movimientos Robot                                  #
#========================================================================================#

def norte(i):
    aBoe[i].nF = 1
    aBoe[i].DirY = -1
    aBoe[i].DirX = 0
    return  

def sur(i):
    aBoe[i].nF = 2
    aBoe[i].DirX = 0
    aBoe[i].DirY = 1
    return

def derecha(i):
    aBoe[i].nF = 3
    aBoe[i].DirY = 0
    aBoe[i].DirX = 1
    return

def izquierda(i):
    aBoe[i].nF = 4
    aBoe[i].DirY = 0
    aBoe[i].DirX = -1
    return

def final(i):
    aBoe[i].nF = 2
    aBoe[i].DirY = 0
    aBoe[i].DirX = 0
    return

#========================================================================================#
#                                     Update Robot                                       #
#========================================================================================#

def Update_Robot():
    for i in range(0, maxBot):
        aBoe[i].RanBot -= 1
        if aBoe[i].RanBot <= 0:
            if aBoe[i].PosX == 0 and aBoe[i].PosY == 0:
                sur(i)
            elif aBoe[i].PosX == 0 and aBoe[i].PosY == 352:
                derecha(i)
            elif aBoe[i].PosX == 88 and aBoe[i].PosY == 352:
                norte(i)
            elif aBoe[i].PosX == 88 and aBoe[i].PosY == 0:
                derecha(i)
            elif aBoe[i].PosX == 176 and aBoe[i].PosY == 0:
                sur(i)
            elif aBoe[i].PosX == 176 and aBoe[i].PosY == 352:
                derecha(i)
            elif aBoe[i].PosX == 352 and aBoe[i].PosY == 352:
                norte(i)
            elif aBoe[i].PosX == 352 and aBoe[i].PosY == 264:
                izquierda(i)
            elif aBoe[i].PosX == 264 and aBoe[i].PosY == 264:
                norte(i)
            elif aBoe[i].PosX == 264 and aBoe[i].PosY == 176:
                derecha(i)
            elif aBoe[i].PosX == 352 and aBoe[i].PosY == 176:
                norte(i)
            elif aBoe[i].PosX == 352 and aBoe[i].PosY == 88:
                izquierda(i)
            elif aBoe[i].PosX == 264 and aBoe[i].PosY == 88:
                norte(i)
            elif aBoe[i].PosX == 264 and aBoe[i].PosY == 0:
                derecha(i)
            elif aBoe[i].PosX == 440 and aBoe[i].PosY == 0:
                sur(i)
            elif aBoe[i].PosX == 440 and aBoe[i].PosY == 352:
                final(i)
        
        aBoe[i].PosY += (aBoe[0].DirY * aBoe[0].VelBot) # Actualizacion de posicision en eje Y
        aBoe[i].PosX += (aBoe[0].DirX * aBoe[0].VelBot) # Actualizacion de posicision en eje x

#========================================================================================#
#                                RECURSOS RUTA CELDAS                                    #
#========================================================================================#
#========================================================================================#
#                            Reconocer Datos de cada celda                               #
#========================================================================================#

def recursosBot():
    for i in range(0,maxBot):
        if aBoe[i].PosY != 352 or aBoe[i].PosX != 440:
            if aBoe[i].PosY % 44 == 0 and aBoe[i].PosX % 44 == 0:
                posicionY = aBoe[i].PosY // tile
                posicionX = aBoe[i].PosX // tile
                recursos(posicionX,posicionY)
                print(aCelda[posicionY][posicionX].nC,
                aCelda[posicionY][posicionX].nF,
                aCelda[posicionY][posicionX].n1,
                aCelda[posicionY][posicionX].n2,
                aCelda[posicionY][posicionX].n3,
                aCelda[posicionY][posicionX].n4,
                aCelda[posicionY][posicionX].n5)
                #serialtry(enviaCOM)
                return

#========================================================================================#
#                     Escribir dato de celdas en recursos txt                            #
#========================================================================================#

def recursos(posicionX,posicionY):
    with open("recursos.txt","a") as r:
        formato = 'F:%02d-C:%02d-Oro:%03d-Acero:%03d-Litio:%03d-Niquel:%03d-Cobre:%03d\n'
        r.write(formato%(aCelda[posicionY][posicionX].nC,
            aCelda[posicionY][posicionX].nF,
            aCelda[posicionY][posicionX].n1,
            aCelda[posicionY][posicionX].n2,
            aCelda[posicionY][posicionX].n3,
            aCelda[posicionY][posicionX].n4,
            aCelda[posicionY][posicionX].n5))
        return

def sobrescribir():
    borrar = open("recursos.txt","w")
    borrar.close()

#========================================================================================#
#                      Lectura de datos File Binario Estructurado                        #
#========================================================================================#

def GetData(name):
    name.readinto(eReg)  # Leemos el Registro completo de tipo eCelda
    return eReg          # lo devolvemos a quien lo pidio

#========================================================================================#
#                                    Lectura .dat                                        #
#========================================================================================#
    
def ReadMapa(matriz):
    nFh = open('mapa.dat','rb')
    for nF in range(len(matriz)):
        for nC in range (len(matriz[nF])):
            eReg = GetData(nFh)
            matriz[nF][nC].nF = eReg.nF
            matriz[nF][nC].nC = eReg.nC
            matriz[nF][nC].n1 = eReg.n1
            matriz[nF][nC].n2 = eReg.n2
            matriz[nF][nC].n3 = eReg.n3
            matriz[nF][nC].n4 = eReg.n4
            matriz[nF][nC].n5 = eReg.n5
    nFh.close()
    return matriz

#========================================================================================#
#                       Escribir dato de celdas en sondeo.dat                            #
#========================================================================================#

def SaveData():
    with open('sondeo.dat','wb') as s:       # Abrimos archivo Mode Binario Escritura
        for nF in range(0,res[1] / tile):    # Fila de eMapa (12) [11]
            for nC in range(0,res[0] / tile):# Columna de eMapa (9) [8]
                eReg = aCelda[nF][nC]        # Asignamos toda la Info Celda Mapa -> eReg
                s.write(eReg)                # Salvamos el registro completo al File
        s.close()                            # Cerramos y vaciamos el buffer RAM File
        return

#========================================================================================#
#                                      Serial                                            #
#========================================================================================#

def serialtry(serial):
    formato = "%d,%d,%d,%d,%d,%d,%d\n"
    for i in range(0,maxBot):
        for nF in range(len(aCelda)):
            for nC in range(len(aCelda[nF])):
                if aBoe[i].PosY // 44 == nF and aBoe[i].PosX // 44 == nC:
                    serial.write(formato%(aCelda[nF][nC].nF,
                    aCelda[nF][nC].nC,
                    aCelda[nF][nC].n1,
                    aCelda[nF][nC].n2,
                    aCelda[nF][nC].n3,
                    aCelda[nF][nC].n4,
                    aCelda[nF][nC].n5))

#========================================================================================#
#                                    While Principal                                     #
#========================================================================================#

Screen = Pygame_Innit()
aSprt = Fig_Innit()
eReg = eCelda() 
#Estructura de clase, filas, columnas, minerales
Mapa = [[eMapa() for nC in range(res[0]/tile)] for nF in range(res[1]/tile)] 
#crea matriz correspondiente al mapa
aBoe = [eRobot() for i in range(0, maxBot)]
#Estructura del robot
aCelda = [[eCelda() for nC in range(res[0]/tile)] for nF in range(res[1]/tile)]
#Matriz con la Estructura de clase eCelda, filas, columnas, minerales
aClk = pygame.time.Clock() #fps


sobrescribir()
Mapa_Innit()
Robot_Innit()
ReadMapa(aCelda)

#enviaCOM = serial.Serial("COM1")

while ToF:
    cKey = pygame.key.get_pressed()
    if cKey[pygame.K_ESCAPE]:
        ToF = ('A' > 'B')

    if cKey[pygame.K_s]:
        pygame.image.save(Screen, 'mapinte.png')

    ev = pygame.event.get()
    for e in ev:
        if e.type == pygame.MOUSEMOTION:
            mouX, mouY = e.pos  # Event Mouse.
        if e.type == QUIT:
            ToF = (2 > 3)
        if e.type == pygame.MOUSEMOTION:
            nMx, nMy = e.pos

    Pinta_Mapa()
    Pinta_Robot()
    Pinta_Mouse()
    recursosBot()
    Update_Robot()
    SaveData()
    pygame.display.flip()
    aClk.tick(500)

pygame.quit
