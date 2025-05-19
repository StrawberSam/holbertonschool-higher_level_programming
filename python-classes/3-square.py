#!/usr/bin/python3
"""
Ce module contient la définition de la classe Square.
Il sert de base pour représenter un carré dans le contexte POO
"""


class Square:
    """
    Classe représentant un carré.
    Elle contiendra des attributs.
    """
    def __init__(self, size=0):
        """Ceci est un attribut d'instance privée

        Args:
            size (_type_): sert à définir la taille du carré
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        C'est une instance public qui retourne la surface carré du carré
        On multiplie la taille par elle-même.
        """

        return (self.__size * self.__size)
