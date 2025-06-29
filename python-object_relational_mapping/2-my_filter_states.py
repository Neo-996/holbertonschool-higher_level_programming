#!/usr/bin/python3
"""
Lists all states with a name matching the given argument
from the database hbtn_0e_0_usa.

Usage:
    ./2-my_filter_states.py <mysql username> <mysql password> \
<database name> <state name>
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to the MySQL database using command line arguments
    connection = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],   # MySQL username
        passwd=sys.argv[2], # MySQL password
        db=sys.argv[3],     # Database name
        port=3306           # Default MySQL port
    )

    # Create a cursor to execute SQL queries
    cursor = connection.cursor()

    # Build the SQL query with exact case-sensitive filtering
    query = ("SELECT * FROM states "
             "WHERE BINARY name = '{}' "
             "ORDER BY states.id ASC"
             ).format(sys.argv[4])

    # Execute the SQL query
    cursor.execute(query)

    # Fetch and print all resulting rows
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    connection.close()
