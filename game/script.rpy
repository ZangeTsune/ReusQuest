# You can place the script of your game in this file.
# - Puedes colocar el 'script' de tu juego en este archivo.


init python:
    from game.model import Personaje, ItemEscena, Dialogo, Jump, Personaje
    from utils import ItemEscenaContainer

    escenaItems = ItemEscenaContainer()

# Declare images below this line, using the image statement.
# - Declara imágenes bajo esta línea, usando 'image' como
#   en el ejemplo.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
# - Declara los personajes usados en el juego como en el 
#   ejemplo.
define protagonista = Personaje( 0, 10, "Protagonista")
define narrador = Personaje(0,0, None)

# The game starts here.
# - El juego comienza aquí.
label start:
    jump cap_01_escena_00
    return