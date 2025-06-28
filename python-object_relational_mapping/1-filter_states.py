#!/usr/bin/env python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],      # utilisateur MySQL
        passwd=sys.argv[2],    # mot de passe MySQL
        db=sys.argv[3]         # nom de la base
    )

    # Création du curseur pour exécuter des requêtes
    cursor = db.cursor()

    # Exécution de la requête
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Affichage ligne par ligne
    for row in cursor.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
