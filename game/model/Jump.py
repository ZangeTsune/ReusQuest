__author__ = 'Zange'
from renpy import exports

class Jump:

    def __init__(self, label):
        self._label = label

    def doTheThing(self):
        exports.jump(self._label)