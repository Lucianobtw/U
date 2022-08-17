import pygame, random, ctypes
from pygame.locals import *

#====================================================================================================#
#                                     Definiciones Globales                                          #
#====================================================================================================#

res = (400,353)                 
#Resolucion de la ventana.      

minX = 0                        ;  maxX=2141
#Valor minimo y maximo del eje X en el mapa.

minY = 0                        ; maxY = 353
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

def pygame_init():
    pygame.init()
    pygame.display.set_caption('Bounce Tales MrRevillod')
    pygame.mouse.set_visible(False)
    return pygame.display.set_mode(res)

def Fig_Init():
    aImg = []
    aImg.append(Load_Image('Level02.png',False )) # Level 2.                [0]
    return aImg

def MapLevel02_Init(AnchoX,AnchoY):
    return pygame.Surface((AnchoX,AnchoY))

def PintaLevel02():
    BigLevel.blit(aSprt[0],(xd,yd))

def Pinta_Mapa():
    Screen.blit(BigLevel.subsurface((xd,yd,maxX,maxY)),(xd,yd))
    return

#====================================================================================================#
#                              Funcion "desplazamiento en ScrollX"                                   #
#====================================================================================================#

def desplazamiento(ScrollX):
    Screen.blit(BigLevel.subsurface((ScrollX,yd,400,353)),(xd,yd))
    return


Screen = pygame_init()
aSprt = Fig_Init()
BigLevel = MapLevel02_Init(maxX,maxY)


pygame.time.set_timer(pygame.USEREVENT+1,Timer1) 

while ToF:
    cKey = pygame.key.get_pressed()
    if cKey[pygame.K_RIGHT]: 
        ScrollX+=1
        if ScrollX>1741: 
                ScrollX = 1741
    if cKey[pygame.K_LEFT]: 
        ScrollX-=1
        if ScrollX>1741:
                ScrollX = 1741
    if ScrollX<0:
        ScrollX = 0
    ev = pygame.event.get()
    for e in ev:
        if e.type == pygame.QUIT:
            ToF = False
    PintaLevel02()
    Pinta_Mapa()
    desplazamiento(ScrollX) 
    pygame.display.flip()
pygame.quit

