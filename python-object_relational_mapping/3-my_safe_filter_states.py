#!/usr/bin/python3
"""Safe script to filter states by name, protected from SQL injection."""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments
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
