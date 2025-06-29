#!/usr/bin/python3
"""
This script takes 4 arguments (mysql username, password, database name,
and state name searched) and safely queries the states table in
hbtn_0e_0_usa database for states with exact matching names (case-sensitive),
preventing SQL injection attacks.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to the database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    # Use parameterized query to avoid SQL injection
    query = "SELECT * FROM states WHERE name = BINARY %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
