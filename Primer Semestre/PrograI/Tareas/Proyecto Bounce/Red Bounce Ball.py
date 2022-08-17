import pygame, random, ctypes
from pygame.locals import *

#====================================================================================================#
#                                     Definiciones Globales                                          #
#====================================================================================================#

res = (400,353)                 
#Resolucion de la ventana.      

minX = 0                        ;  maxX=600
#Valor minimo y maximo del eje X en el mapa.

minY = 0                        ; maxY = 800
#Valor minimo y maximo del eje Y en el mapa.

ToF = True
#Valor True, usado principalmente para crear un ciclo while infinito.

xd = 0                         ; yd = 0                          
#Valor asignado a 0 en x       #Valor asignado a 0 en Y          
#se puede usar para sumar      #se puede usar para sumar         
#un numero y asi cambiar       #un numero y asi cambiar          
#el valor del eje x.           #el valor del eje y.              

ScrollX = 0                    ;Timer1 = 10            
#Posicion 0                    #Timer para f
#en X para la                  #scroll,repre
# #funcion de                  #senta 10ms
#Scroll.                       #(miliseg).

#====================================================================================================#
#                                        Funcion "Load_Image'                                        #
#                            Carga imagenes y convierte formato PyGame.                              #
#====================================================================================================#
#====================================================================================================#
#                                        Funcion "Load_Image'                                        #
#                            Carga imagenes y convierte formato PyGame.                              #
#====================================================================================================#

def Load_Image(sFile,transp = False):
    try: image = pygame.image.load(sFile)
    except pygame.error.message:
        raise SystemExit.message
    image = image.convert()  
    if transp:
        color = image.get_at((0,0))
        image.set_colorkey(color)
    return image

#====================================================================================================#
#                                        Inicializa PyGames.-                                        #
#                                  Inicializa el Engine de PyGame.                                   #
#====================================================================================================#

def Fig_Init():
    aImg = []
    aImg.append(Load_Image('S01.png',False )) # Background               [0]
    aImg.append(Load_Image('S02.png',False )) # Red tile                 [1]
    aImg.append(Load_Image('S03.png',False )) # triangle tile            [2]
    aImg.append(Load_Image('S04.png',False )) # triangle tile            [3]
    aImg.append(Load_Image('S05.png',False )) # Bonus                    [4]
    aImg.append(Load_Image('S06.png',False )) # Obstaculo                [5]
    aImg.append(Load_Image('S07.png',False )) # Red Ball                 [6]
    aImg.append(Load_Image('S08.png',False )) # Blue Ball                [7]
    aImg.append(Load_Image('S09.png',False )) # Plop Ball                [8]
    aImg.append(Load_Image('S10.png',False )) # Change Ring              [9]
    return aImg
def Fig_Init():
    aImg = []
    aImg.append(Load_Image('Level02.png',False )) # Level 2.                [0]
    return aImg

def MapInit(maxX,maxY):
    return pygame.Surface((maxX,maxY))

def Background():
    Map.blit(sprt[0],(xd,yd))

Map = MapInit(maxX,maxY)
sprt = Fig_Init()
while ToF:

    MapInit()