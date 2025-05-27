#!/usr/bin/python3

"""Import contenant la classe Rectangle.
Cette classe servira de base pour définir des formes géométriques.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Module contenant la classe Square, héritant de Rectangle.
    Cette classe servira de base pour définir des formes géométriques.
    """

    def __init__(self, size):
        """conducteur avec attributs d'instance

        Args:
            size (int) : taille
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """définit l'aire du carré

        Returns:
            int: l'aire du carré
        """
        squarearea = self.__size * self.__size
        return squarearea
