__author__ = 'Gerard & Zange'
from renpy import exports

class Utils :

    def __init__(self, globales) :
        self._globales = globales

    def musica (self, cancion):
        if cancion != self._globales.musicaActual :
            self._globales.musicaActual = cancion
            exports.music.play(cancion,loop=True, fadeout=.5)