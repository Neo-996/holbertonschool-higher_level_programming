#!/usr/bin/python3
"""
Lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # MySQL credentials and DB name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    # Create a cursor object
    cursor = db.cursor()

    # Execute query to find states starting with 'N'
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Print all matching rows
    for row in cursor.fetchall():
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
