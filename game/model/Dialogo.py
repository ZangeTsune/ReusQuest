__author__ = 'Zange'
from renpy import exports

class Dialogo:

    def __init__(self, who, what, whatFirst=None, sonido=None):
        self._who = who
        self._what = what
        self._sonido = sonido
        if whatFirst is None:
            self._whatFirst = what
        else:
            self._whatFirst = whatFirst

    def doTheThing(self):
        for linia in self._what:
            if self._sonido is not None:
                exports.play(self._sonido)
            exports.say(self._who, linia)

    def doTheFirstThing(self):
        for linia in self._whatFirst:
            if self._sonido is not None:
                exports.play(self._sonido)
            exports.say(self._who, linia)