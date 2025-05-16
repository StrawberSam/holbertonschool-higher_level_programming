#!/usr/bin/python3
"""
prints a square with the character #
    """


def print_square(size):
    ligne_carre = None
    """prints a square with the character #

    Args:
        size (int): size length of the square

    Raises:
        TypeError: size doit être un entier
        ValueError: size doit être plus grand que 0
        TypeError: size doit être un entier et plus grand que 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        ligne_carre = '#' * size
        print(ligne_carre)
