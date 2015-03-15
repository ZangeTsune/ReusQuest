from game.model import Equipable, Consumible

class Mochila:
    def __init__(self):
        self.dinero = 0.0

        self._consumibles = {Consumible.BEGUDA_PLIM: Consumible(Consumible.BEGUDA_PLIM),
                             Consumible.MENJAR_BLANC: Consumible(Consumible.MENJAR_BLANC),
                             Consumible.MASCLET: Consumible(Consumible.MASCLET),
                             Consumible.ROSA_REUS: Consumible(Consumible.ROSA_REUS),
                             Consumible.FRUITS_SECS: Consumible(Consumible.FRUITS_SECS),
                             Consumible.CARAMEL_VIRGINIES: Consumible(Consumible.CARAMEL_VIRGINIES)}

        self._equipables = {Equipable.ARMA: [],
                            Equipable.BOTAS: [],
                            Equipable.ARMADURA: [],
                            Equipable.CASCO: [],
                            Equipable.ACCESORIO: []}

    def putItems(self, idItem, num=1):

        if idItem in self._consumibles:
            self._consumibles.get(idItem) + num

    def putEquip(self, item):

        if item.getId in self._equipables:
            self._equipables.get(item.getId).append(item)

    #TODO funcion de quitar objeto equipo
            
    def gastarItem(self, id_item):
        if id_item in self._consumibles:            
            self._consumibles.get(id_item) - 1