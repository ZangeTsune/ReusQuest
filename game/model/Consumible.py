class Consumible:

    # Constants
    BEGUDA_PLIM         = 0
    MENJAR_BLANC        = 1
    MASCLET             = 2
    ROSA_REUS           = 3
    FRUITS_SECS         = 4
    CARAMEL_VIRGINIES   = 5

    def __init__(self, idConsumible):
        self.idConsumible = idConsumible
        self._cantidad = 0

    def __add__(self, other):
        if isinstance(other, int):
            self._cantidad += other
        elif isinstance(other, Consumible):
            self._cantidad += other.getCantidad()

    def __radd__(self, other):
        if isinstance(other, int):
            self._cantidad += other
        elif isinstance(other, Consumible):
            self._cantidad += other.getCantidad()

    def __sub__(self, other):
        if isinstance(other, int):
            if self._cantidad < other:
                return False
            else:
                self._cantidad -= other
        elif isinstance(other, Consumible):
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
        elif isinstance(other, Consumible):
            if self._cantidad < other.getCantidad():
                return False
            else:
                self._cantidad -= other

        return True

    def getId(self):
        return self.idConsumible

    def getCantidad(self):
        return self._cantidad
