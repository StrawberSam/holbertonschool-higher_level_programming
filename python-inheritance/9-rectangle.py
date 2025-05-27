#!/usr/bin/python3

"""Module contenant la classe BaseGeometry.
Cette classe servira de base pour définir des formes géométriques.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry

    Args:
        BaseGeometry (class): inherits class
    """

    def __init__(self, width, height):
        """conducteur avec attributs d'instance

        Args:
            width (int): largeur
            height (int): hauteur
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """définit l'aire du rectangle

        Returns:
            int: l'aire du rectangle
        """
        recarea = self.__width * self.__height
        return recarea

    def __str__(self):
        """retourne la description du rectangle

        Returns:
            return en f-string
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
