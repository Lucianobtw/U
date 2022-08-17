# By Alberto Caro S.
# Ing. Civil Computacion
# Dr.(c) Cs. de la Computacion
# Pontificia Universidad Catolica de Chile
#-------------------------------------------
import pygame as PG, time, random as RA, serial as RS # pygame, PIL (Pillow), numpy, matplotlib
from pygame.locals import *    # pyserial -> google  pyserial tutorial

#---------------------------------------------------------------------
# Carga imagenes y convierte formato pygame
#---------------------------------------------------------------------
def Load_Image(sFile,transp=False):
    try: image = PG.image.load(sFile)
    except PG.error,message:
           raise SystemExit,message
    image = image.convert()
    if transp:
       color = image.get_at((0,0))
       image.set_colorkey(color,RLEACCEL)
    return image

#---------------------------------------------------------------------
# Pinta las Temperaturas a Pantalla
#---------------------------------------------------------------------
def Pinta_Data():
    sc.blit(Img,(0,0))
    nDX = 15; nDY = 39 ; nX = 0 ; nRGB = (0,0,0)
    for nT in aT:
     if nT < 10: nRGB = (0,0,255)
     if nT >= 10 and nT <= 25: nRGB = (0,255,0)
     if nT > 25: nRGB = (255,0,0)
     PG.draw.line(sc,nRGB,(nX+nDX,nDY*4),(nX+nDX,(nDY-nT)*4),10)
     nX = nX + 12
    for nX in range(0,29):
     aT[nX] = aT[nX+1] # Corrimiento hacia LEFT <<<---
    return

#---------------------------------------------------------------------
# Imprime Cabezara del Archivo.-
#---------------------------------------------------------------------
def nFh_Head():
 nFh.write(' Data Logger de Temperaturas ' + '\n' )
 nFh.write('-----------------------------' + '\n' )
 nFh.write('Fecha: 06-04-2011'             + '\n' )
 nFh.write('Temperaturas.................' + '\n' )
 nFh.write('-----------------------------' + '\n' )
 return

#---------------------------------------------------------------------
# Main.-
#---------------------------------------------------------------------
#ser = serial.Serial(1)
#ser.baudrate = 2400           -> ser.readline() -> '23\n'

#MyS  = RS.Serial('COM2') # VSPE -> Connector -> COM2
#MyS.baudrate = 2400/9600 8 =  Byte , Sin N 1 Bits de parada -> protocolo
# Metodo -> serial = read(), readline(), readlines(), write() -> R/W Strings = Cadenas
#MyS.write('\n') sData = MySr.readline() sData = '\n' -> PIL

nRes = (475,165) #; Fps = pygame.time.Clock()
nFh  = open('tempe.txt','w')
aT   = [ 0 for i in range(30) ] # 30 Samples.-  aT = [0] * 30 = [0,0,0,.....0]
PG.init()                                                                 #29
sc = PG.display.set_mode(nRes)
Img = Load_Image('base.jpg')
nFh_Head()
lOk = True
while lOk:
 #nData = MyS.read(5) # Un Byte -> 0..1  2.. 254...255 .. 3 y 33
 nData = RA.randint(3,33) # Simulando data x serial port -> 25
 aT[29] = nData
 ev = PG.event.get()
 for e in ev:
  if e.type == PG.QUIT: lOk = False
 Pinta_Data()
 nFh.write(str(nData) + '\n' )
 PG.display.flip()
 #Fps.tick(150)
 time.sleep(.250)
nFh.write('---------[EOF]---------' + '\n' )
#ser.close()
nFh.close()


