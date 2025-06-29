#!/usr/bin/python3
"""Script that lists all states with a name matching the argument."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Création du curseur pour exécuter des requêtes SQL
    cursor = db.cursor()

    # Construction et exécution de la requête SQL
    query = (
        "SELECT * FROM states WHERE name = '{}' "
        "ORDER BY id ASC".format(state_name)
    )
    cursor.execute(query)

    # Récupération et affichage des résultats
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Fermeture de la connexion
    cursor.close()
    db.close()
