#!/usr/bin/python3
"""
Ce module implémente un serveur web HTTP simple utilisant http.server.

Il définit une classe `HandlerRequests` qui gère les requêtes GET pour deux
points de terminaison (endpoints) spécifiques :
- `/data`: Retourne un objet JSON contenant des informations d'exemple sur un
           utilisateur.
- `/info`: Retourne un objet JSON avec la version et une description de l'API.
Toutes les autres requêtes GET reçoivent une réponse d'erreur 404 (Non trouvé).

Le serveur écoute sur le port 8080.
"""
import socketserver
import http.server
import json

PORT = 8000


class HandlerRequests(http.server.BaseHTTPRequestHandler):
    """
    Gère les requêtes HTTP entrantes pour un serveur web simple.

    Cette classe hérite de BaseHTTPRequestHandler et
    implémente la méthode do_GET
    pour répondre aux requêtes GET sur des chemins spécifiques.
    """

    def do_GET(self):
        """
        Gère les requêtes HTTP GET.

        Cette méthode analyse le chemin de la requête (self.path)
        et envoie une réponse JSON appropriée en fonction du chemin :
        - Si le chemin est "/data", retourne des info sur un utilisateur.
        - Si le chemin est "/info", retourne des informations sur l'API.
        - Pour tout autre chemin, retourne une erreur 404 (Not Found).
        """
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            data = {"name": "John", "age": 30, "city": "New York"}
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode('utf-8'))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            datas = {
                "version": "1.0",
                "description": "A simple API built with http.server"
                }
            json_data = json.dumps(datas)
            self.wfile.write(json_data.encode('utf-8'))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


"""
    Point d'entrée principal du script.

    Initialise et démarre un serveur HTTP sur le port 8000.
    Le serveur utilise HandlerRequests pour gérer toutes les requêtes
    entrantes. Le serveur tourne indéfiniment jusqu'à ce qu'il soit arrêté
    manuellement.
    """


with socketserver.TCPServer(("", PORT), HandlerRequests) as httpd:
    print(f"serving at port {PORT}")
    httpd.serve_forever()
