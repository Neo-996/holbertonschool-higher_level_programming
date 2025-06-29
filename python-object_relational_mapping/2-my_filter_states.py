#!/usr/bin/python3
"""
This script takes in 4 arguments (mysql username, password, database name,
and state name searched) and lists all states starting with the given
name (case-sensitive) from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
    )
    cursor = db.cursor()
    query = """
        SELECT * FROM states
        WHERE name LIKE BINARY '{}%'
        ORDER BY id ASC
    """.format(sys.argv[4])
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
