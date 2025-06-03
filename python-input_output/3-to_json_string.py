#!/usr/bin/python3
"""
Module de sérialisation JSON.

Ce module fournit une fonction utilitaire pour convertir un objet Python
(en particulier des structures de données comme dict, list, etc.)
en une chaîne de caractères au format JSON.

Fonction principale :
- to_json_string : transforme un objet Python en une chaîne JSON.

"""
import json


def to_json_string(my_obj):
    """
    Convertit un objet Python en une chaîne JSON.

    Utilise la fonction `dumps()` du module json pour sérialiser l'objet.
    L'objet peut être de type dict, list, str, int, float, bool ou None.

    Args:
        my_obj (any): L'objet Python à convertir.

    Returns:
        str: Une représentation JSON de l'objet sous forme de chaîne.
    """
    return json.dumps(my_obj)
