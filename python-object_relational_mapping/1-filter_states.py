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
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
        )

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
