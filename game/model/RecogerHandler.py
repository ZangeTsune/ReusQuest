from game.model import Monedero, Consumible, Equipable
from renpy import store

__author__ = 'Isidre'

class RecogerHandler:

    def __init__(self, item):
        self._item = item

    def doTheThing(self):
        if isinstance(self._item, Monedero):
            getattr(store, "protagonista").getMochila().gestionarMonedero(self._item)
            #Animacion
            pass

        elif isinstance(self._item, Consumible):
            getattr(store, "protagonista").getMochila().putConsumible(self._item)
            #Animacion
            pass

        elif isinstance(self._item, Equipable):
            getattr(store, "protagonista").getMochila().putEquipable(self._item)
            #Animacion
            pass

    def doTheFirstThing(self):
        self.doTheThing()