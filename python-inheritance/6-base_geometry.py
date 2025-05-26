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
