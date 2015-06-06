# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.

init python:
    from game.model import *
    from utils import ItemEscenaContainer
    from utils import GlobalParams, Utils
    from game.labels.capitulo_1 import *

    globales = GlobalParams()
    utils = Utils(globales)

# - Declara los personajes usados en el juego como
define protagonista = Personaje( 0, 10, "Protagonista",(192, 64, 64, 255))
define antagonista = Personaje( 0, 10, "Antagonista",(28, 64, 184, 255))
define narrador = Personaje(0,0, None)

# The game starts here.
# - El juego comienza aquí.
label start:
    jump cap01_escena00
    return