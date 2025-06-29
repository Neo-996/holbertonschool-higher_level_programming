#!/usr/bin/python3
"""
This script lists all cities for a given state name from the
hbtn_0e_4_usa database in MySQL, using a safe query.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (sys.argv[4],))
    rows = cur.fetchall()
    if rows:
        print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
