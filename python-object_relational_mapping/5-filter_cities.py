#!/usr/bin/python3
"""
This script takes MySQL credentials and a state name as arguments,
connects to the database, and prints all cities of the specified state,
sorted by city id in ascending order.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Connect to the MySQL database using credentials from command line arguments
    db = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    # Create a cursor object to execute SQL queries
    query = db.cursor()

    # Execute a parameterized SQL query to get city names for the given state
    query.execute("""
        SELECT cities.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (sys.argv[4],))
    
    # Fetch all the matching rows
    rows = query.fetchall()

    # Extract city names from the rows
    cities = [row[0] for row in rows]

    # Print city names separated by commas
    print(*cities, sep=", ")
