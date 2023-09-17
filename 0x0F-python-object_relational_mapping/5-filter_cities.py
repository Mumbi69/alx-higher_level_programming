#!/usr/bin/python3
"""
    takes in the name of a state as an argument and lists all cities
    of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    st = argv[4]
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = conn.cursor()
    query = """
        SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ')
        FROM cities
        INNER JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
    """
    cur.execute(query, (st,))
    rows = cur.fetchone()
    if rows:
        print(rows[0])
    cur.close()
    conn.close()
