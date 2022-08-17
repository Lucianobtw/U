
#----------------------------------------------------#
#                      librerias

import ctypes as CT
import random as RA
import time as Ti
import pygame as PG
import telepot as Te
from pygame.locals import*

#----------------------------------------------------#
#       Definicion de ConstantesyVariables
nRES = (1184, 576)
nT_WX = nT_HY = 32
nMAX_ROBOTS = 1
ToF = True
nMx = nMy = 0
nR_1 = 1154
nR_2 = 32

#----------------------------------------------------#
#           Definicion Structura Robots

class eRobot(CT.Structure):
    _fields_ = [
        ('nF', CT.c_short),  # Tile del Robot
        ('nX', CT.c_short),  # Posicion en eje X
        ('nY', CT.c_short),  # Posicion en eje Y
        ('nR', CT.c_short),  # Rango de mov
        ('nS', CT.c_short),  # Switch de cambio de Direccion del Robot
        ('dX', CT.c_short),  # Direccion en X
        ('dY', CT.c_short),  # Direccion en Y
        ('nV', CT.c_short),  # Velocidad 
    ]

#----------------------------------------------------#
#  Definicion Structure Celda Inteligente del Mapa

class eCelda(CT.Structure):
    _fields_ = [
        ('nT', CT.c_ubyte),  # Tipo de Tile/Baldosa
        ('nF', CT.c_ubyte),  # Fila de Mapa
        ('nC', CT.c_ubyte),  # Columna de Mapa
        ('nI', CT.c_ubyte),  # Imagen[0..11]
    ]

#----------------------------------------------------#
#      Carga imagenesyconvierte formato PyGame

def Load_Image(sFile, transp=False):
    try:
        image = PG.image.load(sFile)
    except PG.error.message:
        raise SystemExit.message
    image = image.convert()
    if transp:
        color = image.get_at((0, 0))
        image.set_colorkey(color, RLEACCEL)
    return image

#----------------------------------------------------#
#                   Inicializa PGs.-

def Init_PyGame():
    PG.init()
    PG.mouse.set_visible(False)
    PG.display.set_caption('Mapa 2D+Telegram-Robotica')
    return PG.display.set_mode(nRES)

#----------------------------------------------------#
#       Inicilaiza parametros de los Robots

def Init_Robot():
    for i in range(0, nMAX_ROBOTS):
        aBoe[i].nF = 1          # Robot Tipo1aBoe[i].nF=1
        aBoe[i].nX = 0          # (RA.randint(0,nRES[0]-nT_WX)/nT_WX)*nT_WX
        aBoe[i].nY = 0          # (RA.randint(0,nRES[0]-nT_WX)/nT_WX)*nT_WX
        aBoe[i].nR = nR_1       # (RA.randint(0,nRES[0]-nT_WX)/nT_WX)*nT_WX
        aBoe[i].nS = 1          # Switch por defecto
        aBoe[i].dX = 1          # Por defecto robot Direccion Este.
        aBoe[i].dY = 0
        aBoe[i].nV = 1
    return

#----------------------------------------------------#
#             Inicializa Array de Sprites.

def Init_Fig():
    aImg = []
    aImg.append(Load_Image('T00.png', False))  # Tile sin recurso
    aImg.append(Load_Image('Boe.png', True))  # Tile Robot
    aImg.append(Load_Image('Rat.png', True))  # Tile Raton
    return aImg

#----------------------------------------------------#
# Armando el Mapa con sus recursosytodos sus parametros 
#  para ser utilizado por los sensores de los Robots.

def Init_Mapa():
    for nF in range(0, nRES[1]//nT_HY):
        for nC in range(0, nRES[0]//nT_WX):
            aMap[nF][nC].nT = 0   # Un solo Tile sin recurso
            aMap[nF][nC].nF = nF  # Fila de la Celda
            aMap[nF][nC].nC = nC  # Colu de la Celda
            aMap[nF][nC].nI = RA.randint(0, 11)  # 12 Posibles Imagenes Random
    return

#----------------------------------------------------#
#                   Pinta Mapa

def Pinta_Mapa():
    for nF in range(0, nRES[1]//nT_HY):
        for nC in range(0, nRES[0]//nT_WX):
            if aMap[nF][nC].nT == 0:  # Baldosa sin recursos
                sWin.blit(aFig[0], (aMap[nF][nC].nC *
                                    nT_HY, aMap[nF][nC].nF*nT_WX))
    return

#----------------------------------------------------#
#    Pinta los Robots en el Super Extra Mega Mapa.

def Pinta_Robot():
    for i in range(0, nMAX_ROBOTS):  # Iteramos las 8 Figuras del Robot
        if aBoe[i].nF == 1:
            sWin.blit(aFig[1], (aBoe[i].nX, aBoe[i].nY))
    return

#----------------------------------------------------#
# Actualiza la estructura de datos de cada uno de los 
#           robots dentro del Mapa sMapa.

def Mueve_Robot():
    for i in range(0, nMAX_ROBOTS):  # Recorrimos todos los Robots
        aBoe[i].nR -= 1      # Decrementamos en 1 el Rango del Robot
        if aBoe[i].nR <= 0:   # Robot termino sus pasos?
            if aBoe[i].nS == 1:
                aBoe[i].nS = 2  # Cambio de estado
                aBoe[i].nR = nR_2  # Robot baja nR_2 pasos
                aBoe[i].dX = 0
                aBoe[i].dY = 1
            elif aBoe[i].nS == 2:
                aBoe[i].nS = 3  # Cambio de estado
                aBoe[i].nR = nR_1  # Robot OEste nR_1 pasos
                aBoe[i].dX = -1
                aBoe[i].dY = 0
            elif aBoe[i].nS == 3:
                aBoe[i].nS = 4  # Cambio de estado
                aBoe[i].nR = nR_2  # Robot baja nR_2 pasos
                aBoe[i].dX = 0
                aBoe[i].dY = 1
            else:
                aBoe[i].nS = 1  # Cambio de estado
                aBoe[i].nR = nR_1  # Robot Este nR_1 pasos
                aBoe[i].dX = 1
                aBoe[i].dY = 0
        #----------------------------------------------------#
        # Actualizamos (Xs,Ys) de los Sprites en el Mapa 2D
        # ---------------------------------------------------#
        aBoe[i].nX += aBoe[i].dX*aBoe[i].nV  # Posicion Robot[i] en eje X
        aBoe[i].nY += aBoe[i].dY*aBoe[i].nV  # Posicion Robot[i] en eje Y
        if aBoe[i].nX == 0 and aBoe[i].nY == 544:
            Init_Robot()
        return

#----------------------------------------------------#
#                     Pinta Mouse

def Pinta_Mouse():
    sWin.blit(aFig[2], (nMx, nMy))
    return

#----------------------------------------------------#
#                  Handle de Pause.-

def Pausa():
    while 1:
        e = PG.event.wait()
        if e.type in (PG.QUIT, PG.KEYDOWN):
            return

#              While Principal del Demo.

aMap = [
    [eCelda() for nC in range(nRES[0]//nT_WX)] for nF in range(nRES[1]//nT_HY)
]
sWin = Init_PyGame()
aFig = Init_Fig()
aImg = [  # Imagenes random que estan bajo cada uno de los tiles del Mapa
    'F01.png', 'F02.png', 'F03.png', 'F04.png',
    'F05.png', 'F06.png', 'F07.png', 'F08.png',
    'F09.png', 'F10.png', 'F1l.png', 'F12.png'
]
aBoe = [eRobot() for i in range(0, nMAX_ROBOTS)]
Init_Robot()
Init_Mapa()
aClk = [PG.time.Clock(), PG.time.Clock()]
# Completar con libreria Telepot
teleBot = Te.Bot('API del bot') 

while ToF:
    cKey = PG.key.get_pressed()
    if cKey[PG.K_ESCAPE]:
        ToF = ('A' > 'B')
    if cKey[PG.K_p]:
        Pausa()
    if cKey[PG.K_s]:
        PG.image.save(sWin, 'mapinte.png')
    ev = PG.event.get()
    for e in ev:
        if e.type == QUIT:
            ToF = (2 > 3)
        if e.type == PG.MOUSEMOTION:
            nMx, nMy = e.pos
    Pinta_Mapa()
    Pinta_Robot()
    Mueve_Robot()
    Pinta_Mouse()
    PG.display.flip()
    aClk[0].tick(1000)


PG.quit
