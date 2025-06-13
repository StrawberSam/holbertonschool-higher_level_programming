#!/usr/bin/env python3
"""
Ce module Flask implémente la sécurité d'une API via deux mécanismes
d'authentification :
- Authentification basique (Basic Auth) avec Flask-HTTPAuth
- Authentification par token JWT avec Flask-JWT-Extended

Fonctionnalités incluses :
- Vérification d'identifiants utilisateurs avec mots de passe hachés
- Attribution de rôles aux utilisateurs (admin, user)
- Génération de tokens JWT à la connexion
- Accès sécurisé à des routes protégées par token
- Contrôle d'accès basé sur les rôles (ex: accès admin uniquement)
"""
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_jwt_extended import get_jwt_identity


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "une_clé_très_secrète"
jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
        },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
        }
}


@auth.verify_password
def verify_password(username, password):
    """
    Vérifie les identifiants utilisateur pour l'authentification basique.

    Args:
        username (str): Le nom d'utilisateur fourni.
        password (str): Le mot de passe fourni.

    Returns:
        str: Le nom d'utilisateur si les identifiants sont valides.
        None: Si les identifiants sont incorrects.
    """
    if username in users and \
            check_password_hash(users.get(username)["password"], password):
        return username


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    Route protégée par authentification basique.

    Returns:
        str: Message de succès si les identifiants sont valides.
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Authentifie un utilisateur et génère un token JWT s'il est valide.

    Reçoit un JSON contenant 'username' et 'password'.
    Retourne un token si les identifiants sont corrects.

    Returns:
        JSON: Token JWT si succès.
        JSON: Message d'erreur avec code 401 si échec.
    """
    data = request.get_json()

    username = data.get('username')
    password = data.get('password')

    if (
        username in users and
        check_password_hash(users[username]['password'], password)
    ):
        access_token = create_access_token(
            identity={"username": username, "role": users[username]["role"]}
            )
        return jsonify(access_token=access_token), 200

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    Route protégée nécessitant un token JWT valide.

    Returns:
        str: Message de succès si le token est valide.
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    Route réservée aux utilisateurs avec le rôle 'admin'.

    Le rôle est récupéré depuis le token JWT.

    Returns:
        str: Message de succès si l'utilisateur est admin.
        JSON: Message d'erreur avec code 403 sinon.
    """
    identity = get_jwt_identity()

    if identity["role"] == "admin":
        return "Admin Access: Granted"
    else:
        return {"error": "Admin access required"}, 403


if __name__ == '__main__':
    app.run()
