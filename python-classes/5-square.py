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

    @property  # Getter
    def size(self):
        """Lis la valeur d'un attribut privé

        Returns:
            self.__size: retourne l'attribut privé
        """
        return self.__size

    @size.setter  # Setter
    def size(self, value):
        """Modifie la valeur de l'attribut en contrôlant ce qu'on autorise.

        Args:
            value (int): la valeur que l'on veut

        Raises:
            TypeError: si ce n'est pas un integer
            ValueError: si la valeur est plus petit ou égal à 0
        """

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        C'est une instance public qui retourne la surface carré du carré
        On multiplie la taille par elle-même.
        """

        return (self.__size ** 2)

    def my_print(self):
        """
        that prints in stdout the square with the character #.
        If size is equal to 0, print an empty line
        """
        ligne = None

        if self.size == 0:
            print()

        for i in range(self.size):
            ligne = '#' * self.size
            print(ligne)
