#!/usr/bin/python3
"""
This script takes a state name as an argument and lists all cities of that state
from the database hbtn_0e_4_usa, sorted by cities.id in ascending order.
"""

import MySQLdb  # Import MySQLdb module to work with MySQL
import sys      # Import sys for command-line arguments

if __name__ == '__main__':
    # Connect to the MySQL database using user-provided credentials
    db = MySQLdb.connect(
        user=sys.argv[1],         # MySQL username
        password=sys.argv[2],     # MySQL password
        database=sys.argv[3],     # Database name
        port=3306                 # Default MySQL port
    )

    # Create a cursor object to perform SQL queries
    query = db.cursor()

    # Execute a single parameterized query to prevent SQL injection
    query.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (sys.argv[4],))

    # Fetch all matching rows
    rows = query.fetchall()

    # Extract city names and join them with a comma
    print(", ".join([row[0] for row in rows]))

    # Clean up by closing cursor and connection
    query.close()
    db.close()
