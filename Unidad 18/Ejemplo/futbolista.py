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

        :return dictionary: futbolist params in dictionary form
        :rtype dict
        """
        return {
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "edad": self.edad,
            "demarcacion":self.demarcacion,
            "internacional":self.internacional
        }

    def __str__(self):
        return "Nombre: %s - Apellidos: %s - Edad: %i - Demarcación: %s - Internacional: %r" \
               %(self.nombre, self.apellidos, self.edad, self.demarcacion, self.internacional)
