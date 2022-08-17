# By Alberto Caro S.
# Ing. Civil en Computacion
# Doctor(c) Cs. de la Ingenieria
# Pontificia Universidad Catolica de Chile
#-------------------------------------------

from PIL import Image
from pygame.locals import *
import pygame as pg, random as ra, time as ti

nRES = (469,615) ; lOK = True ; PATH = '.'

#---------------------------------------------------------------------
# Carga imagenes y convierte formato PyGame
#---------------------------------------------------------------------
def Load_Image(sFile,transp = False):
    try: image = pg.image.load(sFile)
    except pg.error,message:
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
    pg.init()
    pg.display.set_caption('PYGAME - By Alberto Caro - 2015()')
    return pg.display.set_mode(nRES)

#---------------------------------------------------------------------
# Pinta la Pantalla Principal de PyGames.-
#---------------------------------------------------------------------
def Pinta_Panel():
    Panta.blit(Panel,(0,0))
    return

#---------------------------------------------------------------------
# Pinta Proyectil en Panta.-
#---------------------------------------------------------------------
def Pinta_Carta(aF):
    aXY = [
           [(7,  9),(72,  9),(137,  9),(202,  9),(267,  9),(332,  9),(397,  9)],
           [(7, 85),(72, 85),(137, 85),(202, 85),(267, 85),(332, 85),(397, 85)],
           [(7,161),(72,161),(137,161),(202,161),(267,161),(332,161),(397,161)],
           [(7,237),(72,237),(137,237),(202,237),(267,237),(332,237),(397,237)],
           [(7,313),(72,313),(137,313),(202,313),(267,313),(332,313),(397,313)],
           [(7,389),(72,389),(137,389),(202,389),(267,389),(332,389),(397,389)],
           [(7,465),(72,465),(137,465),(202,465),(267,465),(332,465),(397,465)],
           [(7,541),(72,541),(137,541),(202,541),(267,541),(332,541),(397,541)]
          ]
    for nF in range(8):
     for nC in range(7):
      Panta.blit(aF[nF][nC],aXY[nF][nC])
    return

#---------------------------------------------------------------------
# Random Cartas
#---------------------------------------------------------------------
def Random_Cartas():
 for i in range(8):
  ra.shuffle(aFig[i])
 return
#---------------------------------------------------------------------
# While Principal del Demo.-
#---------------------------------------------------------------------
Panta = PyGame_Init()
Panel = Load_Image('panel2.png')
aFig  = [
         [Load_Image('a.jpg'),Load_Image('b.jpg'),Load_Image('c.jpg'),Load_Image('d.jpg'),Load_Image('e.jpg'),Load_Image('f.jpg'),Load_Image('g.jpg')],
         [Load_Image('a.jpg'),Load_Image('b.jpg'),Load_Image('c.jpg'),Load_Image('d.jpg'),Load_Image('e.jpg'),Load_Image('f.jpg'),Load_Image('g.jpg')],
         [Load_Image('a.jpg'),Load_Image('b.jpg'),Load_Image('c.jpg'),Load_Image('d.jpg'),Load_Image('e.jpg'),Load_Image('f.jpg'),Load_Image('g.jpg')],
         [Load_Image('a.jpg'),Load_Image('b.jpg'),Load_Image('c.jpg'),Load_Image('d.jpg'),Load_Image('e.jpg'),Load_Image('f.jpg'),Load_Image('g.jpg')],
         [Load_Image('a.jpg'),Load_Image('b.jpg'),Load_Image('c.jpg'),Load_Image('d.jpg'),Load_Image('e.jpg'),Load_Image('f.jpg'),Load_Image('g.jpg')],
         [Load_Image('a.jpg'),Load_Image('b.jpg'),Load_Image('c.jpg'),Load_Image('d.jpg'),Load_Image('e.jpg'),Load_Image('f.jpg'),Load_Image('g.jpg')],
         [Load_Image('a.jpg'),Load_Image('b.jpg'),Load_Image('c.jpg'),Load_Image('d.jpg'),Load_Image('e.jpg'),Load_Image('f.jpg'),Load_Image('g.jpg')],
         [Load_Image('a.jpg'),Load_Image('b.jpg'),Load_Image('c.jpg'),Load_Image('d.jpg'),Load_Image('e.jpg'),Load_Image('f.jpg'),Load_Image('g.jpg')]
        ]

Fps = pg.time.Clock()

while lOK:
 for i in range(8):
  ra.shuffle(aFig[i])
 cKey = pg.key.get_pressed()
 if cKey[pg.K_ESCAPE] : lOK = False
 if cKey[pg.K_r] : Random_Cartas()
 ev = pg.event.get()
 for e in ev:
  if e.type == QUIT:
     lOK = False
 Pinta_Panel()
 Pinta_Carta(aFig)
 Fps.tick(5)
 pg.display.flip()
pg.quit





