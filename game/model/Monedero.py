__author__ = 'Zange'

class Monedero:

    def __init__(self, cantidad=0):
        self._cantidad = cantidad

    def getCantidad(self):
        return self._cantidad

    def setCantidad(self, cantidad):
        self._cantidad = cantidad

    def __add__(self, other):
        if isinstance(other, int):
            self._cantidad += other
        elif isinstance(other, Monedero):
            self._cantidad += other.getCantidad()

    def __radd__(self, other):
        if isinstance(other, int):
            self._cantidad += other
        elif isinstance(other, Monedero):
            self._cantidad += other.getCantidad()

    def __sub__(self, other):
        if isinstance(other, int):
            if self._cantidad < other:
                return False
            else:
                self._cantidad -= other
        elif isinstance(other, Monedero):
            if self._cantidad < other.getCantidad():
                return False
            else:
                self._cantidad -= other

        return True

    def __rsub__(self, other):
        if isinstance(other, int):
            if self._cantidad < other:
                return False
            else:
                self._cantidad -= other
        elif isinstance(other, Monedero):
            if self._cantidad < other.getCantidad():
                return False
            else:
                self._cantidad -= other

        return True