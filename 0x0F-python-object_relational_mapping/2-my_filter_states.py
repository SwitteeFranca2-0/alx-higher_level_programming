#!/usr/bin/python3
"""This is to filter my states"""

import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1],
                           db=sys.argv[3], passwd=sys.argv[2], port=3306)
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE states.name ='{}'" +
                "ORDER BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
