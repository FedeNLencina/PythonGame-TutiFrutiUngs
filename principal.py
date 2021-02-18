import math, os, random, sys

import pygame
from pygame.locals import *

from configuracion import *
from funcionesVACIAS import *
from extras import *
def main():
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()

    gameClock = pygame.time.Clock()
    totaltime = 0
    fps = FPS_INICIAL

    pygame.display.set_caption("TutiFrutiUNGS")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    puntos = 0

    abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


    #items= listaItems()
    categorias = listaCategorias()
    letraAzar = unaAlAzar(abc)
    colores = lectura(letraAzar, "colores")
    paises = lectura(letraAzar, "paises")
    animales = lectura(letraAzar, "animales")
    verduras= lectura(letraAzar, "verduras")
    nombres= lectura(letraAzar, "nombres")
    peliculas= lectura(letraAzar,"peliculas")
    series= lectura(letraAzar,"series")
    marcasRopa = lectura(letraAzar, "marcasRopa")
    marcasAutos = lectura(letraAzar, "marcasAutos")
    listaDeTodo=[colores,paises,animales, verduras, nombres, peliculas, series, marcasRopa, marcasAutos]
    palabraUsuario=""
    eleccionUsuario=[]
    eleccionCompu=[]

    inGame= False
    reglas= False
    menu = True
    pygame.mixer.music.load("Sonidos/Intro.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    while menu and not reglas:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()
            if e.type == KEYDOWN:
                menu = False
                reglas= True
        dibujarMenu(screen)
    pygame.mixer.music.stop()
    screen.fill(COLOR_FONDO)
    pygame.mixer.music.load("Sonidos/Reglas ost.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)
    while reglas and not inGame:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                quit()
            if e.type == KEYDOWN:
                reglas = False
                inGame= True
        dibujarMenuReglas(screen)
    pygame.mixer.music.stop()
    screen.fill(COLOR_FONDO)
    i = 0
    final= False
    while inGame and not final:
        pygame.mixer.music.load("Sonidos/Main ost.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
        while i < len(categorias):
            gameClock.tick(fps)
            totaltime += gameClock.get_time()

            fps = 3
            categoria=categorias[i]
            for e in pygame.event.get():
                if e.type == QUIT:
                    pygame.quit()
                    return
                if e.type == KEYDOWN:
                        letra = dameLetraApretada(e.key)
                        palabraUsuario += letra
                        if e.key == K_BACKSPACE:
                            palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                        if e.key == K_RETURN:
                            eleccionUsuario.append(palabraUsuario)
                            #chequea si es correcta y suma o resta puntos
                            sumar=esCorrecta(palabraUsuario, letraAzar, categoria, categorias, listaDeTodo)
                            if sumar == 10:
                                puntos+=sumar
                                SonidoPuntos=pygame.mixer.Sound("Sonidos/sonic ring sound.wav")
                                SonidoPuntos.play()
                            if sumar == -10:
                                puntos+=sumar
                                SonidoPuntos = pygame.mixer.Sound("Sonidos/sound wrong choice.wav")
                                SonidoPuntos.play()
                            palabraUsuario=""
                            i=i+1

            segundos = pygame.time.get_ticks() / 1000
            screen.fill(COLOR_FONDO)
            if i<len(categorias):
                dibujar(screen, letraAzar, categorias[i], palabraUsuario, puntos, segundos)
            else:
                #recorro el vector de eleccion compu y comparo con eleccion usuario
                eleccionCompu=juegaCompu(letraAzar, listaDeTodo)
                for k in range(len(eleccionCompu)):
                    if eleccionUsuario[k] == eleccionCompu[k]:
                        puntos = puntos + 10

                dibujarSalida(screen, letraAzar, categorias, eleccionUsuario, eleccionCompu, puntos, segundos)

            pygame.display.flip()
            if i == len(categorias):
                inGame = False
                final= True
        pygame.mixer.music.load("Sonidos/Game over.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(1)
    while final:
        for e in pygame.event.get():
            if e.type == KEYDOWN:
                pygame.mixer.music.stop()
                mensajeFinal(screen) #funcion agregada
            if e.type == QUIT:
                pygame.quit()
                return

if __name__ == "__main__":
    main()
