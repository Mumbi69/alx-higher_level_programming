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
    query = """SELECT cities.name \
                FROM cities \
                JOIN states ON states.id = cities.state_id \
                WHERE states.name=%s \
                ORDER BY cities.id ASC
    """
    cur.execute(query, (st,))
    rows = cur.fetchall()
    state_cities = []
    for row in rows:
        state_cities.append(row[0])
    print(', '.join(state_cities))
    cur.close()
    conn.close()
