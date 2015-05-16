__author__ = 'Isidre'

from model import ItemEscena, Dialogo

class MostrarTexto(ItemEscena):

    def __init__(self, who, what, xpos, ypos, xmaximum, ymaximum, whatFirst=None, sonido=None, imgActivo=None, imgDesactivo=None):
        ItemEscena.__init__(self, Dialogo(who, what, whatFirst, sonido))
        self.setClickListener(xpos, ypos, xmaximum, ymaximum, imgActivo, imgDesactivo)