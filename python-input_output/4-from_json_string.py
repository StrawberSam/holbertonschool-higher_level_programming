#!/usr/bin/python3
"""
Module de désérialisation JSON.

Ce module contient une fonction utilitaire pour convertir
une chaîne de caractères au format JSON en objet Python natif
(comme un dictionnaire ou une liste).

Fonction principale :
- from_json_string : transforme une chaîne JSON en objet Python.

"""
import json


def from_json_string(my_str):
    """
    Convertit une chaîne JSON en un objet Python.

    Utilise la fonction `loads()` du module json pour désérialiser la chaîne.
    Cela permet de récupérer une structure de données Python (dict, list, etc.)
    à partir d'une représentation textuelle au format JSON.

    Args:
        my_str (str): Chaîne de caractères au format JSON.

    Returns:
        any: L'objet Python correspondant
        (dict, list, str, int, float, bool, ou None).
    """
    return json.loads(my_str)
