#!/usr/bin/python3
"""
This script takes a state name as an argument and lists all cities of that state
from the hbtn_0e_4_usa database, sorted by cities.id in ascending order.
"""

import MySQLdb  # Import MySQLdb module to interact with MySQL
import sys      # Import sys to get command-line arguments

if __name__ == '__main__':
    # Connect to the MySQL database using command-line arguments
    db = MySQLdb.connect(
        host='localhost',         # MySQL server host
        port=3306,                # MySQL port
        user=sys.argv[1],         # MySQL username
        passwd=sys.argv[2],       # MySQL password
        db=sys.argv[3]            # Database name
    )

    # Create a cursor to execute SQL queries
    query = db.cursor()

    # Use a single parameterized query to prevent SQL injection
    query.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (sys.argv[4],))

    # Fetch all matching rows
    rows = query.fetchall()

    # Join city names by comma and print, or print nothing if no matches
    print(", ".join([row[0] for row in rows]))

    # Clean up: close cursor and database connection
    query.close()
    db.close()
