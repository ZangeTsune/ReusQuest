__author__ = 'Isidre'

import ItemEscena, Jump

class Flecha(ItemEscena):

    IZQUIERDA = "img/b_izquierda"
    DERECHA = "img/b_derecha"
    ARRIBA = "img/b_arriba"
    ABAJO = "img/b_abajo"

    def __init__(self, direccion, label, xpos, ypos, xmaximum, ymaximum, imgActivo=None, imgDesactivo=None, activo=True):

        if (imgActivo == None):
            self._direccion = direccion
        else:
            self._direccion = imgActivo
        self._jump = Jump(label).setClickListener(xpos, ypos, xmaximum, ymaximum, direccion)

        ItemEscena.__init__(self, self._jump, activo)