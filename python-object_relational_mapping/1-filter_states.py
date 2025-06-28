#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
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
