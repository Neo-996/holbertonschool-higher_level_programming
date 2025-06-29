#!/usr/bin/python3
"""
This script takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument (safe from SQL injection).
"""

import MySQLdb  # Import the MySQLdb module to connect to the MySQL database
import sys      # Import sys to access command-line arguments

if __name__ == '__main__':
    # Connect to the MySQL database using command-line arguments
    db = MySQLdb.connect(
        user=sys.argv[1],         # MySQL username
        password=sys.argv[2],     # MySQL password
        database=sys.argv[3]      # Database name
    )

    # Create a cursor object to execute SQL queries
    query = db.cursor()

    # Execute a parameterized SQL query to safely search for the state name
    query.execute("""
        SELECT * FROM states
        WHERE name = %s
        ORDER BY id ASC
    """, (sys.argv[4],))  # sys.argv[4] is the state name to filter by

    # Retrieve all rows from the result of the query
    rows = query.fetchall()

    # Loop through and print each row
    for row in rows:
        print(row)
