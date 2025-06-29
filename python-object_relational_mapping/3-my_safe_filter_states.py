#!/usr/bin/python3
"""Safe script to filter states by name, protected from SQL injection."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération de l'argument
    state_name = sys.argv[4]

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    # Requête paramétrée pour se protéger contre les injections SQL : %s
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()
    for row in results:
        print(row)

    # Fermeture
    cursor.close()
    db.close()
