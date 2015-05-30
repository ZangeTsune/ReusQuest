__author__ = 'Gerard'

class Inicializaciones:

    EQUIPABLE_SHINAI = "img_shinai.png"

    def getEquipable(self, id):
        if id == "EQUIPABLE_SHINAI" :
            return Equipable(Equipable.ARMA, "item_shinai", "Shinai", 10, 1)

