#!/usr/bin/python3
"""Filter cities by states"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    nameState = sys.argv[4]
    cur.execute("""
                SELECT cities.name FROM cities
                INNER JOIN states ON states.id = cities.state_id
                WHERE states.name = %(nameState) s
                ORDER BY cities.id ASC
                """, {'nameState': nameState})
    r = cur.fetchall()
    for w in r:
        for c in w:
            print(c, end="")
            if (w.index(c) == len(w) - 1) and r.index(w) != len(r) - 1:
                print(", ", end="")

    print("")
    cur.close()
    conn.close()
