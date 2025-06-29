#!/usr/bin/python3
"""
script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa

Takes 4 arguments: mysql username, mysql password, database name, state name.
Connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by cities.id.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = db.cursor()

    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE BINARY states.name = %s "
        "ORDER BY cities.id ASC",
        (state_name,)
        )

    rows = cursor.fetchall()

    cities = [row[1] for row in rows]
    print(", ".join(cities))

    cursor.close()
    db.close()
