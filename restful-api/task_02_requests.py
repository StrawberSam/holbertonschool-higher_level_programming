#!/usr/bin/python3
import requests
import csv

"""
Module de récupération et de traitement de publications depuis une API REST.

Ce module utilise la bibliothèque 'requests' pour interroger l'API
JSONPlaceholder.
Il permet soit d'afficher les titres des publications dans la console,
soit de sauvegarder les publications dans un fichier CSV.

Fonctionnalités :
- Afficher les titres de toutes les publications.
- Sauvegarder les publications avec leur ID, titre et contenu dans 'posts.csv'
"""


def fetch_and_print_posts():
    """
    Récupère les publications depuis l'API JSONPlaceholder et affiche
    leurs titres.

    Étapes :
    - Envoie une requête HTTP GET à l'API.
    - Affiche le code de statut de la réponse.
    - Si la réponse est valide (code 200), désérialise les données JSON.
    - Parcourt chaque publication et affiche uniquement son titre.

    Ne sauvegarde aucune donnée, affiche seulement dans la console.
    """
    reponse = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {reponse.status_code}")

    data = reponse.json()

    for post in data:
        if "title" in post:
            print(post["title"])


def fetch_and_save_posts():
    """
    Récupère les publications depuis l'API JSONPlaceholder et les
    enregistre dans un fichier CSV.

    Étapes :
    - Envoie une requête HTTP GET à l'API.
    - Affiche le code de statut de la réponse.
    - Si la réponse est valide (code 200), désérialise les données JSON.
    - Pour chaque publication, extrait les champs 'id', 'title' et 'body'.
    - Écrit ces données dans un fichier CSV nommé 'posts.csv' avec ces trois
      colonnes.

    Ne fait rien si la requête échoue.
    """
    reponse = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {reponse.status_code}")

    if reponse.status_code == 200:
        data = reponse.json()
        liste = []

        for post in data:
            dic = {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            }
            liste.append(dic)

        with open("posts.csv", "w", encoding="utf-8") as fichier:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(fichier, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(liste)

    elif reponse.status_code != 200:
        pass
