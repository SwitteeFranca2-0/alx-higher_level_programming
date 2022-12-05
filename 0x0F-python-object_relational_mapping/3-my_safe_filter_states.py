#!/usr/bin/python3
""" This is a safe filter of safe"""


import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", user=sys.argv[1], passwd=sys.argv[2], 
                           db=sys.argv[3], port=3306)
    cur = conn.cursor()
    nameState = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name = %(nameState) s ORDER BY id ASC",
                 {'nameState' : nameState})
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
