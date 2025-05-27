#!/usr/bin/python3

"""Module contenant la classe BaseGeometry.
Cette classe servira de base pour définir des formes géométriques.
"""


class BaseGeometry:
    """Classe de base pour les opérations géométriques.

    Cette classe est destinée à être étendue par d'autres classes
    représentant des formes géométriques spécifiques.
    """
    def area(self):
        """
        Calcule l'aire de la forme géométrique.

        Raises:
            Exception: Indique que la méthode n'est pas implémentée.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method: def integer_validator(self, name, value):
        that validates value:
        you can assume name is always a string
        if value is not an integer: raise a TypeError exception,
        with the message <name> must be an integer
        if value is less or equal to 0: raise a ValueError exception
        with the message <name> must be greater than 0

        Args:
            name (_type_): nom
            value (_type_): valeur

        Raises:
            TypeError: si le type est pas le bon
            ValueError: si la valeur n'est pas bonne
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
