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
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
