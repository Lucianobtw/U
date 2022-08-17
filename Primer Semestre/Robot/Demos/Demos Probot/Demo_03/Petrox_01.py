# By Alberto Caro S.
# Ing. Civil en Computacion
# Doctor(c) Cs. de la Computacion
# Pontificia Universidad Catolica de Chile
#-------------------------------------------
import pygame,ctypes as ct,serial as RS
from pygame.locals import *

#---------------------------------------------------------------------
# Definicion de Constantes.-
#---------------------------------------------------------------------
nRES = (631,355) ; nMIN_Y = 0   ; nMAX_Y = 480
nMAX_NIVELES = 4 ; nMAX_LED = 4 ; lOK = True

#---------------------------------------------------------------------
# Definicion de Estructura de Datos.-
#---------------------------------------------------------------------
class eNivel(ct.Structure):
 _fields_ = [('nX',ct.c_short),('nY',ct.c_short) ]

class eLeds(ct.Structure):
 _fields_ = [('nX',ct.c_short),('nY',ct.c_short) ]

#---------------------------------------------------------------------
# Carga imagenes y convierte formato PyGame
#---------------------------------------------------------------------
def Load_Image(sFile,transp = False):
    try: image = pygame.image.load(sFile)
    except pygame.error,message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image

#---------------------------------------------------------------------
# Inicializa PyGames.-
#---------------------------------------------------------------------
def PyGame_Init():
    pygame.init()
    pygame.display.set_caption('Simulacion Planta Quimica - By Alberto Caro - 2015()')
    return pygame.display.set_mode(nRES)

#---------------------------------------------------------------------
# Inicializa Array de Figuras.-
#---------------------------------------------------------------------
def Fig_Init():
    aImg = []
    aImg.append(Load_Image('planta.png',False ))
    aImg.append(Load_Image('nivel.png' ,True  ))
    aImg.append(Load_Image('led_u.png' ,True  ))
    aImg.append(Load_Image('led_d.png' ,True  ))
    aImg.append(Load_Image('led_n.png' ,True  ))
    return aImg

#---------------------------------------------------------------------
# Inicilaiza parametros de los 4 Niveles
#---------------------------------------------------------------------
def Niveles_Init():
    aNive[0].nX =  65-31 ; aNive[0].nY = 160
    aNive[1].nX = 219-31 ; aNive[1].nY = 160
    aNive[2].nX = 373-31 ; aNive[2].nY = 160
    aNive[3].nX = 527-31 ; aNive[3].nY = 160
    return

#---------------------------------------------------------------------
# Inicilaiza parametros de los 4 Leds
#---------------------------------------------------------------------
def Leds_Init():
    aLeds[0].nX = 65  ; aLeds[0].nY = 272
    aLeds[1].nX = 215 ; aLeds[1].nY = 272
    aLeds[2].nX = 370 ; aLeds[2].nY = 272
    aLeds[3].nX = 525 ; aLeds[3].nY = 272
    return

#---------------------------------------------------------------------
# Pinta la Planta Quimica
#---------------------------------------------------------------------
def Pinta_Planta():
    Panta.blit(aSprt[0],(0,0))
    return

#---------------------------------------------------------------------
# Pinta los 4 Niveles de los Tanques de Planta Quimica
#---------------------------------------------------------------------
def Pinta_Niveles():
    for i in range(0,nMAX_NIVELES):
     Panta.blit(aSprt[1],(aNive[i].nX,aNive[i].nY))
    return

#---------------------------------------------------------------------
# Pinta los 4 Niveles de los Leds
#---------------------------------------------------------------------
def Pinta_Leds():
    for i in range(0,nMAX_LED):
     Panta.blit(aSprt[aLedP[i]],(aLeds[i].nX,aLeds[i].nY))
    return
#---------------------------------------------------------------------
# Actualiza los 4 Niveles de los Tanques de Planta Quimica
#---------------------------------------------------------------------
def UpDate_Niveles(sPaq):
    Data = sPaq.split(',')
    if Data[0] == '1': # Tanque 1
       if Data[1] == 'U': # Carga H2SO4
          aLedP[0] = 2
          aNive[0].nY -= 1
          if aNive[0].nY <= 100: aNive[0].nY = 100
       if Data[1] == 'D': # Descarga H2SO4
          aLedP[0] = 3
          aNive[0].nY += 1
          if aNive[0].nY >= 240: aNive[0].nY = 240
       if Data[1] == 'N': # Bomba Apagada.-
          aLedP[0] = 4
          aNive[0].nY = aNive[0].nY

    if Data[0] == '2': # Tanque 2
       if Data[1] == 'U': # Carga H2O
          aLedP[1] = 2
          aNive[1].nY -= 1
          if aNive[1].nY <= 100: aNive[1].nY = 100
       if Data[1] == 'D': # Descarga H2O
          aLedP[1] = 3
          aNive[1].nY += 1
          if aNive[1].nY >= 240: aNive[1].nY = 240
       if Data[1] == 'N': # Bomba Apagada.-
          aLedP[1] = 4
          aNive[1].nY = aNive[1].nY

    if Data[0] == '3': # Tanque 3
       if Data[1] == 'U': # Carga HNO3
          aLedP[2] = 2
          aNive[2].nY -= 1
          if aNive[2].nY <= 100: aNive[2].nY = 100
       if Data[1] == 'D': # Descarga HNO3
          aLedP[2] = 3
          aNive[2].nY += 1
          if aNive[2].nY >= 240: aNive[2].nY = 240
       if Data[1] == 'N': # Bomba Apagada.-
          aLedP[2] = 4
          aNive[2].nY = aNive[2].nY

    if Data[0] == '4': # Tanque 4
       if Data[1] == 'U': # Carga H3CL
          aLedP[3] = 2
          aNive[3].nY -= 1
          if aNive[3].nY <= 100: aNive[3].nY = 100
       if Data[1] == 'D': # Descarga H3CL
          aLedP[3] = 3
          aNive[3].nY += 1
          if aNive[3].nY >= 240: aNive[3].nY = 240
       if Data[1] == 'N': # Bomba Apagada.-
          aLedP[3] = 4
          aNive[3].nY = aNive[3].nY
    return

#---------------------------------------------------------------------
# While Principal del Demo.-
#---------------------------------------------------------------------
MyS = RS.Serial('COM2')
Panta = PyGame_Init()
aSprt = Fig_Init()
aLedP = [0,0,0,0]
aLeds = [ eLeds()  for i in range(0,nMAX_LED)     ]
aNive = [ eNivel() for i in range(0,nMAX_NIVELES) ]
Niveles_Init()
Leds_Init()
while lOK:
 cKey = pygame.key.get_pressed()
 if cKey[pygame.K_ESCAPE]: lOK = False
 if cKey[pygame.K_s]: pygame.image.save(Panta,'captura.png')
 ev = pygame.event.get()
 for e in ev:
  if e.type == QUIT: lOK = False
 Pinta_Planta()
 Pinta_Niveles()
 Pinta_Leds()
 pygame.display.flip()
 t = MyS.readline()[:-1]
 UpDate_Niveles(t)
pygame.quit
MyS.close()


