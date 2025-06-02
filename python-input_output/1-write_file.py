#!/usr/bin/python3
"""
Module write_file

Ce module contient une fonction qui écrit une chaîne de caractères
dans un fichier texte encodé en UTF-8, et retourne le nombre de
caractères écrits.
"""


def write_file(filename="", text=""):
    """
    Écrit du texte dans un fichier UTF-8 et retourne le nombre de
    caractères écrits.

    Si le fichier n'existe pas, il est créé. S'il existe,
    son contenu est remplacé.

    Args:
        filename (str): Le chemin du fichier à écrire.
        Doit être une chaîne de caractères.
        text (str): Le texte à écrire dans le fichier.

    Returns:
        int: Le nombre de caractères écrits dans le fichier.
    """
    with open(filename, "w", encoding="utf-8") as file:
        nbcharacter = file.write(text)
        return nbcharacter
