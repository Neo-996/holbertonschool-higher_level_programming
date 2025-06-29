#!/usr/bin/python3
"""
This script takes MySQL credentials and a state name as arguments,
connects to the database, and prints all cities of the specified state,
sorted by city id in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the database
    connection = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],       # MySQL username from command line argument
        passwd=sys.argv[2],     # MySQL password from command line argument
        db=sys.argv[3],         # Database name from command line argument
        port=3306               # MySQL default port
    )

    # Create a cursor to execute queries
    cursor = connection.cursor()

    # SQL query to get city names linked to a given state
    query = ("SELECT cities.name "
             "FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")

    # Execute the query safely with the state name parameter
    cursor.execute(query, (sys.argv[4],))

    # Fetch results and print city names separated by commas
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))

    # Close the cursor and connection
    cursor.close()
    connection.close()
