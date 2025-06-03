#!/usr/bin/python3

"""
Module de gestion de fichiers permettant d'ajouter du texte à un fichier existant.

Ce module contient une fonction principale :
- append_write : ouvre un fichier en mode ajout et y écrit du texte.
"""


def append_write(filename="", text=""):
    """
    Écrit du texte à la fin d’un fichier texte (mode ajout) et retourne
    le nombre de caractères écrits.

    Si le fichier n’existe pas, il sera créé automatiquement.
    Le texte est ajouté à la suite du contenu existant sans l’écraser.

    Args:
        filename (str): Le nom du fichier à ouvrir (chemin relatif ou absolu).
        text (str): Le texte à ajouter dans le fichier.

    Returns:
        int: Le nombre de caractères effectivement écrits dans le fichier.
    """
    with open(filename, "a", encoding="utf-8") as file:
        nbcharacter = file.write(text)
        return nbcharacter
