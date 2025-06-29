#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2],
        db=argv[3], charset="utf8"
    )

    # Create a cursor
    cursor = db.cursor()

    # Execute the query (may return extra results if collation is case-insensitive)
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Filter in Python for strict case sensitivity
    rows = cursor.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)

    # Cleanup
    cursor.close()
    db.close()
