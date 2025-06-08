#!/usr/bin/python3
import csv
import json

"""Module pour convertir un fichier CSV en fichier JSON."""


def convert_csv_to_json(filename):
    """
    Convertit un fichier CSV en fichier JSON.

    Lit les données d'un fichier CSV et les écrit sous
    forme de liste de dictionnaires
    dans un fichier JSON nommé 'data.json'.

    Args:
        filename (str): Le nom du fichier CSV à convertir.

    Returns:
        bool: True si la conversion a réussi, False en cas d'erreur.
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data_list = []

            for ligne in reader:
                data_list.append(ligne)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file)

        return True
    except Exception:
        return False

