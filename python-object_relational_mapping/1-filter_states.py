#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.

Takes 3 arguments: mysql username, mysql password, and database name.
Connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id.
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

    # Récupération des résultats
    rows = cursor.fetchall()

    # Affichage ligne par ligne
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
