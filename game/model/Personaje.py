from game.model import Consumible, Equipo, Mochila
from renpy import store, character

class Personaje():

    def __init__(self, level, maxHp, nombre=None):
        self.nombre      = nombre
        self._level      = level
        self._maxHp      = maxHp
        self._hpActual   = maxHp
        self._mochila    = Mochila()
        self._equipo     = Equipo()
        self.nombreVariable = self.nombre
        if self.nombre is None:
            self.nombreVariable = "Narrador"
        setattr(store, self.nombreVariable, character.Character(self.nombre, ctc_position="fixed"))

    def __call__(self, what, interact=True):
        return getattr(store, self.nombreVariable)(what, interact=interact)

    def predict(self, what):
        return getattr(store, self.nombreVariable).predict(what)

    def say(self, what):
        getattr(store, self.nombreVariable).resolve_say_attributes(self.predict(what))

    def do_extend(self, what):
        getattr(store, self.nombreVariable).resolve_extend_attributes(self.predict(what))

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