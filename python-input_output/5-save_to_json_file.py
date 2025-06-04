#!/usr/bin/python3
"""
Ce module fournit une fonction pour enregistrer un objet
Python dans un fichier texte, en utilisant une représentation JSON.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Écrit un objet Python dans un fichier texte au format JSON.

    Arguments :
        my_obj (any) : L'objet Python à sérialiser.
        filename (str) : Le nom du fichier dans lequel enregistrer l'objet.

    Remarques :
        - La fonction n’effectue aucune gestion des exceptions si
        l’objet ne peut pas être sérialisé en JSON.
        Elle n’effectue pas non plus de gestion des erreurs liées aux
        permissions de fichiers.
    """
    json_file = json.dumps(my_obj)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(json_file)
