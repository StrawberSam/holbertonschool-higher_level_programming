#!/usr/bin/python3
"""fonction qui retourne une liste d'attributs et de méthodes d'un objet
    """


def lookup(obj):
    """fonction qui retourne une liste d'attributs et de méthodes d'un objet

    Args:
        obj (instance de classe ou classe): détient des attributs et méthodes

    Returns:
        list: fonction dir qui récupère la liste des attributs et des méthodes
    """
    return dir(obj)
