from game.model import Equipable


class Equipo:
    def __init__(self):
        self._equipo = {Equipable.ARMA: Equipable,
                        Equipable.BOTAS: Equipable,
                        Equipable.ARMADURA: Equipable,
                        Equipable.CASCO: Equipable,
                        Equipable.ACCESORIO: Equipable}

    def setEquipo(self, equipo):
        if equipo.getId() in self._equipo:
            self._equipo[equipo.getId()] = equipo

    def getAtaque(self):
        ataque = 0
        for k, equipo in self._equipo:
            ataque += equipo.getAtaque()

        return ataque

    def getDefensa(self):
        defensa = 0
        for k, equipo in self._equipo:
            defensa += equipo.getDefensa()

        return defensa