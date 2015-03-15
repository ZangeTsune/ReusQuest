import random


class Ataque:

    #Tipos
    TIPO_OFENSIVO    = 0
    TIPO_CURATIVO    = 1
    TIPO_DOBLE_FILO  = 2
    TIPO_DRENADOR    = 3

    #Efectos
    EFECTO_NULO     = 4
    EFECTO_VENENO   = 5
    EFECTO_ATURDIR  = 6

    def __init__(self, nombre, tipo, efecto, critico, narracion):
        self._nombre = nombre
        self._tipo = tipo
        self._efecto = efecto
        self._critico = critico
        self._narracion = narracion

    def getNombre(self):
        return self._nombre

    def getTipo(self):
        return self._tipo

    def getEfecto(self):
        return self._efecto

    def getNarracion(self):
        return self._narracion

    def isCritico(self):
        resultado = random.randint(0, 100)

        if resultado < self._critico:
            return True
        else:
            return False