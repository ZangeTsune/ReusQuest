from game.model import Equipable, Consumible, Monedero


class Mochila:

    def __init__(self):
        self._monedero = Monedero()

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

    def putConsumible(self, consumible):
        self._consumibles.get(consumible.getId()) + consumible.getCantidad()

    def putEquipable(self, equipable):
        self._equipables.get(equipable.getId).append(equipable)

    #TODO funcion de quitar objeto equipo
            
    def gastarItem(self, id_item):
        if id_item in self._consumibles:            
            self._consumibles.get(id_item) - 1

    def gestionarMonedero(self, monedero):
        self._monedero + monedero