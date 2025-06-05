#!/usr/bin/python3

"""
Ce script ajoute les arguments passés en ligne de commande à une liste Python,
puis les enregistre dans un fichier JSON nommé 'add_item.json'.

Il utilise deux fonctions externes :
- save_to_json_file() : pour sauvegarder la liste dans le fichier
- load_from_json_file() : pour charger la liste depuis le fichier s’il existe

Si le fichier n'existe pas, il est automatiquement créé.
Tous les arguments passés au script sont ajoutés à la liste existante.
"""

import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
filename = "add_item.json"

try:
    add_item = load_from_json_file(filename)
except FileNotFoundError:
    add_item = []

add_item.extend(args)
save_to_json_file(add_item, filename)
