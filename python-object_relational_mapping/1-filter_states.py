#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.

Usage:
    ./1-filter_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
from sys import argv


def main():
    """Connects to MySQL and prints states starting with 'N' sorted by id."""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8")
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
