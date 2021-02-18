import pygame
from pygame.locals import *
from configuracion import *


def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")


def dibujar(screen, letra, item, palabraUsuario, puntos, segundos):
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE)
    defaultFontGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE)
    defaultFontMUYGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_MUYGRANDE)

    ren1 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_NEGRO)
    ren2 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_BORDO if segundos >60 else COLOR_NEGRO)
    ren3 = defaultFontMUYGRANDE.render(item, 1, COLOR_TEXTO)
    ren4 = defaultFontMUYGRANDE.render(letra.upper(), 1, COLOR_NEGRO)

    Fondo = pygame.image.load("Imagenes/Fondo 2.jpg")
    screen.blit(Fondo, [0,0])
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (400, 675))
    screen.blit(ren1, (ANCHO - 170, 10))
    screen.blit(ren2, (10, 10))
    screen.blit(ren3, (ANCHO//2-((len(item)//1.75)*TAMANO_LETRA_GRANDE), ALTO//2.5))
    screen.blit(ren4, (ANCHO//2-TAMANO_LETRA_GRANDE, 50))


def dibujarSalida(screen, letra, items, eleccionUsuario, eleccioncompu, puntos, segundos):
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA)
    defaultFontGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE)
    defaultFontMUYGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_MUYGRANDE)

    ren1 = defaultFont.render("Puntos: " + str(puntos), 1, COLOR_NEGRO)
    ren2 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_BORDO if segundos > 60 else COLOR_NEGRO)
    ren3 = defaultFontMUYGRANDE.render(letra.upper(), 1, COLOR_NEGRO)

    Fondo = pygame.image.load("Imagenes/Fondo 1.jpg")
    screen.blit(Fondo, [0,0])
    screen.blit(ren1, (ANCHO - 120, 10))
    screen.blit(ren2, (10, 10))
    screen.blit(ren3, (ANCHO//2-TAMANO_LETRA_GRANDE, 10))
    screen.blit(defaultFont.render("¡Juego terminado!", 1, COLOR_NEGRO), (400, 675))


    y=80
    for palabra in items:
        screen.blit(defaultFontGRANDE.render(palabra, 1, COLOR_BLANCO), (10, y))
        y=y+TAMANO_LETRA_GRANDE*2

    y=80
    for palabra in eleccionUsuario:
        screen.blit(defaultFontGRANDE.render(palabra, 1, COLOR_CELESTE), (ANCHO//2.8, y))
        y=y+TAMANO_LETRA_GRANDE*2

    y=80
    for palabra in eleccioncompu:
        screen.blit(defaultFontGRANDE.render(palabra, 1, COLOR_VERDE), (ANCHO-400, y))
        y=y+TAMANO_LETRA_GRANDE*2


