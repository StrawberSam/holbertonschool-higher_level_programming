#!/usr/bin/python3
"""
Ce module fournit une fonction pour charger un objet Python
à partir d’un fichier au format JSON.
"""
import json


def load_from_json_file(filename):
    """
    Charge un objet Python depuis un fichier JSON.

    Paramètres :
        filename (str) : Le chemin du fichier JSON à lire.

    Retour :
        object : L’objet Python résultant de la
        désérialisation du contenu JSON.
    """
    with open(filename, "r", encoding="utf-8") as file:
        object = json.load(file)
        return object
