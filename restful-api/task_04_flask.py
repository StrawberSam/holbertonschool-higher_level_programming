#!/usr/bin/env python3

"""
Flask REST API simple pour gérer des utilisateurs.

Ce module expose plusieurs routes permettant :
- d'afficher un message d'accueil
- de lister les noms d'utilisateurs
- de vérifier le statut du serveur
- d'afficher les informations d'un utilisateur donné
- d'ajouter un nouvel utilisateur via une requête POST
"""

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
# Dictionnaire simulant une base de données d'utilisateurs
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
        },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
        }
    }


@app.route('/')
def home():
    """
    Route racine qui renvoie un message de bienvenue.

    Returns:
        str: Message de bienvenue.
    """
    return 'Welcome to the Flask API!'


@app.route('/data', methods=['GET'])
def data():
    """
    Route pour récupérer la liste des noms d'utilisateurs.

    Returns:
        Response: Une liste JSON des clés (usernames) présentes dans la base.
    """
    return jsonify(list(users.keys()))


@app.route('/status', methods=['GET'])
def status():
    """
    Route pour vérifier que le serveur fonctionne bien.

    Returns:
        str: "OK" si le serveur est en ligne.
    """
    return 'OK'


@app.route('/users/<username>', methods=['GET'])
def profil(username):
    """
    Route pour récupérer les informations d'un utilisateur spécifique.

    Args:
        username (str): Nom d'utilisateur à rechercher.

    Returns:
        Response: Les données JSON de l'utilisateur si trouvé,
                  sinon un message d'erreur avec le code 404.
    """
    user_info = users.get(username)
    if user_info:
        return jsonify(user_info)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Route pour ajouter un nouvel utilisateur à la base.

    La requête doit contenir des données JSON avec au minimum le champ
    "username".

    Returns:
        Response: Message de succès et les données de l'utilisateur
        ajouté avec code 201, ou message d'erreur avec code 400 si "username"
        est manquant.
    """
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({"error": "Username is required"}), 400

    users[username] = data

    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
