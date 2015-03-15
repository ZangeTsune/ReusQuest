from game.model.combate import Ataque


class AtaqueOfensivo(Ataque):

    def __init__(self, nombre, tipo, efecto, narracion, dano):
        super(AtaqueOfensivo, self).__init__(nombre, tipo, efecto, narracion)
        self._dano = dano

    def getDano(self):
        if super.isRandom():
            return self._dano * 1.5 #Ejemplo

        return self._dano