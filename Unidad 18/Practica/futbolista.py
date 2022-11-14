"""Module that model futbolist object
"""

class Futbolist:
    """class futbolist with properties of the players
    """
    def __init__(self, nombre, apellidos, edad, demarcacion, internacional):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
        self.demarcacion = demarcacion
        self.internacional = internacional

    def toDBCollection (self) -> dict:
        """Convert object properties into dictionary
        """
        return {
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "edad": self.edad,
            "demarcacion":self.demarcacion,
            "internacional":self.internacional
        }
