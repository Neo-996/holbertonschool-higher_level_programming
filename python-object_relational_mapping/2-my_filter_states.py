#!/usr/bin/python3
"""
This script takes in four arguments: mysql username, mysql password,
database name, and state name searched. It connects to the MySQL
database and lists all states with a name matching the given argument.
"""

import MySQLdb
import sys


def main():
    """
    Connects to the MySQL database and queries the states table for a state
    matching the user input. Prints all matching rows sorted by id.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4])
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
