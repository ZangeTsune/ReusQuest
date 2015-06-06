__author__ = 'Gerard'

from game.model import Equipable

class IniPython:

    EQUIPABLE_SHINAI = "img_shinai.png"

    def getEquipable(self, id):
        if id == self.EQUIPABLE_SHINAI :
            return Equipable(Equipable.ARMA, "item_shinai", "Shinai", 10, 1)

