from game.model import ItemEscena, RecogerHandler

__author__ = 'Zange'

class Recoger(ItemEscena):

    def __init__(self, item, xpos, ypos, xmaximum, ymaximum):
        ItemEscena.__init__(self, RecogerHandler(item))
        self.setClickListener(xpos, ypos, xmaximum, ymaximum)