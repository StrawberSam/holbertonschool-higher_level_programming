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
    def __init__(self, size):
        """Ceci est un attribut d'instance privée

        Args:
            size (_type_): sert à définir la taille du carré
        """
        self.__size = size
