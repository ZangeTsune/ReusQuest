from game.model import Monedero, Consumible, Equipable
from game.labels.capitulo_1 import InitPython
from renpy import store, exports
from renpy.display.motion import Transform

__author__ = 'Zange'

class RecogerHandler:

    def __init__(self, recoger, id_item):
        self._item = InitPython().getEquipable(id_item)
        self._recoger = recoger

    def doTheThing(self):
        if isinstance(self._item, Monedero):
            getattr(store, "protagonista").getMochila().gestionarMonedero(self._item)
            exports.show("coin", Transform(xpos=.3, ypos=.3))
            #Animacion
            pass

        elif isinstance(self._item, Consumible):
            getattr(store, "protagonista").getMochila().putConsumible(self._item)
            exports.show('newItem', [Transform(xpos=.3, ypos=.3)])
            exports.show(self._item.getImagen(), [Transform(xpos=.3,ypos=.3)])
            exports.play('sound/item.wav')
            recoger.desActivar()

            #Animacion
            pass

        elif isinstance(self._item, Equipable):
            getattr(store, "protagonista").getMochila().putEquipable(self._item)
            exports.show('newItem', [Transform(xpos=.3,ypos=.3)])
            exports.show(self._item.getImagen(), [Transform(xpos=.35,ypos=.35)])
            exports.play('sound/item.wav')
            recoger.desActivar()

            #Animacion
            pass

    def doTheFirstThing(self):
        self.doTheThing()