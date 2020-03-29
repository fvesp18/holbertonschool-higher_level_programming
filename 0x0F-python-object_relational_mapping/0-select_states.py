#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="127.0.0.1", user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    table = cur.fetchall()
    for row in table:
        for col in row:
            print("({}, '{}')".format(state.id, state.name))
