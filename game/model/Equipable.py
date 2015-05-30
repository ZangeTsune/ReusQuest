class Equipable:
    
    #Constantes
    ARMA        = 0
    BOTAS       = 1
    ARMADURA    = 2
    CASCO       = 3
    ACCESORIO   = 4
    
    def __init__(self, id_equipable=None, imagen="", nombre="", ataque = 0, defensa = 0):
        self._id_equipable = id_equipable #tipo
        self._imagen = imagen
        self._nombre = nombre
        self._ataque = ataque
        self._defensa = defensa

    def getImagen(self):
        return self._imagen

    def getId(self):
        return self._id_equipable

    def getNombre(self):
        return self._nombre

    def getAtaque(self):
        return self._ataque

    def getDefensa(self):
        return self._defensa