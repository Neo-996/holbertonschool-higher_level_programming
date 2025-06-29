#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
Each city is displayed with its id, name, and state name.
"""

import MySQLdb  # Import the MySQLdb module to connect to MySQL
import sys      # Import sys to use command-line arguments

if __name__ == '__main__':
    # Connect to the MySQL database using command-line arguments
    db = MySQLdb.connect(
        user=sys.argv[1],         # MySQL username
        password=sys.argv[2],     # MySQL password
        database=sys.argv[3],     # Database name
        port=3306                 # Default MySQL port
    )

    # Create a cursor object to execute SQL queries
    query = db.cursor()

    # Execute a single SQL query to retrieve all cities with their state names
    query.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Fetch all results from the executed query
    rows = query.fetchall()

    # Loop through and print each row
    for row in rows:
        print(row)
