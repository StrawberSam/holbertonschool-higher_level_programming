#!/usr/bin/python3
"""
Module read_file

Ce module contient une fonction qui lit un fichier texte UTF-8
et affiche son contenu sur la sortie standard.
"""


def read_file(filename=""):
    """
    Lit un fichier texte en UTF-8 et affiche son contenu à l'écran.

    Args:
        filename (str): Le chemin du fichier à lire.
        Doit être une chaîne de caractères.
        Par défaut, une chaîne vide.

    Returns:
        None

    Ce n'est pas une fonction de lecture silencieuse :
    le contenu est affiché avec un print().
    """
    with open(filename, "r", encoding="utf-8") as file:
        contenu = file.read()
        print(contenu, end="")
