#!/usr/bin/python3
"""
Lists all states with a name matching the given argument
from the database hbtn_0e_0_usa.

Usage:
    ./2-my_filter_states.py <mysql username> <mysql password> \
<database name> <state name>
"""

import MySQLdb
from sys import argv


def main():
    """Connect to MySQL and print states matching the name argument sorted by id."""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2],
                         db=argv[3], charset="utf8")
    cursor = db.cursor()

    # Escape single quotes in the state name to avoid SQL errors
    state_name = argv[4].replace("'", "''")

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
