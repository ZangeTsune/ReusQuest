__author__ = 'Zange'
from renpy import exports, store

class Jump:

    def __init__(self, label):
        self._label = label

    def doTheThing(self):
        getattr(store, "globales").otraEscena = True
        exports.jump(self._label)

    def doTheFirstThing(self):
        self.doTheThing()