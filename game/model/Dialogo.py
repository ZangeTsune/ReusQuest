__author__ = 'Zange'
from renpy import exports

class Dialogo:

    def __init__(self, who, what, whatFirst=None):
        self._who = who
        self._what = what
        if whatFirst is None:
            self._whatFirst = what
        else:
            self._whatFirst = whatFirst

    def doTheThing(self):
        for linia in self._what:
            exports.say(self._who, linia)

    def doTheFirstThing(self):
        for linia in self._whatFirst:
            exports.say(self._who, linia)