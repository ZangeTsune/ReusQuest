from game.model.combate import Ataque


class AtaqueDrenaje(Ataque):

    def __init__(self, nombre, tipo, efecto, narracion, dano, cura):
        super(AtaqueOfensivo, self).__init__(nombre, tipo, efecto, narracion)
        self._dano = dano
        self._cura = cura

    def getDano(self):
        return self._dano

    def getCura(self):
        return self._cura