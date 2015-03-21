from game.model import Consumible, Equipo, Mochila
from renpy import store, character

class Personaje():

    def __init__(self, nombre, level, maxHp):
        self.nombre      = nombre
        self._level      = level
        self._maxHp      = maxHp
        self._hpActual   = maxHp
        self._mochila    = Mochila()
        self._equipo     = Equipo()
        setattr(store, self.nombre, character.Character(self.nombre))

    def __call__(self, what, interact=True):
        return getattr(store, self.nombre)(what, interact=interact)

    def predict(self, what):
        return getattr(store, self.nombre).predict(what)

    def say(self, what):
        getattr(store, self.nombre).resolve_say_attributes(self.predict(what))

    def equipar(self, equipo):
        self._equipo.setEquipo(equipo)

    def usaItem(self, idConsumible):
        if idConsumible == Consumible.BEGUDA_PLIM:
            #TODO
            return True
        elif idConsumible == Consumible.MENJAR_BLANC:
            #TODO
            return True
        elif idConsumible == Consumible.MASCLET:
            #TODO
            return True
        elif idConsumible == Consumible.ROSA_REUS:
            #TODO
            return True
        elif idConsumible == Consumible.FRUITS_SECS:
            #TODO
            return True
        elif idConsumible == Consumible.CARAMEL_VIRGINIES:
            #TODO
            return True
        else:
            return False