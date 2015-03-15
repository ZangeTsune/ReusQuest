from game.model.combate import Ataque


class AtaqueCurativo(Ataque):

    def __init__(self, nombre, tipo, efecto, narracion, cura):
        super(AtaqueOfensivo, self).__init__(nombre, tipo, efecto, narracion)
        self._cura = cura

    def getCura(self):
        return self._cura