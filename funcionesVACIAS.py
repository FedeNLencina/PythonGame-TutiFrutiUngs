from configuracion import *
from principal import *
from funcionesAUX import *

import random


def unaAlAzar(lista):
    letraAzar=random.choice(lista)
    return letraAzar

def esCorrecta(palabraUsuario, letra, item, items, listaDeTodo):
    if palabraUsuario != "" and palabraUsuario[0] == letra:
        indice = dondeEsta(item,items)
        if indice != -1:
            for palabra in listaDeTodo[indice]:
                if palabra == palabraUsuario:
                    return 10
    return -10

def juegaCompu(letraAzar, listaDeTodo):
    salida = []
    for lista in listaDeTodo:
        if lista != []:
            palabraAzar = random.choice(lista)
            salida.append(palabraAzar)
        else:
            salida.append("Not found")
    return salida
#Con esta funcion creo una lista la cual es hecha al azar por la compu.
