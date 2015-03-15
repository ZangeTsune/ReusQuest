from game.model.combate import Ataque


class AtaqueDobleFilo(Ataque):

    def __init__(self, nombre, tipo, efecto, narracion, danoAjeno, danoPropio):
        super(AtaqueOfensivo, self).__init__(nombre, tipo, efecto, narracion)
        self._danoAjeno = danoAjeno
        self._danoPropio = danoPropio

    def getDanoAjeno(self):
        return self._danoAjeno

    def getDanoPropio(self):
        return self._danoPropio