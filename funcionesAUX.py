import pygame
from pygame.locals import *
from configuracion import *


def dondeEsta(palabra,lista): #Funcion implementada que devuelve un indice en una lista.
    for indice in range(len(lista)):
        if lista[indice] == palabra:
            return indice
    return -1

def lectura(letra,item): #Funcion implementada que devuelve una lista con palabras que empiezen con la letra elegida.
    listaPalabras = []
    archivoItem = open ("./archivos/" + item + ".txt", "r" )
    cadena = archivoItem.readline()
    while cadena !="":
        for caracter in cadena:
            if caracter == letra:
                listaPalabras.append(cadena[:-1])
            break
        cadena = archivoItem.readline()
    archivoItem.close()
    return listaPalabras


def listaCategorias(): #Funcion implementada para abrir un archivo de txt y crear la lista de categorias a partir de la misma. Esta funcion devuelve la lista creada.
    listaCategorias=[]
    archivoCategorias= open("./archivos/categorias.txt", "r")
    cadena= archivoCategorias.readline()
    while cadena!="":
        listaCategorias.append(cadena[:-1])
        cadena=archivoCategorias.readline()
    archivoCategorias.close()
    return listaCategorias

def dibujarMenu(screen): #Funcion implementada para dibujar un menu de inicio para el juego.
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE)
    defaultFontGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE)
    defaultFontMUYGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_MUYGRANDE)

    mensaje1 = defaultFontMUYGRANDE.render("Bienvenidos a", 1 , COLOR_BLANCO)
    mensaje2 = defaultFontMUYGRANDE.render("Tuti Fruti UNGS", 1 , COLOR_BLANCO)
    mensaje3 = defaultFontGRANDE.render("Presione enter para comenzar", 1 , COLOR_BLANCO)
    mensaje4 = defaultFontGRANDE.render("o cierre la ventana para salir del juego", 1 , COLOR_BLANCO)

    screen.fill(COLOR_FONDO)
    Fondo = pygame.image.load("Imagenes/Fondo Intro.jpg")
    screen.blit(Fondo, [0,0])

    screen.blit(mensaje1, (280, 200))
    screen.blit(mensaje2, (260, 300))
    screen.blit(mensaje3, (270, 400))
    screen.blit(mensaje4, (230, 450))
    pygame.display.update()

def dibujarMenuReglas(screen): #Funcion implementada para crear una pantalla que muestre las reglas del juego.
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA)

    mensaje1 = defaultFont.render("Las reglas del juego son muy sencillas.", 1 , COLOR_BLANCO)
    mensaje2 = defaultFont.render("El juego viene integrado con varias categorias de palabras.", 1, COLOR_BLANCO)
    mensaje3 = defaultFont.render("Cuando la letra aparezca en pantalla usted debe ingresar una palabra y debe apretar.", 1, COLOR_BLANCO)
    mensaje4 = defaultFont.render("enter para pasar a la siguiente categoria. Si la palabra se encuentra en la memoria,", 1, COLOR_BLANCO)
    mensaje5 = defaultFont.render("sumara 10 puntos, caso contrario se restaran 10 puntos. Si la palabra es correcta y ", 1, COLOR_BLANCO)
    mensaje6 = defaultFont.render("es la misma que la palabra elegida por la compu, el puntaje se duplicara.", 1, COLOR_BLANCO)
    mensaje7 = defaultFont.render("Al final del juego podrá ver de arriba hacia abajo las palabras que ingreso y", 1, COLOR_BLANCO)
    mensaje8 = defaultFont.render("a la derecha la eleccion de la compu. Si aparece escrito Not Found, ", 1,COLOR_BLANCO)
    mensaje9 = defaultFont.render("significa que la compu no encontro una palabra de esa categoria en la memoria.", 1, COLOR_BLANCO)
    mensaje10 = defaultFont.render("Presione enter nuevamente para comenzar. Suerte!", 1, COLOR_BLANCO)

    screen.fill(COLOR_FONDO)
    Fondo = pygame.image.load("Imagenes/Fondo 1.jpg")
    screen.blit(Fondo, [0,0])

    screen.blit(mensaje1, (15, 50))
    screen.blit(mensaje2, (15, 100))
    screen.blit(mensaje3, (15, 150))
    screen.blit(mensaje4, (15, 200))
    screen.blit(mensaje5, (15, 250))
    screen.blit(mensaje6, (15, 300))
    screen.blit(mensaje7, (15, 350))
    screen.blit(mensaje8, (15, 400))
    screen.blit(mensaje9, (15, 450))
    screen.blit(mensaje10, (15, 500))

    pygame.display.update()

def mensajeFinal(screen): #Funcion implementada para mostrar un mensaje al final del juego.
    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE)
    defaultFontGRANDE = pygame.font.Font(pygame.font.get_default_font(), TAMANO_LETRA_GRANDE)

    mensaje1 = defaultFont.render("Tengo esa esperanza que hay una mejor manera.", 1 , COLOR_BLANCO)
    mensaje2 = defaultFontGRANDE.render("Herramientas de más alto nivel que en realidad",1, COLOR_BLANCO)
    mensaje3 = defaultFontGRANDE.render("le permiten ver la estructura de los programas con", 1, COLOR_BLANCO)
    mensaje4 = defaultFontGRANDE.render("mayor claridad, serán de enorme valor.", 1, COLOR_BLANCO)
    mensaje5 = defaultFontGRANDE.render("Guido van Rossum.", 1, COLOR_BLANCO)

    Fondo = pygame.image.load("Imagenes/Fondo 1.jpg")
    screen.blit(Fondo, [0,0])
    screen.blit(mensaje1, (150, 270))
    screen.blit(mensaje2, (150, 320))
    screen.blit(mensaje3, (160, 370))
    screen.blit(mensaje4, (160, 420))
    screen.blit(mensaje5, (350, 500))

    pygame.display.update()
