__author__ = 'Zange'
from renpy import ui, exports

class ItemEscenaContainer:

    def __init__(self):
        self._itemsEscena = []
        self._color = "#0000"
        self._status = 0

    def setItems(self, *args):
        for item in args:
            self._itemsEscena.append(item)

    def getItem(self, pos):
        return self._itemsEscena[pos]

    def setDebugMode(self):
        self._color = "#FFFF"

    def getStatus(self):
        return self._status

    def setStatus(self, value):
        self._status = value

    def avanza(self):
        self._status += 1

    def activeListeners(self):
        botones = []

        for item in self._itemsEscena:
            botones.append(item.getPosition())

        result = exports.call_screen("BotonesFrame", self._color, botones)

        if not result == None:
            for itemEscena in self._itemsEscena:
                if result == self._itemsEscena.index(itemEscena):
                    exports.hide_screen("BotonesFrame")
                    itemEscena.doTheThing()
                    break