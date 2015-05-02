__author__ = 'Isidre'

from model import ItemEscena, Jump

class Flecha(ItemEscena):

    TRANSPARENTE = None
    IZQUIERDA = "img/b_izquierda.png"
    DERECHA = "img/b_derecha.png"
    ARRIBA = "img/b_arriba.png"
    ABAJO = "img/b_abajo.png"

    def __init__(self, direccion, label, xpos, ypos, xmaximum=100, ymaximum=100, imgActivo=None, imgDesactivo=None, activo=True):
        ItemEscena.__init__(self, Jump(label), activo)

        if (imgActivo == None):
            self._direccion = direccion
        else:
            self._direccion = imgActivo

        self.setClickListener(xpos, ypos, xmaximum, ymaximum, direccion, imgDesactivo)