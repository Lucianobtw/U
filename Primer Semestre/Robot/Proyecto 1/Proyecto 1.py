#====================================================================================================#
# UCT ######### Luciano Revillod ########### Ignacio Sube ######### Programacion de robot ############
# PYTHON 2.7.15                           ####ABRIL 2022####                                   PYGAME#
#====================================================================================================#

import pygame, random, ctypes
from pygame.locals import *
import telepot 
#====================================================================================================#
#                                     Definiciones Globales                                          #
#====================================================================================================#

res = (800,480)                 ;  maxBot = 200
#Resolucion de la ventana.      #Cantidad maxima de robots-

minX = 0                        ;  maxX=6400
#Valor minimo y maximo del eje X en el mapa.

minY = 0                        ; maxY = 480
#Valor minimo y maximo del eje Y en el mapa.

tileX = 32; tileY = 32                   ;  FlagX = 361 ;      FlagY = 90
#Valor de eje X e Y de la tile (PX)      #Valor de eje X e Y de la Bandera (Medidas en pixeles)

ToF = True
#Valor True, usado principalmente para crear un ciclo while infinito.

xd = 0                         ; yd = 0                          ; tile = 0
#Valor asignado a 0 en x       #Valor asignado a 0 en Y          #Valor asignado por
#se puede usar para sumar      #se puede usar para sumar         #defecto a 0, que es
#un numero y asi cambiar       #un numero y asi cambiar          #igual a la tile 1, si
#el valor del eje x.           #el valor del eje y.              #el valor cambia a 1 o 2,
#                              #                                 #cambiara a la tile respectiva.

mouX = 0                       ; mouY = 0                        ;ScrollX = 0    ; Timer1 = 10
#Valor asignado a 0 en x       #Valor asignado a 0 en Y          #Posicion 0     #Timer para f
#se puede usar para sumar      #se puede usar para sumar         #en X para la   #scroll,repre
#un numero y asi cambiar       #un numero y asi cambiar          #funcion de     #senta 10ms
#el valor del eje x(MOUSE).    #el valor del eje y(MOUSE).       #Scroll.        #(miliseg).

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
    pygame.display.set_caption('Demo Robotica Mapa2D - Revillod y Sube')
    pygame.mouse.set_visible(False)
    # Se vuelve invisible el cursor, para despues usar un sprite sobre el.
    return pygame.display.set_mode(res)

#====================================================================================================#
#                                   Inicializa Lista de Sprites.-                                    #
#           Utiliza la funcion Load image para cargar imagenes y asignarles tranparencia             #
#        Ademas se crea una lista que contiene todos los sprites a utilizar, esto para una           #
#                            mayor facilidad al utilizar cada sprite.                                #
#====================================================================================================#

def Fig_Init():
    aImg = []
    aImg.append(Load_Image('T02.png',False )) # Baldosa 0.                [0]
    aImg.append(Load_Image('T03.png',False )) # Baldosa 1.                [1]
    aImg.append(Load_Image('T04.png',False )) # Baldosa 2.                [2]
    aImg.append(Load_Image('T05.png',True  )) # Robot 1.                  [3]
    aImg.append(Load_Image('T06.png',True  )) # Robot 2.                  [4]
    aImg.append(Load_Image('T10.png',True  )) # Cursor Mouse.             [5]
    aImg.append(Load_Image('T07.png',False )) # Banner.                   [6]
    aImg.append(Load_Image('T08.png',False )) # Bandera.                  [7]
    aImg.append(Load_Image('T09.png',False )) # Barra nave.               [8]
    aImg.append(Load_Image('T00.png',True ))  # Nave cerrada.             [9]
    aImg.append(Load_Image('T01.png',True ))  # Nave abierta.             [10]
    return aImg

#====================================================================================================#
#                                         Funcion "Mapa_Init"                                        #
#                               Inicializa Superficie del MAPA (HORIZONTAL).                         #
#                     Se crea y retorna (RETURN) el Super Mapa de 6400 x 480 px                      #
#                   Retorna Surface donde se posicionaran los tiles ("TilesOnMap()")                 #
#====================================================================================================#

def Mapa_Init(AnchoX,AnchoY):
    return pygame.Surface((AnchoX,AnchoY))

#====================================================================================================#
#                                         Funcion "Tiles_Init"                                       #
#                      Las Baldosas = Tiles miden : tileX -> 32 px, tileY -> 32 px                   #
#                Asi en: 6400 / 32 = 200 Tiles en Eje X  , 480 / 32 = 15 Tiles en Eje Y.             #
#====================================================================================================#

def Tiles_Init():
    return [[0 for i in range(0,maxX/tileX)] \
                                for i in range(0,maxY/tileY)]

#====================================================================================================#
#                                        Funcion "TilesOnMap"                                        #
#                                    Se "Imprimen" las baldosas.                                     #
#====================================================================================================#

def TilesOnMap():
    nPx = nPy = 0
    for y in range(0, maxY // tileY):
        for x in range(0, maxX // tileX):
            Bigmapa.blit(aSprt[tile],(nPx,nPy))
            nPx += tileX
        nPx = 0 #parte en 0 y se suma 32 (tileX)
        nPy += tileY  
    return

#====================================================================================================#
#                                     Funcion "PintaFlag" (Bandera)                                  #
#           Se le asigna el sprt[7] a la bandera en un rango de 5 veces a lo largo del mapa          #
#                Se define la posicion de la bandera en eje X,Y  (FlagX, FlagY).                     #
#====================================================================================================#

def PintaFlag():
    FlagX = FlagY = 0 #Posicion Inicial de la bandera, se define 0 para ser modificada.
    for x in range(5):  #Ciclo de 5 repeticiones (5 banderas)
        Bigmapa.blit(aSprt[7],(FlagX+900,FlagY+150))#[1]
        FlagX += (2000)#[2]
        #[1]Se imprime la bandera sobre el mapa(6400x4800)px, seguido se encuentra la-
        #   -posicion que tendra la bandera en los respectivos ejes X e Y (-linea 139-)
        #[2]Distancia en pixeles entre cada bandera (-linea 140-)
    return

#====================================================================================================#
#                            Se Define la estructura de los robots (ctypes)                          #
#====================================================================================================#

class eRobot(ctypes.Structure):
    _fields_ = [('TypeBot',ctypes.c_short),('PosBotX',ctypes.c_short),
    ('PosBotY',ctypes.c_short),('RangMov',ctypes.c_short),('DirX',ctypes.c_short),
    ('DirY',ctypes.c_short),('Velbot',ctypes.c_short)]

#====================================================================================================#
#                             Definicion de Estructura de Datos Robots.-                             #
#====================================================================================================#
#                                                                                                    #
# TypeBot : Identificador de robot, 1 o 2, usado para asignar sprite.                                #
# PosBotX : Coordenada en eje X del Robot en el Bigmapa.                                             #
# PosBotY : Coordenada en eje Y del Robot en el Bigmapa.                                             #
# RangMov : Rango de desplazamiento del robot (0,500) (Medida en pixeles).                           #
# DirX : Direccion en Eje X ->                                                                       #
#                           0 : Sin movimiento por eje X.                                            #
#                          +1 : Se Mueve un pixel a la Derecha.                                      #
#                          -1 : Se Mueve un pixel a la Izquierda.                                    #
# DirY :                                                                                             #
#                           0 : Sin movimiento por eje Y.                                            #
#                          +1 : Se Mueve un pixel hacia Abajo.                                       #
#                          -1 : Se Mueve un pixel hacia Arriba.                                      #
# Velbot : Velocidad Aleatoria entre [1,2,3].                                                        #
#                                                                                                    #
#====================================================================================================#

#====================================================================================================#
#                                 Inicilaiza parametros de los Robots                                #
#====================================================================================================#

def Robots_Init():
    for i in range(0,maxBot):
        aBoes[i].TypeBot = random.randint(1,2)       # Asigna un num-
        #                                            # -identificador cada robot(1,2)#
        aBoes[i].PosBotX = random.randint(0,6400)    # Pos. X Robot Mapa.    #
        aBoes[i].PosBotY = random.randint(0,480)     # Pos. Y Robot Mapa.    #
        aBoes[i].RangMov = random.randint(0,500)     # Rango de Desplazamiento del robot.   #
        aBoes[i].DirX = 0                            # Sin movimiento por eje X.            #
        aBoes[i].DirY = 0                            # Sin movimiento por eje Y.            #
        aBoes[i].VelBot = random.randint(1,3)        # Velocidad Aleatoria entre [1,2,3].   #
    return

#====================================================================================================#
#                                         Funcion "Pinta_Robots"                                     #
#                        Se pintan los Robots en Surface -> Bigmapa (6400 x 480).                    #
#====================================================================================================#

def Pinta_Robots():
    for i in range(0,maxBot):                     #Rango 0,200 (Cada uno de los 200 Bots).
        if aBoes[i].TypeBot == 1:                                        # Robot tipo 1. #
            Bigmapa.blit(aSprt[3],(aBoes[i].PosBotX,aBoes[i].PosBotY))
        elif aBoes[i].TypeBot == 2:                                      # Robot tipo 2. #
            Bigmapa.blit(aSprt[4],(aBoes[i].PosBotX,aBoes[i].PosBotY))
    return

#=====================================================================================================#
#                                     Funcion "Update_Robots"                                         #
#         Actualiza la estructura de datos de cada uno de los robots dentro del Mapa Bigmapa.         #
#=====================================================================================================#

def UpDate_Robots():
    for i in range(0,maxBot):                           # Recorrimos todos los Robots.
        aBoes[i].RangMov -= 1 
        # Decrementamos en 1 el Rango del Robot --- robot se detiene dsp de 500px.
        if aBoes[i].RangMov < 0:                        # Si es negativo ->
            aBoes[i].RangMov = random.randint(0,500)    # Asignamos otro Rango aleatorio.
            aBoes[i].VelBot = random.randint(1,3)       # Asignamos otra velocidad.
            BotDir = random.randint(1,9)                # Generamos una Direccion -
            #                                           # - de Movimiento Aleat.

            if BotDir == 1:                               # Norte.
                aBoes[i].DirX = +0 ; aBoes[i].DirY = -1
            elif BotDir == 2:                             # Este.
                aBoes[i].DirX = +1 ; aBoes[i].DirY = 0
            elif BotDir == 3:                             # Sur.
                aBoes[i].DirX = +0 ; aBoes[i].DirY = +1
            elif BotDir == 4:                             # Oeste.
                aBoes[i].DirX = -1 ; aBoes[i].DirY = +0
            elif BotDir == 5:                              # Detenido.
	            aBoes[i].DirX = +0 ; aBoes[i].DirY = +0
            elif BotDir == 6:                              # NorEste.
	            aBoes[i].DirX = +1 ; aBoes[i].DirY = -1
            elif BotDir == 7:                              # NorWeste.
	            aBoes[i].DirX = -1 ; aBoes[i].DirY = -1
            elif BotDir == 8:                              # SurEste.
	            aBoes[i].DirX = +1 ; aBoes[i].DirY = +1
            elif BotDir == 9:                              # SurWeste.
	            aBoes[i].DirX = -1 ; aBoes[i].DirY = +1

#====================================================================================================#
#                  Actualizamos (Xs,Ys) de los Sprites en el Mapa 2D                                 #
#               (-6 para que los bots choquen con el borde del display)                              #
#                                 i=(0,200  Robots)                                                  #
#====================================================================================================#

        aBoes[i].PosBotX += aBoes[i].DirX*aBoes[i].VelBot      # Posicion Robot[i] en eje X.
        aBoes[i].PosBotY += aBoes[i].DirY*aBoes[i].VelBot      # Posicion Robot[i] en eje Y.

        if aBoes[i].PosBotX < minX-6:                          # Check los bordes o limites.
            aBoes[i].PosBotX = minX-6 ; aBoes[i].RangMov = 0

        elif aBoes[i].PosBotX > (maxX - tileX):                # Check los bordes o limites.
            aBoes[i].PosBotX = maxX - tileX ; aBoes[i].RangMov = 0

        elif aBoes[i].PosBotY < minY-6:                         # Check los bordes o limites.
            aBoes[i].PosBotY = minY-6 ; aBoes[i].RangMov = 0

        elif aBoes[i].PosBotY > (maxY - tileY):                 #Check los bordes o limites.
            aBoes[i].PosBotY = maxY - tileY ; aBoes[i].RangMov = 0
    return


#====================================================================================================#
#                                      Funcion "PintaBarSonda"                                       #
#              Usamos Screen.blit para mostrar en pantalla el sprite correspondiente                 #
#    a la barra de la sonda, uso las cordenadas x305 e y445 ya que me permiten posicionar            #
#                            la barra abajo y al medio de la pantalla.                               #
#====================================================================================================#

def PintaBarSonda():
    Screen.blit(aSprt[8],(305,445))
    return

#====================================================================================================#
#                            Se Define la estructura de la sonda (ctypes).                           #
#====================================================================================================#

class eSonda(ctypes.Structure):
    _fields_ = [('SdX',ctypes.c_short),('SdY',ctypes.c_short),
    ('DirX',ctypes.c_short),('SdVel',ctypes.c_short)]

#====================================================================================================#
#                        Definicion de Estructura de Datos de la sonda.-                             #
#====================================================================================================#
#                                                                                                    #
# SdX : Coordenada en eje X de la sonda en el SubSurface.                                            #
# SdY : Coordenada en eje Y de la sonda en el Subsurface.                                            #                         
# DirX : Direccion en Eje X ->                                                                       #
#                          +1 : Se Mueve un pixel a la Derecha.                                      #
#                          -1 : Se Mueve un pixel a la Izquierda.                                    #                                    
# SdVel : Velocidad Constante [1]                                                                    #
#                                                                                                    #
#====================================================================================================#

#====================================================================================================#
#                                       Funcion "SondaInit"                                          #
#                          Asignamos valores a la estructura de la sonda.                            #
#====================================================================================================#

def SondaInit():
    sonda.SdX = 300  # Posicion (px) inicial de la sonda en eje X.
    sonda.SdY = 445  # Posicion (px) inicial de la sonda en eje y.
    sonda.DirX = 1   # Direccion inicial/predeterminada en el eje X.(1 o -1)
    sonda.SdVel = 1  # Velocidad Constante de la Sonda.
    return

#====================================================================================================#
#                                      Funcion "UpdateSonda"                                         #
#                 Usamos condicionales para asignar los limites en el eje X de la sonda.             #
#        Elegimos valores X312, X465 para que la onda no choque con los bordes de la barra.          #
#====================================================================================================#

def UpdateSonda():
    if sonda.SdX >= 465: 
    #Basicamente, si la sonda llega a la posicion 465 del eje X
        sonda.DirX =- 1 #la direccion cambia hacia la izquierda(-1).

    if sonda.SdX <= 312: 
    #Por otro lado, si la sonda llega a la posicion 312 del eje X
        sonda.DirX = 1  #la direccion retomara su sentido inicial (1).

    sonda.SdX += sonda.SdVel  *sonda.DirX
    #Posicion de Sonda en X = sonda.SdX+sonda.SdVel*sonda.DirX.
    return

#====================================================================================================#
#                                        Funcion "Pinta_Sonda"                                       #
#                      Asignamos un sprite al cursor,  mouX y mouY corresponden a 0,                 #
#         Si la direccion del robot es hacia la izquierda (-1), cambia al sprite[10]                 #
#          Si la direccion del robot es hacia la derecha (1), cambia al sprite[9]                    #
#====================================================================================================#

def PintaSonda():
    if sonda.DirX == -1:
        Screen.blit(aSprt[10],(sonda.SdX,sonda.SdY))
    elif sonda.DirX == 1:
        Screen.blit(aSprt[9],(sonda.SdX,sonda.SdY))
    return

#====================================================================================================#
#                              Funcion "desplazamiento en ScrollX"                                   #
#                           -Scroll en funcion al valor de ScrollX                                   #
#                Posicion del scroll en X, comienza en las cordenadas senaladas                      #
#                       y desplaza la subsurface a traves del Bigmapa.                               #
#====================================================================================================#

def desplazamiento(ScrollX):
    Screen.blit(Bigmapa.subsurface((ScrollX,yd,800,480)),(xd,yd))
    return

#====================================================================================================#
#                                          Funcion "banner"                                          #
#                  Asignamos los sprite al banner en su respectiva posicion de X e Y                 #
#      Cabe resaltar que el o los banners van por sobre todo lo que hay en la pantalla.              #
#====================================================================================================#

def banner():
    Screen.blit(aSprt[6],(220,50))
    return

#====================================================================================================#
#                                       Funcion "Pinta_Mouse"                                        #
#                 Asignamos un sprite al cursor,  mouX y mouY corresponden a 0,                      #
#                         pero se ira actualizando en pociciones de x e y                            #
#                          en funcion de el movimiento del mouse.                                    #
#====================================================================================================#

def Pinta_Mouse():
    Screen.blit(aSprt[5],(mouX,mouY))
    return

#====================================================================================================#
#                                     While Principal del Demo.-                                     #
#====================================================================================================#

Screen = pygame_init()                           # Surface Display principal.               #
aSprt = Fig_Init()                               # Cargamos los graficos al Array aSprt.    #
aTile = Tiles_Init();                            # Inicializamos el Array de Tiles.         #
aBoes = [ eRobot() for i in range(0,maxBot) ]    # Array de Robots (0,200).                 #
Bigmapa = Mapa_Init(6400,480)                    # Creamos Bigmapa (6400,480)  (Surface).   #
sonda = eSonda()                # sonda. corresponde a los datos asignados en la structure. #
Robots_Init() # linea 153  #Inicializamos la funcion, asignamos, rango, posicion, id, etc.  #
SondaInit()   # Inicializamos los valores de estructura de la sonda.                        #

pygame.time.set_timer(pygame.USEREVENT+1,Timer1) 
#Creamos un evento en funcion del tiempo (Timer1)

#====================================================================================================#
#                                   While y condicionales principales                                #
#====================================================================================================#

while ToF:            #Damos inicio a nuestro ciclo principal con valor constante ToF (True).
    ev = pygame.event.get()
    #Captura eventos, tales como Cerrar el Proyecto, el movimiento del mouse.
    for e in ev:
        if e.type == pygame.MOUSEMOTION : mouX,mouY = e.pos #Event Mouse.
        if e.type == pygame.QUIT:                           #Event QUIT/SALIR.
            ToF = False                                     #Se detiene el Ciclo. 

        if e.type == pygame.USEREVENT+1:
            ScrollX+=1       #Sumamos 1px al eje X del scroll.
            if ScrollX>5600: #Si el eje X llega a los 5600 pixeles, entonces-
                ScrollX=0    #el eje X del Scroll se reinicia, desde 0.

    cKey = pygame.key.get_pressed()  #Captura pulsamiento de teclas.
    if cKey[pygame.K_F1] : tile = 0  #Si se presiona la tecla F1,F2 o F3 entonces-
    if cKey[pygame.K_F2] : tile = 1  #-la variable tile cambiara su valor a 0, 1 o 2 -
    if cKey[pygame.K_F3] : tile = 2  #usamos esta variable en la funcion "TilesOnMap"-
    #De esta forma es como modificamos el fondo, (Tiles).
    if cKey[pygame.K_ESCAPE] : ToF = False
    #Actua de igual manera a pygame.quit, solo que con la tecla ESC.
    if cKey[pygame.K_s]      : pygame.image.save(Screen,'Capture.png') 
    # Captura imagen en pantalla.

#====================================================================================================#
#                                    Ejecucion las funciones                                         #
#====================================================================================================#

    TilesOnMap()
    PintaFlag()
    UpdateSonda()
    UpDate_Robots()
    Pinta_Robots()
    desplazamiento(ScrollX)
    Pinta_Mouse()
    PintaBarSonda()
    PintaSonda()

    if cKey[pygame.K_a]  : banner() 
    #si se presiona la tecla a, se inicia la funcion banner().
    pygame.display.flip()
pygame.quit
