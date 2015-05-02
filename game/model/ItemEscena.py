class ItemEscena:

    def __init__(self, item=None, activo=True):
        self._item = item
        self._encontrado = False
        self._activo = activo

    def isEncontrado(self):
        return self._encontrado

    def activar(self):
        self._activo = True

    def desActivar(self):
        self._activo = False

    def isActivado(self):
        return self._activo

    def setEncontrado(self, encontrado=True):
        self._encontrado = encontrado

    def getItem(self):
        return self._item

    def setClickListener(self, xpos, ypos, xmaximum, ymaximum, imgActivo=None, imgDesactivo=None):
        self._xpos = xpos
        self._ypos = ypos
        self._xmaximum = xmaximum
        self._ymaximum = ymaximum
        self._imgActivo = imgActivo
        self._imgDesactivo = imgDesactivo
        return self

    def getPosition(self):
        if self._activo:
            return [self._xpos, self._ypos, self._xmaximum, self._ymaximum, self._imgActivo]
        else:
            return [self._xpos, self._ypos, self._xmaximum, self._ymaximum, self._imgDesactivo]

    def doTheThing(self):
        if self._activo:
            if not self.isEncontrado():
                self.doTheFirstThing()
            else:
                self._item.doTheThing()

    def doTheFirstThing(self):
        self.setEncontrado()
        self._item.doTheFirstThing()