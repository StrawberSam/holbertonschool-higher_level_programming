#!/usr/bin/python3

"""
Retourne une description sous forme de dictionnaire d’un objet simple
pouvant être sérialisé en JSON.

Cette fonction prend une instance d’une classe et retourne un dictionnaire
représentant ses attributs, prêt à être converti en JSON.

Arguments :
    obj : Une instance de classe disposant d’un attribut __dict__.

Retourne :
    dict : Le dictionnaire des attributs de l’objet.
"""


def class_to_json(obj):
    return obj.__dict__
