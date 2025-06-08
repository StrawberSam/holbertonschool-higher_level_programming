#!/usr/bin/python3
import json

"""Module permettant de sérialiser et désérialiser des données JSON."""


def serialize_and_save_to_file(data, filename):
    """
    Sérialise un objet Python en JSON et l'enregistre dans un fichier.

    Args:
        data: Données Python à sérialiser (dict, list, etc.).
        filename: Nom du fichier dans lequel enregistrer les données JSON.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Charge un fichier JSON et le désérialise en objet Python.

    Args:
        filename: Nom du fichier JSON à charger.

    Returns:
        L'objet Python obtenu après désérialisation.
    """
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
        return data

